import os
import subprocess

ws = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
if ws:
    try:
        result = subprocess.run(
            ["bazel", "info", "output_base"],
            cwd=ws,
            capture_output=True,
            text=True,
            check=True,
        )
        output_base = result.stdout.strip()
        print(f"Output base directory: {output_base}")
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving output base: {e}")
else:
    print("BUILD_WORKSPACE_DIRECTORY environment variable is not set.")