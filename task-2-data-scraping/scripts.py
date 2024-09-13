import logging
import time

import pandas as pd
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from config import config

logger = logging.getLogger(__name__)
URL = config.get_URL


def get_rows(driver):
    WebDriverWait(driver, 2).until(
        ec.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr"))
    )
    return driver.find_elements(By.CSS_SELECTOR, "table tbody tr")


def parse_page_data(driver):
    data = []
    rows = get_rows(driver)
    row_count = len(rows)

    logger.info(f"Found {len(rows)} rows on this page.")

    for row_index in range(row_count):
        try:
            rows = get_rows(driver)
            row = rows[row_index]

            logger.info(f"Parsing row: {row}")

            organization_url = row.find_element(By.CSS_SELECTOR, "td a").get_attribute(
                "href"
            )

            organization_name = row.find_element(By.CSS_SELECTOR, "td a strong").text
            logger.info(f"Get organization name: {organization_name}")

            organization_bin = row.find_element(
                By.CSS_SELECTOR, "td:nth-of-type(3)"
            ).text
            logger.info(f"Get participant name: {organization_bin}")

            logger.info(f"Navigating to organization page: {organization_url}")
            driver.get(organization_url)

            ceo_name = driver.find_element(
                By.XPATH, "//th[text()='ФИО']/following-sibling::td"
            ).text
            logger.info(f"Get ceo name: {ceo_name}")

            ceo_iin = driver.find_element(
                By.XPATH, "//th[text()='ИИН']/following-sibling::td"
            ).text

            logger.info(f"Get ceo iin: {ceo_iin}")

            contact_info_block = driver.find_element(
                By.XPATH,
                '//div[@class="panel-heading"]/h4[text()="Контактная информация"]/../..',
            )
            contact_rows = contact_info_block.find_elements(
                By.CSS_SELECTOR, "table tbody tr"
            )
            full_address = contact_rows[1].find_elements(By.TAG_NAME, "td")[2].text

            logger.info(f"Get full address: {full_address}")

            data.append(
                {
                    "Organization Name": organization_name,
                    "BIN": organization_bin,
                    "CEO Name": ceo_name,
                    "CEO IIN": ceo_iin,
                    "Full Address": full_address,
                }
            )

            logger.info(f"Collected data for organization: {organization_name}")

            driver.back()
            time.sleep(1)
        except WebDriverException as wb:
            logger.error(
                f"StaleElementReferenceException in row {row_index + 1}, skipping...: {wb}"
            )
        except Exception as e:
            logger.error(f"Error processing row {row_index + 1}: {e}")

    return data


def navigate_to_next_page(driver):
    active_page = driver.find_element(By.CSS_SELECTOR, "ul.pagination li.active")
    logger.warning(f"Current active page: {active_page.text}")

    next_page = active_page.find_element(By.XPATH, "following-sibling::li[1]/a")
    if next_page.text != "»":
        logger.warning(f"Navigating to the next page: {next_page.text}")
        next_page.click()
        time.sleep(1)
        return True

    logger.warning("No more pages to navigate.")
    return False


def parse_organization_data(driver):
    all_data = []
    logger.warning(f"Navigating to page: {URL}")
    driver.get(URL)
    WebDriverWait(driver, 3).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "div.panel-body"))
    )

    while True:
        logger.info("Parsing current page for organization links.")
        page_data = parse_page_data(driver)
        all_data.extend(page_data)

        if not navigate_to_next_page(driver):
            break

    return all_data


def main():
    config.configure_logging(level=logging.WARNING)
    driver = config.get_driver()

    try:
        data = parse_organization_data(driver)
        logger.info(f"Data length {len(data)}")

        df = pd.DataFrame(data)
        df = df.drop_duplicates()
        df.to_excel("organizations_data.xlsx", index=False)

        logger.info("Data successfully saved to 'organizations_data.xlsx'.")
    finally:
        driver.quit()
        logger.info("Browser driver closed.")


if __name__ == "__main__":
    try:
        main()
    except WebDriverException as web_driver_exceptions:
        logger.error(f"Stale element reference: {web_driver_exceptions}")
        raise web_driver_exceptions
    except Exception as exception:
        logger.error(f"Unhandled exception in the main execution: {exception}")
        raise exception
    except KeyboardInterrupt as key_interrupt_exception:
        logger.warning("Execution interrupted by user.")
        raise key_interrupt_exception
