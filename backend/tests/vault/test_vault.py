from backend.vault.vault import Vault

def test_verify_valid_signature():
    data = {'foo': 'test_data'}
    vault = Vault()
    signature = vault.sign(data)

    assert Vault.verify(vault.public_key, data, signature)

def test_verify_invalid_signature():
    data = {'foo': 'test_data'}
    vault = Vault()
    signature = vault.sign(data)

    assert not Vault.verify(Vault().public_key, data, signature)