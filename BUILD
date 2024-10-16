# load("@rules_python//python:defs.bzl", "py_binary")
load("@python//3.9:defs.bzl", py_binary_3_9 = "py_binary")

filegroup(
    name = "filesysytem",
    srcs = [
        "AutosarFile.arxml",
        "db",
    ],
)

py_binary_3_9(
    name = "run",
    srcs = ["run.py"],
    data = [":filesysytem"],
    visibility = ["//visibility:public"],
    deps = ["//app:arxml_parsing"] + [
        "@pypi//openpyxl:pkg",
    ],
)
