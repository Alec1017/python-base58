import base58

# Decode the private key from base58
byte_array = base58.b58decode("SOLANA_PRIVATE_KEY_HERE")
json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"

# paste this into the contents of a ~/.config/solana/key.json file
print(json_string)
