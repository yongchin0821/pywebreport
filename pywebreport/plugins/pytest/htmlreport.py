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

report = {
    "result": {}
}


class HTMLReport:
    def pytest_sessionstart(self, session):
        pass

    def pytest_terminal_summary(self, terminalreporter, exitstatus, config):
        """收集测试结果"""
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

    def pytest_report_collectionfinish(self, config, startdir, items):
        suitelist = {}
        for i in items:
            fspath = i.nodeid.split(":")[0]

            if fspath in suitelist:
                pass
            else:
                suitelist[fspath] = {}
                suitelist[fspath]["cases"] = {}
                suitelist[fspath]["results"] = {
                    "counts": 0,
                    "passed": 0,
                    "failed": 0,
                    "warnings": 0,
                    "error": 0,
                    "skipped": 0,
                }
                suitelist[fspath]["duration"] = 0

            suitelist[fspath]["cases"][i.name] = {}

        report["suites"] = suitelist

    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        out = yield
        results = out.get_result()
        case_name = results.head_line.split('.')[-1]

        if results.when == "call":
            print('测试报告：%s' % results)
            print('步骤：%s' % results.when)
            print('nodeid：%s' % results.nodeid)
            print('description:%s' % str(item.function.__doc__))
            print(('运行结果: %s' % results.outcome))
            if results.passed:
                report["suites"][results.fspath]["results"]["counts"] += 1
                report["suites"][results.fspath]["cases"][case_name]["status"] = "passed"
                report["suites"][results.fspath]["cases"][case_name]["duration"] = round(results.duration, 3)
                report["suites"][results.fspath]["duration"] += round(results.duration, 3)
                report["suites"][results.fspath]["results"]["passed"] += 1

        if results.skipped:
            print("skip")
            report["suites"][results.fspath]["results"]["counts"] += 1
            report["suites"][results.fspath]["cases"][case_name]["status"] = "skip"
            report["suites"][results.fspath]["cases"][case_name]["duration"] = round(results.duration, 3)
            report["suites"][results.fspath]["duration"] += round(results.duration, 3)
            report["suites"][results.fspath]["results"]["skipped"] += 1

        if results.failed:
            if getattr(results, "when", None) == "call":
                if hasattr(report, "wasxfail"):
                    # pytest < 3.0 marked xpasses as failures
                    xpassed = 1
                else:
                    failed = 1
            else:
                errors = 1
            report["suites"][results.fspath]["results"]["counts"] += 1
            report["suites"][results.fspath]["cases"][case_name]["status"] = "failed"
            report["suites"][results.fspath]["cases"][case_name]["duration"] = round(results.duration, 3)
            report["suites"][results.fspath]["duration"] += round(results.duration, 3)
            report["suites"][results.fspath]["results"]["failed"] += 1

    def pytest_sessionfinish(self, session):
        exec_file = sys.argv[0]
        exec_path = os.path.dirname(exec_file)
        input_path = session.config.getoption("--report")
        if input_path:
            report_path = os.path.join(exec_path, input_path)
        else:

            report_path = os.path.join(exec_path, "temps/index.html")

        report_title = session.config.getoption("--title")
        report["path"] = report_path
        report["title"] = report_title
