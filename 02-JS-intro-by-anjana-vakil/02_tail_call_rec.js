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


