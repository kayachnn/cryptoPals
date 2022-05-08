import base64
import re
from unittest import result
from converters import Converters
import string
import os
#exercise 1
#hex to base64

crypto_pal_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
converter = Converters()



######question 1
# bytearrayFromHex = converter.hex_to_byte_array(crypto_pal_string)
# print("byte array from hex")
# print(bytearrayFromHex)
# print()
# print("base64")
# bytes_base64 = converter.bytes_to_base64(bytearrayFromHex)
# string_bytes_base64 = converter.base64BytesToString(bytes_base64)
# print(string_bytes_base64)
# print(base64.b64encode(bytearrayFromHex).decode("ascii"))
###############


######question 2
""" key = "686974207468652062756c6c277320657965"
plain_text =         "1c0111001f010100061a024b53535009181c"
bytearray_plain_text = bytearray.fromhex(plain_text)

bytearray_key = bytearray.fromhex(key)



cipher_text = converter.xor_cipher(key, plain_text)
print(cipher_text.hex()) """

########question 2######
cipher_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
cipher_text_byte_array = bytearray.fromhex(cipher_text)
len_of_cipher_text = len(cipher_text) // 2
alphabet = list(string.ascii_letters)
for char_alp in alphabet:
    #print(char_alp)
    key = char_alp
    len_of_key = len(key.encode().hex()) // 2
    if(len_of_key > len_of_cipher_text):
        print("key is more than cipher text, pad cipher text")
    elif(len_of_key == len_of_cipher_text):
        print("no need padding")
    elif len_of_key < len_of_cipher_text:
        #print("pad key")
        #print("difference between key and cipher text")
        len_difference = len_of_cipher_text - len_of_key
        #print("padding key ")
        m_key = ""
        for i in range(len_difference*2):
            m_key += key.encode().hex()
        m_key += key.encode().hex()
        #print(m_key)
        #print(len(m_key) // 2 - len_of_cipher_text)
        #print()
        #print()
        result = bytes(a ^ b for(a, b) in zip(bytearray.fromhex(m_key), bytearray.fromhex(cipher_text)))
        #print(result.decode())

key = os.urandom(32)
iv = os.urandom(16)
plain_text_byte_array = "asdfasdaefqwefasxaaaadasfdfasdfasdfas".encode()
converter.cipher(iv, key, plain_text_byte_array)
#converter.pad_key(key, "asdfasdasdfasdfasdfsadfasda".encode(), 0)

######question 3#######