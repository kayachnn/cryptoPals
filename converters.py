import base64

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
            for (byte_text, byte_key) in zip(plain_text, key):
                cipher_text.append(byte_text^byte_key)
        return bytearray(cipher_text)
            

    def cipher(self, iv, key, plain_text):
        if ( isinstance(key, (bytes, bytearray)) and isinstance(iv, (bytes, bytearray)) \
            and isinstance(plain_text, (bytes, bytearray))):
            print("formats are true")
            self.check_iv_length(iv)
            self.check_key_length(key)
            print("key plain text before pad")
            print(key)
            print(plain_text)
            plain_text = self.pad_plain_text(plain_text)
            print("plain text after pad")
            print(plain_text)
            print("######beginnign cipher operation########")
            len_plain_text = len(plain_text)
            print(len_plain_text)
            process_count = len_plain_text // 16
            cipher_text_len = process_count + 3
            cipher_text = []
            cipher_text.append(iv.hex())
            print("process counter")
            print(process_count)
            print("len of key")
            print(len(key))
            key_start = len(key)-16
            key_end = key_start + 16
            key_least_significant = key[key_start: key_end]
            print()
            for i in range(process_count):
                #print(i)
                start = i * 16
                end = start + 16
                #print(start)
                #print(end)
                #print()
                #print("key xor")
                #print(key)
                ciphered_text = self.xor_cipher(plain_text[start:end], key_least_significant)
                #print(ciphered_text)
                cipher_text.append(ciphered_text.hex())
            cipher_text.append(key_least_significant.hex())
            print("cipher text")
            print(cipher_text)
        else:
            raise ValueError("bad formats")

        
    def calculate_tag(self, cipher_text):
        pass
    def pad_plain_text(self, plain_text):
        len_of_plain_text = len(plain_text)
        print("len of plain text: " + str(len_of_plain_text))
        #len of plain text should be sth time 16
        len_of_plain_text_mod_16 = len_of_plain_text % 16
        if(len_of_plain_text_mod_16 != 0):
            print("padding required")
            divider = len_of_plain_text // 16
            difference = ((divider + 1)*16) - len_of_plain_text
            print("difference")
            print(difference)
            padding_str = "0" * (difference*2)
            print(padding_str)
            new_plain_text = padding_str + plain_text.hex()
            new_plain_text_byte_array = bytearray.fromhex(new_plain_text)
            print(new_plain_text_byte_array)

            print(len(new_plain_text_byte_array))
            return new_plain_text_byte_array
        else:
            print("no padding required")
            return plain_text
        


    def check_key_length(self, key):
        len_key = len(key)
        if len_key not in (16, 20, 24, 28, 32):
            raise ValueError("key lenght not correct")

    def check_iv_length(self, iv):
        len_iv = len(iv)
        if len_iv != 16:
            raise ValueError("iv length not correct")