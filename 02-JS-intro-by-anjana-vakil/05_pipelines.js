/*
 * Pipelines
 */

function pipeline(...functions) {
  if (functions.length === 0) return input => input;
  if (functions.length === 1) return input => functions[0](input);
  return function(input) {
    return pipeline(...functions.slice(1))(functions[0](input))
  };
}

let functions = [
  [],
  [x => x*22],
  [x => x*22, x => x-1]
]

functions.map(funcs => console.log(pipeline(...funcs)(1))); 

/*
 * Reduce
 */
function reduce(reducerFn, acc, array) {
  if (array.length === 0) return acc;
  return reduce(reducerFn, reducerFn(acc, array[0]),array.slice(1))
}

console.log( 
  reduce((acc, x) => acc + x, 0, [1, 2, 3])
)

/*
 * Pipeline with Reduce
 */

function pipeline2(...functions) {
  return function(x) {
    return reduce( (acc, fn) => fn(acc), x, functions)
  } 
}
console.log('pipeline implemented using reduce');
functions.map(funcs => console.log(pipeline2(...funcs)(1))); 
