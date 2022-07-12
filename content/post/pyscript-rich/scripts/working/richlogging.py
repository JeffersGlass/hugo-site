import logging
from rich.logging import RichHandler

from faker import Faker
from random import choice

FORMAT = "%(message)s"
logging.basicConfig(
    level="INFO", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

#Generate some fake but interesting logs:
fake = Faker()

for _ in range(10):
    log_level = choice([logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL])
    if log_level == logging.INFO:
        logging.info(f"New Email from  {fake.unique.name()} ({fake.unique.ascii_email()})")
    elif log_level == logging.WARNING:
        logging.warning(f"Purchase from card {fake.unique.credit_card_number()} failed")
    elif log_level == logging.ERROR:
        logging.error(f"Host {fake.unique.hostname()} at {fake.unique.ipv4} is offline")
    else:
        logging.critical(f"Bank account with Account Number {fake.unique.bban()} is at $0!")