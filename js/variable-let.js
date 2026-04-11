// --------------------------------------------------------------------------------
// VARIABLES BY LET
// --------------------------------------------------------------------------------
/**
 * Variables declared with let have Block Scope
 * Variables declared with let must be Declared before use
 * Variables declared with let cannot be Redeclared in the same scope
 */
 
 // --------------------------------------------------------------------------------
// JS SCOPE
// --------------------------------------------------------------------------------
/**
 * Before ES6 (2015), JavaScript did not have Block Scope.
 * JavaScript had Global Scope and Function Scope.
 * ES6 introduced the two new JavaScript keywords: let and const.
 * These two keywords provided Block Scope in JavaScript
 */
 
 // BLOCK SCOPE 
 // Variables declared inside a { } block cannot be accessed from outside the block
 {
  let x = 2;
}
// x can NOT be used here

// FUNCTION SCOPE 
// Inside a function all variables declared with var, let or const have Function Scope
function myfunction() {
  var x = 1;
  let y = 2;
  const z = 3;
}
//x can NOT be used here
//y can NOT be used here
//z can NOT be used here

// GLOBAL SCOPE 
/**
 * Variables declared with the var always have Global Scope.
 * Variables declared with the var keyword can NOT have block scope
 */
 // Variables declared with varinside a { } block can be accessed from outside the block
 {
  var x = 2;
}
// x CAN be used here


// Variables defined with let can not be redeclared.
// With let we can not do this:
let x = "John Doe";

let x = 0;

// Variables defined with var can be redeclared.
// USING var 
var x = "John Doe";

var x = 0;

// Redeclaring Variables
var x = 10;
// Here x is 10

{
var x = 2;
// Here x is 2
}

// USING let 
let x = 10;
// Here x is 10

{
let x = 2;
// Here x is 2
}

// Here x is 10

// Here x is 2