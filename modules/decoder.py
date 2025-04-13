import base64
import binascii
from urllib.parse import unquote


def decode_string(encoded_str):
    """
    Decodes a string based on the type (Base64, Hex, URL, etc.)
    """

    # Check if the string is Base64 encoded
    try:
        decoded_base64 = base64.b64decode(encoded_str).decode('utf-8')
        print(f"Decoded Base64: {decoded_base64}")
        return
    except Exception as e:
        pass

    # Check if the string is Hex encoded
    try:
        decoded_hex = bytes.fromhex(encoded_str).decode('utf-8')
        print(f"Decoded Hex: {decoded_hex}")
        return
    except ValueError:
        pass

    # Check if the string is URL encoded
    try:
        decoded_url = unquote(encoded_str)
        print(f"Decoded URL: {decoded_url}")
        return
    except Exception as e:
        pass

    print("Unable to decode the string. Try different formats or check input.")
