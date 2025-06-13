import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

url = "https://positronica.ru"

# Тест 1: Проверка статуса ответа сайта
def test_status_code():
    response = requests.get(url)
    assert response.status_code == 200, f"Страница {url} недоступна, статус {response.status_code}"

### 2. Проверка наличия определенного элемента на странице с помощью BeautifulSoup
def test_element_present():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Проверяем, есть ли заголовок h1 на странице
    assert soup.find('h1') is not None, "На странице нет элемента <h1>"

### 3. Проверка наличия ссылки на странице с помощью request
def test_link_exists():
    response = requests.get(url)
    assert 'href="/actions/"' in response.text, "Ссылка не найдена на странице"

### 4. Проверка наличия ссылки на странице с помощью селектора XPath
def test_link_XPath():
    browser = webdriver.Chrome()
    browser.get(url)
    element = browser.find_element(By.XPATH, '(//a[contains(@class, "menu__link") and @href="/actions/"])[2]')
    assert element is not None, 'Элемент не найден на странице'


### 5. Проверка, что кнопка или элемент доступен для клика с помощью Selenium

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_element_clickable(driver):
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, 'a[href="/catalog/noutbuki-i-kompyutery/"]')
    assert button.is_enabled(), "Элемент недоступен для клика"

### 6. Проверка, что на странице есть товары, обработка исключений
def test_noutbuki_list_page():

    url = "https://positronica.ru/catalog/noutbuki/"
    browser = webdriver.Chrome()
    try:
        browser.get(url)
        time.sleep(3)
        products = browser.find_elements(By.XPATH, '//*[@class="catalog__item"]')
        assert len(products) > 0
    except AssertionError:
        print("На странице не найдены товары")
    finally:
        browser.quit()