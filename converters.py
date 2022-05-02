import base64
from email.mime import base

class Converters:
    def __init__(self):
        pass

    def ascii_of_str(self, str_to_ascii):
        code = ""
        for my_char in str_to_ascii:
            code += str(ord(my_char)) + " "
        return code


    def str_to_bytes(self, str_to_byte):
        return str_to_byte.encode("ascii")
    
    def decimal_to_byte_array(self, dec_string):
        return bytearray(dec_string)

    def hex_to_byte_array(self, hexString):
        return bytearray.fromhex(hexString)

    def bytes_to_base64(self, bytes_to_base64):
        return base64.b64encode(bytes_to_base64)

    def base64BytesToString(self, base64bytes):
        return base64bytes.decode("ascii")

    def xor_cipher(self, plain_text, key):
        if( len(plain_text) is not len(key)):
            raise ValueError("text and key lengths are not the same")
        else:
            cipher_text = []
            for (byte_text, byte_key) in zip(bytearray.fromhex(plain_text), bytearray.fromhex(key)):
                cipher_text.append(byte_text^byte_key)
        return bytearray(cipher_text)
            
    def pad_key(self, key, plain_text):
        if isinstance(key, (bytes, bytearray)):
            len_of_key = len(key.hex())
            len_of_plain_text = len(plain_text.hex())
            print(len_of_key)
            print(len_of_plain_text)
            if(len_of_key > len_of_plain_text):
                #add zero to the plain text
                len_difference = len_of_key - len_of_plain_text
                pad_number = len_difference
                print(pad_number)
                pad_str = "0"*pad_number
                print(pad_str)
                new_plain_text = pad_str + plain_text.hex()
                print(new_plain_text)
                print(key.hex())
                print()
                print()
                return [bytearray.fromhex(new_plain_text), bytearray(key)]
            elif(len_of_key < len_of_plain_text):
                len_difference = len_of_plain_text - len_of_key
                pad_number = len_difference
                print(pad_number)
                pad_str = "0"*pad_number
                print(pad_str)
                new_key = pad_str + key.hex()
                print(new_key)
                print(plain_text.hex())
                print()
                print()
                return [bytearray.fromhex(new_key), bytearray(plain_text)]
            elif(len_of_key == len_of_plain_text):
                len_difference = 0
                print(len_difference)
            else:
                pass
        else:
            raise ValueError("bad format")