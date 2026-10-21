# Basic JavaScript for Automation Testing

---

## Table of Contents
* [Hello World Program](#hello-world-program)
* [Declaring the variables](#declaring-the-variables)
* [Understanding the Datatypes](#understanding-the-datatypes)
* [Loops and Conditions](#loops-and-conditions)
* [Logical operators and Assignments](#logical-operators-and-assignments)
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

#### Important Note:
* **Use `const` by default**: It prevents accidental reassignment and makes your code easier to reason about. Note that while you cannot reassign a `const` object or array, you can still modify its internal properties or elements.

* **Use `let` for variables that must change**: Perfect for loops, counters, or values you know you will reassign later.

* **Avoid `var` in modern JavaScript**: Its lack of block scoping and loose rules around redeclaration often lead to bugs.

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
let name = "John Smith"

// boolean variable
let required = true
// to reverse boolean, use "!"
console.log(!required)

// null and undefined variable
let d = null
```

---

## Understanding the Datatypes

![alt text](images/basic-js-for-automation/2026-10-21_12-46.png)

---

## Loops and Conditions

---

## Logical operators and Assignments

---

## Arrays and its methods

---

## Functions

---

## String and its related functions

---

## What are JavaScript Objects?

---

## Classes and its Properties

---

## Methods

---