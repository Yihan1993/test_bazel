# My Bazel Module

A reusable Bazel module providing CLI helper utilities.

## Usage

Add this to your `MODULE.bazel`:

```python
bazel_dep(name = "my_bazel_module", version = "1.0.0")

# Use git_override for Git-based dependencies
git_override(
    module_name = "my_bazel_module",
    remote = "https://github.com/your-org/my_bazel_module.git",
    commit = "abc123...",  # or tag = "v1.0.0"
)
```

### Available Targets

#### CLI Helper Macro
```python
load("@my_bazel_module//tools:cli_helper.bzl", "cli_helper")

cli_helper(
    name = "help",
    visibility = ["//visibility:public"],
)
```

#### CLI Help Library
```python
py_binary(
    name = "my_app",
    srcs = ["main.py"],
    deps = ["@my_bazel_module//tools:cli_help_lib"],
)
```

## Publishing

This module is available through:
- **Local**: Use `local_path_override`
- **Git**: Use `git_override`
- **BCR**: (Coming soon) Use standard `bazel_dep`
