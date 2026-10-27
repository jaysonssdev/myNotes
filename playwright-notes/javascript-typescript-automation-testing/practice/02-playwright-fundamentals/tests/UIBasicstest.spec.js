const { test, expect } = require('@playwright/test');

// Long version, use {browser} when you want to add cookies on your browser

test('Browser Context Playwright test', async ({ browser }) => {
    const context = await browser.newContext(); // you can add cookies here if needed
    const page = await context.newPage();
    await page.goto("https://practice.expandtesting.com/login");
});


// Short version, use {page} if you want a fresh instance of the browser

test('Login test - Correct Credentials', async ({ page }) => {
    await page.goto("https://practice.expandtesting.com/login");

    // get title - assertion
    console.log(await page.title());
    await expect(page).toHaveTitle("Test Login Page for Automation Testing Practice");

    // login - correct credentials
    await page.locator("#username").fill("practice");
    await page.locator("#password").fill("SuperSecretPassword!");
    await page.locator("#submit-login").click();

});

test.only('Login test - Wrong Credentials', async ({ page }) => {

    await page.goto("https://practice.expandtesting.com/login");

    // login - wrong password
    const userName = page.locator("#username")
    const passWord = page.locator("#password")
    const loginButton = page.locator("#submit-login")
    const errorMessage = page.locator("#flash")

    await userName.fill("practice");
    await passWord.fill("WrongPassword!");
    await loginButton.click();
    console.log(await errorMessage.textContent());
    await expect(errorMessage).toContainText("Your password is invalid!");

});