import logging
from selenium import webdriver


class Config:
    @property
    def get_URL(self):
        return "https://www.goszakup.gov.kz/ru/registry/rqc"

    @staticmethod
    def configure_logging(level: int = logging.INFO):
        logging.basicConfig(
            level=level,
            datefmt="%Y-%m-%d %H:%M:%S",
            format="[%(asctime)s.%(msecs)03d] %(funcName)20s %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
        )

    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        elif browser == "edge":
            return webdriver.Edge()
        else:
            raise ValueError("Browser not supported")


config = Config()
