import unittest
from cryptography.fernet import Fernet, InvalidToken
from chat import encrypt_message, decrypt_message

class TestMessaging(unittest.TestCase):
    def test_roundtrip(self):
        key = Fernet.generate_key()
        self.assertEqual(decrypt_message(key, encrypt_message(key, "hello")), "hello")
    def test_wrong_key(self):
        key1, key2 = Fernet.generate_key(), Fernet.generate_key()
        with self.assertRaises(InvalidToken):
            decrypt_message(key2, encrypt_message(key1, "secret"))

if __name__ == "__main__":
    unittest.main()
