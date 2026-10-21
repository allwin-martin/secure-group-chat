# Secure Group Chat — Encryption Baseline

A local **Fernet authenticated-encryption demo**. Not yet a networked or multi-user group chat.

## Run
```bash
python -m pip install -r requirements.txt
python chat.py "hello team"
python -m unittest discover -p "test_*.py"
```

## Demo
Show ciphertext differs from plaintext, correct-key decryption, and wrong-key authentication failure.

## Next phase
Implement transport, identities, authenticated key exchange, key rotation, group membership and replay protection. **Not suitable for production messaging.**
