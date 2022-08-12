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


