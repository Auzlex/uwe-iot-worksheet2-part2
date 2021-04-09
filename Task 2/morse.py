"""
    Scripted by Charles Edwards
    Worksheet 2 Part 2 Task 2
"""
"""
    imports
"""
from tree import encode # only access the encode function from tree.py

"""
    Binary Heap/ Ham Encode decode
"""
# our binary heap of letters
binary_heap = list('-ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3*¿?2&*+****16=/***(*7***8*90*************_****"**.********\'**-********;!*)***¡*,****:-')

def decode_bt(msg): # invoked when we want to decode with a binary heap

    morse_segments = msg.split("/") # split the morse code words into morse segments for decoding

    decoded_message = "" # string for holding our decoded message
    index = 1            # index used for our decoding

    # for every segment of morse code given to us
    for morse_segment in morse_segments: 

        # we strip excess spaces on the start ends of the string
        morse_segment = morse_segment.strip()

        # make sure we append an additional space on the end of every morse char, used to determine end of traversing tree
        morse_segment += " "

        # for every character in a morse segment
        for morse_char in morse_segment: # for every morse char in msg

            if morse_char == ".": # if we have a dot
                index = 2 * index # branch left
            elif morse_char == "-": # if we have a dash
                index = (2 * index) + 1 # branch right
            elif morse_char == " ": # theres a spacee in the morse character so output the found char and reset index to 1
                index -= 1 # decrement index
                #print("appending:",decoded_message,"+",binary_heap[index]) # debug
                decoded_message += binary_heap[index] # append to decoded message from binary heap with index
                index = 1 # reset index

            #print(morse_char,binary_heap[index-1]) # debug

        decoded_message += " " # if a / is detected then add a space into the decoded the message

    decoded_message = decoded_message.strip().lower() # strip any uncessary chars, and force message case to be lower

    return decoded_message # return the message

def decode_ham(msg): # invoked when we want to decode a ham radio morse code

    # decode the entire given message
    decoded_raw = decode_bt(msg)
    decoded_raw_splitted_data = decoded_raw.split("=") # perform string split for keyword '=' separate, recipients, message
    
    # get message
    recipients = decoded_raw_splitted_data[0].split("de") # perform another string split for recipients
    sender = recipients[1] # sender
    rec = recipients[0] # receiver
    content = decoded_raw_splitted_data[1] # message contents

    # debug
    #print(f"decoded_raw: {decoded_raw},\nsender: {sender},\nrec: {rec},\ncontent: {content}")

    return ( sender, rec, content ) # in the task specifies to return a turple

def encode_ham(send, rec, msg): # invoked when we want to encode a ham radio morse code message

    # construct the contents of our message in a decoded form
    #ham_to_encode = str(send) + "de" + str(rec) + "=" + str(msg) + "=("
    ham_to_encode = str(rec) + "de" + str(send) + "=" + str(msg) + "=("

    # shove it into the encode function imported from tree.py
    encoded_message = encode(ham_to_encode)

    return encoded_message # return the encoded message

#print("decoded message:",decode_bt('..- ...'))
#print("decoded message:",decode_bt('-.. --- --. . -.-. --- .. -. / - --- / - .... . / -- --- --- -.'))
#print("decoded message:",decode_bt(".-. .---- -.. . ... .---- -...- .... .. -...- -.--."))
#print("decoded message:",decode_bt("-.-. .... .- .-. .-.. . ... -.. . .--- .- -- . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--."))
#print(decode_ham("-.-. .... .- .-. .-.. . ... -.. . .--- .- -- . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--."))
#print(encode_ham("charles","james","urgency"))

#print(decode_ham("-.-. .... .- .-. .-.. . ... -.. . .--- .- -- . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--."))
# result = encode_ham( "charles", "james", "urgency" )
# print(result)
# print(decode_ham(result))
#print(decode_ham("-.-. .... .- .-. .-.. . ... -.. . .--- --- ... .... -...- -..- .-. .--. ..--. -...- -.--."))
