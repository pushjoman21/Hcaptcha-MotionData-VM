import base64
import urllib.parse

class Utils:

    def __init__(self):
        pass

    @staticmethod
    def js_bool(value):
        return bool(value)
    
    def string_decode(self,string_table, start_index, length, shift):
        sliced = string_table[start_index:start_index + length]
        decoded_base64 = base64.b64decode(sliced)
        decoded_str = urllib.parse.unquote(decoded_base64.decode("utf-8"))
        return ''.join(chr((256 + ord(c) + shift) % 256) for c in decoded_str)