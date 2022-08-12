Working through Anjana Vakil's "Functional Javascript: First Steps"

- Repo: https://observablehq.com/collection/@anjana/functional-javascript-first-steps
- Anjana Vakil : https://twitter.com/anjanavakil

---

# Tail Call Optimization

Video explanation : https://www.youtube.com/watch?v=-PX0BV9hGZY

Tail Call rewriting tips 
```javascript
// woot writes `n` times `!`
const woot = (n) => {
	const woo = (n, acc) => {
		if (n === 0) return acc;
		return woo(n-1, acc + "!")
	}
	return woo(n, "") // base case passed through the func
}
```

---

A predicate function is a function that returns boolean.

---

Partial application

```javascript
const add_a_and_b = (a, b) => a + b;

const add_5_to_a = (a) =>  add_a_and_b(a, 5) ;

const make_add_X_function = (x) => {
	return function(a) {
		return add_a_and_b(a, x)
	}
}
```

---

# Lambda Calculus

video : https://youtu.be/qTHGmVrOGZo 

- abstraction defines a function `λx.x` : `x => x`
- currying : `λxλy.x+y` : `x => y => x + y`
- application (call a function) `(λxλy.x+y) 5 1` : `(x => y => x + y)(5)(1)`


---

Immutable Data Structures in Javascript
- Immutable-JS : https://immutable-js.com/
- Immer : https://immerjs.github.io/immer/

More resources : https://observablehq.com/@anjana/next-steps
