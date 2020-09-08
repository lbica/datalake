"""
logging
~~~~~~~~~~~~~

:copyright: 2020 Laurentiu BICA
:license: 
"""


import logging
from logging.config import fileConfig
from os import path

log_file_path = path.join(path.dirname(
    path.abspath(__file__)), 'config\\logging.ini')
logging.basicConfig(level=logging.INFO)
logger = logging


if not path.exists(log_file_path):
    logging.warning(
        'The logging.ini file doesn\'t exists. A default logger will be used.')
else:
    fileConfig(fname=log_file_path, disable_existing_loggers=False)
    # Name the logger after the package.
    logger = logging.getLogger("exercise1")


# if ctx is None:
#     raise RuntimeError(
#         "Attempted to stream with context but "
#         "there was no context in the first place to keep around."
#     )
