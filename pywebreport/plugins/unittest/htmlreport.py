#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 11:10 AM
# @Author  : Yongchin
import os.path
import time
import sys
import pytest
from pywebreport.formatter import formatter
from pywebreport.reportor import Process
import unittest
import datetime
from unittest import TestResult

report = {
    "result": {}
}


class _TestResult(unittest.TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.suitelist = {}

        # Log is a list of Log in 4 tuple
        # (
        #   Log code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        # 增加一个测试通过率 --Findyou
        self.passrate = float(0)

    def startTest(self, test):
        test.class_name = test.__class__.__qualname__
        test.method_name = test.__dict__['_testMethodName']
        test.method_doc = test.shortDescription()
        test_id_list = test.id().split('.')
        test.file_name = test_id_list[0] + ".py"

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
        # self.outputBuffer = StringIO()
        # stdout_redirector.fp = self.outputBuffer
        # stderr_redirector.fp = self.outputBuffer
        # self.stdout0 = sys.stdout
        # self.stderr0 = sys.stderr
        # sys.stdout = stdout_redirector
        # sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        # if self.stdout0:
        #     sys.stdout = self.stdout0
        #     sys.stderr = self.stderr0
        #     self.stdout0 = None
        #     self.stderr0 = None
        # return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        test.run_time = '{:.3}s'.format((time.time() - self.start_time))

        # self.fields['results'].append(test)
        # self.fields["testClass"].add(test.class_name)
        # self.complete_output()

    def addSuccess(self, test):
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

    def addError(self, test, err):
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

    def addFailure(self, test, err):
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

    def stopTestRun(self) -> None:
        # report["suites"] = self.suitelist
        pass

    def _record_case(self, results, status):
        self.suitelist[results.file_name]["results"]["counts"] += 1
        self.suitelist[results.file_name]["cases"][results.method_name]["status"] = status
        self.suitelist[results.file_name]["cases"][results.method_name]["duration"] = round(float(results.run_time), 3)
        self.suitelist[results.file_name]["cases"][results.method_name]["className"] = results.class_name
        self.suitelist[results.file_name]["duration"] += round(float(results.run_time), 3)
        self.suitelist[results.file_name]["results"][status] += 1


class WebReportRunner:
    def run(self, testlist, rerun=0, save_last_run=False):
        """
        Run the given test case or test suite.
        """
        result = _TestResult()
        testlist(result)
        self.end_time = datetime.datetime.now()

        exec_file = sys.argv[0]
        exec_path = os.path.dirname(exec_file)
        input_path = ""
        if input_path:
            report_path = os.path.join(exec_path, input_path)
        else:
            report_path = os.path.join(exec_path, "temps/index.html")

        report_title = "ddd"
        report["path"] = report_path
        report["title"] = report_title

        # self.run_times += 1
        # self.generate_report(testlist, result)

        total = terminalreporter._numcollected
        passed = terminalreporter.stats.get("passed", [])
        failed = terminalreporter.stats.get("failed", [])
        error = terminalreporter.stats.get("error", [])
        warnings = terminalreporter.stats.get("warnings", [])
        skipped = terminalreporter.stats.get("skipped", [])
        duration = time.time() - terminalreporter._sessionstarttime
        deselected = terminalreporter.stats.get("deselected", [])  # 过滤的用例数

        report["result"]["total"] = total
        report["result"]["exec"] = total - len(deselected)
        report["result"]["passed"] = len(passed)

        failed_count = len(failed) + len(error)
        report["result"]["failed"] = failed_count

        report["result"]["error"] = len(error)
        report["result"]["warnings"] = len(warnings)
        report["result"]["skipped"] = len(skipped)
        report["result"]["duration"] = duration
        report["result"]["deselected"] = len(deselected)

        formatter.use_formatter(report)
        formatter.output()
        p = Process(formatter.common_datas.path)
        p.run()

        return result
