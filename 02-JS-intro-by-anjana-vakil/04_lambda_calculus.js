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
