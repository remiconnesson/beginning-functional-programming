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
