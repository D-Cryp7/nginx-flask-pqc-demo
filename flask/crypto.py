from wolfcrypt.ciphers import MlDsaType, MlDsaPrivate, MlDsaPublic

class Signer:
    def __init__(self, param_set = MlDsaType.ML_DSA_65, keys_path = "./keys"):
        private_key = open(keys_path + "/priv.key", "rb").read()
        public_key = open(keys_path + "/pub.key", "rb").read()

        self.private_key = MlDsaPrivate(param_set)
        self.private_key.decode_key(private_key, public_key)

        self.public_key = MlDsaPublic(param_set)
        self.public_key.decode_key(public_key)

    def sign(self, message: bytes) -> bytes:
        return self.private_key.sign(message)

    def verify(self, message: bytes, signature: bytes) -> bool:
        return self.public_key.verify(signature, message)
