# Solana Private Key Converter

A collection of Python scripts for converting Solana private keys between base58 and JSON array formats.

## Prerequisites

- **Python 3.11+** - Required for this project
- **[uv](https://docs.astral.sh/uv/)** - package manager

## Install Dependencies
```bash
uv sync
```

## Using the Scripts

### 1. `from_priv_key.py`

Converts a base58-encoded private key to JSON array format (suitable for Solana config files).

**Usage:**
```bash
uv run from_priv_key.py <base58_private_key>
```

**Example:**
```bash
uv run from_priv_key.py 3DaByPpJMzAWCeVL7n1cDsuny8ZFowmXbW1ugASEgsF2hu2RuDkpYhLbybPnDeZtsgvYcGFuJTVBASj61s6n9kZJ
```

**Output:**
```json
[110,224,52,248,160,167,198,244,205,71,27,225,25,254,141,81,187,212,204,246,97,103,143,72,24,29,76,63,116,59,32,148,82,110,133,228,186,177,237,31,20,116,167,216,147,117,139,199,60,144,30,212,35,79,66,240,177,191,191,104,50,69,179,13]
```

**Common use case:**
Save the output to a Solana configuration file:
```bash
python from_priv_key.py YOUR_BASE58_KEY > ~/.config/solana/id.json
```

### 2. `to_priv_key.py`

Converts a JSON keypair file to base58 format, displaying both public and private keys.

**Usage:**
```bash
python to_priv_key.py <path_to_json_file>
```

**Example:**
```bash
python to_priv_key.py ~/.config/solana/id.json
```

**Input file format (`keypair.json`):**
```json
[110,224,52,248,160,167,198,244,205,71,27,225,25,254,141,81,187,212,204,246,97,103,143,72,24,29,76,63,116,59,32,148,82,110,133,228,186,177,237,31,20,116,167,216,147,117,139,199,60,144,30,212,35,79,66,240,177,191,191,104,50,69,179,13]
```

**Output:**
```
Public key (base58): 6YnBLveruEC8DGEydVCiZB8o5Y91gc6xNpRR6yDNvvuz
Private key (base58): 3DaByPpJMzAWCeVL7n1cDsuny8ZFowmXbW1ugASEgsF2hu2RuDkpYhLbybPnDeZtsgvYcGFuJTVBASj61s6n9kZJ
```

## Security Note

⚠️ **Important**: Private keys are sensitive information. Never share them or commit them to version control. Always keep your private keys secure and use appropriate file permissions when storing keypair files.
