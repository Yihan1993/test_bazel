import os
import subprocess
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def dummy_function():
    logger.info("This is a dummy function.")
    # Example usage of environment variable to get Bazel output base directory
    subprocess.run(["echo", "Retrieving Bazel output base directory..."])
    subprocess.run(["bazel", "info"])
    return 0
    
def main():
    
    ws = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
    logger.info(f"Workspace directory: {ws}")
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
            logger.info(f"Output base directory: {output_base}")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error retrieving output base: {e}")
    else:
        logger.error("BUILD_WORKSPACE_DIRECTORY environment variable is not set.")
        
if __name__ == "__main__":
    main()