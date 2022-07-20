#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 3:53 PM
# @Author  : Yongchin

from jinja2 import Environment, FileSystemLoader
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "template")

env = Environment(loader=FileSystemLoader(BASE_DIR))
TEMPLATE_HTML = "template.html"
STYLESHEET_HTML = "stylesheet.html"


def gen_report(datas: dict):
    template = env.get_template("layouts.html")
    a = template.render(
        title=datas["title"],
        result=datas["result"],
        suites=datas["suites"],
    )
    if datas["path"] == "" or datas["path"] is None:
        datas["path"] = "index.html"
    else:
        pass

    report_dir = os.path.dirname(datas["path"])
    if not os.path.exists(report_dir) and report_dir != "":
        os.mkdir(report_dir)

    b = open(datas["path"], "wb")
    b.write(a.encode("utf-8"))
    b.close()

    output_dir = os.path.dirname(datas["path"])
    src_dir = os.path.dirname(__file__)

    shutil.copyfile(os.path.join(src_dir, "city.png"), os.path.join(output_dir, "city.png"))
    shutil.copyfile(os.path.join(src_dir, "report.css"), os.path.join(output_dir, "report.css"))

    print("Report generated successfully")
    print("Report path: " + datas["path"])


if __name__ == '__main__':
    datas = {
        "title": "PyWebReport",
        "path": "./dist/index.html",
        "result": {
            "total": "5",
            "passed": "3",
            "failed": "1",
            "warnings": "1",
            "error": "0",
            "skipped": "1",
            "duration": "0.0580599308013916",
            "deselected": "0",
            "rate_passed": "60.00%",
            "rate_failed": "20.00%",
            "rate_warnings": "20.00%",
            "rate_skipped": "20.00%"
        },
        "cases": {
            "testsuites/test_admin.py": [
                "test_case1",
                "test_case2",
                "test_case3"
            ],
            "testsuites/test_home.py": [
                "test_case1",
                "test_case2"
            ]
        }
    }
    gen_report(datas)
