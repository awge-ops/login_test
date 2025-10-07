# Playwright Login Test

## Локальный запуск

1. Установить зависимости:
```bash
python -m pip install -r requirements.txt
```

2. Установить браузеры Playwright:
```bash
python -m playwright install
```

3. Запустить все тесты:
```bash
pytest -q
```

4. Запуск конкретного теста:
```bash
pytest -q tests/test_login.py::test_login_saucedemo
```
