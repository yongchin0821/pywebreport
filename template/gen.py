#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/9 3:53 PM
# @Author  : Yongchin

from jinja2 import Environment, FileSystemLoader
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(BASE_DIR, "template")

env = Environment(loader=FileSystemLoader(BASE_DIR))
TEMPLATE_HTML = "template.html"
STYLESHEET_HTML = "stylesheet.html"

template = env.get_template("layouts.html")
a = template.render()
b = open("index.html", "wb")
b.write(a.encode("utf-8"))
b.close()