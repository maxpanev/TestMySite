from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_field(driver, wait, field_id, value_1, value_2):
    # Ждем, пока элемент станет видимым
    element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    # Добавляем небольшую задержку, чтобы страница успела отреагировать
    time.sleep(1)
    element.clear()
    element.click()
    element.send_keys(value_1)
    wait.until(lambda d: element.get_attribute("value") == value_2)


def fill_incorrect_field(driver, wait, field_id, value):
    # Ждем, пока элемент станет видимым
    element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)  # задержка для стабилизации
    element.clear()
    element.click()
    time.sleep(0.5)
    element.send_keys(value)
    # Кликаем за пределами поля, чтобы сработала проверка ошибок
    body = driver.find_element(By.TAG_NAME, 'body')
    body.click()

def click_checkbox(driver, wait, checkbox_id):
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, checkbox_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    checkbox.click()
    # повторно ищем чекбокс, чтобы избежать проблем со stale element
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, checkbox_id)))
    assert checkbox.is_enabled(), f"Чекбокс {checkbox_id} стал неактивен после клика"

def clear_field(driver, wait, field_id, value_1, value_2):
    # Ждем, пока элемент станет видимым
    element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    # Добавляем небольшую задержку, чтобы страница успела отреагировать
    time.sleep(0.5)
    element.click()
    element.clear()

def find_link(driver, wait, link_selector):
    link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, link_selector)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
    time.sleep(0.5)
    link.click()

def return_to_start(driver):
    driver.get("https://positronica.ru/support/")
    WebDriverWait(driver, 10).until(lambda d: d.current_url == "https://positronica.ru/support/")