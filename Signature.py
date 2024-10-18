import hashlib
import base64
import json
from ecdsa import SigningKey, VerifyingKey, NIST256p, BadSignatureError
from abc import ABC


class Signature(ABC):

	@staticmethod
	def Sign(message, privateKey):
		"""
		- private_key: SigningKey
		"""
		messageHash = hashlib.sha256(message.encode('utf-8')).digest()
		signature = privateKey.sign(messageHash)
		publicKey = base64.b64encode(
		    privateKey.get_verifying_key().to_string()).decode('utf-8')
		signatureBase64 = base64.b64encode(signature).decode('utf-8')

		obj = {
		    "publicKey": publicKey,
		    "signature": signatureBase64,
		    "message": message,
		    "algorithm": "SHA256withECDSA"
		}

		return json.dumps(obj)

	@staticmethod
	def Verify(signatureBase64, message, publicKeyBase64):
		publicKeyBytes = base64.b64decode(publicKeyBase64)
		signatureBytes = base64.b64decode(signatureBase64)

		verifyingKey = VerifyingKey.from_string(publicKeyBytes, curve=NIST256p)

		messageHash = hashlib.sha256(message.encode('utf-8')).digest()

		try:
			return verifyingKey.verify(signatureBytes, messageHash)
		except BadSignatureError:
			return False
