# Instructions  

This unit is about performance.

We are going to go through this work together in class. Work on this as directed by your teacher as you should be able to complete most of the work and activities as part of our daily warmup activities (unless you need to catch up).

__Note:__ that our systems are pretty fast for running this code so running under the debugger slows things down enough to generate better graph output.

## Summary of Steps
1. Run the code in `review.py` using the Shell tab. Run the code to generate graphs. Examine the code and graphs and answer the questions #1A-D in the readme.  
2. Implement the code to generate primes in the file `primes.py`. Measure the performance and create a graph. Answer questions #2A-C in the readme file.
3. Implement the method `hailstone_seq` in the file `hailstone.py`. Measure the performance and create a graph. Answer questions #3A-B in the readme file. 
4. Get a partner student to read your answers and attest that the answers are **complete and correct**. Have that student `sign` your notebook and print their name clearly.  


## Big-O 
This project will execute a method multiple times each with a different size (value for n). 
Each time it runs, the method will be timed and then the results will be graphed. 
We want to illustrate how using a good/poor algorithm or data structure will impact the performance.

# Step 1 - review.py
This section has a few methods that are timed and graphed. The goal of this section is to inspect and reflect upon performance. You will have seen stuff like these problems in your homework.   

**Methods & Questions Summary:**  
* Question 1A:  
    * `get_sum`  
* Question 1B:
    * `limit_list_to_range_slow`
    * `limit_list_to_range_fast` 
* Question 1C:  
    * `get_list_slow`  
    * `get_list_med`  
    * `get_list_fast`  
* Question 1D:  
    * `species_count_list`
    * `species_count_set`  

In the Shell Tab, execute the `review.py` file. This will create several plots in the `plots` folder. 

## get_sum
**Examine the graph** `get_sum.png` and explain what it is saying 
in **Question 1A** in the `readme.md` file.

## limit_list_to_range
The code is working to include items in a list only if they are within a 
specific range. One common solution is very slow:
```python
return [ n for n in range(low, high) if n in items]
```
Another solution is much better.
```python
return [n for n in items if n >= low and n < high ]
```

Examine the two graphs created. 
* limit_list_to_range_fast.png  
* limit_list_to_range_slow.png  

In each of these graphs, we are using n values that grow exponentially. 
For example, the list of n values might be: 
`[100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600]` Note that the value 
of n starts at 100 and doubles each time. We call the method using these 
different n values and measure the time it takes. Because the slow method 
is so much slower, we stop with n = 3200. But, for the fast algorithm, we 
let n grow to 3276800.  

For this problem, we've actual have 3 input values (list, low, high). All of 
them relate to n in the following ways:
* There are n values in the list. AND, 
* The range between high and low has size N, where N = high - low. 

**Examine the code and the times** printed in the console window.  
**Examine the graphs.** Be sure to look at the scale in the graphs.

**Fill out both parts of question #1B in the `readme.md` file.**

## get_list
This step is similar to the previous steps. You will look at the code for 
`get_list_slow`, `get_list_med` and `get_list_fast`. Look at the graphs 
and answer Question #1C in the readme.md file.  

> **Important:** The analysis of these methods involves yet another consideration.
> This is discussed in `Lesson 17: Revisiting Time Efficiency`. 

## species_count
In this part of the assignment, we are attempting to illustrate the differences in performance when using `set` vs `list`. Answer questions 1D in the readme.


# Step 2 - primes.py
You will implement a method that finds prime numbers in three different ways. For each different implementation, you'll **test** the solution to verify that it works and then **graph** its performance.  

There is a sample testing method provided for you, `test_set_of_primes`.  

You'll graph the performance using the `TimeGraph` class provided for you. Here is sample code for how to graph `my_get_primes`.  
```python
# plots will be created and put into the "plots" folder
timer = TimeGraph()
# default value for max_iters = 16. When graphing the speed of a slow
# algorithm, set max_iters to something "small" such as 8.
# As max_iters grows, time is impacted exponentially which can be dangerous!
# In slow situations it may take 60 seconds to complete!
timer.time_and_graph(my_get_primes, max_iters=8)
```

1. `my_get_primes`: This will be entirely **your own solution** to finding prime numbers.  Don't worry if it is slow, just make sure that it works.  
2. `sieve_get_primes`: Code this yourself. Do **NOT** get code from the internet. However, you can learn about _how_ the algorithm works online if the explanation below is insufficient. This implementation will use the algorithm, **Sieve of Eratosthenes**. You'll need to learn the algorithm before you implement it. The algorithm is described below. This specific approach uses sets while most other implementations use arrays of boolean values. Please use this _set_ approach so the implementation can verifiably be your own.   

**Sieve of Eratosthenes**:  
```
Fill a set with all numbers {2, 3, ... , max}   
For every number n still in the set of primes:   
     Remove all multiples of n, but not n itself   
```
For example, the values in the set will update as follows:

`# fill a set with every number`  
{ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, ... }   
`# remove multiples of 2 that are greater than 2`   
{ 2, 3, **~~&nbsp;4&nbsp;~~**, 5, **~~&nbsp;6&nbsp;~~**, 7, **~~&nbsp;8&nbsp;~~**, 9, **~~&nbsp;10&nbsp;~~**, 11, **~~&nbsp;12&nbsp;~~**, 13, **~~&nbsp;14&nbsp;~~**, 15, **~~&nbsp;16&nbsp;~~**, 17, **~~&nbsp;18&nbsp;~~**, 19, **~~&nbsp;20&nbsp;~~**, 21, **~~&nbsp;22&nbsp;~~**, 23, **~~&nbsp;24&nbsp;~~**, 25, **~~&nbsp;26&nbsp;~~**, ... }   
`# remove multiples of 3 that are greater than 3`  
{ 2, 3, 5, 7, **~~&nbsp;9&nbsp;~~**, 11, 13, **~~&nbsp;15&nbsp;~~**, 17, 19, **~~&nbsp;21&nbsp;~~**, 23, 25, **~~&nbsp;27&nbsp;~~**, 29, 31, **~~&nbsp;33&nbsp;~~**, 35, 37, **~~&nbsp;39&nbsp;~~**, 41, 43, **~~&nbsp;45&nbsp;~~**, 47, 49, ... }  
`# We skip 4 because 4 is not in the set`  
`# remove multiples of 5 that are greater than 5`  
{ 2, 3, 5, 7, 11, 13, 17, 19, 23, **~~&nbsp;25&nbsp;~~**, 29, 31, **~~&nbsp;35&nbsp;~~**, 37, 41, 43, 47, 49, ... }   
`# We skip 6 because 6 is not in the set`  
`# remove multiples of 7 that are greater than 7 `  
{ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, **~~&nbsp;49&nbsp;~~**, ... }  
`# We skip 8, 9 and 10 because those are not in the set`  
`# remove multiples of 11... `  

More information can be found on the [internet](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).  

3. `webs_get_primes`: Copy the best Python implementation you can find on the internet. It may return a list or a set, whichever is fastest! But, you must still verify that it works.  

**Answer the questions 2A-C in the readme.md file**

# Step 3 - hailstone.py
Implement the Hailstone Sequence in the file `hailstone.py`. You'll implement it, verify that it works, and then graph it. You'll do this **twice**.  

The hailstone sequence is a famous sequence of numbers. As far as we know, no matter what number we start with, the sequence will result in a repeated ending in: `[16, 8, 4, 2, 1]`. If we continue, the sequence repeats `[ 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, ...]` which is why we STOP when we hit the number 1.  

The rules to generating the number in the sequence is: 
```
  next = n / 2     if n is even
  next = n * 3 + 1 if n is odd
```
The goal is to create a dictionary where the key is the starting number and the value is the length of the sequence. Here is a sample dictionary where the max n value is 16. Each value is the length of the sequence.  
```python
{ 1:1, 2:2, 3:8, 4:3, 5:6, 6:9, 7:17, 8:4, 
  9:20, 10:7, 11:15, 12:10, 13:10, 14:18, 15:18, 16:5
}
```
Here some sample sequences:  
```
1 [ 1 ]
2 [ 2, 1 ]
3 [ 3, 10, 5, 16, 8, 4, 2, 1 ]
4 [ 4, 2, 1 ]
5 [ 5, 16, 8, 4, 2, 1 ]
6 [ 6, 3, 10, 5, 16, 8, 4, 2, 1 ]
7 [ 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 ]
```

Your **first** implementation, `my_hailstone_seq`, should be simple. It won't be horribly slow, but it won't be fast.  Test it and plot it.  

Your **second** implementation, `dynamic_hailstone_seq`, should be a bit more complicated but a LOT faster. Do your best to implement the dynamic solution yourself. If you cannot get it, get hints from other students.  

## Dynamic Solution Details
One category of algorithmic solutions is called `Dynamic` which means that answers
found along with way are cached and reused again later in subsequent solutions. For example, when we solve for the length of the hailstone sequence starting at 6, the second number in the sequence is 3. We've already solved for the length of the sequence for 3 earlier in our loop to build the full dictionary!   

This _crazy buggy_ pseudo-code illustrates the idea of Dynamic Programming.
```python
# this code is incredibly BUGGY! But, the concept is present
solution = dict()
while n != 1:
    next = n / 2         # if n is even
    next = n * 3 + 1     # if n is odd
    if next in solution:
        solution[n] = 1 + solution[next]
        continue
    n = next
```
Illustrated slightly differently:  
```python
hailstone_length(16) = 1 + hailstone_length(8)
hailstone_length(6) = 1 + hailstone_length(3)
hailstone_length(5) = 1 + hailstone_length(16)
```

# Profiling
It can be cool to see how your code performs line-by-line. Let's profile your code!  

1. Add the package `line-profiler` using the `conda install line_profiler` or find this in your anaconda navigator for your idp environment and add it there. 
2. Add `@profile` at the top of a few methods that calculate primes and hailstone sequence lengths.
3. Run in the Shell tab: `kernprof -v -l primes.py` to see the profiler output.  


# Loose.py
In this section, we will Explore and Discuss:  
* Loosely Typed vs Strongly Typed  
* Dynamic Typing vs Static Typing  
* Duck Typing
* Overloaded Methods

In class, we will walk the classroom through a series of "experiments"
on the loose.py file in an attempt to understand through trial an error how
Python interprets code

Python is a `Loosely Typed` language that Dynamically types the identifiers using
Duck Typing. In contrast, Java is a Stongly Typed language with Static Typing. This
means that Java determines all the types a compile time and those types cannot change.

> Side Note: Python doesn't necessarily _compile_ the code in the traditional way that we
> understand compiling (e.g. with Java). However, this doesn't mean that code
> isn't compiled at all. It all depends on which Python Compiler is installed.

Python is a `Dynamic` language. This means that the types of a variable/identifier
is determined at runtime. In Python we do NOT specifically declare that a variable has a type.
Instead, we let the interpreter figure out the type. Python will use a method
called `Duck Typing` to figure out the type. 

> What is a Duck? Well...

> “If it looks like a duck, walks like a duck and quacks like a duck, it must be a duck”

This means that the type (or class) of an object is less important than the methods 
it defines. Using `Duck Typing`, Python does not check types at all. Instead, 
it checks for the presence of a given method or attribute. 

**Steps:**
1) Run `loose.py`.
2) BEFORE you run the code, what do you expect the output to be.
     * Note the method `strange`. 
4) Run to see the output. Compare with your expectations.
5) Update the method `main()` to include the code below. Predict the output. Then verify. Explain using technical CS vocabulary.
```
   loose(b, a)
   loose(0, -1)
   loose('c', 'd')
```
6) Update `main()` to call `strange`. Predict the behavior. Then verify. Explain using technical CS vocabulary.
> This method `strange` demonstrates how the program can run even
> with clear errors present in the file. There is no method
> with the name `no_existence`. But, we won't discover that until
> we run the program and add a call to `strange`.

7) Using what we've learned, explain why Python doesn't have `Overloaded Methods` like Java does
     * How does Python support our desire for overloaded methods?
9) What are the differences between Dynamically Typed vs Loosely Typed?
     * Answer: Not much if anything! If we get pedantic, we could say...
     * Loosely Typed is deciding the type at runtime without declaration. Vs Strongly typed which is deciding at compile time.
     * Dynamically Typed allows an identifier to change its type in the same scope. Vs Static where type cannot change.
10) Write down in your notes:
     * Definitions for: Dynamically, Loosely, Statically, Strongly Typed
     * Definition of Duck Typing
     * What you learned about Python code execution.
     * The Pros/Cons of Interpreted Languages like Python. Consider:
          * speed
          * readability
          * flexibility/extensibility
          * error catching 