"""
    Scripted by Charles Edwards
    Worksheet 2 Part 2 Task 2
"""
import morse

def test_ham_encodes(): # perform 5 ham encodes
    print("test HAM encodes start")
    assert morse.encode_ham( "charles","james","urgency" ) == '.--- .- -- . ... -.. . -.-. .... .- .-. .-.. . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--.', "Should be .--- .- -- . ... -.. . -.-. .... .- .-. .-.. . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--."
    assert morse.encode_ham( "charles", "josh", "xrp?" ) == '.--- --- ... .... -.. . -.-. .... .- .-. .-.. . ... -...- -..- .-. .--. ..--. -...- -.--.', "Should be .--- --- ... .... -.. . -.-. .... .- .-. .-.. . ... -...- -..- .-. .--. ..--. -...- -.--."
    assert morse.encode_ham( "jake", "rias", "boosted gear!" ) == '.-. .. .- ... -.. . .--- .- -.- . -...- -... --- --- ... - . -.. / --. . .- .-. -.-.-- -...- -.--.', 'Should be .-. .. .- ... -.. . .--- .- -.- . -...- -... --- --- ... - . -.. / --. . .- .-. -.-.-- -...- -.--.'
    assert morse.encode_ham( "omega", "zulu", "bombs" ) == '--.. ..- .-.. ..- -.. . --- -- . --. .- -...- -... --- -- -... ... -...- -.--.', 'Should be --.. ..- .-.. ..- -.. . --- -- . --. .- -...- -... --- -- -... ... -...- -.--.'
    assert morse.encode_ham( "utar8", "115", "zombies!" ) == '.---- .---- ..... -.. . ..- - .- .-. ---.. -...- --.. --- -- -... .. . ... -.-.-- -...- -.--.', 'Should be, .---- .---- ..... -.. . ..- - .- .-. ---.. -...- --.. --- -- -... .. . ... -.-.-- -...- -.--.'
    print("test HAM encodes PASSED")

def test_ham_decodes(): # perform 5 ham decodes
    print("test HAM decodes start")
    assert morse.decode_ham( '.--- .- -- . ... -.. . -.-. .... .- .-. .-.. . ... -...- ..- .-. --. . -. -.-. -.-- -...- -.--.' ) == ('charles', 'james', 'urgency'), "Should be ('charles', 'james', 'urgency')"
    assert morse.decode_ham( '.--- --- ... .... -.. . -.-. .... .- .-. .-.. . ... -...- -..- .-. .--. ..--. -...- -.--.' ) == ( 'charles', 'josh', 'xrp?' ), "Should be ( 'charles', 'josh', 'xrp?' )"
    assert morse.decode_ham( '.-. .. .- ... -.. . .--- .- -.- . -...- -... --- --- ... - . -.. / --. . .- .-. -.-.-- -...- -.--.' ) == ( 'jake', 'rias', 'boosted gear!' ), "Should be ( 'jake', 'rias', 'boosted gear!' )"
    assert morse.decode_ham( '--.. ..- .-.. ..- -.. . --- -- . --. .- -...- -... --- -- -... ... -...- -.--.' ) == ( 'omega', 'zulu', 'bombs' ), "Should be ( 'omega', 'zulu', 'bombs' )"
    assert morse.decode_ham( '.---- .---- ..... -.. . ..- - .- .-. ---.. -...- --.. --- -- -... .. . ... -.-.-- -...- -.--.' ) == ( 'utar8', '115', 'zombies!' ), "Should be, ( 'utar8', '115', 'zombies!' )"
    print("test HAM decodes PASSED")


# begin tests if this module is the entry point of code
if __name__ == "__main__":
    print("---------------- test start ----------------")
    test_ham_encodes()
    test_ham_decodes()
    print("---------------- test end ----------------")
