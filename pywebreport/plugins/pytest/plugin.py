#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 4:32 PM
# @Author  : Yongchin

from .htmlreport import HTMLReport


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


def pytest_configure(config):
    config._htmlreport = HTMLReport()
    config.pluginmanager.register(config._htmlreport)
