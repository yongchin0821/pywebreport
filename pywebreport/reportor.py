#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 10:10 AM
# @Author  : Yongchin

import json
import os.path
from pywebreport.template.gen import gen_report


class Process:
    def __init__(self, path):
        self.result_path = path
        self.report_dir = os.path.dirname(self.result_path)

    def get_result(self):
        f = open(self.report_dir + "/datas.json", "r")
        result = f.read()
        results = json.loads(result)
        return results

    def run(self):
        result = self.get_result()
        gen_report(result)


if __name__ == '__main__':
    p = Process("test/datas.json")
    p.run()
