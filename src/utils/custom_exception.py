import sys

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, exc_tb = sys.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"

    def __str__(self):
        return self.error_message

# what do we do here?
# - We define a custom exception class called CustomException that inherits from the built-in Exception class.
# - The constructor of the CustomException class takes a message and an optional error_detail parameter.
# - The get_detailed_error_message method is a static method that constructs a detailed error message by including the original message, the error detail, and information about the file and line number where the exception occurred.
# - The __str__ method is overridden to return the detailed error message when the exception is
#converted to a string.
