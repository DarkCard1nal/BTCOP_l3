from ecdsa import SigningKey, NIST256p
from Transaction import Transaction
from Block import Block
from Blockchain import Blockchain
import copy


class Node:

	def __init__(self, blockchain, version, addres, reward, target=0x1d00ffff):
		self.__blockchain = copy.deepcopy(blockchain)
		self.__version = version
		self.__target = target
		self.__addres = addres
		self.__reward = reward
		self.__transactions = []
		self.__privateKey = SigningKey.generate(curve=NIST256p)

	@property
	def Blockchain(self):
		return copy.deepcopy(self.__blockchain)

	@property
	def BlockchainHashLastBlock(self):
		return self.__blockchain.GetLastBlock().Hash

	@property
	def Version(self):
		return self.__version

	@property
	def Target(self):
		return self.__target

	@property
	def Addres(self):
		return self.__addres

	@property
	def Reward(self):
		return self.__reward

	@property
	def Transactions(self):
		return self.__transactions.copy()

	def AddTransaction(self, transactions):
		denied = []
		for transaction in transactions[:]:
			if not transaction.VerifySignature():
				denied.append(transaction)
				transactions.remove(transaction)

		self.__transactions.extend(transactions)
		return denied

	def ClearTransaction(self):
		self.__transactions.clear()

	def UpdateTarget(self, target):
		self.__target = target

	def UpdateAddres(self, addres):
		self.__addres = addres

	def UpdateReward(self, reward):
		self.__reward = reward

	def UpdateVersion(self, version):
		self.__version = version

	def AddBlock(self, block):
		try:
			self.__blockchain.AddBlock(block)
			return None
		except ValueError as e:
			return f"ValueError occurred: {e}"

	def MineBlock(self):
		nonceMax = 2**32
		nonce = 0
		block = Block(self.__version,
		              self.__blockchain.GetLastBlock().Hash, self.__target,
		              self.__transactions, 0, self.__privateKey)
		block.AddTransactions(
		    Transaction('',
		                {self.__addres: self.__reward + block.AllCommission}, 0,
		                self.__privateKey))
		while True:
			block.UpdateHash(nonce)

			if int(block.Hash, 16) < self.__target:
				break
			elif nonce > nonceMax:
				return False
			else:
				nonce += 1

		block.UpdateSignature(self.__privateKey)
		self.ClearTransaction()
		return self.AddBlock(block)


def testNode():
	privateKey = SigningKey.generate(curve=NIST256p)
	transaction0 = Transaction("sender_address_0", {"recipient_address_0": 0},
	                           0, privateKey)
	transaction1 = Transaction("sender_address_1", {"recipient_address_1": 10},
	                           0.1, privateKey)
	transaction2 = Transaction("sender_address_2", {"recipient_address_2": 20},
	                           0.2, privateKey)
	blockchain = Blockchain()
	blockchain.AddBlock(
	    Block(version="1.0",
	          prevHash="0" * 64,
	          target=0x1d00ffff,
	          transactions=[transaction0],
	          privateKey=privateKey))
	node = Node(
	    blockchain,
	    version=1,
	    addres="miner_address",
	    reward=50,
	    target=0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)

	deniedTransactions = node.AddTransaction([transaction1, transaction2])
	assert len(deniedTransactions) == 0, "Expected no denied transactions"
	assert len(node.Transactions) == 2, "Expected 2 transactions in Node"

	miningResult = node.MineBlock()
	assert miningResult is None, f"Expected no error while mining block, got: {miningResult}"

	lastBlock = node.Blockchain.GetLastBlock()
	assert lastBlock.Hash is not None, "Last Block Hash should not be None"
	assert node.Blockchain.Count == 2, "Expected block in Blockchain after mining"

	assert len(node.Transactions
	          ) == 0, "Expected transactions to be cleared after mining"

	print("All tests passed!")


if __name__ == "__main__":
	testNode()
