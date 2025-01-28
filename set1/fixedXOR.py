def fixed_xor(hex1: str, hex2: str) -> str:
    """Takes two equal-length hex strings and returns their XOR combination as a hex string."""
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)

    # XOR each byte pair and convert back to hex
    xored_bytes = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))

    return xored_bytes.hex()

# Test the function
hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"
expected_output = "746865206b696420646f6e277420706c6179"

# Run and verify
output = fixed_xor(hex1, hex2)
print(output)  # Should print: 746865206b696420646f6e277420706c6179
assert output == expected_output, "XOR function did not produce the expected output!"
