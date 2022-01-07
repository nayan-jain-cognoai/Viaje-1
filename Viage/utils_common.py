import os
import sys
import logging
import linecache
import json
import inspect

logger = logging.getLogger(__name__)

def return_lineno_filename_file_called_exception():
    exc_type, exc_obj, tb = sys.exc_info()
    frame = tb.tb_frame
    lineno = tb.tb_lineno
    filename = frame.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, frame.f_globals)

    return exc_obj, lineno, filename, line


def raise_exception(message=''):
    callerframerecord = inspect.stack()[1]
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    function_name = info.function
    line_no = info.lineno
    try:
        exc_obj, lineno, filename, line = return_lineno_filename_file_called_exception()
        logger.error(message + " [ERROR] %s at %s in function %s",
                     exc_obj, lineno, function_name)
    except:
        logger.error(message + " [ERROR] of function %s at %s",
                     function_name, line_no)


def raise_info(message=''):
    try:
        exc_obj, lineno, filename, line = return_lineno_filename_file_called_exception()
        logger.info(message + " [INFO] %s at %s ", exc_obj, lineno)
    except:
        callerframerecord = inspect.stack()[1]
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)
        function_name = info.function
        line_no = info.lineno
        logger.info(message + " [INFO] of function %s at %s",
                    function_name, line_no)