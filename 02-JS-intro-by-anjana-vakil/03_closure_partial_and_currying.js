/*
 * Closures
 */ 

function add(a, b) {
	return a + b;
}

// closure, inner function will remember x
function make_add_x_func(x) {
	return function(a) {
		return add(a, x);
	}
}

const add_one_to = make_add_x_func(1);

const six = add_one_to(5)
console.log(six)

/*
 * Currying
 */

function podium(first, second, last) {
	return `${first}, ${second}, ${last}` 
}

console.log(podium(1, 2, 3))

const curriedPodium = first => second => last => podium(first, second, last);

console.log(curriedPodium(1)(2)(3));

const iWillAlwaysBeFirst = curriedPodium("Rémi");


console.log(iWillAlwaysBeFirst(1)(2))
