import time
import logging
import string
import secrets

def make_random_string(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))

def setup_logging() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger("random_string_app")


if __name__=="__main__":
    logger = setup_logging()
    token = make_random_string(24)
    while True:
        logger.info(token)
        time.sleep(5)

