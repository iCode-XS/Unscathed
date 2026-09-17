#!/usr/bin/env python3

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()

    page1.goto('https://www.ioba.org/members-directory')

    container = page1.locator('._FiCX').first.wait_for(state='visible')

    container = page1.locator('._FiCX').all()

    for x in container:

        title = x.locator('span[style="font-weight:bold;"]').first

        title_p = title.inner_text()

        print(title_p)

        email = x.locator('span[style="font-size:14px;"] a').first

        email_p = email.inner_text()

        print(email_p)

        number = x.locator('span[style="font-size:14px;"]').nth(1)

        number_p = number.inner_text()

        print(number_p)

        address = x.locator('span[style="font-size:14px;"]').nth(2)

        address_p = address.inner_text()

        print(address_p)

        print()

    next_button = page1.locator('a[aria-label="Next"]')

    if next_button:

        next_button.click()

    time.sleep(5)

    browser.close()
