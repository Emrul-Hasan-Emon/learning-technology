function analyzeOrders(orders) {
  console.log("---- Order Analyzer ----");

  // 1️. Basic FOR loop (index based)
  console.log("\n1) FOR LOOP → List order IDs");
  for (let i = 0; i < orders.length; i++) {
    console.log("Order ID:", orders[i].id);
  }

  // 2️. WHILE loop (condition-based)
  console.log("\n2) WHILE LOOP → Count expensive orders (>500)");
  let i = 0;
  let expensiveCount = 0;

  while (i < orders.length) {
    if (orders[i].total > 500) expensiveCount++;
    i++;
  }
  console.log("Expensive orders:", expensiveCount);

  // 3️. DO WHILE loop (runs at least once)
  console.log("\n3) DO WHILE → Try processing until success");
  let attempts = 0;
  let success = false;

  do {
    attempts++;
    console.log("Processing attempt", attempts);
    if (attempts === 2) success = true;
  } while (!success);

  // 4️. FOR...OF (iterate values)
  console.log("\n4) FOR...OF → List customer names");
  for (const order of orders) {
    console.log(order.customer);
  }

  // 5️. FOR...IN (iterate object keys)
  console.log("\n5) FOR...IN → Inspect one order object");
  for (const key in orders[0]) {
    console.log(key, ":", orders[0][key]);
  }

  // 6️. forEach loop
  console.log("\n6) forEach → Print totals");
  orders.forEach(order => console.log(order.total));

  // 7️. MAP loop (transform array)
  console.log("\n7) map → Get order totals with VAT");
  const totalsWithVAT = orders.map(o => o.total * 1.15);
  console.log(totalsWithVAT);

  // 8️. FILTER loop (select items)
  console.log("\n8) filter → Only delivered orders");
  const delivered = orders.filter(o => o.status === "delivered");
  console.log(delivered);

  // 9️. REDUCE loop (accumulator)
  console.log("\n9) reduce → Total revenue");
  const revenue = orders.reduce((sum, o) => sum + o.total, 0);
  console.log("Revenue:", revenue);

  // 10. FIND loop (first match)
  console.log("\n10) find → First pending order");
  const pending = orders.find(o => o.status === "pending");
  console.log(pending);

  // 11. SOME loop (any match?)
  console.log("\n11) some → Any cancelled order?");
  console.log(orders.some(o => o.status === "cancelled"));

  // 12. EVERY loop (all match?)
  console.log("\n12) every → All paid?");
  console.log(orders.every(o => o.paid === true));

  // 13. BREAK example
  console.log("\n13) BREAK → Stop when big order found");
  for (const order of orders) {
    if (order.total > 1000) {
      console.log("Big order found:", order.id);
      break;
    }
  }

  // 14. CONTINUE example
  console.log("\n14) CONTINUE → Skip cancelled orders");
  for (const order of orders) {
    if (order.status === "cancelled") continue;
    console.log("Processing order:", order.id);
  }

  // 15. NESTED LOOPS (orders + items)
  console.log("\n15) NESTED LOOPS → List all items");
  for (const order of orders) {
    console.log("Order:", order.id);
    for (const item of order.items) {
      console.log("  -", item);
    }
  }

  // 16. LABELLED LOOP (advanced)
  console.log("\n16) LABELLED LOOP → Stop all loops if banned item found");

  outerLoop:
  for (const order of orders) {
    for (const item of order.items) {
      if (item === "Illegal Item") {
        console.log("🚫 Illegal item found! Stop everything.");
        break outerLoop;
      }
    }
  }

  console.log("\n---- Analysis Complete ----");
}