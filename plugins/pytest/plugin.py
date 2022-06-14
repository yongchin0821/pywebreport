#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:32 PM
# @Author  : Yongchin
import time
from typing import Optional
from pydantic import BaseModel
from formatter import formatter

report = {
    "title": None,
    "result": {}
}


def pytest_sessionstart(session):
    pass


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    total = terminalreporter._numcollected
    passed = terminalreporter.stats.get("passed", [])
    failed = terminalreporter.stats.get("failed", [])
    error = terminalreporter.stats.get("error", [])
    warnings = terminalreporter.stats.get("warnings", [])
    skipped = terminalreporter.stats.get("skipped", [])
    duration = time.time() - terminalreporter._sessionstarttime
    deselected = terminalreporter.stats.get("deselected", [])  # 过滤的用例数
    # content = "【自动化测试报告】\t\n" \
    #           "用例总数：%s\t\n" \
    #           "执行用例总数：%s \t\n" \
    #           "执行成功数：%s \t\n" \
    #           "执行失败数：%s \t\n" \
    #           "执行ERROR数：%s \t\n" \
    #           "执行SKIP数：%s \t\n" \
    #           "执行成功数：%.2f %%  \t\n" \
    #           "执行时长：%.2f 秒 \t\n" % (
    #               len(total), len(total) - len(deselected), len(passed), len(failed), len(error), skipped, passed / (total - deselected) * 100,
    #               duration)

    # print(content)
    report["result"]["total"] = total
    report["result"]["passed"] = len(passed)
    report["result"]["failed"] = len(failed)
    report["result"]["error"] = len(error)
    report["result"]["warnings"] = len(warnings)
    report["result"]["skipped"] = len(skipped)
    report["result"]["duration"] = duration
    report["result"]["deselected"] = len(deselected)

    formatter.use_formatter(report)
    formatter.output()


def pytest_report_collectionfinish(config, startdir, items):
    caselist = []
    for i in items:
        caselist.append(i.name)
    report["cases"] = caselist


def pytest_sessionfinish(session):
    report_path = session.config.getoption("--report")
    if not report_path:
        report_path = "temps"

    report_title = session.config.getoption("--title")
    report["path"] = report_path
    report["title"] = report_title


def pytest_addoption(parser):
    group = parser.getgroup("pywebreport")
    group.addoption(
        "--report",
        action="store",
        metavar="path",
        default=None,
        help="create html report file at given path.",
    )
    group.addoption(
        "--title",
        action="store",
        metavar="path",
        default="PyWebReport",
        help="create html report file at given path.",
    )
