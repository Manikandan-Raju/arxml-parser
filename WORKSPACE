# workspace(name = "bazel_monorepo")

# load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
# http_archive(
#     name = "bazel_skylib",
#     sha256 = "bc283cdfcd526a52c3201279cda4bc298652efa898b10b4db0837dc51652756f",
#     urls = [
#         "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.7.1/bazel-skylib-1.7.1.tar.gz",
#         "https://github.com/bazelbuild/bazel-skylib/releases/download/1.7.1/bazel-skylib-1.7.1.tar.gz",
#     ],
# )

# load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

# bazel_skylib_workspace()


# http_archive(
#     name = "rules_python",
#     sha256 = "15f84594af9da06750ceb878abbf129241421e3abbd6e36893041188db67f2fb",
#     strip_prefix = "rules_python-0.7.0",
#     url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.7.0.tar.gz",
# )

# load("@rules_python//python:repositories.bzl", "python_register_toolchains")

# python_register_toolchains(
#     name = "python39",
#     python_version = "3.9",
# )

# load("@python39_resolved_interpreter//:defs.bzl", python_interpreter = "interpreter")
# load("@rules_python//python:pip.bzl", "pip_install")

# pip_install(
#     name = "py_deps",
#     python_interpreter_target = python_interpreter,
#     requirements = "//:requirements.txt",
# )
