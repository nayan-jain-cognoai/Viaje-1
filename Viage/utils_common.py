import os
import sys
import logging
import linecache
import json
from inspect import getframeinfo, stack

logger = logging.getLogger(__name__)

def raise_exception(message=''):
    exc_type, exc_obj, tb = sys.exc_info()
    caller = getframeinfo(stack()[1][0])
    logger.error("Error [%s] File: [%s]: at Line [%d] :-Message [%s]",exc_obj,caller.filename, caller.lineno, message)



def raise_info(message=''):
    caller = getframeinfo(stack()[1][0])
    logger.info("File: %s: at Line %d :- %s",caller.filename, caller.lineno, message)