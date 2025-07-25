import base58
import argparse

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Convert Solana private key from base58 to JSON format')
parser.add_argument('private_key', help='The base58 encoded private key')
args = parser.parse_args()

# Decode the private key from base58
byte_array = base58.b58decode(args.private_key)
json_string = "[" + ",".join(map(lambda b: str(b), byte_array)) + "]"

# paste this into the contents of a ~/.config/solana/key.json file
print(json_string)
