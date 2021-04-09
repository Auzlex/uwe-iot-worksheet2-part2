"""
    Scripted by Charles Edwards
"""

# our binary heap
binary_heap = list("-ETIANMSURWDKGOHVF*L*PJBXCYZQ**54*3*¿?2&*+****16=/***(*7***8*90-")

def decode_bt(msg):

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
                print("appending:",decoded_message,"+",binary_heap[index]) # debug
                decoded_message += binary_heap[index] # append to decoded message from binary heap with index
                index = 1 # reset index

            print(morse_char,binary_heap[index-1]) # debug

        decoded_message += " " # if a / is detected then add a space into the decoded the message

    decoded_message = decoded_message.strip().lower() # strip any uncessary chars, and force message case to be lower

    return decoded_message # return the message

# print("decoded message:",decode_bt('..- ...'))
# print("decoded message:",decode_bt('-.. --- --. . -.-. --- .. -. / - --- / - .... . / -- --- --- -.'))
# print("decoded message:",decode_bt(".-. .---- -.. . ... .---- -...- .... .. -...- -.--."))
