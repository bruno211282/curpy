import logging
from functools import wraps

logging.basicConfig(
    filename="pynotes.log",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S',
    level=logging.INFO
)


def log_try_exc_deco(action=""):
    def inner(orig_func):

        @wraps(orig_func)
        def wrapper(self, *args):

            logging.info(f"Trying to {action}...")
            try:
                result = orig_func(self, *args)
                logging.info(
                    f"Method '{orig_func.__name__}' executed successfully!")
                return result
            except Exception:
                logging.error(
                    f"Method '{orig_func.__name__}' returned an error...")
        return wrapper
    return inner
