# Internet Of Things | Worksheet 2 Part 2
This gitlab repo contains the resources for worksheet 2 part 2

## Contents
1. [Task 1](#Task-1)
2. [Task 2](#Task-2)
3. [Task 3](#Task-3)
4. [Task 4](#Task-4)

## Task 1
In this task we had to create what is known as a binary heap. A binary heap is a linear representation of a complete binary tree. In this task our binary heap is represented as a python list of chars. 

In task 1 we had to implement the following function:
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

## Task 2
In this task we had to understand and explore how "Ham Radio Conversations" were conducted. This involved port forwarding a port "10101" from the remote development server. We connected to a site via "localhost:10101". This allowed us to understand how the messages are constructed and decoded better.

<img src="./resources/ws2_p2_t2.png" width="70%"/>

In this we also had to implement 2 new additional functions as follows:
```python

# encoding will take in a sender the recipient and the a message payload
# the arguments passed are all strings and will return a string encoded in morse code
encode_ham(sender: str, receiver: str, msg:str) -> str
encode_ham("charles","james","urgency")

output: 

    ".--- .- -- . ... -.. . -.-. .... .- .-. .-.. . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--."

# decode ham will take in a ham conversation morse code message and will decode the message to return the sender, recipient, message
decode_ham(msg:str) -> (str, str, str)
decode_ham(".--- .- -- . ... -.. . -.-. .... .- .-. .-.. . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--.")

output:

    decoded_raw: jamesdecharles=urgency=(,
    sender: charles,
    rec: james,
    content: urgency
    ('charles', 'james', 'urgency')

```

Encode ham will be responsible for converting our a message and given arguments into the ham radio conversation style by grouping sender and receiver names separated with the char set "de" in this example. Charles is the sender, the receiver is james the formatted message for the ham radio conversation will be "charlesdejames" we then append an equals along with our message. at the end of our message we will append "=(" to mark the end of the message.

The decode ham will decode the ham conversation style message to return us separate values into a turple. This turple will contain the sender, receiver and the message in that order. 

