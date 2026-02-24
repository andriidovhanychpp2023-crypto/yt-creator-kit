from playwright.sync_api import sync_playwright


def test_add_brainrot_meme_scenario():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Відкриваємо сайт
        page.goto("https://www.google.com")

        # Критичний шлях: пошук "хайпового" контенту
        search_field = page.locator("textarea[name='q']")
        search_field.fill("Skibidi Rizz")
        page.keyboard.press("Enter")

        # Чекаємо, поки з'являться результати (елемент #search)
        page.wait_for_selector("#search", timeout=15000)

        # ПЕРЕВІРКА: чи видимий блок з результатами
        results = page.locator("#search")
        assert results.is_visible()

        page.wait_for_timeout(10000)

        browser.close()
