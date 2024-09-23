import os

class Cd:
    def __init__(self, new_dir):
        if not os.path.isdir(new_dir):
            raise ValueError(f"{new_dir} is not a valid directory or does not exist.")
        self.new_dir = new_dir
        self.prev_dir = None

    def __enter__(self):
        # Save the current working directory
        self.prev_dir = os.getcwd()
        # Change the working directory to the new directory
        os.chdir(self.new_dir)

    def __exit__(self, exc_type, exc_value, traceback):
        # Change the working directory back to the previous one
        os.chdir(self.prev_dir)
