#!/usr/bin/env python3

from playwright.sync_api import sync_playwright
import time
from loguru import logger


logger.remove()
logger.add('run.log', rotation='4MB')

# play_playwright() starts the browser and visits the target website

def play_playwright():

    logger.info('Firing Browser...')

    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()

    logger.info('Visiting the target website...')
    page1.goto('https://www.ioba.org/members-directory')

    return browser, page1

# extraction() is meant for rendering the dynamic javascript for the website
# after rendering, this function is parsing the tags and extracting the data

def extraction(browser, page1):

    logger.info('Finding master container of data needed...')

    container = page1.locator('._FiCX').first.wait_for(state='visible')

    container = page1.locator('._FiCX').all()

    logger.info('Starting main extraction loop...')

    for x in container:

        title = x.locator('span[style="font-weight:bold;"]').first

        title_p = title.inner_text()

        print(title_p)

        email = x.locator('span[style="font-size:14px;"] a').first

        email_p = email.inner_text(timeout=1000) if email.count() > 0 else 'N/A'

        print(email_p)

        number = x.locator('span[style="font-size:14px;"]').nth(1)

        number_p = number.inner_text()

        print(number_p)

        address = x.locator('span[style="font-size:14px;"]').nth(2)

        address_p = address.inner_text()

        print(address_p)

        print()

    next_button = page1.locator('a[aria-label="Next"]')

    last_page = page1.locator('div[class*="currentPage"]').last

    last_page_name = last_page.inner_text()

    return next_button, last_page_name

# pagination() handles the logic for changing the page and waiting

def pagination(next_button):

    logger.info('Trying to change the page...') 

    next_button.click()

    logger.info('')

    time.sleep(3)


# This is the initialization phase of the entire script

with sync_playwright() as p:

    init_browser = play_playwright()

    browser, page1 = init_browser

    loop = True

    loop_count = 0

    while loop:

        loop_count += 1

        extract_data, last_page = extraction(browser, page1)

        print(loop_count)
        print(last_page)

        change_page = pagination(extract_data)

        if loop_count == int(last_page):

            loop = False

    browser.close()
