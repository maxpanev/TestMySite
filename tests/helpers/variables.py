# Валидные email для тестирования
valid_emails = [
        ("test@example.com",  "test@example.com"),
        ("test123@example.com",  "test123@example.com"),
        ("test @example.com",  "test@example.com"),
        ("firsttest.lasttest@domain.co", "firsttest.lasttest@domain.co"),
        ("TEST@EXAMPLE.COM", "TEST@EXAMPLE.COM"),
        ("testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttestttesttesttesttesttest"
         "testtesttestesttesttest@example.com", "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttestttesttesttesttesttest"
         "testtesttestesttesttest@example.com"),
        ("t@example.com", "t@example.com"),
        ("test@example.co", "test@example.co")
    ]

# Невалидные email и ожидаемые сообщения об ошибке
invalid_emails = [
        ("test@example.c", "Неверный формат Email"),
        ("test@example", "Неверный формат Email"),
        ("?test+@,example!.com", "Неверный формат Email"),
        ("мейл", "Неверный формат Email")
    ]

# Валидные номера телефонов для тестирования
valid_phone_numbers = [
    ("9001234567", "+7 900 123 45 67"),
    ("(900)-123-45-67", "+7 900 123 45 67"),
    ("900-123-45-67", "+7 900 123 45 67"),
    ("900 123 45 67", "+7 900 123 45 67"),
    ("(900) 123-45-67 ext.89", "+7 900 123 45 67"),
    ("9001234567891234567", "+7 900 123 45 67")
]

# Невалидные номера телефонов и ожидаемые сообщения об ошибке
invalid_phone_numbers = [
    ("123456", "Неверный формат телефона"),
    ("+7900abc4567", "Неверный формат телефона")
]

# Переменная с положительными тестовыми данными для поля "Имя"
valid_names = [
    ("Иван", "Иван"),
    ("Хуберт Блейн", "ХубертБлейн"),
    ("ИВАН", "ИВАН"),
    ("Иван4", "Иван"),
    ("Ив@н", "Ивн"),
    ("Хуберт Блейн Вольфшлегельштайнхаузенбергердорф-старший", "ХубертБлейнВольфшлег"),
    ("     ", "")
]

# Переменная с отрицательными тестовыми данными для поля "Имя" и ожидаемыми сообщениями об ошибке
invalid_names = [
    ("Ivan", "Введите имя русскими буквами"),
    ("ИванPetrov", "Введите имя русскими буквами"),
    ("И", "Неверный формат имени")
]

# Переменная с положительными тестовыми данными для поля "Сообщение"
valid_messages = [
    ("Привет", "Привет"),
    ("   Три   ", "   Три   "),
    ("!@#$%^&*()_-+=[]{}|;:'\",.<>/?~`", "!@#$%^&*()_-+=[]{}|;:'\",.<>/?~`"),
    ("1234567890", "1234567890"),
    ("Hello my friend", "Hello my friend"),
    ( "Тест с пробелами     внутри     и с переносами\nв новых строках.",
      "Тест с пробелами     внутри     и с переносами\nв новых строках."),
    ("<script>alert('test')</script>", "<script>alert('test')</script>")
]

# Переменная с отрицательными тестовыми данными для поля "Сообщение" и ожидаемыми сообщениями об ошибке
invalid_messages = [
    ("Три", "Минимально допустимое количество символов: 6. Длина текста сейчас: 3.")
]

# Переменная с данными для чекбокса
checkbox_ids = [
    "choices--form_multiselect_CATEGORY_QUESTION-item-choice-2",
    "choices--form_multiselect_CATEGORY_QUESTION-item-choice-3",
    "choices--form_multiselect_CATEGORY_QUESTION-item-choice-4",
    "choices--form_multiselect_CATEGORY_QUESTION-item-choice-5"
]