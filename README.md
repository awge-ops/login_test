# Playwright login test (portfolio)

## Локальный запуск

1. Установить зависимости:

```bash
python -m pip install -r requirements.txt

python -m playwright install

export BASE_URL="https://your-site.com"
export TEST_USER="user@example.com"
export TEST_PASS="Password123"

pytest -q
