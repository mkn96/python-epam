import os
import shutil
import tempfile

class TempDir:
    def __enter__(self):
        # Create a temporary directory in the current directory
        self.temp_dir = tempfile.mkdtemp(dir=os.getcwd())
        # Save the current working directory
        self.prev_dir = os.getcwd()
        # Change the working directory to the temporary directory
        os.chdir(self.temp_dir)
        return self.temp_dir

    def __exit__(self, exc_type, exc_value, traceback):
        # Change the working directory back to the previous one
        os.chdir(self.prev_dir)
        # Remove the temporary directory and its contents
        shutil.rmtree(self.temp_dir)

# Example usage:
with TempDir() as temp_dir:
    # Inside this block, temp_dir is the temporary directory
    print("Current directory:", os.getcwd())  # Should print the temporary directory
    # Perform actions in the temporary directory

# Outside the block, the temporary directory has been removed
print("Current directory after exiting TempDir block:", os.getcwd())  # Should print the original directory
