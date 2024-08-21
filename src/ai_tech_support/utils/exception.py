import sys
from enum import Enum
from src.ai_tech_support.utils.logger import get_logger

logger = get_logger(__name__)

class ErrorSeverity(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

def error_message_detail(error, error_detail, severity=ErrorSeverity.MEDIUM):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"[{severity.value}] Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail, severity=ErrorSeverity.MEDIUM):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail, severity)
        self.severity = severity

    def __str__(self):
        return self.error_message

    def log_error(self):
        if self.severity in [ErrorSeverity.HIGH, ErrorSeverity.CRITICAL]:
            logger.error(self.error_message)
        else:
            logger.warning(self.error_message)

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomException as e:
            e.log_error()
            raise
        except Exception as e:
            custom_exception = CustomException(e, sys, ErrorSeverity.HIGH)
            custom_exception.log_error()
            raise custom_exception from e
    return wrapper