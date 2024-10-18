import random
from ecdsa import SigningKey, NIST256p
from Transaction import Transaction
from Block import Block
from Blockchain import Blockchain
from Node import Node


def SendBlock(blok, nodes):
	for node in nodes:
		res = node.AddBlock(blok)
		if isinstance(res, Block):
			print(f"Node {node.Addres} added block to its blockchain")
		else:
			print(
			    f"Node {node.Addres} has not block to its blockchain and return: {res}"
			)


target = 0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
reward = 5
version = "1.0"
nBlock = 4

privateKey = SigningKey.generate(curve=NIST256p)
transaction0 = Transaction("sender_address_0", {"recipient_address_0": 0}, 0,
                           privateKey)
transaction1 = Transaction("sender_address_1", {"recipient_address_1": 10}, 0.1,
                           privateKey)
transaction2 = Transaction("sender_address_2", {"recipient_address_2": 20}, 0.2,
                           privateKey)
transaction3 = Transaction("sender_address_3", {"recipient_address_3": 30}, 0.3,
                           privateKey)

blockchain = Blockchain()
blockchain.AddBlock(
    Block(version="1.0",
          prevHash="0" * 64,
          target=0x1d00ffff,
          transactions=[transaction0],
          privateKey=privateKey))

print("Blockchain with 1 genesis block created")
print(f"target: {target:#0x}")

nodes = [
    Node(blockchain, version, "miner_address0", reward, target),
    Node(blockchain, version, "miner_address1", reward, target),
    Node(blockchain, version, "miner_address2", reward, target),
    Node(blockchain, version, "miner_address3", reward, target),
]

print(f"{len(nodes)} nodes were created")

for i in range(nBlock):
	miner = random.choice(nodes)
	mining_result = miner.MineBlock()
	print()
	if isinstance(mining_result, Block):
		print(f"Block mined: {mining_result}")
		print(
		    f"Block {miner.BlockchainCount} mined by {miner.Addres}, nonce: {mining_result.Nonce:#0x}, hash: {mining_result.Hash}"
		)
		SendBlock(mining_result, nodes)
	else:
		print(f"New block failed mined by {miner.Addres}: {mining_result}")

print("Stop mining")
