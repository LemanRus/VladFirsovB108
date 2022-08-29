import logging

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - %(filename)s line %(lineno)d - %(message)s"


def get_file_handler():
    file_handler = logging.FileHandler("log.log", "a", "utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger


def log(logger):
    def _log(func):
        def inner_func(*args, **kwargs):
            logger.info(f"Функция {func.__name__} вызвана из функции {__name__}")
            func(*args, **kwargs)
        return inner_func
    return _log