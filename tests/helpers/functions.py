from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_field(driver, wait, field_id, value_1, value_2):
    # Ждет, пока поле станет видимым, заполняет его и ожидает, что значение обновится
    element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)
    element.clear()
    element.click()
    element.send_keys(value_1)
    wait.until(lambda d: element.get_attribute("value") == value_2)

def fill_incorrect_field(driver, wait, field_id, value):
    # Ждет, пока поле станет видимым, заполняет его неправильным значением и триггерит проверку ошибок
    element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(1)
    element.clear()
    element.click()
    time.sleep(0.5)
    element.send_keys(value)
    # Кликает за пределами поля для активации проверки ошибок
    body = driver.find_element(By.TAG_NAME, 'body')
    body.click()

def open_dropdown(wait, index=1):
    # Открывает выпадающий список по указанному индексу
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".choices[data-type*=select-one]")))
    dropdown = elements[index]
    dropdown.click()
    time.sleep(2)
    return dropdown

def select_option_by_text(wait, text):
    # Выбирает опцию из выпадающего списка по тексту
    option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, f"//div[contains(@class, 'choices__list')]//div[text()='{text}']")))
    option.click()
    time.sleep(2)

def select_category(driver, wait, checkbox_id):
    # Выбирает категорию по идентификатору чекбокса
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, checkbox_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    checkbox.click()

def click_checkbox(driver, wait):
    # Кликает по чекбоксу с классом 'form-checkbox__fake'
    checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form-checkbox__fake")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
    time.sleep(0.5)
    checkbox.click()

def click_button(driver, wait):
    # Находит и кликает по кнопке "Отправить"
    submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    time.sleep(0.5)
    return submit_btn

def clear_field(driver, wait, field_id):
    # Ждет, пока поле станет видимым, очищает его
    element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.5)
    element.click()
    element.clear()

def find_link(driver, wait, link_selector):
    # Ищет и переходит по ссылке по CSS-селектору
    link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, link_selector)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
    time.sleep(0.5)
    link.click()

def return_to_start(driver):
    # Возвращает браузер на стартовую страницу
    driver.get("https://positronica.ru/support/")
    WebDriverWait(driver, 10).until(lambda d: d.current_url == "https://positronica.ru/support/")