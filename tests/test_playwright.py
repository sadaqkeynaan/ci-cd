from playwright.sync_api import sync_playwright

def test_open_page():
    with sync_playwright() as p:
        # Starta Chromium webbläsare headless
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Gå till sidan
        page.goto("https://test-379574553568.us-central1.run.app/")
        
        # Kontrollera att sidan har en titel (exempelvis att den inte är tom)
        assert page.title() != ""
        
        # Stäng webbläsaren
        browser.close()
        