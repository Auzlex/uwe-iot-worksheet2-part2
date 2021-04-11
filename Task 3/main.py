"""
    Scripted by Charles Edwards
    Worksheet 2 Part 2 Task 3
"""
import asyncio              # required for asynchronous events when communicating with the server
import morse                # import morse

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

def test_send_echos(): # perform 5 send echos
    print("test_send_echos start")
    assert asyncio.run( morse.send_echo("s","test") ) == ('echo', 's', 'test'), "Should be ('echo', 's', 'test')"
    assert asyncio.run( morse.send_echo("james","helloworld") ) == ('echo', 'james', 'helloworld'), "Should be ('echo', 'james', 'hello world')"
    assert asyncio.run( morse.send_echo("charles","amazing") ) == ('echo', 'charles', 'amazing'), "Should be ('echo', 'charles', 'amazing')"
    assert asyncio.run( morse.send_echo("josh","buyxrp") ) == ('echo', 'josh', 'buyxrp'), "Should be ('echo', 'josh', 'buyxrp')"
    assert asyncio.run( morse.send_echo("allice","rooos") ) == ('echo', 'allice', 'rooos'), "Should be ('echo', 'allice', 'rooos')"
    print("test_send_echos PASSED") 

def test_send_time(): # perform a test for send time
    print("test_send_time start")

    import time # for checking date time
    # get time for gmt
    current_time = time.strftime("%H:%M:%S", time.gmtime())

    # get the result from the send_time
    result = asyncio.run( morse.send_time("s") )
    print(f"system time: {current_time},\nsend_time response: {result[2]}")

    # if for what ever REASON this returns false it seems the server time is different to your system time
    assert asyncio.run( morse.send_time("s") ) == ('time', 's', current_time), f"Should be('time', 's', {current_time})"
    print("test_send_time PASSED") 


# begin tests if this module is the entry point of code
if __name__ == "__main__":
    print("---------------- test start ----------------")
    test_ham_encodes()
    test_ham_decodes()
    test_send_echos()
    test_send_time()
    print("---------------- test end ----------------")
