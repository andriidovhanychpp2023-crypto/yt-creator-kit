from playwright.sync_api import sync_playwright


def test_google_accessibility():
    with sync_playwright() as p:
        # Запуск у headless режимі обов'язковий для CI
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Перевіряємо просто доступ до мережі та роботу браузера
        response = page.goto("https://www.google.com")

        # Якщо статус 200 — значить інтернет є і браузер працює
        assert response.status == 200
        browser.close()
