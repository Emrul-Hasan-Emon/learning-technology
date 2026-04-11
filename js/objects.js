function objectPlayground() {
  console.log("---- OBJECT PLAYGROUND ----");

  // 1. Create object (literal)
  const user = {
    name: "Emon",
    age: 22,
    isPremium: true,
    address: {
      city: "Dhaka",
      country: "BD"
    }
  };

  console.log(user);

  // 2. Access properties
  console.log(user.name);
  console.log(user["age"]);

  // 3. Add new property
  user.email = "emon@gmail.com";
  console.log(user);

  // 4. Update property
  user.age = 23;

  // 5. Delete property
  delete user.isPremium;

  // 6. Nested access + optional chaining
  console.log(user.address?.city);

  // 7. Check property exists
  console.log("name" in user);
  console.log(user.hasOwnProperty("email"));

  // 8. Object keys / values / entries
  console.log(Object.keys(user));
  console.log(Object.values(user));
  console.log(Object.entries(user));

  // 9. Loop object (for...in)
  console.log("\nLoop object:");
  for (let key in user) {
    console.log(key, user[key]);
  }

  // 10. Object destructuring
  const { name, age } = user;
  console.log(name, age);

  // 11. Rename destructuring + default value
  const { city: userCity = "Unknown" } = user.address;
  console.log(userCity);

  // 12. Spread operator (clone object)
  const clone = { ...user };
  console.log(clone);

  // 13. Merge objects
  const extra = { role: "Developer" };
  const merged = { ...user, ...extra };
  console.log(merged);

  // 14. Object.freeze (immutable)
  const frozen = Object.freeze({ app: "Shop" });
  // frozen.app = "New"; ❌ won't change
  console.log(frozen);

  // 15. Object.seal
  const sealed = Object.seal({ version: 1 });
  sealed.version = 2; // can update
  console.log(sealed);

  // 16. Methods inside object
  const calculator = {
    add(a, b) {
      return a + b;
    }
  };
  console.log(calculator.add(5, 3));

  // 17. this keyword
  const person = {
    name: "Sara",
    greet() {
      return "Hello " + this.name;
    }
  };
  console.log(person.greet());

  // 18. Constructor function
  function Product(name, price) {
    this.name = name;
    this.price = price;
  }
  const p1 = new Product("Phone", 500);
  console.log(p1);

  // 19. Class syntax (modern)
  class Car {
    constructor(brand) {
      this.brand = brand;
    }
    drive() {
      return this.brand + " driving";
    }
  }
  const car = new Car("Toyota");
  console.log(car.drive());

  // 20. Getter / Setter
  const account = {
    _balance: 1000,
    get balance() {
      return this._balance;
    },
    set balance(val) {
      if (val >= 0) this._balance = val;
    }
  };
  account.balance = 2000;
  console.log(account.balance);

  // 21. Dynamic property name
  let keyName = "score";
  const game = {
    [keyName]: 95
  };
  console.log(game);

  // 22. Optional chaining + nullish coalescing
  console.log(user.phone?.number ?? "No phone");

  // 23. Object.assign
  const objA = { a: 1 };
  const objB = { b: 2 };
  const combined = Object.assign({}, objA, objB);
  console.log(combined);

  // 24. JSON convert
  const json = JSON.stringify(user);
  console.log(json);

  const parsed = JSON.parse(json);
  console.log(parsed);

  // 25. Deep clone (modern)
  const deepClone = structuredClone(user);
  console.log(deepClone);

  console.log("---- END ----");
}