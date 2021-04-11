"""
    Scripted by Charles Edwards
    Worksheet 2 Part 2 Task 3
    Derived from Worksheet 2 Part 1, unnecessary code removed
"""
class Node: ## Node Class

    def __init__(self, turple): ## Constructor
        self.left = None        # left node
        self.right = None       # right node
        self.data  = turple     # turple data assigned to current node

    def recursivelyInsertAlphabetical(tree, turple): # called when we want to insert a letter into the binary tree alphabetically

        # get the letter and full morse code from the turple
        letter = turple[0]
        morse = turple[1]

        # if the tree is none
        if tree is None:
            # append a new node
            return Node( (letter, morse) )
        else: # if the node is not none then lets attempt to insert missing elements

            if letter < tree.data[0]:  # determine letter ord / ASCII value and perform comparison
                tree.left = Node.recursivelyInsertAlphabetical(tree.left, turple) # perform recurisvely insert
                return tree # return the tree
            elif letter > tree.data[0]:  # determine letter ord / ASCII value and perform comparison
                tree.right = Node.recursivelyInsertAlphabetical(tree.right, turple) # perform recurisvely insert
                return tree # return the tree
            else:
                tree.data =  (letter, morse) # replace tree if same as
                return tree # return the tree

    def recursivelyFindAlphabeticalLetter( tree, letter ): # called when we want to search a letter from alphabetically to return a morse code
        if tree is None: # null check tree
            raise Exception( "Invalid letter" )
        else:# if tree is valid
            if letter < tree.data[0]: # determine alphabetical order of letter
                return Node.recursivelyFindAlphabeticalLetter( tree.left, letter ) # search the left trees recursively
            elif letter > tree.data[0]: # determine alphabetical order of letter
                return Node.recursivelyFindAlphabeticalLetter( tree.right, letter ) # search the right trees recursively
            else:
                return tree.data[1] # return the morse code

# morse code letters are created left to right from branch top to down
# due to the nature we add them
morseCodeLetters = [  

    # first layer
    ( "E", "." ),
    ( "T", "-" ),

    # second layer
    ( "I", ".." ),
    ( "A", ".-" ),
    ( "N", "-." ),
    ( "M", "--" ),

    # third layer
    ( "S", "..." ),
    ( "U", "..-" ),
    ( "R", ".-." ),
    ( "W", ".--" ),
    ( "D", "-.." ),
    ( "K", "-.-" ),
    ( "G", "--." ),
    ( "O", "---" ),

    # fourth layer :: NOTE 4 nodes are blank
    ( "H", "...." ),
    ( "V", "...-" ),
    ( "F", "..-." ),
    ( "BLANK", "..--" ),

    ( "L", ".-.." ),
    ( "BLANK", ".-.-" ),
    ( "P", ".--." ),
    ( "J", ".---" ),

    ( "B", "-..." ),
    ( "X", "-..-" ),
    ( "C", "-.-." ),
    ( "Y", "-.--" ),

    ( "Z", "--.." ),
    ( "Q", "--.-" ),
    ( "BLANK", "---." ),
    ( "BLANK", "----" ),

    # fifth layer
    ( "5", "....." ),
    ( "4", "....-" ),
    ( "3", "...--" ),
    ( "2", "..---" ),

    ( "+", ".-.-." ),
    ( "1", ".----" ),

    ( "6", "-...." ),
    ( "=", "-...-" ),
    ( "/", "-..-." ),
    
    ( "7", "--..." ),
    ( "8", "---.." ),
    ( "9", "----." ),
    ( "0", "-----" ),

    # task 4 adding missing symbols

    # missing blank nodes
    ( "BLANK", "--..-" ),
    ( "BLANK", "...-." ),
    ( "BLANK", "...-.." ),
    ( "BLANK",".-..-" ),
    ( "BLANK","-.-.-" ),

    ( ".", ".-.-.-" ),
    ( "(", "-.--." ),
    ( "¿", "..-.- " ),

    ( ",", "--..--" ),
    ( ")", "-.--.-" ),
    ( "-", "-....-" ),
    ( "¡", "--...-" ),

    ( "?", "..--." ),
    ( "&", ".-..." ),
    ( "_", "..--.-" ),

    ( "'", ".----." ),
    ( ":", "---..." ),
    ( '"', ".-..-." ),

    ( "!", "-.-.--" ),
    ( ";", "-.-.-." ),
    ( "$", "...-..-" ),
    
]

"""
    Construct Alphabetical Binary Tree
"""
# root node
root_AlphabeticalCodeTree = Node( ("root","r") )

# for every turple in morseCodeLetters
for turple in morseCodeLetters:
    # recursively construct branch
    root_AlphabeticalCodeTree = Node.recursivelyInsertAlphabetical( root_AlphabeticalCodeTree, turple )

def encode(text): # called when we want to encode text
    encodedStr = "" # string that will be used for construction of morse code
    for letter in text:
        if letter != " ": # if there is no space char then convert char into morse code and add a space on the end
            encodedStr += str(Node.recursivelyFindAlphabeticalLetter(root_AlphabeticalCodeTree,letter.upper())) + " " 
        else:# else if the char is a space then append a forward slash with a space on the end
            encodedStr += "/ "

    # return encoded string
    return encodedStr[:-1] # chop off the last space