function arrayPlayground() {
  console.log("---- ARRAY PLAYGROUND ----");

  // 1. Create arrays
  let products = ["Phone", "Laptop", "Shoes"];
  let prices = [500, 1200, 80];
  let mixed = ["Book", 100, true];

  console.log(products);

  // 2. Length
  console.log("Length:", products.length);

  // 3. Access elements
  console.log(products[0]);
  console.log(products.at(-1)); // last item

  // 4. Add elements
  products.push("Watch"); // end
  products.unshift("Tablet"); // start
  console.log(products);

  // 5. Remove elements
  products.pop();
  products.shift();
  console.log(products);

  // 6. Splice (insert/remove anywhere)
  products.splice(1, 0, "Camera");
  console.log(products);

  // 7. Slice (copy part)
  console.log(products.slice(1, 3));

  // 8. Merge arrays
  let more = ["TV", "Headphone"];
  let allProducts = products.concat(more);
  console.log(allProducts);

  // 9. Spread operator
  let spreadProducts = [...products, ...more];
  console.log(spreadProducts);

  // 10. Index search
  console.log(products.indexOf("Laptop"));
  console.log(products.includes("Phone"));

  // 11. Reverse & Sort
  console.log([...prices].reverse());
  console.log([...prices].sort((a, b) => a - b));

  // 12. forEach loop
  console.log("\nforEach:");
  products.forEach(p => console.log(p));

  // 13. Map (transform)
  let priceWithVAT = prices.map(p => p * 1.15);
  console.log(priceWithVAT);

  // 14. Filter
  let expensive = prices.filter(p => p > 100);
  console.log(expensive);

  // 15. Reduce
  let total = prices.reduce((sum, p) => sum + p, 0);
  console.log("Total:", total);

  // 16. Find / FindIndex
  console.log(prices.find(p => p > 100));
  console.log(prices.findIndex(p => p > 100));

  // 17. Some / Every
  console.log(prices.some(p => p > 1000));
  console.log(prices.every(p => p > 10));

  // 18. Join array → string
  console.log(products.join(", "));

  // 19. Split string → array
  let str = "apple,banana,orange";
  console.log(str.split(","));

  // 20. Fill
  let arr = new Array(5).fill(0);
  console.log(arr);

  // 21. Array.from
  let nums = Array.from("12345", x => Number(x));
  console.log(nums);

  // 22. Flat
  let nested = [1, [2, [3, 4]]];
  console.log(nested.flat(2));

  // 23. FlatMap
  let words = ["hello world", "js arrays"];
  console.log(words.flatMap(w => w.split(" ")));

  // 24. Destructuring
  let [first, second] = products;
  console.log(first, second);

  // 25. Rest operator
  let [head, ...tail] = products;
  console.log(head, tail);

  // 26. Copy array
  let copy = [...products];
  console.log(copy);

  // 27. Check if array
  console.log(Array.isArray(products));

  // 28. Entries / Keys / Values
  console.log([...products.entries()]);
  console.log([...products.keys()]);
  console.log([...products.values()]);

  // 29. ReduceRight
  let right = [1, 2, 3].reduceRight((acc, v) => acc + v);
  console.log(right);

  // 30. Sorting objects
  let users = [
    { name: "Emon", age: 22 },
    { name: "Sara", age: 30 },
    { name: "John", age: 25 },
  ];
  users.sort((a, b) => a.age - b.age);
  console.log(users);

  console.log("---- END ----");
}