from contextlib import ContextDecorator
import datetime

class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename
        self.start_time = None

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        execution_time = datetime.datetime.now() - self.start_time
        with open(self.filename, 'a') as log_file:
            log_file.write(f"Start: {self.start_time} | Run: {execution_time} | An error occurred: {exc_value}\n")
        return False  # Re-raise any exceptions
