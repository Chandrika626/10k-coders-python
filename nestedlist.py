# 1. List ([])
# Definition

# A list is an ordered and mutable collection of elements. It can store different data types and allows duplicate values.

# Features
# Ordered
# Mutable (can be modified)
# Allows duplicate values
# Supports indexing and slicing
# Stores multiple data types
# Example
# fruits = ["Apple", "Banana", "Mango"]
# print(fruits)
# Common Methods
# append() – Adds an element at the end.
# insert() – Inserts an element at a specific position.
# remove() – Removes a specified element.
# pop() – Removes an element by index.
# sort() – Sorts the list.
# reverse() – Reverses the list.
# count() – Counts occurrences of an element.
# index() – Returns the index of an element.
# extend() – Adds elements from another list.
# clear() – Removes all elements.

# 2. Tuple (())
# Definition

# A tuple is an ordered and immutable collection of elements.

# Features
# Ordered
# Immutable (cannot be modified)
# Allows duplicate values
# Supports indexing and slicing
# Faster than lists
# Example
# colors = ("Red", "Green", "Blue")
# print(colors)
# Common Methods
# count() – Counts occurrences of an element.
# index() – Returns the index of an element.
# 3. Set ({})
# Definition

# A set is an unordered collection of unique elements.

# Features
# Unordered
# Mutable
# Does not allow duplicate values
# No indexing
# Useful for mathematical operations
# Example
# numbers = {10, 20, 30, 40}
# print(numbers)
# Common Methods
# add() – Adds an element.
# remove() – Removes an element.
# discard() – Removes an element without error if not found.
# pop() – Removes a random element.
# clear() – Removes all elements.
# union() – Combines two sets.
# intersection() – Returns common elements.
# difference() – Returns different elements.
# 4. Dictionary ({key: value})
# Definition

# A dictionary is a collection of key-value pairs.

# Features
# Stores data as key-value pairs
# Mutable
# Keys must be unique
# Values can be duplicated
# Fast data retrieval using keys
# Example
# student = {
#     "name": "Chandrika",
#     "age": 20,
#     "course": "Python"
# }

# print(student)
# Common Methods
# keys() – Returns all keys.
# values() – Returns all values.
# items() – Returns key-value pairs.
# get() – Gets the value of a key.
# update() – Updates the dictionary.
# pop() – Removes a key-value pair.
# clear() – Removes all items.
# Quick Comparison

# Nested List – Notes
# A nested list is a list that contains one or more lists as its elements.
# It is also called a list of lists or 2D list.
# Nested lists are ordered and mutable.
# They allow duplicate values.
# Elements are accessed using multiple indexes (list[row][column]).
# Nested lists can store different data types.
# They are commonly used to represent matrices, tables, student records, and multidimensional data.
# You can add, remove, and modify elements just like a normal list.
# Nested lists can be traversed using nested for loops.