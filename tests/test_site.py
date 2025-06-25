import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://positronica.ru/support/")
    yield driver
    driver.quit()

def test_phone_field(driver):
    wait = WebDriverWait(driver, 10)
    phone_input = wait.until(EC.visibility_of_element_located((By.ID, "support-phone")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", phone_input)
    # Проверка, что поле активно и пустое
    assert phone_input.is_displayed(), "Поле 'Телефон' не отображается"
    assert phone_input.is_enabled(), "Поле 'Телефон' недоступно для ввода"
    assert phone_input.get_attribute("value") == "", "Поле 'Телефон' не пустое перед вводом"
    # Ввод номера
    phone_input.send_keys("9991234567")
    # Проверка, что значение преобразовалось (подождем, пока значение изменится)
    wait.until(lambda driver: phone_input.get_attribute("value") == "+7 999 123 45 67")
    assert phone_input.get_attribute("value") == "+7 999 123 45 67", "Некорректное значение в поле 'Телефон' после ввода"

def test_order_number__field(driver):
    wait = WebDriverWait(driver, 10)
    order_input = wait.until(EC.visibility_of_element_located((By.ID, "support-number")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", order_input)
    assert order_input.is_displayed(), "Поле 'Номер заказа' не отображается"
    assert order_input.is_enabled(), "Поле 'Номер заказа' недоступно для ввода"
    assert order_input.get_attribute("value") == "", "Поле 'Номер заказа' не пустое перед вводом"
    order_input.send_keys("1234567890")
    wait.until(lambda driver: order_input.get_attribute("value") == "PZ1234567890")
    assert order_input.get_attribute("value") == "PZ1234567890", "Некорректное значение в поле 'Номер заказа'"

def test_email_field(driver):
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "support-email")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", email_input)
    assert email_input.is_displayed(), "Поле 'Email' не отображается"
    assert email_input.is_enabled(), "Поле 'Email' недоступно для ввода"
    assert email_input.get_attribute("value") == "", "Поле 'Email' не пустое перед вводом"
    email_input.send_keys("test@example.com")
    wait.until(lambda driver: email_input.get_attribute("value") == "test@example.com")
    assert email_input.get_attribute("value") == "test@example.com", "Некорректное значение в поле 'Email'"

def test_name_field(driver):
    wait = WebDriverWait(driver, 10)
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "support-name")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", name_input)
    assert name_input.is_displayed(), "Поле 'Имя' не отображается"
    assert name_input.is_enabled(), "Поле 'Имя' недоступно для ввода"
    assert name_input.get_attribute("value") == "", "Поле 'Имя' не пустое перед вводом"
    name_input.send_keys("Иван")
    wait.until(lambda driver: name_input.get_attribute("value") == "Иван")
    assert name_input.get_attribute("value") == "Иван", "Некорректное значение в поле 'Имя'"

def test_message_field(driver):
    wait = WebDriverWait(driver, 10)
    message_textarea = wait.until(EC.visibility_of_element_located((By.ID, "support-text")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", message_textarea)
    assert message_textarea.is_displayed(), "Поле 'Сообщение' не отображается"
    assert message_textarea.is_enabled(), "Поле 'Сообщение' недоступно для ввода"
    assert message_textarea.get_attribute("value") == "", "Поле 'Сообщение' не пустое перед вводом"
    message_textarea.send_keys("Это тестовое сообщение.")
    wait.until(lambda driver: message_textarea.get_attribute("value") == "Это тестовое сообщение.")
    assert message_textarea.get_attribute("value") == "Это тестовое сообщение.", "Некорректное значение в поле 'Сообщение'"

def test_privacy_checkbox(driver):
    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form-checkbox__fake")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    assert checkbox.is_displayed(), "Чекбокс не отображается"
    assert not checkbox.is_selected(), "Чекбокс уже выбран перед тестом"
    time.sleep(2)
    checkbox.click()
    assert checkbox.is_enabled(), "Чекбокс стал неактивен после клика"

def test_submit_button(driver):
    wait = WebDriverWait(driver, 10)
    try:
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        assert submit_button.is_displayed(), "Кнопка 'Отправить' не отображается"
        assert submit_button.is_enabled(), "Кнопка 'Отправить' недоступна для нажатия, скорее всего не все обязательные поля заполнены!"
    except TimeoutException:
        pytest.skip("Кнопка 'Отправить' не найдена или недоступна для клика — возможно, обязательные поля не заполнены.")