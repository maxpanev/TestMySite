### Тест-кейс №11: Проверка обработки валидных email-адресов

**ID:** TC011  
**Название:** Проверка валидных значений для поля Email

### Предварительные условия
- Страница формы загружена
- Поле "Email "пустое

### Проверяемые значения:
- `test@example.com` — ввод валидного email.
- `test123@example.com` — ввод валидного email с цифрами.
- `test @example.com` - пробелы автоматически удаляются, ввод валидного email.
- `firsttest.lasttest@domain.co` — ввод многоуровневого валидного email.
- `TEST@EXAMPLE.COM` — ввод валидного email в верхнем регистре.
- `testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttestttesttesttesttesttest
testtesttestesttesttest@example.com` - максимально допустимая длина, ввод валидного email.
- `t@example.com` - минимально допустимая длина, ввод валидного email.
- `test@example.co` - сжатие домена до двух символов, email принимается.


### Ожидаемый результат:
- При вводе валидного email адреса сообщение об ошибке отсутствует, поле выделяется зеленой рамкой.
