console.log("---- FUNCTION PLAYGROUND ----");

/* 1. Function Declaration */
function greet(name) {
  return "Hello " + name;
}
console.log(greet("Emon"));

/* 2. Function Expression */
const add = function (a, b) {
  return a + b;
};
console.log(add(5, 3));

/* 3. Arrow Function */
const multiply = (a, b) => a * b;
console.log(multiply(4, 6));

/* 4. Default Parameters */
function registerUser(name = "Guest") {
  console.log("User:", name);
}
registerUser();
registerUser("Sara");

/* 5. Rest Parameters */
function totalPrice(...prices) {
  return prices.reduce((sum, p) => sum + p, 0);
}
console.log(totalPrice(10, 20, 30, 40));

/* 6. Function Returning Function (Closure) */
function createMultiplier(multiplier) {
  return function (num) {
    return num * multiplier;
  };
}
const double = createMultiplier(2);
console.log(double(10));

/* 7. Callback Function */
function processUser(name, callback) {
  callback(name);
}
processUser("Emon", function (n) {
  console.log("Processed:", n);
});

/* 8. Higher Order Function */
function calculator(a, b, operation) {
  return operation(a, b);
}
console.log(calculator(10, 5, (x, y) => x - y));

/* 9. Immediately Invoked Function (IIFE) */
(function () {
  console.log("IIFE runs instantly");
})();

/* 10. Recursive Function */
function factorial(n) {
  if (n === 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(5));

/* 11. Anonymous Function */
setTimeout(function () {
  console.log("Runs after delay");
}, 100);

/* 12. Named Function Expression */
const sayHi = function hello() {
  console.log("Hi!");
};
sayHi();

/* 13. Method inside Object */
const user = {
  name: "Emon",
  greet() {
    return `Hello ${this.name}`;
  },
};
console.log(user.greet());

/* 14. Function Constructor (rare) */
const sum = new Function("a", "b", "return a + b");
console.log(sum(2, 3));

/* 15. Generator Function */
function* idGenerator() {
  let id = 1;
  while (true) yield id++;
}
const gen = idGenerator();
console.log(gen.next().value);
console.log(gen.next().value);

/* 16. Async Function */
async function fetchData() {
  return "Data loaded";
}
fetchData().then(console.log);

/* 17. Function with try/catch */
function safeDivide(a, b) {
  try {
    if (b === 0) throw new Error("Divide by zero");
    return a / b;
  } catch (err) {
    return err.message;
  }
}
console.log(safeDivide(10, 0));

/* 18. Currying Function */
const curriedAdd = a => b => c => a + b + c;
console.log(curriedAdd(1)(2)(3));

/* 19. Pure Function */
function pureAdd(a, b) {
  return a + b;
}

/* 20. Impure Function */
let counter = 0;
function impure() {
  counter++;
}

/* 21. Function Borrowing (call/apply/bind) */
const person = { name: "John" };
function sayName() {
  console.log(this.name);
}
sayName.call(person);
sayName.apply(person);

const bound = sayName.bind(person);
bound();

/* 22. Arrow vs Regular (this difference) */
const obj = {
  name: "Arrow Test",
  regular() {
    console.log("Regular:", this.name);
  },
  arrow: () => console.log("Arrow:", this.name),
};
obj.regular();
obj.arrow();

/* 23. Debounce Function */
function debounce(fn, delay) {
  let timer;
  return function () {
    clearTimeout(timer);
    timer = setTimeout(() => fn(), delay);
  };
}
const sayHello = debounce(() => console.log("Hello after delay"), 500);
sayHello();

/* 24. Memoization */
function memoize(fn) {
  const cache = {};
  return function (n) {
    if (cache[n]) return cache[n];
    cache[n] = fn(n);
    return cache[n];
  };
}
const slowSquare = n => {
  console.log("Calculating...");
  return n * n;
};
const fastSquare = memoize(slowSquare);
fastSquare(5);
fastSquare(5);

console.log("---- END ----");