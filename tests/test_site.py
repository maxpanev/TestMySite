import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://positronica.ru/support/")
    yield driver
    driver.quit()

def test_phone_field(driver):
    phone_input = driver.find_element(By.ID, "support-phone")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", phone_input)
    time.sleep(1)
    assert phone_input.is_displayed()
    phone_input.send_keys("9991234567")
    time.sleep(2)
    assert phone_input.get_attribute("value") == "+7 999 123 45 67"


def test_order_number__field(driver):
    order_input = driver.find_element(By.ID, "support-number")
    assert order_input.is_displayed()
    order_input.send_keys("1234567890")
    time.sleep(2)
    assert order_input.get_attribute("value") == "PZ1234567890"


def test_email_field(driver):
    email_input = driver.find_element(By.ID, "support-email")
    assert email_input.is_displayed()
    email_input.send_keys("test@example.com")
    time.sleep(2)
    assert email_input.get_attribute("value") == "test@example.com"


def test_name_field(driver):
    name_input = driver.find_element(By.ID, "support-name")
    assert name_input.is_displayed()
    name_input.send_keys("Иван")
    time.sleep(2)
    assert name_input.get_attribute("value") == "Иван"


def test_message_field(driver):
    message_textarea = driver.find_element(By.ID, "support-text")
    assert message_textarea.is_displayed()
    message_textarea.send_keys("Это тестовое сообщение.")
    time.sleep(2)
    assert message_textarea.get_attribute("value") == "Это тестовое сообщение."


def test_privacy_checkbox(driver):
    checkbox = driver.find_element(By.CLASS_NAME, "form-checkbox__fake")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    time.sleep(1)
    assert checkbox.is_displayed()
    assert not checkbox.is_selected()
    checkbox.click()
    time.sleep(2)
    assert checkbox.is_enabled()

def test_submit_button(driver):
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Отправить')]")
    time.sleep(2)
    assert submit_button.is_enabled()
