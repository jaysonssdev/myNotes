from playwright.sync_api import Page, expect


def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page).to_have_title("Demo Web Shop")

    # tag#id
    page.locator("input#small-searchterms").fill("macbook pro")
    # tag name is only optional, so you can also write this as:
    # page.locator("#small-searchterms").fill("macbook pro")
    page.wait_for_timeout(3000)

    # tag.class
    page.locator("input.search-box-text").fill("lenovo laptop")
    page.wait_for_timeout(3000)

    # tag[attribute="value"]
    page.locator('input[name="q"]').fill("asus vivobook")
    page.wait_for_timeout(3000)

    # tag.class[attribute="value"]
    page.locator("input.button-1[value=Search]").click()
    page.wait_for_timeout(3000)

    # using SelectorsHub - Rel cssSelector
    page.locator("#As").click()
    page.wait_for_timeout(3000)
