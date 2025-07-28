from requests.packages.urllib3.exceptions import InsecureRequestWarning

import requests
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def test_sign():
    signature = requests.post("https://127.0.0.1:8443/sign", json = {
        "message": "8.8 Matrix 2025 with PQC!"
    }, verify = False).json()["signature"]

    return signature

def test_verify():
    signature = test_sign()

    verify = requests.post("https://127.0.0.1:8443/verify", json = {
        "message": "8.8 Matrix 2025 with PQC!",
        "signature": signature
    }, verify = False).json()

    return verify

if __name__ == "__main__":
    print(test_verify())
