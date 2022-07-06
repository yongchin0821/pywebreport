#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 11:10 AM
# @Author  : Yongchin
import os.path
import time
import sys
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
        report["result"]["failed"] = len(failed)
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
        caselist = {}
        for i in items:
            fspath = i.nodeid.split(":")[0]
            if fspath in caselist:
                caselist[fspath].append(i.name)
            else:
                caselist[fspath] = [i.name]

        report["cases"] = caselist

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
