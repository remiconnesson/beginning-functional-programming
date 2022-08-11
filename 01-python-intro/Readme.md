I'm gonna work through "an introduction to functional programmin" by Mary Rose Cook

- Tutorial : https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming
- Mary Rose Cook : https://maryrosecook.com

# Notes from the article

## Definitions

**Imutable Data**
> An immutable piece of data is one that cannot be changed. Some languages, like Clojure, make all values immutable by default. Any “mutating” operations copy the value, change it and pass back the changed copy. This eliminates bugs that arise from a programmer’s incomplete model of the possible states their program may enter.

**First Class Functions**
> Languages that support first class functions allow functions to be treated like any other value. This means they can be created, passed to functions, returned from functions and stored inside data structures.

**Tail Call Optimization**
> Tail call optimisation is a programming language feature. Each time a function recurses, a new stack frame is created. A stack frame is used to store the arguments and local values for the current function invocation. If a function recurses a large number of times, it is possible for the interpreter or compiler to run out of memory. Languages with tail call optimisation reuse the same stack frame for their entire sequence of recursive calls. Languages like Python that do not have tail call optimisation generally limit the number of times a function may recurse to some number in the thousands. In the case of the `race()` function, there are only five time steps, so it is safe. 

**Currying**
> Currying means decomposing a function that takes multiple arguments into a function that takes the first argument and returns a function that takes the next argument, and so forth for all the arguments.

**Parallelization**
> Parallelization means running the same code concurrently without synchronization. These concurrent processes are often run on multiple processors.

**Lazy Evaluation**
> Lazy evaluation is a compiler technique that avoids running code until the result is needed.

**Deterministic Process**
> A process is deterministic if repetitions yield the same result every time.

Mary Rose Cook says about the above stuff :
> Ignore all that. Functional code is characterised by one thing: the absence of side effects. It doesn’t rely on data outside the current function, and it doesn’t change data that exists outside the current function. Every other “functional” thing can be derived from this property. Use it as a guide rope as you learn.

# Takeaway

- replace loop by passing state to a recursive function of that state
- replace sequence of statements affecting the same state by a pipeline 

From the tutorial: 

```python
print pipeline_each(bands,
										[set_canada_as_country,
                    strip_punctuation_from_name,
										capitalize_names])
```

> This code is easy to understand. It gives the impression that the auxiliary functions are functional because they seem to be chained together. The output from the previous one comprises the input to the next. If they are functional, they are easy to verify. They are also easy to reuse, easy to test and easy to parallelize.

> This contrast between the mutability of strings and dictionaries in Python illustrates the appeal of languages like Clojure. The programmer need never think about whether they are mutating data. They aren’t.

```python
def assoc(_d, key, value):
    from copy import deepcopy
		d = deepcopy(_d)
		d[key] = value
		return d

def call(fn, key):
    def apply_fn(record):
        return assoc(record, key, fn(record.get(key)))
		return apply_fn
```


> Five. There is no mention of bands in the call() code. That is because call() could be used to generate pipeline functions for any program, regardless of topic. Functional programming is partly about building up a library of generic, reusable, composable functions.

# Conclusion
> What now?

>Functional code co-exists very well with code written in other styles. The transformations in this article can be applied to any code base in any language. Try applying them to your own code.

> Think of Mary, Isla and Sam. Turn iterations of lists into maps and reduces.

> Think of the race. Break code into functions. Make those functions functional. Turn a loop that repeats a process into a recursion.

> Think of the bands. Turn a sequence of operations into a pipeline.
