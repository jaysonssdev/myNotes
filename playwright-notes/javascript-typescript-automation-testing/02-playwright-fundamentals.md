# 01 - Playwright Fundamentals

---

## Table of Contents
* [Getting Started with Playwright Automation Core Concepts](#getting-started-with-playwright-automation-core-concepts)
* [Playwright Basic Methods for Web Automation Testing](#playwright-basic-methods-for-web-automation-testing)

---

<br>

## Getting Started with Playwright Automation Core Concepts

### Create npm Project and install Playwright dependencies for testing
1. Create a new project directory.
2. In this directory, open terminal.
3. Run `npm init playwright`.
4. Select the following: **JavaScript -> tests -> true**

### Importance of Playwright Test Annotation and async await understanding
1. In the **tests** directory, create a new practice test file : `UIBasicstest.spec.js`
2. This is the common test case syntax:
```js
const {test} = require('@playwright/test');

test('First Playwright test', async ()=>
{
    // playwright code
    // step 1 - open browser
    await
    // step 2
});
```
* `async` means your code will run in **sequential order**, `await` means it will wait for the first step to finish before proceeding to the next step.
* `await` will NOT work if you forgot to put `async`

### What is browser context and Page fixtures in Playwright
```js
const { test } = require('@playwright/test');

test('Browser Context Playwright test', async ({ browser }) => {
    const context = await browser.newContext(); // you can add cookies here if needed
    const page = await context.newPage();
    await page.goto("https://practice.expandtesting.com/login");
});

test('Page Playwright test', async ({ page }) => {
    await page.goto("https://google.com/");
});
```
* Use the `{browser}` fixture if you need to add cookies or plugins on the browser. If you only need a fresh instance, `{page}` fixture is enough.

### Importance of Playwright configuration file and its details

#### Customizing your own config object

1. Open `playwright.config.js`
2. You can change here the following:
    - **tests directory:** choose which test will run.
    - **test timeout:** default is 30secs for each test. You can override it here.
    - **global timeout:** for assertion validation timeout. Default is also 30secs, change it only if you need to override it.
    - **browsers:** which browsers will be used on your tests
3. Sample customized **config** object:

![alt text](images/02-playwright-fundamentals/2026-10-25_15-47.png)

#### Running the playwright.config.js
1. Open the terminal on your project directory.
2. Run `npx playwright test` to run all the tests in your `./tests` directory.
    - default test run is headless
    - to see the browser execution, add `--headed` on the command
    - or in your **playwright.config.js**, in `use:` add `headless: false`

3. If you have several tests inside your javascript file, you can add `.only` to the test that you only want to execute.
```js
const {test} = require('@playwright/test');

test.only('Page Playwright test', async ({page})=>
{
    await page.goto("https://google.com/");
});
```

### Setup Assertions in Playwright tests & multiple browsers Configuration

```js
// get test and expect fixtures from the playwright module
const {test, expect} = require('@playwright/test');

test.only('Page Playwright test', async ({page})=>
{
    await page.goto("https://google.com/");

    // get title - assertion
    console.log(await page.title());
    await expect(page).toHaveTitle("Google");
});
```
* To provide a 5 seconds timeout for the **expect** method, add this in the **playwright.config.js**:

![alt text](images/02-playwright-fundamentals/2026-10-26_12-23.png)

<br>

---

<br>

## Playwright Basic Methods for Web Automation Testing

### Using locator() method to select an element

* Prefer using **css locators** rather than **xpath locators**.
* Rules for using **css locator**:

![alt text](images/02-playwright-fundamentals/2026-10-26_12-43.png)

* On your target website:
1. Use **Inspect** or hit **(F12)**.
2. Pick the target element, in this example, the **Username input box**.
3. Use **ChroPath** browser extension to see the css selector value. (or **SelectorsHub** extension)

![alt text](images/02-playwright-fundamentals/2026-10-26_14-21.png)

Note: Better to create variables for the locators in your test. Example:
```js
const userName = page.locator("#username")
```

4. Do the same process with **Password input box**, to fill them.
5. Do the same process with the **Login** button, to click it.

```js
const { test, expect } = require('@playwright/test');

test('Login test - Correct Credentials', async ({ page }) => {
    await page.goto("https://practice.expandtesting.com/login");

    // login - correct credentials
    await page.locator("#username").fill("practice");
    await page.locator("#password").fill("SuperSecretPassword!");
    await page.locator("#submit-login").click();
```

6. Create a new test that provides a wrong password.
    - Get the **css selector** of the pop-up error.

    ![alt text](images/02-playwright-fundamentals/2026-10-26_15-33.png)

    - Then **print** its **error message** by using the `textContent()` method.
    - Then **expect** the correct **error message** by using `toContainText` method. 

```js
const { test, expect } = require('@playwright/test');

test('Login test - Wrong Password', async ({ page }) => {
    await page.goto("https://practice.expandtesting.com/login");

    // login - wrong password
    await page.locator("#username").fill("practice");
    await page.locator("#password").fill("WrongPassword!");
    await page.locator("#submit-login").click();
    console.log(await page.locator("#flash").textContent());
    await expect(page.locator("#flash")).toContainText("Your password is invalid!");
});
```

#### Deleting a filled input box
If you already filled up an input box, **you can make it blank again** by using the **fill** method again. Example:
```js
await page.locator("#username").fill("");
```

<br>

### How to work with locators that extract multiple web elements

#### 1. Index
If your locator is selecting multiple elements, you can select the correct element by putting its index.

![alt text](images/02-playwright-fundamentals/2026-10-26_18-51.png)

```js
console.log(await page.locator(".card—body a").nth(0).textContent());
```
In this example the locator is selecting 4 elements, to get the first one, specify the `0` index.

#### 2. first or last
You can select the correct element by putting **first** or **last**. This is only applicable with **first** and **last**, there are no second, third, fourth and so on.
```js
console.log(await page.locator(".card—body a").first().textContent());
```

#### 3. Listing all the elements
If you want to have an **array** of elements that your locator is selecting, use the `allTextContents()` method.
```js
console.log(await page.locator(".card—body a").allTextContents());
```
This is useful if you need an array for you loop code.

<br>

### Techniques to wait dynamically for new page in Service based applications

* **Inspect -> Network tab -> Fetch/XHR tab** - to see how data load on your browser.

![alt text](images/02-playwright-fundamentals/2026-10-26_19-49.png)

* `waitForLoadState()` method - is used to **wait until all the network calls are completed**. In this example after logging in it will wait for the 4 calls (login, get-all-products...) to load first.
    ![alt text](images/02-playwright-fundamentals/2026-10-26_20-03.png)

    - Without this, your next method (allTextContents) might return an empty array, because it will not load all the data.

* `waitFor()` method - is a better alternative than using **networkidle**. In this example if you know that `".card—body b"` has 8 elements, wait for the last index to load.
```js
await page.locator(".card—body b").nth(7).waitFor();

const titles = await page. locator(".card—body b").allTextContents();
console.log(titles);
```

<br>

---