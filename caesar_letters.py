import pandas as pd

def caesar_right(val,message):
    message = message.lower()
    encrypted = ""
    for let in message:
        if let.isalpha():
            encrypted += chr(ord("a") + (ord(let) -ord("a") + val) % 26)
        else:
            encrypted += let
    return encrypted

def caesar_reverse(val,message):
    if pd.notnull(message):
        message = message.lower()
        decrypted = ""
        for let in message:
            if let.isalpha():
                decrypted += chr(ord("a") + (ord(let) - ord("a") - val) % 26)
            else:
                decrypted += let
        return decrypted
    else:
        return None

      