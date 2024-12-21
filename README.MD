# D&A
I’ve been a software engineer since the end of 2020, and it’s about time I git good.

There’s simply no escape from D&A (Data & Algorithms). If you want to build fast, efficient products, you need a solid foundation in them. One way or another, I’m diving in—no turning back!

## Way of working
To keep things easy I will just go through 2 or maybe 3 books if needed.

The first book is `grokking algorithms, an illustrated guide for programmers and other curious people`

The next books is `CRLS  (Introduction to Algorithms)` the t h i c c book. Have it since 2022 it's about time I read more then the first 50 pages.


# Book notes
## Grokking Introduction to algorithms
A introductionary book to algorithms, simple and effective in giving you a intuition of algorithms with good visuals.
For a engineer like me who is schooled in mechanical engineering these type of books are gold. 
It gives me a tangible idea of how data gets stored in memory and the difference how a linkedlist does this instead of a array. So 10/10 book if you already kinda know how to program and need to a starter on algorthms. 

## Binary search
`binary_search.py`
Set a low and a high, usually the beginning and end of your data input. 
Then make a guessing the middle low + high // 2 
If your guess is the item return the guess. 
If the guess < item, low + 1, if guess > item, low - 1.
Else return None 

```python
def binary_search(array, item):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None  
```

## Big O notation
Big O notation tells you how fast an algorithm is. Big O doesn't tell you the speed in seconds. Big O notation lets you compare the number of operations.It tells you how fast the algorithm grows.

### Big O establishes a worst-case run time 
Big O notation is about the worst-case scenario, it's a reassurance, you know that the algorithm will not exceed the Big O time. 

### Common Big O run times 
- O(log n) log time, example binary search
- O(n) linear time, Simple search (bad)
- O(n * log n) fast sorting algorithm, example quicksort 
- O(n^2) slow sorting algorithm, example selection sort 
- O(n!) really slow algorithm, like traveling salesperson


# Runtimes for common operations on arrays and lists

            Arrays  Lists
Reading     O(1)    O(n)
Insertion   O(n)    O(1)
Deletion    O(n)    O(1)


Arrays and lists, arrays allow random access , lists only allow sequential access. 


# SelectionSort 
You look at a entire list, you find the smallest element in that list. 
And swap it with the first element. 
You keep doing this in a loop untill you went through every element in the original input array. 
