# BTCOP_l2

_Created for the course "Blockchain technologies and cryptocurrency operating platforms" V. N. Karazin Kharkiv National University_

Python 3.10.6 "Primitive blockchain system" using the ecda library.

---

This program implements the main components of a blockchain system, including classes for transactions, blocks, and the blockchain itself. The main purpose of the program is to demonstrate the structure and interaction of these elements, as well as their functionality.

## 1. Transaction class

_The Transaction class represents a transaction in a blockchain system._ The main attributes and methods include:

**Attributes**:

- `input`: sender's address.
- `outputs`: a dictionary containing recipient addresses and corresponding transfer amounts.
- `amount`: the amount of the transfer.
- `txTimestamp`: the time when the transaction was created.
- `txHash`: the hash of the transaction.
- `signature`: the digital signature of the transaction.

**Methods**:

- `__init__()`: constructor that initializes the fields and computes the hash and signature.
- `AddOutput()`: adds output to the transaction.
- `CalculateHash()`: calculates the hash based on the transaction data.
- `UpdateSignature()`: updates the signature based on the private key.
- `VerifySignature()`: verifies the validity of the signature.
- `GetTotalAmount()`: calculates the total amount of outputs.

## 2. Block class

_The Block class represents a block in the blockchain system that contains transactions and metadata about the block._ The main attributes and methods include:

**Attributes**:

- `version`: protocol version.
- `prevHash`: the hash of the previous block.
- `timestamp`: the time the block was created.
- `target`: difficulty of mining.
- `nonce`: a random value for mining.
- `MerkleRoot`: the root of the Merkle tree for transactions.
- `transactions`: a list of transactions.
- `signature`: digital signature of the block.

**Methods**:

- `__init__()`: constructor that initializes the fields and calculates the block hash.
- `AddTransactions()`: adds new transactions to the block.
- `UpdateMerkleRoot()`: updates the root of the Merkle tree.
- `CalculateHash()`: calculates the hash of the block header.
- `VerifyHash()`: checks the validity of the block hash.

## 3. Blockchain class

_The Blockchain class implements the block chain, providing block management and verification._ The main attributes and methods include:

**Attributes**:

- `blocks`: a list of blocks in the chain.

**Methods**:

- `__init__()`: constructor that initializes an empty list of blocks.
- `AddBlock()`: adds a new block to the chain and checks its validity.
- `GetLastBlock()`: returns the last block in the chain.
- `GetBlock()`: returns the block at the specified index.
- `__str__()`: formats the string representation of the block chain.

# Conclusion

The program demonstrates the principles of working with blockchain technology through the implementation of the main classes that perform the functions necessary to manage transactions, blocks and their verification.

# Examples and tests

_Each class file contains a test function `testBlockchain()`_

```python
[Running] python -u "Blockchain.py"
Blockchain with 2 blocks.
Last Block: Block
Version: 1.0,
PreviousBlockHash: 34bcbe2a317dc7a4b317c2401c47ffaea53036aeb9a2ce3889b2af9268299541,
Timestamp: 2024-10-11 23:52:08.321724,
DificultyTarget: 486604799,
Nonce: 1508784432,
MerkleRoot: 43e4fc6bd2df5b7a77fbfa317d0fe802788bd7cf651277dfcc4e92512a5e4c13,
Hash: 658905e8064a1e8eee9317088d5eea3f62a65b2e81245670047ca8c4182e1f7e,
Signature: {
"publicKey": "0+dMy5mzdylLczGAhHp/JQEsmZwP/uNk97WvDKcoMvsDJcxNWK4ESq0FU0BFGU8cbgeTPsjEEBPC1kOh6OQotg==",
"signature": "H3oyxhRUVCH3n7YLCJ18znFzXvV5WB8ioVE7+MQMLKfC/mVFQ/WhtQegq3OTunj9DTbQM8UeBgJNN9KJjIKhEQ==",
"message": "Block\nVersion: 1.0,
PreviousBlockHash: 34bcbe2a317dc7a4b317c2401c47ffaea53036aeb9a2ce3889b2af9268299541,
Timestamp: 2024-10-11 23:52:08.321724,
DificultyTarget: 486604799,
Nonce: 1508784432,
MerkleRoot: 43e4fc6bd2df5b7a77fbfa317d0fe802788bd7cf651277dfcc4e92512a5e4c13,
Hash: 658905e8064a1e8eee9317088d5eea3f62a65b2e81245670047ca8c4182e1f7e",
"algorithm": "SHA256withECDSA"
}
All blockchain tests passed!

[Done] exited with code=0 in 0.167 seconds
```
