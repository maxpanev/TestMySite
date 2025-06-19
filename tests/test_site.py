import requests
import pytest
from bs4 import BeautifulSoup

base_url = "https://positronica.ru/support/"

# Добавляем фикстуру `response`, которая делает один запрос и передается во все тесты
@pytest.fixture
def response():
    return requests.get(base_url)

# Тест 1: Проверка статуса ответа страницы
def test_status_code(response):
    assert response.status_code == 200, f"Страница {base_url} недоступна, статус {response.status_code}"

# Тест 2: Проверка наличия элемента заголовка h1 на странице
def test_h1_element_present(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.find('h1')
    assert h1 is not None, "Элемент <h1> не найден на странице"
    header_text = h1.get_text(strip=True)
    assert header_text in ["Поддержка", "Support"], "Заголовок <h1> не совпадает с ожидаемыми вариантами"

# Тест 3: Проверка наличия конкретной ссылки на странице
def test_support_page_contains_contact_link(response):
    assert 'href="/kontakty/"' in response.text, "Ссылка на страницу контактов не найдена"

# Тест 4: Проверка, что изображение существует
def test_image_exists(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    img = soup.find('img', title='Поддержка')
    assert img is not None, "Изображение с title='Поддержка' не найдено"

# Тест 5: Проверка, что есть телефон поддержки
def test_support_phone_exists(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    support_texts = soup.find_all(text=True)
    phone_found = any('телефон' in text.lower() or '+' in text for text in support_texts)
    assert phone_found, "Информация о телефоне поддержки не найдена на странице"