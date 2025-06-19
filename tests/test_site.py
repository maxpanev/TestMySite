import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://positronica.ru/support/")
    yield driver
    driver.quit()


def test_city_field(driver):
    city_field = driver.find_element(By.XPATH, "(//div[contains(@class, 'choices__inner')])[2]")
    assert city_field.is_displayed()



def test_email_field(driver):
    email_input = driver.find_element(By.ID, "support-email")
    assert email_input.is_displayed()
    # Вводим тестовый email
    email_input.send_keys("test@example.com")
    # Проверяем, что значение введено
    assert email_input.get_attribute("value") == "test@example.com"


def test_phone_field(driver):
    phone_input = driver.find_element(By.ID, "support-phone")
    assert phone_input.is_displayed()
    phone_input.send_keys("9991234567")
    time.sleep(2)
    assert phone_input.get_attribute("value") == "+7 999 123 45 67"


def test_message_field(driver):
    message_textarea = driver.find_element(By.ID, "support-text")
    assert message_textarea.is_displayed()
    message_textarea.send_keys("Это тестовое сообщение.")
    time.sleep(2)
    assert message_textarea.get_attribute("value") == "Это тестовое сообщение."


def test_privacy_checkbox(driver):
    checkbox = driver.find_element(By.CLASS_NAME, "form-checkbox__fake")
    # Прокрутить к чекбоксу к центру
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    time.sleep(1)
    assert checkbox.is_displayed()
    assert not checkbox.is_selected()

def test_submit_button(driver):
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Отправить')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
    time.sleep(2)
    assert submit_button.is_displayed()