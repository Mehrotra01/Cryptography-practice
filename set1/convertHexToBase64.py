import base64
print("Convert Hex to Base64")
str =input("Enter the hex_string: ") #49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
bytes_data = bytes.fromhex(str)

# Encode bytes to base64
base64_data = base64.b64encode(bytes_data).decode('ascii')

print(base64_data) #SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t