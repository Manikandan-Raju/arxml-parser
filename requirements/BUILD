load("@python//3.11:defs.bzl", compile_pip_requirements_3_11 = "compile_pip_requirements")
load("@python//3.9:defs.bzl", compile_pip_requirements_3_9 = "compile_pip_requirements")

compile_pip_requirements_3_9(
    name = "requirements_3_9",
    src = "requirements.in",
    requirements_txt = "requirements_lock_3_9.txt",
)


compile_pip_requirements_3_11(
    name = "requirements_3_11",
    src = "requirements.in",
    requirements_txt = "requirements_lock_3_11.txt",
)