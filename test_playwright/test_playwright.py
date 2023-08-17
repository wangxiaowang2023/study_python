# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("http://www.baidu.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)