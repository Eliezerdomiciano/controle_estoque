# import pandas as pd
# import os


import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:5000/")
    time.sleep(5)
    page.locator(".menu .fas.fa-bolt").click()
    page.locator("#inputSerialNumber4 >> nth=0").click()
    page.locator("#inputSerialNumber4 >> nth=0").fill("Serial Number")
    page.locator("#inputPartNumber4 >> nth=0").click()
    page.locator("#inputPartNumber4 >> nth=0").fill("part Number")
    page.locator("#inputPosicao >> nth=0").click()
    page.locator("#inputPosicao >> nth=0").fill("Posição")

    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
