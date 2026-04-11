function numberPlayground(price, quantity, discountPercent) {
  console.log("---- NUMBER PLAYGROUND ----");

  // 1. Basic arithmetic
  let total = price * quantity;
  console.log("Total:", total);

  console.log("Add:", price + 10);
  console.log("Subtract:", price - 5);
  console.log("Multiply:", price * 2);
  console.log("Divide:", price / 2);
  console.log("Remainder:", price % 3);
  console.log("Exponent:", price ** 2);

  // 2. Increment / Decrement
  let count = 5;
  console.log(count++); // post
  console.log(++count); // pre
  console.log(count--);
  console.log(--count);

  // 3. Order of operations (PEMDAS)
  let complex = 10 + 5 * 2 ** 2;
  console.log("Complex:", complex);

  // 4. Floating point issue
  console.log(0.1 + 0.2); // 0.30000000000000004 😮

  // Fix using toFixed
  console.log((0.1 + 0.2).toFixed(2));

  // 5. String → Number conversion
  console.log(Number("123"));
  console.log(parseInt("50px"));
  console.log(parseFloat("12.99$"));
  console.log(+"100"); // unary plus

  // 6. Number → String
  console.log((500).toString());

  // 7. Math object basics
  console.log("PI:", Math.PI);
  console.log("E:", Math.E);

  // 8. Rounding numbers
  let num = 4.7;
  console.log(Math.round(num));
  console.log(Math.floor(num));
  console.log(Math.ceil(num));
  console.log(Math.trunc(num));

  // 9. Absolute & sign
  console.log(Math.abs(-10));
  console.log(Math.sign(-5));

  // 10. Min / Max
  console.log(Math.max(10, 20, 5));
  console.log(Math.min(10, 20, 5));

  // 11. Random numbers
  let random0to1 = Math.random();
  console.log("Random:", random0to1);

  // Random 1–10
  let dice = Math.floor(Math.random() * 10) + 1;
  console.log("Dice:", dice);

  // 12. Power & square root
  console.log(Math.pow(2, 3));
  console.log(Math.sqrt(25));

  // 13. Logarithms
  console.log(Math.log(10));
  console.log(Math.log10(1000));

  // 14. Check number types
  console.log(Number.isInteger(5));
  console.log(Number.isNaN(NaN));
  console.log(isNaN("hello")); // global version

  // 15. Infinity
  console.log(1 / 0);
  console.log(-1 / 0);

  // 16. Safe integers
  console.log(Number.MAX_SAFE_INTEGER);
  console.log(Number.MIN_SAFE_INTEGER);

  // 17. BigInt (very large numbers)
  let big = 123456789012345678901234567890n;
  console.log(big + 10n);

  // 18. Discount calculation
  let discount = (total * discountPercent) / 100;
  let finalPrice = total - discount;
  console.log("Discount:", discount);
  console.log("Final price:", finalPrice);

  // 19. Formatting numbers
  console.log(finalPrice.toFixed(2));

  // 20. Locale formatting (currency)
  console.log(
    finalPrice.toLocaleString("en-US", {
      style: "currency",
      currency: "USD",
    })
  );

  // 21. Clamping values (min/max limit)
  let score = 120;
  score = Math.min(Math.max(score, 0), 100);
  console.log("Clamped score:", score);

  // 22. Percentage calculation
  let progress = (75 / 120) * 100;
  console.log(progress.toFixed(1) + "%");

  console.log("---- END ----");
}