# import pandas as pd
# import os


from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("http://127.0.0.1:5000")
    print(page.title())
    # other actions...
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
