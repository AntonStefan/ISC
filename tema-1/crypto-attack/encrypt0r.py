#!/usr/bin/env python3

import base64
import json
import gmpy2
from encodings import utf_8


def str_to_number(text):
    """ Encodes a text to a long number representation (big endian). """
    return int.from_bytes(text.encode("latin1"), 'big')


def number_to_str(num):
    """ Decodes a text to a long number representation (big endian). """
    num = int(num)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode('latin1')


def encrypt(pub_k, msg_num):
    """ We only managed to steal this function... """
    cipher_num = gmpy2.powmod(msg_num, pub_k["e"], pub_k["n"])
    # note: gmpy's to_binary uses a custom format (little endian + special GMPY header)!
    cipher_b64 = base64.b64encode(gmpy2.to_binary(cipher_num))
    return cipher_b64


def decrypt(priv_k, cipher):
    """ We don't have the privary key, anyway :( """
    # you'll never get it!
    pass


if __name__ == "__main__":

    message = "eyJuIjogMTExMzcyMDE1OTQxNjUwNjg0MzY2OTI0MTczODIxNzc5NjQwNTA1NDkwMDA4MTg4NDQxODAwNTkwOTM1NjYwMjE5MzgwNzk0OTgwNjAyNjk1Njc1NzM2NDExODgxMTMwMDMzMzU4MTQxMTAzNzc3OTExNDczMzQyOTYyMzAzOTc4NDQ0MTQ0MzQ5MDYxMTI1NDA4Mjg0OTIzMzcyMTY3MzAxODA3NzczOTU3NDY1OTE3Njk4OTQzNTE0NTUxMTE3NTUwMDQyNDYxMTA0ODU4MzM2MDg4MzMxOTQxMDIzMDIyMjU3NzAxNzIzNTE0ODA2NzA4MTE3NjQxMzAwOTgyODY0NzA4ODQyNzk1NTY0NjcxNjMyNzIzMzg1NjkyODI2NTEzMTYzNDU2MDM1ODMzODMxODAxMjkxMzc0MzE3NTIwNTc4OTk1MDE2ODE0NzEwMTU5Mjk4NzA4OTQ3NTI3Mzg0NDUzMzE3NTE1NzYwMDA0Nzk1MDE3MTI1ODYzODAwMTMwNjQyNzAxNTE1NzczNjMyNjIxOTg2OTQxMTA5MjMwMTgxNjc0OTgxMTM5NzkwOTM5OTYyMzQ5MDI3MTc5ODcyOTM4NDQ1MjE2MTc4ODMzNDA3NjgzOTEzOTUzNDQyOTA4NTU1NDI2ODcyNDIxNDk4ODI1MjA2NTQ2ODkzMTMyNjIwNDEzNDQ0MDQwODc4MDM4MDc5NjE0MTkyNzQ0NjEzMDM5NTkwMjkwNzM1NDE2NzE1NDY2OTgzMzkzODc2OTA4MDc4MTExOTk0OTU1MzEyNDYzNjE4NTMxNjQ5MTA3NzU1MTI5MzEsICJlIjogNDQwNTY5LCAiZmxhZyI6ICJBUUg2ako4czk5SjBVbEhDK0FFaHV5YUxDd3ZOSmZidlZHNmtDT0t6NzBIY25UR0tjbCtqWkNZWTQzSmZ3YTJ1bzRJRHlCcDJLMFpFU1RtcUVNSDYxZ3FMWngwYzQzMlNIS1NQTGEzeUIzQmZ6cm1EeDEwZVIwV1ppOUJkUzh1d3diZFVZTVNKZGtrOTRkZkJyNkNVcW9GaS9UTXMxZGk1K09ZOWV1MEc0NXpJRVYrZ05vOTltcVFKZHVmTTAzU1RlQ0tzZ3RJMVIxV3RjOHVKOVlXL3Z2em5tWnBwdWRTMHZtRzFaWE4yRG9zSXRuWTRoK3B0Rmk4UWREcVowMEdwbE9xeWx5SFc2U3h0RWZvZ1gvMGlkVWZVbFFGVVRSK05HMW1STmlsZk5pbGlPY1ZseWd0Wi85MDgzbnM2TGVuTytCYXY0c0pkWFhxRmxoTEFZemRjV2t3bSJ9"    
    print(base64.b64decode(message))
    
    this = json.loads(base64.b64decode(message))

    # random number, I choosed 5
    r = 5
    cipher_dash = (gmpy2.from_binary(base64.b64decode(this['flag'])) * (gmpy2.powmod( r,this['e'], this['n']))) % this['n']
    
    message_json = {
        "n": 11137201594165068436692417382177964050549000818844180059093566021938079498060269567573641188113003335814110377791147334296230397844414434906112540828492337216730180777395746591769894351455111755004246110485833608833194102302225770172351480670811764130098286470884279556467163272338569282651316345603583383180129137431752057899501681471015929870894752738445331751576000479501712586380013064270151577363262198694110923018167498113979093996234902717987293844521617883340768391395344290855542687242149882520654689313262041344404087803807961419274461303959029073541671546698339387690807811199495531246361853164910775512931,
        "e": 440569,
        "flag": base64.b64encode(gmpy2.to_binary(cipher_dash)).decode('utf-8')
        }

    print()
    print(message_json)
    
    send_to_server = base64.b64encode(json.dumps(message_json).encode())
    
    print()
    print("Server_send")
    print(send_to_server)
    print()

    decode_from_sv = b"\x01\xa11\xfb\x0fA\t`\x1d\xe7\x05hF\x15\x19\t\x1a\x13\xfa~\x19\x13}\x19t-\x1d\x9b\xf0[6\x13\xfbs`\x0e\xfa\x8c\x19\x83's\xc2\xf7q"

    decode_dec = decode_from_sv.decode("unicode_escape")
    final = str_to_number(decode_dec)
    response = final // r
    response_to_str = number_to_str(response)
    print(response_to_str)
    