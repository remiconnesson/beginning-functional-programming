/*
 * Count 
 */

let zero = f => x => x;
let one = f => x => f(x);
let two = f => x => f(f(x))
let three = f => x => f(f(f(x)));

let lambdaToNumber = lambda => lambda(i => i+1)(0);

console.log([zero, one, two, three].map(lambdaToNumber))

/*
 * Addition
 */

let addition = a => b => f => x => b(f)(a(f)(x))

let four = addition(one)(three);
let five = addition(two)(three);
let teteAToto = addition(zero)(zero);

console.log(lambdaToNumber(four));
console.log(lambdaToNumber(five));
console.log(lambdaToNumber(teteAToto));


/*
 * Multiplication
 */

let multiplication = a => b => f => x => b(a(f))(x);

let twenty = multiplication(four)(five);

console.log(lambdaToNumber(twenty));

/*
 * Booleans
 */

let TRUE = a => b => a;
let FALSE = a => b => b;
let IF_ELSE = bool => a => b => bool(a)(b);

let tired = TRUE;
// IF_ELSE(condition)(if-true)(if-false)
let coffee = IF_ELSE(tired)(three)(zero)

console.log(lambdaToNumber(coffee))

/*
 * Logic Gates
 */
const lambdaToBoolean = bool => bool(true)(false);

// partial application of the boolean
const NOT = bool => a => b => bool(b)(a);

const NOT_TRUE = NOT(TRUE)
console.log(lambdaToBoolean(NOT_TRUE))

const NOT_FALSE = NOT(FALSE)
console.log(lambdaToBoolean(NOT_FALSE))

// note: A & B sont des booleans lambda (donc sous la forme bool => a => b => bool(b)(a))
const OR = A => B => A(A)(B)


const table = [[FALSE, FALSE], [FALSE, TRUE], [TRUE, FALSE], [TRUE, TRUE]];
const apply_logic_operation = OPERATOR => OPERANDES => lambdaToBoolean(OPERATOR(OPERANDES[0])(OPERANDES[1]))

console.log("OR")
// nice use of partial application 
console.log(table.map(apply_logic_operation(OR)));

const AND = A => B => A(B)(A)

console.log("AND")
console.log(table.map(apply_logic_operation(AND)))

const NAND = A => B => NOT(AND(A)(B))

console.log("NAND")
console.log(table.map(apply_logic_operation(NAND)))

const XOR = A => B => AND(OR(A)(B))(NAND(A)(B))

console.log("XOR")
console.log(table.map(apply_logic_operation(XOR)))
