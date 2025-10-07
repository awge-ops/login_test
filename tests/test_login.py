from playwright.sync_api import sync_playwright

def test_example():
    assert True


def test_login_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        # Вводим логин и пароль
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # Кликаем по кнопке входа
        page.click("#login-button")

        # Проверяем, что произошёл переход на страницу каталога
        assert "inventory" in page.url

        browser.close()
