import pytest
from helpers.functions import (fill_field, fill_incorrect_field, open_dropdown, select_option_by_text,
                               clear_field, click_checkbox)
from data.variables import (ValidVariables as vv, InvalidVariables as iv)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(scope="module")
def driver():
    # Инициализация веб-драйвера Chrome для всей тестовой сессии модуля
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://positronica.ru/support/")  # Открытие стартовой страницы
    yield driver
    driver.quit()  # Закрытие браузера после завершения тестов модуля


@pytest.fixture(scope="function")
def wait(driver):
    # Создание объекта ожидания для использования в отдельных тестах
    return WebDriverWait(driver, 10)


@pytest.fixture(autouse=True)
def refresh_page(driver):
    # Обновление страницы перед каждым тестом
    driver.refresh()


@pytest.fixture(autouse=True)
def close_popup(wait, driver):
    # Автоматическое закрытие всплывающих окон перед каждым тестом, если они есть
    try:
        close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Закрыть')]")))
        close_btn.click()
    except:
        # Если окно уже закрыто или кнопка не найдена, ничего не делаем
        pass


# ТЕСТ-КЕЙСЫ с положительными значениями
class TestValidInputs:

    # ТЕСТ-КЕЙС №4
    @pytest.mark.parametrize("value_1, value_2", vv.valid_order_numbers)  # Импорт переменной valid_phone_numbers из каталога helpers
    def test_valid_order(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-number", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-number")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

    # ТЕСТ-КЕЙС №5
    def test_select_city(self, driver, wait):
        dropdown = open_dropdown(wait, index=1)
        select_option_by_text(wait, "Омск")
        selected_text = dropdown.text
        assert "Омск" in selected_text, f"Выбранный город: {selected_text} не совпадает с ожидаемым"

    def test_input_city(self, driver, wait):
        dropdown = open_dropdown(wait, index=1)
        input_field = wait.until(EC.element_to_be_clickable((By.NAME, "search_terms")))
        input_field.send_keys("Омск")
        input_field.click()
        select_option_by_text(wait, "г Омск, Омская обл")
        selected_text = dropdown.text
        assert "г Омск, Омская обл" in selected_text, f"Выбранный город: {selected_text} не совпадает с ожидаемым"

    # ТЕСТ-КЕЙС №6
    @pytest.mark.parametrize("value_1, value_2", vv.valid_emails) # Импорт переменной valid_emails из каталога helpers
    def test_valid_email(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-email")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

    # ТЕСТ-КЕЙС №7
    @pytest.mark.parametrize("value_1, value_2", vv.valid_phone_numbers) # Импорт переменной valid_phone_numbers из каталога helpers
    def test_valid_phone(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-phone", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-phone")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

    # ТЕСТ-КЕЙС №8
    @pytest.mark.parametrize("value_1, value_2", vv.valid_names) # Импорт переменной valid_names из каталога helpers
    def test_valid_names(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-name", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-name")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

    # ТЕСТ-КЕЙС №9
    @pytest.mark.parametrize("value_1, value_2", vv.valid_messages) # Импорт переменной valid_messages из каталога helpers
    def test_valid_messages(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-text", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-text")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"


# ТЕСТ-КЕЙСЫ с отрицательнами значениями
class TestInvalidInputs:
    # ТЕСТ-КЕЙС №6
    @pytest.mark.parametrize("value, expected_error", iv.invalid_emails) # Импорт переменной invalid_emails из каталога helpers
    def test_invalid_email(self, driver, wait, value, expected_error):
        # Импорт функции fill_incorrect_field из каталога helpers
        fill_incorrect_field(driver, wait, "support-email", value)
        error_element = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[contains(@class, 'hf-warning') and text() = 'Неверный формат Email']")))
        assert error_element.text == expected_error, f"Текст ошибки не соответствует ожидаемому: {expected_error}"

    # ТЕСТ-КЕЙС №7
    @pytest.mark.parametrize("value, expected_error", iv.invalid_phone_numbers) # Импорт переменной invalid_phone_numbers из каталога helpers
    def test_invalid_phone(self, driver, wait, value, expected_error):
        # Импорт функции fill_incorrect_field из каталога helpers
        fill_incorrect_field(driver, wait, "support-phone", value)
        # Проверяем, что ошибка отображается правильно
        # error_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "hf-warning")))
        error_element = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[contains(@class, 'hf-warning') and text() = 'Неверный формат телефона']")))
        assert error_element.text == expected_error, f"Текст ошибки не соответствует ожидаемому: {expected_error}"

    # ТЕСТ-КЕЙС №8
    @pytest.mark.parametrize("value, expected_error", iv.invalid_names) # Импорт переменной invalid_names из каталога helpers
    def test_invalid_names(self, driver, wait, value, expected_error):
        # Импорт функции fill_incorrect_field из каталога helpers
        fill_incorrect_field(driver, wait, "support-name", value)
        # Находим все элементы с классом 'hf-warning'
        warning_elements = driver.find_elements(By.CLASS_NAME, 'hf-warning')
        error_found = False
        for warning in warning_elements:
            # Проверяем, содержит ли текст один из ожидаемых вариантов
            warning_text = warning.text.strip()
            if warning_text == expected_error or warning_text in ["Введите имя русскими буквами", "Неверный формат имени"]:
                error_found = True
                break
        assert error_found, f"Ошибка '{expected_error}' не найдена среди предупреждений."

    # ТЕСТ-КЕЙС №9
    @pytest.mark.parametrize("value, expected_error", iv.invalid_messages) # Импорт переменной invalid_messages из каталога helpers
    def test_invalid_messages(self, driver, wait, value, expected_error):
        # Импорт функции fill_incorrect_field из каталога helpers
        fill_incorrect_field(driver, wait, "support-text", value)
        # Проверяем, что ошибка отображается правильно
        error_element = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[contains(@class, 'hf-warning') and text() = 'Минимально допустимое количество символов: 6. "
                      "Длина текста сейчас: 3.']")))
        assert error_element.text == expected_error, f"Текст ошибки не соответствует ожидаемому: {expected_error}"


# ТЕСТ-КЕЙСЫ с пустыми значениями
class TestEmptyFields:
    # ТЕСТ-КЕЙС №10
    def test_empty_field_email(self, driver, wait):
        # Импорт функции fill_field из каталога helpers
        clear_field(driver, wait, "support-email")
        fill_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        fill_field(driver, wait, "support-name", "Иван", "Иван")
        fill_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        submit_btn.click()
        time.sleep(1)
        error_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "errortext")))
        assert error_element.text == 'Не заполнены следующие обязательные поля:\n  » "E-mail"', f"Текст ошибки не соответствует ожидаемому"

    def test_empty_field_phone(self, driver, wait):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        clear_field(driver, wait, "support-phone")
        fill_field(driver, wait, "support-name", "Иван", "Иван")
        fill_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()

    def test_empty_field_name(self, driver, wait):
        # БАГ ФОРМЫ! AssertionError! Сообщить разработчикам!
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        fill_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        clear_field(driver, wait, "support-name")
        fill_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()

    def test_empty_field_text(self, driver, wait):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        fill_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        fill_field(driver, wait, "support-name", "Иван", "Иван")
        clear_field(driver, wait, "support-text")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()
        checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form-checkbox__fake")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
        time.sleep(0.5)  # небольшая задержка
        checkbox.click()


# ТЕСТ-КЕЙСЫ с некорректными значениями
class TestIncorrectFields:
    # ТЕСТ-КЕЙС №11
    def test_incorrect_field_email(self, driver, wait):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "test@example.c", "test@example.c")
        fill_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        fill_field(driver, wait, "support-name", "Иван", "Иван")
        fill_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()

    def test_incorrect_field_phone(self, driver, wait):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        fill_field(driver, wait, "support-phone", "+7900abc4567", "+7 790 045 67   ")
        fill_field(driver, wait, "support-name", "Иван", "Иван")
        fill_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()

    def test_incorrect_field_name(self, driver, wait):
        # БАГ ФОРМЫ! AssertionError! Сообщить разработчикам!
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        fill_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        fill_field(driver, wait, "support-name", "Ivan", "Ivan")
        fill_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()

    def test_incorrect_field_text(self, driver, wait):
        # БАГ ФОРМЫ! AssertionError! Сообщить разработчикам!
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        fill_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        fill_field(driver, wait, "support-name", "Иван", "Иван")
        fill_field(driver, wait, "support-text", "Тест", "Тест")
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()