import os
from hashlib import sha256
from hmac import HMAC



"""
加密密码
"""
def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    #assert isinstance(salt, str)

    password = password.encode('UTF-8')

    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()
    return salt + result

"""
与传过来的hash值和正式密码的hash值比较
"""
def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])



hashed = encrypt_password('secret password')

print(validate_password(hashed,'1 password'))
