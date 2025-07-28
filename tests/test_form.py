import pytest
from helpers.functions import (fill_field, find_link, return_to_start, clear_field, select_category,
                               click_checkbox, click_button)
from data.variables import (ValidVariables as vv, InvalidVariables as iv, empty_fields, checkbox_ids)
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
        for field_id, value_1, value_2 in vv.valid_fields:
            fill_field(driver, wait, field_id, value_1, value_2)
        # После заполнения всех полей - кликаем чекбокс
        click_checkbox(driver, wait)
        # Проверить, что кнопка активна
        submit_btn = click_button(driver, wait)
        assert submit_btn.is_displayed()
        assert submit_btn.is_enabled()

    # ТЕСТ-КЕЙС №2
    def test_empty_form_submission(self, driver, wait):
        # Импорт функции clear_field из каталога helpers
        for field_id in empty_fields:
            clear_field(driver, wait, field_id)
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка неактивна
        submit_btn = click_button(driver, wait)
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()

    # ТЕСТ-КЕЙС №3
    def test_incorrect_form_submission(self, driver, wait):
        # Импорт функции fill_field из каталога helpers
        for field_id, value_1, value_2 in iv.invalid_fields:
            fill_field(driver, wait, field_id, value_1, value_2)
        # Поставить галочку
        click_checkbox(driver, wait)
        # Проверить, что кнопка неактивна
        submit_btn = click_button(driver, wait)
        assert submit_btn.is_displayed()
        assert not submit_btn.is_enabled()


class TestLinks:
    # ТЕСТ-КЕЙС №4
    def test_marketplace_claims_link(self, driver, wait):
        # Импорт функции find_link из каталога helpers
        find_link(driver, wait, ".button.button_small.button_border")
        assert driver.current_url == "https://positronica.ru/pretenzii-po-zakazam-s-markepleysov/", "Страница не соответствует ожидаемой"
        # Импорт функции return_to_start из каталога helpers
        return_to_start(driver)

    # ТЕСТ-КЕЙС №5
    def test_logo_link(self, driver, wait):
        # Импорт функции find_link из каталога helpers
        find_link(driver, wait, ".logo__icon.logo__icon_logo.icon.icon_logo")
        assert driver.current_url == "https://positronica.ru/", "Страница не соответствует ожидаемой"
        # Импорт функции return_to_start из каталога helpers
        return_to_start(driver)

    # ТЕСТ-КЕЙС №6
    def test_return_link(self, driver, wait):
        # Импорт функции find_link из каталога helpers
        find_link(driver, wait, ".breadcrumbs__link")
        assert driver.current_url == "https://positronica.ru/", "Страница не соответствует ожидаемой"
        # Импорт функции return_to_start из каталога helpers
        return_to_start(driver)


class TestCheckbox:
    # ТЕСТ-КЕЙС №7
    @pytest.mark.parametrize("checkbox_id", checkbox_ids) # Импорт переменной checkbox_ids из каталога helpers
    def test_select_category_checkbox(self, driver, wait, checkbox_id):
        # Импорт функции select_category из каталога helpers
        select_category(driver, wait, checkbox_id)
        # повторно ищем чекбокс, чтобы избежать проблем со stale element
        checkbox = wait.until(EC.element_to_be_clickable((By.ID, checkbox_id)))
        assert checkbox.is_enabled(), f"Чекбокс {checkbox_id} стал неактивен после клика"
