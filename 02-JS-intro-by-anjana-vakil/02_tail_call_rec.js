/*
 * sum of an array tc?
 */

const sum_array = (arr) => {
	const func = (arr, acc) => {
		if (arr.length === 0) return acc;
		return func(arr.slice(1), acc + arr[0]);
	}
	return func(arr, 0);
}

console.log(sum_array([1, 2, 3]));

/*
 * factorial
 */

const factorial = (n) => {
	const func = (n, acc) => {
		if ( n === 0 ) return acc;
		return func(n-1, acc * n);
	}
	return func(n, 1);
}

console.log(factorial(10), 10*9*8*7*6*5*4*3*2*1)

/*
 * fibonnaci
 */
const fibonnaci = (n) => {
	const func = (n, current, next) => {
		if (n === 0) return current;
		return func(n - 1, next, current + next)
	}
	return func(n, 0, 1)
}

const loop_fibo = (n) => {
	const func = (n, i) => {
		console.log(i, fibonnaci(i));
		if (n === 0) return;
		func(n-1, i + 1)
	}
	func(n, 0);
}

loop_fibo(21);


