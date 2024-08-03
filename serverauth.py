import hashlib
import os
import random


def hash_string(input_string, salt):
    input_bytes = input_string.encode()
    salt_bytes = salt.encode
    combined_bytes = input_bytes + salt_bytes
    hash_object = hashlib.sha256()
    hash_object.update(combined_bytes)
    hash_value = hash_object.hexdigest()
    return hash_value

input_string = "Joseph"
salt = "secure"
hashed_string = hash_string(input_string, salt)

print(hashed_string)
