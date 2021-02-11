import hmac
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5, AES, DES3
from Crypto.PublicKey import RSA
from binascii import b2a_hex, a2b_hex, b2a_base64, a2b_base64, hexlify, unhexlify

# 生成随机通信密钥
def gen_rnd_comm_key():
    char_list = "0123456789qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP!@#$%^&*"
    max_idx = len(char_list) - 1
    comm_key = ""
    for _ in range(16):
        idx = randint(0, max_idx)
        char = char_list[idx]
        comm_key += char
    return comm_key

# ---------------------------------------- 单向散列加密 ----------------------------------------
# 获取加密后字符
def get_encrypted_str(ori_bytes: bytes) -> str:
    encrypted = hmac.new(b"dkstFeb.1st", ori_bytes, "sha1")
    return encrypted.hexdigest()


# ---------------------------------------- 对称加密 ----------------------------------------
class AesEncryption():
    def __init__(self, key: str, mode=AES.MODE_GCM):
        self.key = key.encode()
        # 密钥key 长度必须为16(AES-128),24(AES-192),或者32(AES-256)
        assert len(self.key) in [16, 24, 32], "密钥key长度必须为16,24,32!"
        self.mode = mode
        self.iv = Random.new().read(AES.block_size)  # 随机生成16字节的字节流

    # 对明文进行加密
    def encrypt(self, plain_str: str):
        cipher_obj = AES.new(self.key, self.mode, self.iv)
        encrypt_str = b2a_hex(cipher_obj.encrypt(plain_str.encode())).decode()
        return encrypt_str

    # 对密文进行解密
    def decrypt(self, encrypt_str: str):
        cipher_obj = AES.new(self.key, self.mode, self.iv)
        decrypt_str = cipher_obj.decrypt(a2b_hex(encrypt_str.encode())).decode()
        return decrypt_str

class Des3Encryption():
    def __init__(self, key: str, mode=DES3.MODE_CFB):
        self.key = key.encode()
        assert len(self.key) in [16, 24, 32], "密钥key长度必须为16,24,32!"
        self.mode = mode
        self.iv = Random.new().read(DES3.block_size)  # 随机生成8字节的字节流

    # 对明文进行加密
    def encrypt(self, plain_str: str):
        cipher_obj = DES3.new(self.key, self.mode, self.iv)
        encrypt_str = b2a_base64(cipher_obj.encrypt(plain_str.encode())).decode()
        return encrypt_str

    # 对密文进行解密
    def decrypt(self, encrypt_str: str):
        cipher_obj = DES3.new(self.key, self.mode, self.iv)
        decrypt_str = cipher_obj.decrypt(a2b_base64(encrypt_str.encode())).decode()
        return decrypt_str

# ---------------------------------------- RSA非对称加密 ----------------------------------------
# 生成RSA公私钥对
def gen_rsa_public_private_pair():
    # 创建一个rsa算法对应的密钥对生成器实例
    rsa = RSA.generate(2048)
    # 获取生成的私钥
    public_key = rsa.public_key().export_key()
    private_key = rsa.export_key()
    return public_key, private_key

# RSA加密
def encrypt_rsa(public_key: bytes, plain_str: str):
    try:
        # 导入二进制密钥, 生成一个RSA的密钥对象
        rsa_key_obj = RSA.import_key(public_key)
        # 创建加密对象
        cipher_obj = PKCS1_v1_5.new(rsa_key_obj)
        # 对明文加密, 获得加密的二进制数据
        encrypt_bytes = cipher_obj.encrypt(plain_str.encode())
        # 对加密的二进制数据转16进制字符串
        hex_encrypt_str = hexlify(encrypt_bytes).decode()
        return {"state": 1, "msg": hex_encrypt_str}
    except Exception as e:
        return {"state": 0, "msg": str(e)}

# RSA解密
def decrypt_rsa(private_key: bytes, hex_encrypt_str: str):
    try:
        # 导入二进制密钥, 生成一个RSA的密钥对象
        rsa_key_obj = RSA.import_key(private_key)
        # 创建加密对象
        cipher_obj = PKCS1_v1_5.new(rsa_key_obj)
        # 对16进制加密字符串先转字节, 再转二进制
        encrypt_bytes = unhexlify(hex_encrypt_str.encode())
        # 对加密的二进制数据解密, 得到明文
        plain_str = cipher_obj.decrypt(encrypt_bytes, b"").decode()
        return {"state": 1, "msg": plain_str}
    except Exception as e:
        return {"state": 0, "msg": str(e)}


public_key_client = b"-----BEGIN PUBLIC KEY-----\n" \
                    b"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAskf++tlor1gVM2Xh51wH\n" \
                    b"fOxfY3whdsWr11FeDC5IfSOZeAKPKh9kXHH9z4IL3c7HmKQuWilcyIkLCOLYR0Q0\n" \
                    b"YkRxS82gT/wWFWkXRZwCZrGFvEtdKLjUtIJzw6EEHKWJVOetc7zg9KcREYxpHCPx\n" \
                    b"2V6/MCChfn86GYhuOl66VoMvdHzzQ2ssOV711T6q/ZGmLSmZTcePI/bgGAeSQ7rl\n" \
                    b"CdCtj5IDeZeKZh/8rvKD8vSHMH94AuZp/lRgNvx5uxG5GyNi2iFV1dvFdftUpLQG\n" \
                    b"k49T65a1cMPJ29us7yih+F3PdfvTVXngGK1XGe9eDN9knnHZDQ86Kw85njuilP2k\n" \
                    b"CwIDAQAB\n" \
                    b"-----END PUBLIC KEY-----"

private_key_client = b"-----BEGIN RSA PRIVATE KEY-----\n" \
                     b"MIIEpQIBAAKCAQEAskf++tlor1gVM2Xh51wHfOxfY3whdsWr11FeDC5IfSOZeAKP\n" \
                     b"Kh9kXHH9z4IL3c7HmKQuWilcyIkLCOLYR0Q0YkRxS82gT/wWFWkXRZwCZrGFvEtd\n" \
                     b"KLjUtIJzw6EEHKWJVOetc7zg9KcREYxpHCPx2V6/MCChfn86GYhuOl66VoMvdHzz\n" \
                     b"Q2ssOV711T6q/ZGmLSmZTcePI/bgGAeSQ7rlCdCtj5IDeZeKZh/8rvKD8vSHMH94\n" \
                     b"AuZp/lRgNvx5uxG5GyNi2iFV1dvFdftUpLQGk49T65a1cMPJ29us7yih+F3PdfvT\n" \
                     b"VXngGK1XGe9eDN9knnHZDQ86Kw85njuilP2kCwIDAQABAoIBAAPfcS2NLYCpntmd\n" \
                     b"UU6k/tClkzORDb+2bujgLp/VyDitCPdvbswRHy1W7ew6Z1GWiAV2g5SX025+c6E/\n" \
                     b"dEf6tlHwKgSQifaoLj6hfXeYpQC1bdyiR9Ag+8CUGORbX2spOWuBFjvZEuCdryQ8\n" \
                     b"yEfBNs7BsnuJf0NFNkOPECiact0li8kZwOqYAUaPmJxlDYcKXwIxb/z5CCGcgu77\n" \
                     b"AL66ZUWWIHySmI13gvsgN9dWMfc6ZAxqwwwWyeof7ZXFZ85vA7I6OkH7R/CAXfV2\n" \
                     b"FEAeLL7Vg22gmSa0vvuae75WiDCysb7HiyWaH6FRjKSjyW1Lhl8bhYdqbdRsyDqe\n" \
                     b"wu4jCgECgYEA03SB0MkyieM8eeL9NmNfKxMNn7YQxXMU40h2Mns+xPlzxMMhmBwc\n" \
                     b"Xt6969D6dSychLHvsoZXAYfdHUa+Xc1DyjK7CytAkPJNvQw+VK7v8XFdqZLTsZ1X\n" \
                     b"1pCwxk2aXcfMlQBwDffW5AWCoQBoQ642zWqny+zJ9wqfbvm8+All9QsCgYEA19Z3\n" \
                     b"U1NGYjg/hhPhzn6GBvVYqSP3zZdaXgDowTuK7iNKvBP92mvLhx7+Re7s2sqYZQJI\n" \
                     b"LjoeAKnsA+BrnnIAnk5gs/Oms8kRCXZ/nTRyHEPF97PspwuaZjGraG5wJFIYElWq\n" \
                     b"l8ktww2ewqclgpbUhqpO4b3MUiNDf7TMyawGbQECgYEAlQgyTmLfmctsXkObT2/u\n" \
                     b"LT+6hGwfmeooOKBjneS7MrzV2UHmNXzqifrXRJL/UwJkNinq1JpWTB/jubSYiygW\n" \
                     b"tTXYGmEbmo0MOUedzrWVK0hJSTDQvwg0VmeYD8u2Fo6xI/sw/sdEz2UK0kqlMb5h\n" \
                     b"pZmcNd/n4JO+FssxYmfNUk0CgYEAqby0fGfp2wYnFrb+BllD56b8gY+SqjDT1Udb\n" \
                     b"w9KikGJavIvwP9wz4+BA0RhzViCrNgxUXV5BB/6ZZ/cOSz2WNOiobfw35f1Ck7GH\n" \
                     b"7EY5UvcNcZ4ihr++PY3kIa1wLXAOFCUgkluYzGMiriuqeQdKvVijzi1nyFSJGZ5C\n" \
                     b"ynqpVwECgYEAlrjk8jJxRz9HYSbl+FoOClRF1VxJM2y9MP16/mxfjd2VbcInGcZD\n" \
                     b"1NGqKCzGULiozdLIBOCbu42mceFQtAD6LvkGDNTdSCn7K1/y7St8j8HJihj6ebtx\n" \
                     b"Bhm2cf09JR+Qh7rlKjkFc9aWs8E1Th0oyEcthLUlB8C2In+GdDZcoN8=\n" \
                     b"-----END RSA PRIVATE KEY-----"

public_key_server = b"-----BEGIN PUBLIC KEY-----\n" \
                    b"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA9CwF74Q6OuxB42BsscZy\n" \
                    b"8Nf4QvnWKkMfbSvz4a7WKLXjxVOfFooAnaom/TVfWxQw0Uud4rTZa3T3Yf3fldZJ\n" \
                    b"9He6Z8r0V/79oVPAydBGdj9U6BPWyVY1O76cEquc6Ymfg18ytxuRzd7T11hDe1Zo\n" \
                    b"sUPYmTA70BUbEsK9EwmPDAI9KBTnWBOy4rx+Gcc7Op/tr+WD+yDVaARyOS/7RwNT\n" \
                    b"QvO+D+38Q0yL/IM/hhnMN+lKXGVBJ6BpFaZXQ7QATwPU2oLO/DhXDpGdtO0GF31b\n" \
                    b"STh/GLGnrs02rquGPzX+b1/vaEyVEwKuvITIclQsxVpvDUjfSgzRnTlNquOlHCz4\n" \
                    b"9wIDAQAB\n" \
                    b"-----END PUBLIC KEY-----"

comm_key = gen_rnd_comm_key()
en_comm_key = encrypt_rsa(public_key_server, comm_key)