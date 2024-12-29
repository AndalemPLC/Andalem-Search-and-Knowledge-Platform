import logging
import sys

class SystemLogger:

  system_logger = logging.getLogger(__name__)
  system_logger.setLevel(logging.ERROR)
  system_logger.propagate = False

  logging_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s') 

  logging_file_handler = logging.FileHandler('./logs/system_logs/system_log.log')
  logging_file_handler.setLevel(logging.ERROR)
  logging_file_handler.setFormatter(logging_formatter) 

  logging_stdout_handler = logging.StreamHandler(sys.stdout)
  logging_stdout_handler.setLevel(logging.ERROR)
  logging_stdout_handler.setFormatter(logging_formatter)

  if not system_logger.hasHandlers():

    system_logger.addHandler(logging_file_handler)
    system_logger.addHandler(logging_stdout_handler)  