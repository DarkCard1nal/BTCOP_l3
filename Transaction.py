import hashlib
import json
from ecdsa import SigningKey, VerifyingKey, NIST256p, BadSignatureError
from datetime import datetime
from Signature import Signature


class Transaction:

	def __init__(self, input_address, outputs={}, privateKey=None):
		self.__input = input_address
		self.__outputs = outputs.copy()
		self.__txTimestamp = datetime.now()
		self.__txHash = self.CalculateHash()
		self.__signature = self.UpdateSignature(privateKey)

	@property
	def Input(self):
		return self.__input

	@property
	def Outputs(self):
		return self.__outputs.copy()

	@property
	def Signature(self):
		return self.__signature

	@property
	def TxHash(self):
		return self.__txHash

	@property
	def TxTimestamp(self):
		return self.__txTimestamp

	def AddOutput(self, address, amount):
		self.AddOutputs({address: amount})

	def AddOutputs(self, outputs):
		self.__outputs.update(outputs)
		self.UpdateHash()

	def CalculateHash(self):
		txData = self.StrNoSignatureAndHash()
		return hashlib.sha256(txData.encode()).hexdigest()

	def UpdateHash(self):
		self.__txTimestamp = datetime.now()
		self.__txHash = self.CalculateHash()
		return self.__txHash

	def VerifyHash(self):
		currentHash = self.CalculateHash()
		return self.__txHash == currentHash

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

	def GetTotalAmount(self):
		return sum(self.__outputs.values())

	def __str__(self):
		return (f"{self.StrNoSignature()}, Signature: {self.__signature}")

	def StrNoSignature(self):
		return (f"{self.StrNoSignatureAndHash()}, Hash: {self.__txHash}")

	def StrNoSignatureAndHash(self):
		return (
		    f"Transaction\nInput: {self.__input}, Outputs: {self.__outputs}, "
		    f"TotalAmount: {self.GetTotalAmount()}, Timestamp: {self.__txTimestamp}"
		)


def testTransaction():
	privateKey = SigningKey.generate(curve=NIST256p)

	tx = Transaction("1SenderAddress", {
	    "1ReceiverAddress": 0.5,
	    "2ReceiverAddress": 0.3
	})

	print("Initial Transaction:")
	print(tx)

	assert tx.VerifyHash(), "Initial hash verification failed"

	tx.UpdateSignature(privateKey)

	print("\nTransaction after signing:")
	print(tx)

	assert tx.VerifySignature(), "Signature verification failed"

	print("\nSignature verification passed.")

	tx.AddOutput("3ReceiverAddress", 0.2)

	print("\nTransaction after adding an output:")
	print(tx)

	if (tx.VerifyHash() is False):
		print("Hash verification after adding output failed")

	tx.UpdateSignature(privateKey)

	print("\nTransaction after updating signature:")
	print(tx)

	assert tx.VerifySignature(), "Signature verification after update failed"

	print("\nAll tests passed.")


if __name__ == "__main__":
	testTransaction()
