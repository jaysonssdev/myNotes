const { test, expect } = require('@playwright/test');

// Test to select Option 2 from a dropdown list
test('UI Dropdown', async ({ page }) => {
    const url = "https://practice.expandtesting.com/dropdown";
    const dropdownSimple = page.locator("#dropdown");

    await page.goto(url);

    // Select dropdown
    await dropdownSimple.selectOption("2"); // put here the option value
    // Assert if option value 2 is selected
    await expect(dropdownSimple).toHaveValue("2");
    // Just to see what's happening if you are in headed mode
    await page.pause();
});

// Test if radio button black is selected
test('UI Radio Button - Select black color', async ({ page }) => {
    const url = "https://practice.expandtesting.com/radio-buttons";
    const radioButtonColor = page.locator("#black");

    await page.goto(url);

    // Select radio button black
    await radioButtonColor.click();
    // Assert if black is selected
    await expect(radioButtonColor).toBeChecked();
});

// Test if checkbox 1 is checked and checkbox 2 is NOT checked
test('UI Check Boxes', async ({ page }) => {
    const url = "https://practice.expandtesting.com/checkboxes";
    const checkBox1 = page.locator("#checkbox1");
    const checkBox2 = page.locator("#checkbox2");

    await page.goto(url); // Checkbox 2 is checked by default

    // Select the first checkbox to check it
    await checkBox1.click();
    // Select the second checkbox to uncheck it
    await checkBox2.click();
    // Assert if checkbox 1 is checked and checkbox 2 is not selected anymore
    await expect(checkBox1).toBeChecked();
    await expect(checkBox2).not.toBeChecked();
});

// Test to click a redirect link and check if the text title "Status Codes" exists on this webpage
test('UI Redirect Link - Same page window', async ({ page }) => {
    const url1 = "https://practice.expandtesting.com/redirector";
    const url2 = "https://practice.expandtesting.com/status-codes";
    const redirectLink = page.locator("#redirect");
    const textTitle = page.locator("//h1[contains(text(),'Status Codes')]");

    await page.goto(url1);

    // Click the redirect link
    await redirectLink.click();

    // Assert we are now on url2 and the "Status Codes" title is present
    await expect(page).toHaveURL(url2);
    await expect(textTitle).toBeVisible();
    await expect(textTitle).toHaveText("Status Codes");
});

// Let's say the redirect link opens on a new tab or browser window
test('UI Redirect Link - New Tab', async ({ page, context }) => {
    const url1 = "https://practice.expandtesting.com/redirector";
    const url2 = "https://practice.expandtesting.com/status-codes";
    const redirectLink = page.locator("#redirect");

    await page.goto(url1);

    // Wait for the new page to open while clicking the link
    const newPagePromise = context.waitForEvent('page');

    await page.locator("#redirect").click();

    const newPage = await newPagePromise;

    // Wait for the new page to load
    await newPage.waitForLoadState();

    // Verify the destination URL and title
    await expect(newPage).toHaveURL(url2);

    const textTitle = newPage.locator("//h1[contains(text(),'Status Codes')]");

    await expect(textTitle).toBeVisible();
    await expect(textTitle).toHaveText("Status Codes");
});