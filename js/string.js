function stringPlayground(rawName, email, message) {
  console.log("---- STRING PLAYGROUND ----");

  // 1. String creation
  let str1 = "Hello";
  let str2 = 'World';
  let str3 = `Template literal`;
  console.log(str1, str2, str3);

  // 2. Length
  console.log("Name length:", rawName.length);

  // 3. Trim (remove spaces)
  let name = rawName.trim();
  console.log("Trimmed name:", name);

  // 4. Case conversion
  console.log(name.toUpperCase());
  console.log(name.toLowerCase());

  // 5. Access characters
  console.log("First char:", name[0]);
  console.log("Last char:", name[name.length - 1]);

  // 6. charAt & charCodeAt
  console.log(name.charAt(1));
  console.log(name.charCodeAt(1));

  // 7. Includes / startsWith / endsWith
  console.log("Has gmail?", email.includes("gmail"));
  console.log("Starts with admin?", email.startsWith("admin"));
  console.log("Ends with .com?", email.endsWith(".com"));

  // 8. Index searching
  console.log("Index of @:", email.indexOf("@"));
  console.log("Last index of .:", email.lastIndexOf("."));

  // 9. Extract parts
  console.log("Slice name:", name.slice(0, 3));
  console.log("Substring:", name.substring(0, 4));

  // 10. Split email
  let emailParts = email.split("@");
  console.log("Username:", emailParts[0]);
  console.log("Domain:", emailParts[1]);

  // 11. Replace text
  let cleanMessage = message.replace("bad", "***");
  console.log("Clean message:", cleanMessage);

  // Replace all
  let sentence = "cat dog cat dog";
  console.log(sentence.replaceAll("cat", "tiger"));

  // 12. Repeat text
  console.log("⭐".repeat(5));

  // 13. Pad text (useful for IDs)
  let orderId = "45";
  console.log(orderId.padStart(5, "0")); // 00045

  // 14. Template literals
  let greeting = `Hello ${name}, your email is ${email}`;
  console.log(greeting);

  // 15. Multiline string
  let multiLine = `
  Welcome ${name}
  Thanks for registering!
  `;
  console.log(multiLine);

  // 16. Escape characters
  console.log("He said \"Hello\"");

  // 17. Regex test
  let hasNumber = /\d/.test(message);
  console.log("Message contains number?", hasNumber);

  // 18. Match words
  console.log(message.match(/\b\w{4}\b/g));

  // 19. Compare strings
  console.log("a" < "b"); // lexicographic compare

  // 20. Convert number to string
  let price = 500;
  console.log(price.toString());

  // 21. Convert string to number
  console.log(Number("123"));
  console.log(parseInt("50px"));
  console.log(parseFloat("12.99$"));

  // 22. Concatenation
  let full = name.concat(" - ", email);
  console.log(full);

  // 23. Raw string (ignore escapes)
  console.log(String.raw`Line1\nLine2`);

  // 24. Unicode
  console.log("❤️".length);
  console.log("Hello 😊");

  console.log("---- END ----");
}