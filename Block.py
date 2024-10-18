import hashlib
import json
import secrets
from ecdsa import SigningKey, VerifyingKey, NIST256p, BadSignatureError
from datetime import datetime
from Signature import Signature
from Transaction import Transaction


class Block:

	def __init__(self,
	             version,
	             prevHash,
	             target,
	             transactions=[],
	             privateKey=None):
		self.__version = version
		self.__prevHash = prevHash
		self.__timestamp = datetime.now()
		self.__target = target
		self._nonce = secrets.randbits(32)
		self.__transactions = transactions
		self.__merkleRoot = self.UpdateMerkleRoot()
		self.__hash = self.UpdateHash()
		self.__signature = self.UpdateSignature(privateKey)

	@property
	def Version(self):
		return self.__version

	@property
	def PrevHash(self):
		return self.__prevHash

	@property
	def Timestamp(self):
		return self.__timestamp

	@property
	def Target(self):
		return self.__target

	@property
	def Nonce(self):
		return self._nonce

	@property
	def MerkleRoot(self):
		return self.__merkleRoot

	@property
	def Transactions(self):
		return self.__transactions.copy()

	@property
	def Hash(self):
		return self.__hash

	@property
	def Signature(self):
		return self.__signature

	def AddTransactions(self, transactions):
		self.__transactions.append(transactions)
		self.UpdateMerkleRoot()

	def UpdateMerkleRoot(self):
		if not self.__transactions:
			self.__merkleRoot = None
			self.UpdateHash()
			return self.__merkleRoot

		transactionHashes = [tx.TxHash for tx in self.__transactions]

		# Генерируем дерево Меркла
		while len(transactionHashes) > 1:
			if len(transactionHashes) % 2 != 0:
				transactionHashes.append(transactionHashes[-1])

			# Параллельно хешируем пары хешей
			transactionHashes = [
			    self.HashPair(transactionHashes[i], transactionHashes[i + 1])
			    for i in range(0, len(transactionHashes), 2)
			]

		self.__merkleRoot = transactionHashes[0]
		self.UpdateHash()
		return self.__merkleRoot

	@staticmethod
	def HashPair(left, right):
		return hashlib.sha256((left + right).encode('utf-8')).hexdigest()

	def CalculateHash(self):
		txData = self.StrNoSignatureAndHash()
		return hashlib.sha256(txData.encode()).hexdigest()

	def UpdateHash(self):
		self.__timestamp = datetime.now()
		self.__hash = self.CalculateHash()
		return self.__hash

	def VerifyHash(self):
		currentHash = self.CalculateHash()
		return self.__hash == currentHash

	def UpdateSignature(self, privateKey):
		"""
		- private_key: SigningKey
		"""
		if privateKey is None:
			return None

		self.__signature = Signature.Sign(self.StrNoSignature(), privateKey)
		return self.__signature

	def VerifySignature(self):
		obj = json.loads(self.__signature)
		publicKeyBase64 = obj['publicKey']
		signatureBase64 = obj['signature']
		message = obj['message']

		return Signature.Verify(signatureBase64, message, publicKeyBase64)

	def __str__(self):
		return (f"{self.StrNoSignature()}, Signature: {self.__signature}")

	def StrNoSignature(self):
		return (f"{self.StrNoSignatureAndHash()}, Hash: {self.__hash}")

	def StrNoSignatureAndHash(self):
		return (
		    f"Block\nVersion: {self.__version}, PreviousBlockHash: {self.__prevHash}, "
		    f"Timestamp: {self.__timestamp}, DificultyTarget: {self.__target}, "
		    f"Nonce: {self._nonce}, MerkleRoot: {self.__merkleRoot}")


def testBlock():
	privateKey = SigningKey.generate(curve=NIST256p)

	tx1 = Transaction("SenderAddress1", {"ReceiverAddress1": 0.5}, privateKey)
	tx2 = Transaction("SenderAddress2", {"ReceiverAddress2": 0.3}, privateKey)

	block = Block(version="1.0",
	              prevHash="0" * 64,
	              target=0x1d00ffff,
	              transactions=[tx1, tx2],
	              privateKey=privateKey)

	print("Block after creation:")
	print(block)

	assert block.Version == "1.0", "Version mismatch"
	assert block.PrevHash == "0" * 64, "PrevHash mismatch"
	assert len(block.Transactions) == 2, "Transaction count mismatch"
	assert block.MerkleRoot is not None, "Merkle root should not be None"
	assert block.Signature is not None, "Signature should not be None"

	assert block.VerifyHash(), "Block hash verification failed"
	assert block.VerifySignature(), "Block signature verification failed"

	tx3 = Transaction("SenderAddress3", {"ReceiverAddress3": 0.2}, privateKey)
	block.AddTransactions(tx3)

	print("\nBlock after adding a new transaction:")
	print(block)

	assert len(
	    block.Transactions) == 3, "Transaction count mismatch after addition"
	assert block.MerkleRoot is not None, "Merkle root should not be None after addition"
	assert block.VerifyHash(), "Block hash verification failed after addition"
	assert block.VerifySignature(
	), "Block signature verification failed after addition"

	print("\nAll tests passed!")


if __name__ == "__main__":
	testBlock()
