import base58
import argparse
import json

# Set up command line argument parsing
parser = argparse.ArgumentParser(description='Convert Solana private key from JSON array to base58 format')
parser.add_argument('json_file', help='Path to JSON file containing the private key array')
args = parser.parse_args()

# Read the private key array from the JSON file
try:
    with open(args.json_file, 'r') as f:
        keypair_array = json.load(f)
except FileNotFoundError:
    print(f"Error: File '{args.json_file}' not found")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: Invalid JSON in file '{args.json_file}'")
    exit(1)

# Show the public key (last 32 bytes)
public_key_array = keypair_array[32:]
public_key_bytes = bytes(public_key_array)
public_key_base58 = base58.b58encode(public_key_bytes).decode()
print("Public key (base58):", public_key_base58)

# Extract the private key from the full keypair array
private_key_array = keypair_array
private_key_bytes = bytes(private_key_array)
private_key_base58 = base58.b58encode(private_key_bytes).decode()

print("Private key (base58):", private_key_base58)

