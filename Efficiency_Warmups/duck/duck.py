"""
The purpose of this file is to show how dynamically typed,
interpreted language can behave strangely.

We define two classes A, B which override some special methods.
  * The < operator (less than)
  * The + operator (add)
  * the toString method

The addition operator doesn't actually do addition.

To reduce the redundant code, B inherits from A.
But, B has its own definition for less than (<).

1) Run `duck.py`.
2) BEFORE you run the code, what do you expect the output to be.
     * Note the method `strange`. 
3) Run to see the output. Compare with your expectations.
4) Update the method `main()` to include the code below. Predict the output.
   Then verify. Explain using technical CS vocabulary.
```
    duck(0, -1)
    duck("c", "d")
    c = B(1)
    duck(c, b)
```
5) Update `main()` to call `strange`. Predict the behavior. Then verify. 
   Explain using technical CS vocabulary.
> This method `strange` demonstrates how the program can run even
> with clear errors present in the file. There is no method
> with the name `no_existence`. But, we won't discover that until
> we run the program and add a call to `strange`.
6) Using what we've learned, explain why Python doesn't have `Overloaded Methods`
   like Java does
     * How does Python support our desire for overloaded methods?
7) What are the differences between Dynamically Typed vs Loosely Typed?
8) Write down in your notes:
     * Definitions for: Statically, Strongly Typed, Duck Typing
     * What you learned about Python code execution.
     * The Pros/Cons of Interpreted Languages like Python. Consider:
          * speed
          * readability
          * flexibility/extensibility
          * error catching

"""


class A:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return True

    def __add__(self, other):
        return A(self.value**other.value)

    def __str__(self):
        return str(self.value)


class B(A):
    def __lt__(self, other):
        return False


def duck(o1, o2):
    """
    This one method will work with all objects that implement both
       __lt__
       __add__
    """
    if o1 < o2:
        print(f"{o1} < {o2}")
    else:
        print(f"{o1} >= {o2}")
    print(f"{o1} + {o2} = {o1 + o2}")


def strange(b):
    if b.no_existence():
        b.complain()


def identifier_t():
    t = 7
    t = str(t) + " is prime"
    t = A(7)


def main():
    # a = A(1)
    # b = B(2)
    # duck(a, b)
    # duck(b, a)
    # duck(0, -1)
    # duck("c", "d")
    # c = B(1)
    # duck(c, b)
    b = B(2)
    strange(b)


if __name__ == "__main__":
    main()