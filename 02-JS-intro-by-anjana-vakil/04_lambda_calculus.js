/*
 * Count 
 */

let zero = f => x => x;
let one = f => x => f(x);
let two = f => x => f(f(x))
let three = f => x => f(f(f(x)));

let lambdaToNumber = lambda => lambda(i => i+1)(0);

console.log([zero, one, two, three].map(lambdaToNumber))




