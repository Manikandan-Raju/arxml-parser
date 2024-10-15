load("@my_deps//:requirements.bzl", "requirement")

filegroup(
    name = "filesysytem",
    srcs = [
        "AutosarFile.arxml",
        "db",
    ],
)

py_binary(
    name = "run",
    srcs = ["run.py"],
    data = [":filesysytem"],
    visibility = ["//visibility:public"],
    deps = ["//app:arxml_parsing"]+ [requirement("openpyxl")],
)
