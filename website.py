#!/usr/bin/env python3

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()

    page1.goto('https://www.ioba.org/members-directory')

    container = page1.locator('._FiCX').first

    wait1 = container.wait_for(state='visible')

    title = container.locator('span[style="font-weight:bold;"]').first

    x = title.inner_text()

    print(x)

    browser.close()
