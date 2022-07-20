#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 9:02 AM
# @Author  : Yongchin

import os
from typing import Optional, List, Dict
from pydantic import BaseModel


class Results(BaseModel):
    total: Optional[str] = None
    passed: Optional[str] = None
    failed: Optional[str] = None
    warnings: Optional[str] = None
    error: Optional[str] = None
    skipped: Optional[str] = None
    duration: Optional[str] = None
    deselected: Optional[str] = None

    rate_passed: Optional[str] = None
    rate_failed: Optional[str] = None
    rate_warnings: Optional[str] = None
    rate_skipped: Optional[str] = None


class Report(BaseModel):
    title: Optional[str] = None
    path: Optional[str] = None
    result: Optional[Results] = None
    suites: Dict = {}


class Formatter:
    def __init__(self):
        self.common_datas = Report()

    def use_formatter(self, datas):
        self.common_datas = Report(**datas)
        return self.common_datas

    def output(self):
        self.compute()
        report_dir = os.path.dirname(self.common_datas.path)
        if not os.path.exists(report_dir):
            os.mkdir(report_dir)

        f = open(report_dir + "/datas.json", "w+")
        f.write(self.common_datas.json())
        f.close()

    def compute(self):
        if int(self.common_datas.result.total) == 0:
            raise IOError("result total is 0, please check the testcases are collected")
        else:
            self.common_datas.result.rate_passed = "{:.2%}".format(float(self.common_datas.result.passed) / float(
                self.common_datas.result.total))
            self.common_datas.result.rate_failed = "{:.2%}".format(float(self.common_datas.result.failed) / float(
                self.common_datas.result.total))
            self.common_datas.result.rate_warnings = "{:.2%}".format(float(self.common_datas.result.warnings) / float(
                self.common_datas.result.total))
            self.common_datas.result.rate_skipped = "{:.2%}".format(float(self.common_datas.result.skipped) / float(
                self.common_datas.result.total))

            for i in self.common_datas.suites:
                self.common_datas.suites[i]["results"]["rate_passed"] = "{:.2%}".format(float(self.common_datas.suites[i]["results"]["passed"]) / float(self.common_datas.suites[i]["results"]["counts"]))


formatter = Formatter()
