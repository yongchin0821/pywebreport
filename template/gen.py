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


def gen_report(datas: dict, path="index.html"):
    template = env.get_template("layouts.html")
    a = template.render(
        title=datas["title"],
        result=datas["result"],
    )
    b = open(path, "wb")
    b.write(a.encode("utf-8"))
    b.close()

    output_dir = os.path.dirname(path)
    src_dir = os.path.dirname(__file__)
    shutil.copyfile(src_dir + "/city.png", output_dir + "/city.png")
    shutil.copyfile(src_dir + "/report.css", output_dir + "/report.css")


if __name__ == '__main__':
    datas = {
        "title": "PyWebReport",
        "path": "datas.json",
        "result": {
            "total": "2",
            "passed": "1",
            "failed": "1",
            "warnings": "0",
            "error": "0",
            "skipped": "0",
            "duration": "0.04762387275695801",
            "deselected": "0"
        },
        "cases": [
            "test_case1",
            "test_case2"
        ]
    }
    gen_report(datas)
