#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 11:10 AM
# @Author  : Yongchin
import os.path
import time
import sys
from pywebreport.formatter import formatter
from pywebreport.reportor import Process
import unittest
import datetime
from unittest import TestResult
from io import StringIO

report = {
    "result": {}
}
origin_stdout = sys.stdout
origin_stderr = sys.stderr


class OutputRedirector:
    """Wrapper to redirect stdout or stderr"""

    def __init__(self, fp):
        self.fp = fp
        self.stdbak = fp

    def write(self, s):
        self.fp.write(s)
        self.stdbak.write(str(s) + "\r")
        # origin_stdout.write(str(s))

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


class _TestResult(unittest.TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.
    def __init__(self, verbosity=2):
        TestResult.__init__(self)
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.skip_count = 0
        self.verbosity = verbosity
        self.suitelist = {}

        # result is a list of result in 4 tuple
        # (
        #   Result code (0: success; 1: fail; 2: error; 3:skip),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []

        self.sys_stdout = None
        self.sys_stderr = None
        self.outputBuffer = None

    def startTest(self, test):
        test.class_name = test.__class__.__qualname__
        test.method_name = test.__dict__['_testMethodName']
        test.method_doc = test.shortDescription() if test.shortDescription() is not None else ""
        test_id_list = test.id().split('.')
        test.file_name = test_id_list[0] + ".py"

        self._struct_time = time.localtime()
        test.exec_time = time.strftime("%Y-%m-%d %H:%M:%S", self._struct_time)

        if test.file_name in self.suitelist:
            pass
        else:
            self.suitelist[test.file_name] = {}
            self.suitelist[test.file_name]["cases"] = {}
            self.suitelist[test.file_name]["results"] = {
                "counts": 0,
                "passed": 0,
                "failed": 0,
                "warnings": 0,
                "error": 0,
                "skipped": 0,
            }
            self.suitelist[test.file_name]["duration"] = 0

        self.suitelist[test.file_name]["cases"][test.method_name] = {}

        TestResult.startTest(self, test)
        self.start_time = time.time()

        # just one buffer for both stdout and stderr
        self.outputBuffer = StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.sys_stdout = sys.stdout
        self.sys_stderr = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.sys_stdout:
            sys.stdout = self.sys_stdout
            sys.stderr = self.sys_stderr
            self.sys_stdout = None
            self.sys_stderr = None

        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        test.run_time = '{:.3}s'.format((time.time() - self.start_time))

    def addSuccess(self, test: unittest.case.TestCase) -> None:
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        test.run_time = '{:.3}'.format((time.time() - self.start_time))
        self._record_case(test, "passed")
        # if self.verbosity > 1:
        #     sys.stderr.write('ok ')
        #     sys.stderr.write(str(test))
        #     sys.stderr.write('\n')
        # else:
        #     sys.stderr.write('.')

    def addError(self, test: unittest.case.TestCase, err) -> None:
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        test.run_time = '{:.3}'.format((time.time() - self.start_time))
        self._record_case(test, "failed")
        # if self.verbosity > 1:
        #     sys.stderr.write('E  ')
        #     sys.stderr.write(str(test))
        #     sys.stderr.write('\n')
        # else:
        #     sys.stderr.write('E')

    def addFailure(self, test: unittest.case.TestCase, err) -> None:
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        test.run_time = '{:.3}'.format((time.time() - self.start_time))
        self._record_case(test, "failed")
        # if self.verbosity > 1:
        #     sys.stderr.write('F  ')
        #     sys.stderr.write(str(test))
        #     sys.stderr.write('\n')
        # else:
        #     sys.stderr.write('F')

    def addSkip(self, test: unittest.case.TestCase, reason: str) -> None:
        self.skip_count += 1
        TestResult.addSkip(self, test, reason)
        _, _exc_str = self.skipped[-1]
        output = self.complete_output()
        self.result.append((3, test, output, _exc_str))
        test.run_time = '{:.3}'.format((time.time() - self.start_time))
        self._record_case(test, "skipped")

    def stopTestRun(self) -> None:
        pass

    def _record_case(self, results, status):
        self.suitelist[results.file_name]["results"]["counts"] += 1

        test_id = results.id().replace(".", "::")
        test_id_list = test_id.split("::")
        test_id_list[0] += ".py"
        test_id = "::".join(test_id_list)
        self.suitelist[results.file_name]["cases"][results.method_name]["id"] = test_id

        self.suitelist[results.file_name]["cases"][results.method_name]["desc"] = results.method_doc
        self.suitelist[results.file_name]["cases"][results.method_name]["status"] = status
        self.suitelist[results.file_name]["cases"][results.method_name]["duration"] = round(float(results.run_time), 3)
        self.suitelist[results.file_name]["cases"][results.method_name]["className"] = results.class_name
        self.suitelist[results.file_name]["cases"][results.method_name]["consoleLog"] = self.result[-1][2]
        self.suitelist[results.file_name]["cases"][results.method_name]["errMsg"] = self.result[-1][3]
        self.suitelist[results.file_name]["cases"][results.method_name]["execTime"] = results.exec_time
        self.suitelist[results.file_name]["duration"] += round(float(results.run_time), 3)
        self.suitelist[results.file_name]["results"][status] += 1


class WebReportRunner:
    def __init__(self, report=None, title="pywebreport"):
        self.input_path = report
        self.title = title

    def _compute(self, suites):
        total = 0
        passed = 0
        failed = 0
        error = 0
        warnings = 0
        skipped = 0
        duration = 0

        for file_name in suites:
            duration += suites[file_name]["duration"]
            total += suites[file_name]["results"]['counts']
            passed += suites[file_name]["results"]['passed']
            failed += suites[file_name]["results"]['failed']
            error += suites[file_name]["results"]['warnings']
            warnings += suites[file_name]["results"]['error']
            skipped += suites[file_name]["results"]['skipped']

        report["result"]["total"] = total
        report["result"]["exec"] = passed + failed + error + skipped
        report["result"]["passed"] = passed

        failed_count = failed + error
        report["result"]["failed"] = failed_count

        report["result"]["error"] = error
        report["result"]["warnings"] = warnings
        report["result"]["skipped"] = skipped
        report["result"]["duration"] = duration
        report["result"]["deselected"] = ""

    def run(self, testlist, rerun=0, save_last_run=False):
        """
        Run the given test case or test suite.
        """
        result = _TestResult()
        testlist(result)
        self.end_time = datetime.datetime.now()

        exec_file = sys.argv[0]
        exec_path = os.path.dirname(exec_file)

        if self.input_path:
            report_path = os.path.join(exec_path, self.input_path)
        else:
            report_path = os.path.join(exec_path, "temps/index.html")

        report_title = self.title
        report["path"] = report_path
        report["title"] = report_title
        report["suites"] = result.suitelist
        self._compute(report["suites"])

        formatter.use_formatter(report)
        formatter.output()
        p = Process(formatter.common_datas.path)
        p.run()

        return result
