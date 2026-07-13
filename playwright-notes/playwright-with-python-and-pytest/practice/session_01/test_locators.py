import re  # when you want to use Regular Expressions (Regex)

from playwright.sync_api import Page, expect


def test_verify_locators(page: Page):
    page.goto("https://playwright.dev/python/")
    # use 'wait for timeout' to pause and see the page for a specified time. This is not required.
    page.wait_for_timeout(3000)  # 3000ms = 3 seconds

    # page.get_by_alt_text()
    logo = page.get_by_alt_text("Chromium, Firefox, WebKit")
    expect(logo).to_be_visible()

    # page.get_by_text(), you can choose on the 3 examples below
    expect(page.get_by_text("Any browser. Any platform.")).to_be_visible()  # full text
    expect(page.get_by_text("Any browser. Any")).to_be_visible()  # partial text
    expect(
        page.get_by_text(re.compile(".*browser. Any.*"))
    ).to_be_visible()  # use re.compile() if you want to use regex

    # page.get_by_role()
    page.goto("https://practice.expandtesting.com/locators")
    role = page.get_by_role("button", name="Add Item")
    expect(role).to_be_visible()

    # page.get_by_label()
    page.get_by_label("Choose a country").select_option(label="Japan")
    page.get_by_label("Email for newsletter").fill("name@test.com")

    # page.get_by_placeholder()
    page.get_by_placeholder("Search the site").fill("Hello!")

    # page.get_by_title()
    page.get_by_title("Refresh content").click()

    # page.get_by_test_id()
    expect(page.get_by_test_id("status-message")).to_contain_text(
        "All systems operational"
    )
    expect(page.get_by_test_id("status-message")).to_have_class("alert alert-success")
    page.wait_for_timeout(3000)  # 3000ms = 3 seconds
