import logging
from utilities.system_logger import SystemLogger

class SearchLogger:

  search_logger = logging.getLogger(__name__)
  search_logger.setLevel(logging.INFO)
  search_logger.propagate = False

  logging_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

  logging_file_handler = logging.FileHandler('./logs/search_logs/search_log.log')
  logging_file_handler.setLevel(logging.INFO)
  logging_file_handler.setFormatter(logging_formatter)

  if not search_logger.hasHandlers():
      
    search_logger.addHandler(logging_file_handler)

  @classmethod
  def log_search(cls, query, results, summary, excerpts, related_queries):
      
    try:
        
      cls.search_logger.info('User Query: %s', query)
      cls.search_logger.info('Returned Results: %s', results)
      cls.search_logger.info('Generated Summary: %s', summary)
      cls.search_logger.info('Generated Excerpts: %s', excerpts)
      cls.search_logger.info('Generated Related Queries: %s', related_queries)

    except Exception as exception:
        
      SystemLogger.system_logger.error('An error occurred while logging search data: %s', str(exception))