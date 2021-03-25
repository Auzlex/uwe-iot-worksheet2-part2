# Internet Of Things | Worksheet 2 Part 2
This gitlab repo contains the resources for worksheet 2 part 2

## Contents
1. [Task 1](#Task-1)
2. [Task 2](#Task-2)
3. [Task 3](#Task-3)
4. [Task 4](#Task-4)

## Task 1
In this task we had to create what is known as a binary heap. A binary heap is a linear representation of a complete binary tree. In this task our binary heap is represented as a python list of chars. 

In task 1 we had to implmenet the following function:
```python
decode_bt( str : message ) : return str
```
It would take in our morse code message and return the decoded message using a binary heap. We had to create an algorithm that would do this using the following rules:
```python
# sample binary heap
binary_heap = list( "-ARWL-" )

# starting index is 1
x = 1
# returns the first left branch char of the binary tree e.g. a . in morse
binary_heap[ 2 * x ] # returns A
# returns the first right branch char of the binary tree e.g. a - in morse
binary_heap[ ( 2 * x ) + 1 ] # returns R

# the morse code to decode would be: .- = AR
```
The algorithm I created would traverse the linear representation of our binary tree (heap) with the given morse code segment. And will construct our decoded message.