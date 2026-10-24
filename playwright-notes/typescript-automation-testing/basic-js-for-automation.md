# Basic JavaScript for Automation Testing

---

## Table of Contents
* [Hello World Program](#hello-world-program)
* [Declaring the variables](#declaring-the-variables)
* [Understanding the Datatypes](#understanding-the-datatypes)
* [Conditions and Loops](#conditions-and-loops)
* [Logical Operators and Assignments](#logical-operators-and-assignments)
* [Arrays and its methods](#arrays-and-its-methods)
* [Functions](#functions)
* [String and its related functions](#string-and-its-related-functions)
* [What are JavaScript Objects?](#what-are-javascript-objects)
* [Classes and its Properties](#classes-and-its-properties)
* [Methods](#methods)

---

## Hello World Program
* To simply print on the console/terminal:
```js
console.log("Hello World!")
```

* To add comments:
```js
// for single line comment

/*
for
multiple
lines
*/
```
* To run a javascript file on the terminal: 
    - `node <js file name>`
    - Example: `node basics1.js`

---

## Declaring the variables
* You can use var, let, or const:
    - `var`: variable name can be declared again and will replace the previous one.
    - `let`: you won't be able to repeat a variable name again if declared using **let**. Don't put "let" to re-assign the same variable name.
    - `const`: strictly NO re-assigning of the same variable name.

![alt text](images/basic-js-for-automation/2026-10-21_12-49.png)

#### Important Notes:
* **Use `const` by default**: It prevents accidental reassignment and makes your code easier to reason about. Note that while you cannot reassign a `const` object or array, you can still modify its internal properties or elements.

* **Use `let` for variables that must change**: Perfect for loops, counters, or values you know you will reassign later.

* **Avoid `var` in modern JavaScript**: Its lack of block scoping and loose rules around redeclaration often lead to bugs.

#### Naming Style Guide

![alt text](images/basic-js-for-automation/2026-10-21_13-25.png)

#### Naming Rules
1. **No Reserved Words**: You cannot name a variable after keywords like `const, let, if, class, function`

2. **First Character Constraints**: A name must start with a letter, an underscore (_), or a dollar sign ( $ ). **It cannot start with a number**.

3. **No Hyphens or Spaces**


#### Examples:

```js
// number variable
let a = 4
let b = 123.45
let c = a + b
// To know what type of variable
console.log(typeof (a))

// to re-assign variable for "let", don't put "let" anymore
c = "c variable is now replaced."
console.log(c)
// no re-assigning if "const" is used
const e = "You cannot use the 'e' again as a variable name!"
// e = 5 will cause an error

// string variable
let userName = "John Smith"

// boolean variable
let isRequired = true
// to reverse boolean, use "!"
console.log(!isRequired)

// null and undefined variable
let d = null
```

---

## Understanding the Datatypes

![alt text](images/basic-js-for-automation/2026-10-21_12-46.png)

---

## Conditions and Loops

### Conditions — Making decisions
* How it works:
    - `if` checks whether the condition is true.

    - `else if` checks another condition if the previous one is false.

    - `else` runs when none of the previous conditions are true.

#### Example:

```js
const score = 85;

if (score >= 90) {
  console.log("Excellent!");
} else if (score >= 75) {
  console.log("Passed!");
} else {
  console.log("Try again.");
}
```
**Output:** Passed!

<br>

### Loops — Repeating tasks

#### A. `for` loop
Use a `for` loop **when you know how many times** you want to repeat something.

```js
for (let i = 1; i <= 4; i++) {
  console.log(i);
}
```
**Output:**
```
1
2
3
4
```
* How it works:
    - let i = 1 — starts the counter at 1.
    - i <= 4 — continues while the condition is true.
    - i++ — increases the counter by 1 after each iteration.

#### B. `for...of` loop
A modern and readable way **to loop through arrays**.

```js
const fruits = ["Apple", "Mango", "Banana"];

for (const fruit of fruits) {
  console.log(fruit);
}
```
**Output:**
```
Apple
Mango
Banana
```

#### C. `while` loop
Use a `while` loop when you want to repeat something **as long as a condition remains true**.

```js
let count = 1;

while (count <= 3) {
  console.log(count);
  count++;
}
```
**Output:**
```
1
2
3
```

#### D. `do...while` loop
Use a `do while` loop when you want the code to **run at least once, even if the condition is initially false**.

```js
let count = 1;

do {
  console.log(count);
  count++;
} while (count <= 3);
```
**Output:**
```
1
2
3
```

### Combining loops and conditions
You can use an `if` statement inside a loop to make decisions for each item.

```js
const numbers = [1, 2, 3, 4, 5];

for (const number of numbers) {
  if (number % 2 === 0) {
    console.log(`${number} is even`);
  } else {
    console.log(`${number} is odd`);
  }
}
```
**Output:**
```
1 is odd
2 is even
3 is odd
4 is even
5 is odd
```

### Loop Control Statements

* `break`: stops the loop completely.
* `continue`: skips the current iteration and proceeds to the next one.

---

## Logical Operators and Assignments

### Logical Operators

![alt text](images/basic-js-for-automation/2026-10-22_13-29.png)

#### More Examples:

```js
// AND (&&)
console.log(5 > 3 && 10 > 7); // true

// OR (||)
console.log(5 > 3 || 10 < 7); // true

// NOT (!)
console.log(!true); // false

// Nullish coalescing (??)
console.log(null ?? "Default"); // "Default"
```

### Logical Assignment Operators

![alt text](images/basic-js-for-automation/2026-10-22_13-30.png)

---

## Arrays and its methods

An array is a variable that stores multiple values in a single list.

```js
let fruits = ["Apple", "Banana", "Mango"];

console.log(fruits[0]); // Apple
console.log(fruits[1]); // Banana
console.log(fruits[2]); // Mango
```

### 1. Common Array Methods

![alt text](images/basic-js-for-automation/2026-10-22_13-59.png)

**Note:** These examples assume each method starts with a fresh `nums = [1, 2, 3]`. Some methods modify the original array, while others do not.

### 2. Methods for working with array items

![alt text](images/basic-js-for-automation/2026-10-22_14-01.png)

### 3. Other useful array features

![alt text](images/basic-js-for-automation/2026-10-22_14-05.png)

### 4. The most important difference to remember
Some methods **modify the original array**, while others return a new value.

![alt text](images/basic-js-for-automation/2026-10-22_14-06.png)

---

## Functions

### 1. What is a function in JavaScript?

A **function** is a reusable block of code designed to perform a specific task.

```js
function greet() {
  console.log("Hello, world!");
}

greet(); // Hello, world!
greet(); // Hello, world!
```
* **How it works:**
    - `function` — keyword used to declare a function.
    - `greet` — the function's name.
    - `()` — parentheses that can hold parameters.
    - `{}` — the function body, where the code goes.
    - `greet()` — calls or executes the function.

* **Remember:** Declaring a function doesn't automatically run it. You need to call it.

<br>

### 2. The main types of functions

#### A. Function declaration
* This is the traditional way to create a function.
```js
function add(a, b) {
  return a + b;
}

console.log(add(5, 3)); // 8
```

#### B. Function expression
* A function is stored inside a variable.
```js
const add = function(a, b) {
  return a + b;
};

console.log(add(5, 3)); // 8
```

#### C. Arrow function
* A shorter way to write a function, introduced in ES6. **Arrow functions are especially common in modern JavaScript.**
```js
const add = (a, b) => {
  return a + b;
};

console.log(add(5, 3)); // 8

// For a single expression, you can shorten it further:
const add = (a, b) => a + b;
```

#### Quick comparison

![alt text](images/basic-js-for-automation/2026-10-23_14-51.png)

<br>

### 3. Parameters vs. arguments
* These two terms are closely related but have different meanings.
```js
function greet(name) {
  console.log("Hello, " + name);
}

greet("Alex");
```
* **Parameter:** `name` — the variable in the function definition.
* **Argument:** `"Alex"` — the actual value passed when calling the function.

You can use multiple parameters:
```js
function introduce(name, age) {
  console.log(`I'm ${name} and I'm ${age} years old.`);
}

introduce("Alex", 22);
```
**Output:** I'm Alex and I'm 22 years old.

#### Default parameters
You can provide a fallback value if an argument is omitted.
```js
function greet(name = "Guest") {
  console.log(`Hello, ${name}!`);
}

greet();       // Hello, Guest!
greet("Mia");  // Hello, Mia!
```

<br>

### 4. The `return` statement
`return` sends a value back to the code that called the function.
```js
function multiply(a, b) {
  return a * b;
}

const result = multiply(4, 5);

console.log(result); // 20
```
Compare `return` with `console.log()`:
```js
function first() {
  console.log(10);
}

function second() {
  return 10;
}
```
* `console.log()` displays a value in the console.
* `return` gives a value back so it can be stored, reused, or passed to another function.
* A function without a `return` statement returns `undefined` by default.
* Once `return` executes, the function stops running.

<br>

### 5. Scope: where variables can be accessed
Scope determines where a variable is available.

#### Global scope
```js
const name = "Alex";

function greet() {
  console.log(name);
}

greet(); // Alex
```
The variable `name` is accessible inside the function because it was declared outside it in the global scope.

#### Local or function scope
```js
function greet() {
  const message = "Hello!";
  console.log(message);
}

greet();

// console.log(message); // ReferenceError
```
The variable `message` is only accessible inside the function.

#### Block scope
Variables declared with let and const inside a block are limited to that block.
```js
if (true) {
  let age = 20;
}

// console.log(age); // ReferenceError
```

<br>

### 6. Anonymous functions and callbacks

#### Anonymous function
- is a function without a name.
```js
const greet = function() {
  console.log("Hello!");
};
```

#### Callback function
- is a function passed to another function as an argument.
```js
function processUser(callback) {
  callback();
}

processUser(function() {
  console.log("User processed!");
});
```
Callbacks are commonly used with event listeners, timers, and array methods.

For example, in the DOM:
```js
const button = document.querySelector("button");

button.addEventListener("click", () => {
  console.log("Button clicked!");
});
```
The arrow function is the callback. It runs when the button is clicked.

<br>

### 7. Higher-order functions
A higher-order function is a function that **accepts another function as an argument or returns a function**.

Array methods such as `map()`, `filter()`, and `forEach()` are common examples.
```js
const numbers = [1, 2, 3, 4];

const doubled = numbers.map(number => number * 2);

console.log(doubled); // [2, 4, 6, 8]
```

<br>

### 8. Other important function concepts

**Recursion:** A function calls itself to solve a problem in smaller steps.
```js
function countDown(n) {
  if (n <= 0) return;
  console.log(n);
  countDown(n - 1);
}

countDown(3); // 3, 2, 1
```
**Asynchronous functions:** Used when work takes time, such as fetching data from an API.
```js
async function getData() {
  const response = await fetch(
    "https://jsonplaceholder.typicode.com/users"
  );

  const data = await response.json();
  console.log(data);
}

getData();
```
`async` allows a function to return a **Promise**, while `await` waits for a **Promise to settle**.

**Closures:** A function can remember variables from the scope where it was created, even after the outer function has finished.
```js
function counter() {
  let count = 0;

  return function() {
    count++;
    return count;
  };
}

const increment = counter();

console.log(increment()); // 1
console.log(increment()); // 2
```

<br>

### 9. Common mistakes to avoid

![alt text](images/basic-js-for-automation/2026-10-23_15-31.png)

---

## String and its related functions

---

## What are JavaScript Objects?

---

## Classes and its Properties

---

## Methods

---