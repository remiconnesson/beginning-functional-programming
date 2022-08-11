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
