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
