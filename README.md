# BTCOP_l3

_Created for the course "Blockchain technologies and cryptocurrency operating platforms" V. N. Karazin Kharkiv National University_

Python 3.10.6 "Primitive blockchain network" using the ecda library.

---

This program implements the basic network components of the blockchain system, including classes for transactions, blocks, and the blockchain itself, the node of the network. The main purpose of the program is to demonstrate the structure and interaction of these elements, as well as their functionality. The TestBlockchainNetwork.py file provides a simple simulation of a blockchain network.

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
- `VerifyBlock()`: checks the validity of the block.

## 3. Blockchain class

_The Blockchain class implements the block chain, providing block management and verification._ The main attributes and methods include:

**Attributes**:

- `blocks`: a list of blocks in the chain.

**Methods**:

- `Count`: count of blocks in Blockchain.
- `__init__()`: constructor that initializes an empty list of blocks.
- `AddBlock()`: adds a new block to the chain and checks its validity.
- `GetLastBlock()`: returns the last block in the chain.
- `GetBlock()`: returns the block at the specified index.
- `__str__()`: formats the string representation of the block chain.

## 3. Node class

_The Node class represents a node in a blockchain network. A node performs several important functions such as storing a copy of the blockchain, participating in the mining of new blocks, and managing transactions._ The main attributes and methods include:

**The main properties of the class**:

- `blockchain`: a copy of the blockchain that the node works with. It is created when the node is initialized.
- `version`: the version of the blockchain used by the node.
- `target`: the target value of block mining difficulty (usually the difficulty to create a new block). The lower the value, the higher the mining difficulty.
- `addres`: address of the node (or miner) where the reward for mining will be received.
- `reward`: the reward for the mined block, which is sent to the miner's address.
- `transactions `: list of transactions that the node collects and can include in a new block.
- `privateKey`: the node's private key, which is used to sign transactions and blocks.

**Main methods of the class**:

- `AddTransaction(transactions)`: Adds a list of transactions to the node. Checks each transaction for a valid signature. Returns a list of rejected transactions that did not pass validation.
- `ClearTransaction()`: Clears the node's list of transactions.
- `UpdateTarget(target)`: Updates the target difficulty value for block mining.
- `UpdateAddres(addres)`: Updates the node's address for rewards.
- `UpdateReward(reward)`: Updates the reward amount for mining a new block.
- `UpdateVersion(version)`: Updates the version of the blockchain.
- `AddBlock(block)`: Adds a new block to the blockchain if its previous hash matches the hash of the last block in the blockchain. Checks if the block is correct and adds it to the blockchain. If the block is incorrect, throws a ValueError exception .
- `MineBlock()`: The main method for mining (mining) a new block. Creates a new block with the current transactions, and adds a transaction with a reward for the miner. Tries to find a hash of the block that is less than the target difficulty value (target) by modifying the nonce field . If the block is successfully generated, signs it with the node's private key, clears the transaction list, and adds the block to the blockchain.

# Conclusion

The program demonstrates the principles of working with blockchain technology through the implementation of the main classes that perform the functions necessary to manage transactions, blocks and their verification.

# Examples and tests

_Each class file contains a test function `testClassName()`_

```python
[Running] python -u "TestBlockchainNetwork.py"
Blockchain with 1 genesis block created
target: 0x1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
4 nodes were created

Block mined: Block
Version: 1.0, PreviousBlockHash: 81f187461331f1db53e047ec18cbe9d6fa640cd7f4ebb2e82be0ffc432e4aa8e, Timestamp: 2024-10-18 14:41:22.127922, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 4961688, MerkleRoot: 9e0e891da564a00ca5a2ed324afe7d0e3097693891fb4df50703a466ff01d344, Hash: 0000007576f9df16059e22a3dcd234844afa6388d93141b094708d6c6bf3a46e, Signature: {"publicKey": "ljWViucCvf+o5FRKY+Jt/XaoRLLMcaqQh2+PE7OJfH8mLxdUBQKNtTlF9/98LUGv4s/flBNMFmVWesME/7TCNQ==", "signature": "QMvOBB26pBTMeiPt0oP2MOJH4OR6CyZTSiPvHuSO4gUzEgTiNBY3HRF3IyuABeTwya1vj/MdKUU7/PDlME5X8g==", "message": "Block\nVersion: 1.0, PreviousBlockHash: 81f187461331f1db53e047ec18cbe9d6fa640cd7f4ebb2e82be0ffc432e4aa8e, Timestamp: 2024-10-18 14:41:22.127922, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 4961688, MerkleRoot: 9e0e891da564a00ca5a2ed324afe7d0e3097693891fb4df50703a466ff01d344, Hash: 0000007576f9df16059e22a3dcd234844afa6388d93141b094708d6c6bf3a46e", "algorithm": "SHA256withECDSA"}
Block 2 mined by miner_address1, nonce: 0x4bb598, hash: 0000007576f9df16059e22a3dcd234844afa6388d93141b094708d6c6bf3a46e
Node miner_address0 added block to its blockchain
Node miner_address1 has not block to its blockchain and return: True
Node miner_address2 added block to its blockchain
Node miner_address3 added block to its blockchain

Block mined: Block
Version: 1.0, PreviousBlockHash: 0000007576f9df16059e22a3dcd234844afa6388d93141b094708d6c6bf3a46e, Timestamp: 2024-10-18 14:41:41.341175, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 4203522, MerkleRoot: d232304581b373f28b4b12d32ef71d04fc8f2fc9c68fb266bee45e13f2bff411, Hash: 0000000b0463f9c67f29769c47a475042a76253c35deb21a0b9e55607a01bdb1, Signature: {"publicKey": "H/hy4ZSIqBjmVl6nQDFbQ0h6UQvMPpDzjrOmQQYasVQwZFR/D4ktD/orySx/dJ0ISsIuifxZhPrKBJtcmHHumw==", "signature": "ykin94Vp6UbW4nUE44iyUw1VUO+tDTOJ6MiTnaOkJcmfSpUQbUiLGrwAKcJeikVgKq+n3Tm7OQn9Y7AktD6oXg==", "message": "Block\nVersion: 1.0, PreviousBlockHash: 0000007576f9df16059e22a3dcd234844afa6388d93141b094708d6c6bf3a46e, Timestamp: 2024-10-18 14:41:41.341175, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 4203522, MerkleRoot: d232304581b373f28b4b12d32ef71d04fc8f2fc9c68fb266bee45e13f2bff411, Hash: 0000000b0463f9c67f29769c47a475042a76253c35deb21a0b9e55607a01bdb1", "algorithm": "SHA256withECDSA"}
Block 3 mined by miner_address0, nonce: 0x402402, hash: 0000000b0463f9c67f29769c47a475042a76253c35deb21a0b9e55607a01bdb1
Node miner_address0 has not block to its blockchain and return: True
Node miner_address1 added block to its blockchain
Node miner_address2 added block to its blockchain
Node miner_address3 added block to its blockchain

Block mined: Block
Version: 1.0, PreviousBlockHash: 0000000b0463f9c67f29769c47a475042a76253c35deb21a0b9e55607a01bdb1, Timestamp: 2024-10-18 14:42:49.977102, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 15276400, MerkleRoot: 5fec93ac843bbe7c147ea06f1d9140bb39f3af128ed7d5de7561ee12e41adce3, Hash: 000001edd8b258f3fd5aaedd505496518c60ee3bccabf2b8f62e504adbe87e63, Signature: {"publicKey": "X8o3OShw8prfRh+JN0IomT0bz/4SwqRAGdRs9a6A9jECvp6icftbyeJAuGfVplMECFWmhhOWnOYe1EXYADGATQ==", "signature": "mTMrhOVpL2ixmH705z80BxD72a8o2x50iwzrzL50mhQM8jSrV9di0Hb7JtAc0oYdsCQRuLuRz60Gfin+Kfb6pg==", "message": "Block\nVersion: 1.0, PreviousBlockHash: 0000000b0463f9c67f29769c47a475042a76253c35deb21a0b9e55607a01bdb1, Timestamp: 2024-10-18 14:42:49.977102, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 15276400, MerkleRoot: 5fec93ac843bbe7c147ea06f1d9140bb39f3af128ed7d5de7561ee12e41adce3, Hash: 000001edd8b258f3fd5aaedd505496518c60ee3bccabf2b8f62e504adbe87e63", "algorithm": "SHA256withECDSA"}
Block 4 mined by miner_address3, nonce: 0xe91970, hash: 000001edd8b258f3fd5aaedd505496518c60ee3bccabf2b8f62e504adbe87e63
Node miner_address0 added block to its blockchain
Node miner_address1 added block to its blockchain
Node miner_address2 added block to its blockchain
Node miner_address3 has not block to its blockchain and return: True

Block mined: Block
Version: 1.0, PreviousBlockHash: 000001edd8b258f3fd5aaedd505496518c60ee3bccabf2b8f62e504adbe87e63, Timestamp: 2024-10-18 14:42:55.509784, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 1188027, MerkleRoot: b51dda8a40a23350affcb631b2f353ca856dd195f8bf4fd07b73094d81617616, Hash: 0000003ffd4b12eb3cbd18de49c89cd4616a911c59e9aa47b7569a2361d24671, Signature: {"publicKey": "ljWViucCvf+o5FRKY+Jt/XaoRLLMcaqQh2+PE7OJfH8mLxdUBQKNtTlF9/98LUGv4s/flBNMFmVWesME/7TCNQ==", "signature": "4/pVxKQHma4+d+/wZYvYGgF6PvrcHeTymc2GD8XQw+JmwD2nESKeMSuRosKn3qQCMgcp9HxH5Z/R7cSE07zFDw==", "message": "Block\nVersion: 1.0, PreviousBlockHash: 000001edd8b258f3fd5aaedd505496518c60ee3bccabf2b8f62e504adbe87e63, Timestamp: 2024-10-18 14:42:55.509784, DificultyTarget: 13803492693581127574869511724554050904902217944340773110325048447598591, Nonce: 1188027, MerkleRoot: b51dda8a40a23350affcb631b2f353ca856dd195f8bf4fd07b73094d81617616, Hash: 0000003ffd4b12eb3cbd18de49c89cd4616a911c59e9aa47b7569a2361d24671", "algorithm": "SHA256withECDSA"}
Block 5 mined by miner_address1, nonce: 0x1220bb, hash: 0000003ffd4b12eb3cbd18de49c89cd4616a911c59e9aa47b7569a2361d24671
Node miner_address0 added block to its blockchain
Node miner_address1 has not block to its blockchain and return: True
Node miner_address2 added block to its blockchain
Node miner_address3 added block to its blockchain
Stop mining

[Done] exited with code=0 in 116.88 seconds
```
