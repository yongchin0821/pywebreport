#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/14 9:02 AM
# @Author  : Yongchin

from typing import Optional, List
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


class Report(BaseModel):
    title: Optional[str] = None
    path: Optional[str] = None
    result: Optional[Results] = None
    cases: List[str] = []


class Formatter:
    def __init__(self):
        self.common_datas = Report()

    def use_formatter(self, datas):
        self.common_datas = Report(**datas)
        return self.common_datas

    def output(self):
        f = open(self.common_datas.path, "w+")
        f.write(self.common_datas.json())
        f.close()


formatter = Formatter()
