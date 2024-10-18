from ecdsa import SigningKey, NIST256p
from Transaction import Transaction
from Block import Block


class Blockchain:

	def __init__(self):
		self.__blocks = []

	@property
	def Count(self):
		return len(self.__blocks)

	def AddBlock(self, block):
		if not isinstance(block, Block):
			raise ValueError("Only Block instances can be added.")

		if self.__blocks:
			last_block = self.__blocks[-1]
			if block.PrevHash != last_block.Hash:
				raise ValueError(
				    "Block's PrevHash does not match the last block's Hash.")

		if not block.VerifyBlock():
			raise ValueError("Block has not passed verification")

		self.__blocks.append(block)

	def GetLastBlock(self):
		return self.__blocks[-1] if self.__blocks else None

	def GetBlock(self, index):
		if index < 0 or index >= len(self.__blocks):
			raise IndexError("Block index out of range.")
		return self.__blocks[index]

	def __str__(self):
		return f"Blockchain with {len(self.__blocks)} blocks."


def testBlockchain():
	privateKey = SigningKey.generate(curve=NIST256p)

	tx1 = Transaction("SenderAddress1", {"ReceiverAddress1": 0.5}, 0.1,
	                  privateKey)
	tx2 = Transaction("SenderAddress2", {"ReceiverAddress2": 0.3}, 0.1,
	                  privateKey)
	tx3 = Transaction("SenderAddress3", {"ReceiverAddress3": 0.2}, 0.1,
	                  privateKey)

	block1 = Block(version="1.0",
	               prevHash="0" * 64,
	               target=0x1d00ffff,
	               transactions=[tx1, tx2],
	               privateKey=privateKey)
	block2 = Block(version="1.0",
	               prevHash=block1.Hash,
	               target=0x1d00ffff,
	               transactions=[tx3],
	               privateKey=privateKey)

	blockchain = Blockchain()

	blockchain.AddBlock(block1)
	blockchain.AddBlock(block2)

	print(blockchain)
	print("Last Block:", blockchain.GetLastBlock())

	for i in range(len(blockchain._Blockchain__blocks)):
		block = blockchain.GetBlock(i)
		assert block.VerifyHash(), f"Block {i} hash verification failed."
		assert block.VerifySignature(
		), f"Block {i} signature verification failed."

		for tx in block.Transactions:
			assert tx.VerifyHash(
			), f"Transaction in Block {i} hash verification failed."
			assert tx.VerifySignature(
			), f"Transaction in Block {i} signature verification failed."

	print("All blockchain tests passed!")


if __name__ == "__main__":
	testBlockchain()
