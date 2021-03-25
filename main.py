import morse

def test_decode(): # perform 5 decodes
    print("test decodes")
    assert morse.decode_bt('..- ...') == 'us', "Should be us"
    assert morse.decode_bt('--.- .-- . .-. - -.-- ..- .. --- .--. .- ... -.. ..-. --. .... .--- -.- .-.. --.. -..- -.-. ...- -... -. -- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----') == 'qwertyuiopasdfghjklzxcvbnm1234567890', "Should be qwertyuiopasdfghjklzxcvbnm1234567890"
    assert morse.decode_bt('-.. --- --. . -.-. --- .. -. / - --- / - .... . / -- --- --- -.') == 'dogecoin to the moon', "Should be dogecoin to the moon"
    assert morse.decode_bt('-...-') == '=', "Should be ="
    assert morse.decode_bt('--.-') == 'q', "Should be q"
    print("decodes passed")

# begin tests if this module is the entry point of code
if __name__ == "__main__":
    print("test start")
    test_decode()
    print("test end")
