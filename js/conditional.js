function shoppingSystem(user, cartTotal, coupon) {
  console.log("---- Shopping System ----");

  // 1️. Guard clauses
  if (!user) return console.log("No user data provided");
  if (!user.isActive) return console.log("Account disabled");

  // 2️. Optional chaining + Nullish coalescing
  let userName = user.profile?.name ?? "Guest";

  console.log("Hello", userName);

  // 3️. Role check using switch
  switch (user.role) {
    case "admin":
      console.log("Admin dashboard access");
      break;
    case "seller":
      console.log("Seller dashboard access");
      break;
    case "customer":
      console.log("Customer shopping access");
      break;
    default:
      console.log("Unknown role");
  }

  // 4️. Nested IF (age + country)
  if (user.age >= 18) {
    if (user.country === "BD") {
      console.log("Local adult user");
    } else {
      console.log("Foreign adult user");
    }
  } else {
    console.log("Minor user - limited features");
  }

  // 5️. Truthy / Falsy check
  if (!user.email) {
    console.log("⚠️ Email not verified");
  }

  // 6️. AND / OR / NOT operators
  if (user.isLoggedIn && !user.isBanned) {
    console.log("User can proceed to shop");
  } else {
    return console.log("User cannot shop");
  }

  // 7️. Short-circuit example
  user.isPremium && console.log("⭐ Premium benefits unlocked");

  // 8️. Default values using ||
  let shippingAddress = user.address || "Default Warehouse Pickup";
  console.log("Shipping:", shippingAddress);

  // 9️. Coupon using ternary
  let couponDiscount = coupon ? 50 : 0;
  console.log("Coupon discount:", couponDiscount);

  // 10. Complex discount logic (if else if)
  let discount = 0;

  if (cartTotal > 1000) {
    discount = 200;
  } else if (cartTotal > 500) {
    discount = 100;
  } else if (cartTotal > 200) {
    discount = 50;
  } else {
    discount = 0;
  }

  // 11. Multiple ternary grading style
  let membershipLevel =
    cartTotal > 1000 ? "Gold" :
    cartTotal > 500 ? "Silver" :
    cartTotal > 200 ? "Bronze" : "Basic";

  console.log("Membership:", membershipLevel);

  // 12. Equality checks
  if (user.loginAttempts === 3) {
    console.log("Warning: Last attempt before lock");
  }

  if (user.role === "admin") {
    console.log("Strict equality used ✔");
  }

  // 13. Final price calculation
  let finalPrice = cartTotal - discount - couponDiscount;

  // 14. Final ternary result
  let message =
    finalPrice > 0 ? "Proceed to payment" : "Free order 🎉";

  console.log("Cart total:", cartTotal);
  console.log("Discount:", discount);
  console.log("Final price:", finalPrice);
  console.log(message);
}