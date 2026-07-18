from playwright.sync_api import Page, expect


def test_xpath_locators(page: Page):
    # 1. Launch the URL
    page.goto("https://demowebshop.tricentis.com/")

    # Absolute xpath (full path) - NOT recommended
    logo = page.locator("//html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
    expect(logo).to_be_visible()

    # 2. Relative xpath (partial path) - recommended
    logo = page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()

    # 3. XPath with contains() Function
    products = page.locator("//h2//a[contains(@href,'computer')]")
    products_count = products.count()

    print("Products count:", products_count)
    expect(products).to_have_count(products_count)

    # To print a specific item
    print(
        "First computer product:", products.first.text_content()
    )  # To get the first product's name by using 'first' and 'text_content' methods
    print("Last computer product:", products.last.text_content())  # Get last
    print(
        "N-th computer product:", products.nth(2).text_content()
    )  # Get 3rd (started at index 0)

    # To print all the items using loop
    product_titles = (
        products.all_text_contents()
    )  # 'all_text_contents' method gets all the items and put them in a list

    print("Print product titles using loop:")
    for i in product_titles:
        print(i)

    # 4. XPath with starts-with() Function
    build_products = page.locator("//h2//a[starts-with(@href,'/build')]")

    print("Build products count:", build_products.count())
    expect(build_products).to_have_count(3)

    # 5. XPath with text() Function - is representing the inner text of the element
    registration_link = page.locator("//a[text()='Register']")
    expect(registration_link).to_be_visible()

    # 6. XPath with last() Function
    google_plus_link = page.locator("//div[@class='column follow-us']//li[last()]")
    expect(google_plus_link).to_have_text("Google+")

    # 7. XPath with position() Function
    twitter_link = page.locator("//div[@class='column follow-us']//li[position()=2]")
    expect(twitter_link).to_have_text("Twitter")

    page.wait_for_timeout(3000)
