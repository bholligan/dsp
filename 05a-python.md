# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists both store a collection of items that can be assigned to a variable. The key difference between them is that tuples are immutable, meaning the values inside the tuple can not be changed. Tuples also have a fixed size in memory, which is beneficial for reducing space.  
>> Tuples will work as keys in dictionaries. Dictionary values can be of any type, but dictionary keys must be immutable, and this includes tuples (as well as strings and numbers).

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set is an ordered collection with no duplicate elements. This is a crucial behavior that allows it to behave like the mathematical definition of a set and enable operations like union and difference. Sets can't contain mutable objects, but they are mutable themselves. Lists are ordered collections, so you can index and slice them. Because sets are unordered, they behave more akin to dictionaries when referencing and removing values.  
  
```python
#Lists and Sets examples  
>>> name_set = {'Bob', 'James', 'Mary', 'Bob'}
>>> print(name_set)  
{'Bob', 'James', 'Mary'}   # All duplicate values are eliminated. Collection is unordered.  
>>> 'Bob' in name_set     #This is case sensitive.   
True  
>>> name_list = ['Bob', 'James', 'Mary', 'Bob']
>>> print(name_list)
['Bob', 'James', 'Mary', 'Bob']  #All list items are retained.
>>> print(name_list[3])
'Bob'     #Lists are ordered, and thus can be indexed and referenced with indexing  
```  
>> For performance, a set will be faster than a list when testing for membership. This is because sets are implemented with hash tables, so the existence of an item within a set can be determined very quickly using the item's hash. Python uses dynamically resized hashtables that improve lookup times.  

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The `lambda` keyword is a convenient way to express one-line functions. Lambda functions can be used anyplace a function object is required. They are restricted to a single expression.  
```python
# Base example  
# This function:  
def f(x):  
  return x*2   
# is the same as:  
f = lambda x: x*2 
```
>> Lambda can be used with the map() function. The inputs to a map are a function  
>> and a sequence, which allows an array of values to be processed by the lambda function.  
>> Map() returns an iterator that can be placed in a list with ease.  
```python
>>> a = [1, 2, 3]
>>> b = [7, 8, 9]
>>> list(map(lambda x,y:x+y, a,b)
[8, 10, 12]  
```  
>> The sorted() function accepts an iterable, a key function, and an optional reverse  
>> parameter to toggle between ascending and descending sorts. They key function applies  
>> to each element of the iterable before any comparisons are made. This can be combined  
>> in a useful way with lambda to use an object's indices as keys.  
```python  
>>> points = [('Kobe', 21), ('LeBron', 25), ('Wade', 18)]
>>> sorted(points, key = lambda x: x[1])
[('Wade', 18), ('Kobe', 21), ('LeBron', 25)]
# In this example, players are sorted in ascending order by their points,  
# which is in position 1 of the tuple.  
```  
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions allow lists to be created concisely and elegantly. The simplest list comprehension takes the form of [`expression-involving-loop-variable` for `loop-variable` in `sequence`].  The following will show list comprehension on different names.
```python
>>> names = ['Adam','Barry','Grace','George','Martha','Tom']
#1. Output the length of each name in the names list 
>>> [len(name) for name in names]
[4, 5, 5, 6, 6, 3]
#2. Output the first letter of each name if the name does not end in 'm'.
>>> [name[0] for name in names if name[len(name)-1] != 'm']
['B', 'G', 'G', 'M']
```
>> Examples 1 and 2 above can be done using the `map` and `filter` functions respectively. `map` is explained in Question 3. Filter works by accepting a function that returns True or False and applying it to a given sequence. Filter will return the members that evaluated to True in the function.  
```python
#1. Getting the length of each name with map().
>>> list(map(len, names)) #len is the function being passed in, names is the iterable. 
[4, 5, 5, 6, 6, 3]
#2. This filter retrieves each name not ending in 'm'.
>>> list(filter(lambda name: name[len(name)-1] != 'm', names))
['Barry', 'Grace', 'George', 'Martha']
```
>> Set comprehension is similar to list comprehension. Of course the set will exclude duplicate values, meaning if we run our name length comprehension, the following will occur.
```python
>>> {len(name) for name in names}
{3, 4, 5, 6}
#Per our expectation, the 5 letter and 6 letter names are only recorded once in the set.
```
>> Dictionary comprehension can be used to create key value pairs out of the name and length of names that we have been using. In dictionary comprehension, a colon is used to separate the key and value expressions.
```python
>>> {name: len(name) for name in names}
{'Adam': 4, 'Barry': 5, 'George': 6, 'Grace': 5, 'Martha': 6, 'Tom': 3}
```
  
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





