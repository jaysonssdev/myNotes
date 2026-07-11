from playwright.sync_api import Page, expect


# Verify the URL
def test_verifyPageUrl(page: Page):
    page.goto("https://www.google.com/")  # passing url

    # Put the URL in a variable
    my_url = page.url
    print("URL of the application:", my_url)

    expect(page).to_have_url("https://www.google.com/")  # expected url


# Verify the title
def test_verifyTitle(page: Page):
    page.goto("https://www.google.com/")

    # Put the title in a variable
    my_title = page.title()
    print("Title of the page:", my_title)

    expect(page).to_have_title("Google")
