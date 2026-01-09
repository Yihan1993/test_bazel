import os
import subprocess

def test_function():
    print("This is a test function.")
    # Example usage of environment variable to get Bazel output base directory
    subprocess.run(["echo", "Retrieving Bazel output base directory..."])
    subprocess.run(["bazel", "info"])
    
def main():
    
    ws = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    print(f"Workspace directory: {ws}")
    if ws:
        os.chdir(ws)
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
        
if __name__ == "__main__":
    main()