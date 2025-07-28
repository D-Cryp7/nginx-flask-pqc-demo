from wolfcrypt.ciphers import MlDsaType, MlDsaPrivate, MlDsaPublic

def keygen(param_set = MlDsaType.ML_DSA_65):
    private_key = MlDsaPrivate.make_key(param_set)

    return private_key.encode_priv_key(), private_key.encode_pub_key()

if __name__ == "__main__":
    private_key, public_key = keygen()
    
    with open("priv.key", "wb") as f:
        f.write(private_key)
    
    with open("pub.key", "wb") as f:
        f.write(public_key)