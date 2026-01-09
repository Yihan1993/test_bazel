load("@aspect_rules_py//py:defs.bzl", "py_test")

py_test(
    name = "test_cli_help",
    srcs = ["test_cli_help.py"],
    deps = [
        "@my_bazel_module//cli_helper/tool:cli_help_lib",
        "@pip_tooling//pytest",
    ],
)