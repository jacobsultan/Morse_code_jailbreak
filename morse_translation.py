import pandas as pd


eng_to_morse = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
'1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
'0':'-----',',':'--..--','.':'.-.-.-','?':'..--..','/':'-..-.','-':'-....-','(':'-.--.', ')':'-.--.-',
"'": '.----.','!': '---.',':': '---...', ';': '-.-.-.','=': '-...-', '+': '.-.-.','-': '-....-','_': '..--.-','"': '.-..-.',
'$': '...-..-','@': '.--.-.','^': '..-..-','%': '.--..-.',' ': '/','--··--':','
}

morse_to_eng = {value:key for key,value in eng_to_morse.items()}


# encryption to morsecode 
def encrypt(message):
    message = message.upper()
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += eng_to_morse[letter] + ' '
        else:
            cipher += ' / '
    return cipher.strip()


# decryption from morse code to english
def decrypt(message):
    # check if its a filled out entry
    if pd.notnull(message):
        message = message.lower()
        # some messages aren't responded in morse so first we check that 
        if not is_morse(message):
            return message
        message += ' '
        decipher = ''
        citext = ''
        for letter in message:
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2 :
                    decipher += ' '
                else:
                    if str(citext) in morse_to_eng:
                        decipher += morse_to_eng[str(citext)]
                    else:
                        decipher += '??'
                    citext = ''
        return decipher.lower()
    else:
        return None

# to see if a response is actually morse as it should be
def is_morse(message):
    if pd.notnull(message):
        for let in message:
            if let.isalpha():
                return False
        return True
    else:
        return None