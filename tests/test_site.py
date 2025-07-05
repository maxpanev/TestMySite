import pytest
from helpers.functions import fill_field, fill_incorrect_field, find_link, return_to_start, clear_field, click_checkbox
from helpers.variables import (valid_emails, invalid_emails, valid_phone_numbers, invalid_phone_numbers,
                               valid_names, invalid_names, valid_messages, invalid_messages, checkbox_ids)
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
def close_popup(wait):
    # Автоматическое закрытие всплывающих окон перед каждым тестом, если они есть
    try:
        close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Закрыть')]")))
        close_btn.click()
    except:
        # Если окно уже закрыто или кнопка не найдена, ничего не делаем
        pass

class TestFormSubmission:
    # ТЕСТ-КЕЙС №1
    def test_full_form_submission(self, driver, wait):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        fill_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        fill_field(driver, wait, "support-name", "Иван", "Иван")
        fill_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Поставить галочку
        checkbox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "form-checkbox__fake")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
        time.sleep(0.5)  # небольшая задержка
        checkbox.click()
        # Проверить, что кнопка активна
        submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert submit_btn.is_enabled()

    # ТЕСТ-КЕЙС №2
    def test_empty_form_submission(self, driver, wait):
        # Импорт функции clear_field из каталога helpers
        clear_field(driver, wait, "support-email", "ivanov@mail.ru", "ivanov@mail.ru")
        clear_field(driver, wait, "support-phone", "999 123 45 67", "+7 999 123 45 67")
        clear_field(driver, wait, "support-name", "Иван", "Иван")
        clear_field(driver, wait, "support-text", "Тестовое сообщение", "Тестовое сообщение")
        # Проверить, что кнопка неактивна
        submit_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Отправить')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
        time.sleep(0.5)  # небольшая задержка, чтобы страница "подтянулась"
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()

# ТЕСТ-КЕЙСЫ с положительнами значениями
class TestValidInputs:
    # ТЕСТ-КЕЙС №3
    @pytest.mark.parametrize("value_1, value_2", valid_emails) # Импорт переменной valid_emails из каталога helpers
    def test_valid_email(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-email", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-email")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

    # ТЕСТ-КЕЙС №4
    @pytest.mark.parametrize("value_1, value_2", valid_phone_numbers) # Импорт переменной valid_phone_numbers из каталога helpers
    def test_valid_phone(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-phone", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-phone")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

    # ТЕСТ-КЕЙС №5
    @pytest.mark.parametrize("value_1, value_2", valid_names) # Импорт переменной valid_names из каталога helpers
    def test_valid_names(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-name", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-name")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

    # ТЕСТ-КЕЙС №6
    @pytest.mark.parametrize("value_1, value_2", valid_messages) # Импорт переменной valid_messages из каталога helpers
    def test_valid_messages(self, driver, wait, value_1, value_2):
        # Импорт функции fill_field из каталога helpers
        fill_field(driver, wait, "support-text", value_1, value_2)
        # После заполнения поля проверяем значение
        element = wait.until(EC.visibility_of_element_located((By.ID, "support-text")))
        current_value = element.get_attribute("value")
        assert current_value == value_2, f"Ожидалось значение: '{value_2}', но получили: '{current_value}'"

# ТЕСТ-КЕЙСЫ с отрицательнами значениями
class TestInvalidInputs:
    # ТЕСТ-КЕЙС №3
    @pytest.mark.parametrize("value, expected_error", invalid_emails) # Импорт переменной invalid_emails из каталога helpers
    def test_invalid_email(self, driver, wait, value, expected_error):
        # Импорт функции fill_incorrect_field из каталога helpers
        fill_incorrect_field(driver, wait, "support-email", value)
        # Проверяем, что ошибка отображается правильно
        # error_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "hf-warning")))
        error_element = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[contains(@class, 'hf-warning') and text() = 'Неверный формат Email']")))
        assert error_element.text == expected_error, f"Текст ошибки не соответствует ожидаемому: {expected_error}"

    # ТЕСТ-КЕЙС №4
    @pytest.mark.parametrize("value, expected_error", invalid_phone_numbers) # Импорт переменной invalid_phone_numbers из каталога helpers
    def test_invalid_phone(self, driver, wait, value, expected_error):
        # Импорт функции fill_incorrect_field из каталога helpers
        fill_incorrect_field(driver, wait, "support-phone", value)
        # Проверяем, что ошибка отображается правильно
        # error_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "hf-warning")))
        error_element = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[contains(@class, 'hf-warning') and text() = 'Неверный формат телефона']")))
        assert error_element.text == expected_error, f"Текст ошибки не соответствует ожидаемому: {expected_error}"

    # ТЕСТ-КЕЙС №5
    @pytest.mark.parametrize("value, expected_error", invalid_names) # Импорт переменной invalid_names из каталога helpers
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

    # ТЕСТ-КЕЙС №6
    @pytest.mark.parametrize("value, expected_error", invalid_messages) # Импорт переменной invalid_messages из каталога helpers
    def test_invalid_messages(self, driver, wait, value, expected_error):
        # Импорт функции fill_incorrect_field из каталога helpers
        fill_incorrect_field(driver, wait, "support-text", value)
        # Проверяем, что ошибка отображается правильно
        error_element = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//div[contains(@class, 'hf-warning') and text() = 'Минимально допустимое количество символов: 6. "
                      "Длина текста сейчас: 3.']")))
        assert error_element.text == expected_error, f"Текст ошибки не соответствует ожидаемому: {expected_error}"

class TestLinks:
    # ТЕСТ-КЕЙС №7
    def test_marketplace_claims_link(self, driver, wait):
        # Импорт функции find_link из каталога helpers
        find_link(driver, wait, ".button.button_small.button_border")
        assert driver.current_url == "https://positronica.ru/pretenzii-po-zakazam-s-markepleysov/", "Страница не соответствует ожидаемой"
        # Импорт функции return_to_start из каталога helpers
        return_to_start(driver)

    # ТЕСТ-КЕЙС №7
    def test_logo_link(self, driver, wait):
        # Импорт функции find_link из каталога helpers
        find_link(driver, wait, ".logo__icon.logo__icon_logo.icon.icon_logo")
        assert driver.current_url == "https://positronica.ru/", "Страница не соответствует ожидаемой"
        # Импорт функции return_to_start из каталога helpers
        return_to_start(driver)

    # ТЕСТ-КЕЙС №9
    def test_return_link(self, driver, wait):
        # Импорт функции find_link из каталога helpers
        find_link(driver, wait, ".breadcrumbs__link")
        assert driver.current_url == "https://positronica.ru/", "Страница не соответствует ожидаемой"
        # Импорт функции return_to_start из каталога helpers
        return_to_start(driver)

class TestCheckbox:
    # ТЕСТ-КЕЙС №10
    @pytest.mark.parametrize("checkbox_id", checkbox_ids) # Импорт переменной checkbox_ids из каталога helpers
    def test_select_category_checkbox(self, driver, wait, checkbox_id):
        # Импорт функции lick_checkbox из каталога helpers
        click_checkbox(driver, wait, checkbox_id)
