# Reminder
Do the activities in the Instructions and answer these questions in your notebook. Have a partner review your answers and 'sign' his/her name in your notebook along with clearly printing their name for each step below. After we complete all work I will sign off on your notebook for all warmups combined for Unit 6.

> By signing you attest that I read the answers and agree that they are full and correct. I will gladly accept their grade as my own.   
## Reviewed by: {Student Name}

# Step #1 - review.py
**Question #1A**  
Examine the `get_sum.png` graph. Explain what the graph is saying about the code found in the method `get_sum`. What is the Big-O?

> Explain in 1-3 sentences.

 **Question #1B**  
Examine the graphs `limit_range_fast.png` and `limit_range_slow.png`. How do the points on each of the graphs grow on the y-axis? Does it look linear? Describe how the graphs **look** using Big-O notation.

> Explain graph observations in 1-3 sentences.

Examine the **code** for the `limit_range_slow`. Explain why it is so slow. Explain the Big-O complexity as best you can. Do your best to _show_ the work to _derive_ the Big-O complexity. In this example, we will assume that there are n values in the list. AND, the range will be of size n. (e.g. n = high - low).   

For reference, the slow code is:
```python
return [ n for n in range(low, high) if n in items]
```
> Explain the slowness of the code in 2-4 sentences.

**Question #1C**  
Examine the graphs and code for the three method:  
* `get_list_slow`  
* `get_list_med`  
* `get_list_fast`   

Explain why the code is slower or faster. Don't forget to look at the scale. Explain what you see in the graphs. What is the Big-O for each method?

Explain why there are outlier data points when many of the data points are zero.

> Explain in 3-5 sentences.

**Question #1D**  
Examine the graphs and code for the two method:  
* `species_count_list`  
* `species_count_set`  

Explain why the code is slower or faster. Don't forget to look at the scale. Explain what you see in the graphs. What is the Big-O for each method?

> Explain in 1-2 sentences.


# Step #2 - primes.py
**Question #2A**   
After looking at your graph, what is your best guess for the time complexity of your **ORIGINAL** `my_get_primes` algorithm?
Does it appear Linear or Quadratic? Does this meet your expectations as you examine the code? Explain.  

> explanation/analysis. 1-2 sentences

**Question #2B**   
After looking at your graph, what is your best guess for the time complexity of your implementation of **Sieve of Eratosthenes** (`sieve_get_primes`)? Does it appear Linear or Quadratic? Does this meet your expectations as you examine the code? Explain.  

> explanation/analysis here. 2-4 sentences

**Question #2C**   
After looking at your graph, what is your best guess for the time complexity of your "plagiarized" version of **Sieve of Eratosthenes** (`web_get_primes`)? Does it appear Linear or Quadratic? Does this meet your expectations as you examine the code? Explain.  

Feel free to do some online research of Sieve of Eratosthenes to provide the true, theoretical Big-O time complexity.

> explanation/analysis here. 2-4 sentences

# Step #3 - hailstone.py
**Question #3A**   
After looking at your graph, what is your best guess for the time complexity of your implementation of **Hailstones Sequence** (`my_hailstone_seq`)? Does it appear Linear or Quadratic? Does this meet your expectations as you examine the code? Explain.  

> explanation/analysis here. 2-4 sentences

**Question #3B**   
After looking at your graph, what is your best guess for the time complexity of your revised implementation of **Hailstones Sequence** using Dynamic Programming (`dynamic_hailstone_seq`)? Does it appear Linear or Quadratic? Does this meet your expectations as you examine the code? Explain.  

> explanation/analysis. 2-4 sentences

