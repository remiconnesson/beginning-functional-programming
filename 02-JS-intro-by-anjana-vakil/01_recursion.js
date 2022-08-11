function sum1 (numbers) {
	let total = 0;
	for (i=0; i < numbers.length ; i++) {
		total += numbers[i];
	}
	return total;
}

console.log(sum1([0, 1, 2, 3, 4]));

// my attempt
function sum2 (acc, numbers) {
	if (numbers.length === 0) {
		return acc
	} else { 
		return sum2(acc + numbers[0], numbers.slice(1))
	}
}

console.log(sum2(0, [0,1,2,3,4]));

// Anjana's solution
function sum3 (numbers) {
	if (numbers.length === 1) {
		return numbers[0]
	} else {
		return numbers[0] + sum3(numbers.slice(1));
	}
}

console.log(sum3([0, 1, 2, 3, 4]));
