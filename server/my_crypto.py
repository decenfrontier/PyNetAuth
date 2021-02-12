from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5, AES, DES3
from Crypto.PublicKey import RSA
from binascii import b2a_hex, a2b_hex, b2a_base64, a2b_base64, hexlify, unhexlify

# ---------------------------------------- 对称加密 ----------------------------------------
class AesEncryption():
    def __init__(self, key: str, mode=AES.MODE_GCM):
        # 密钥key 长度必须为16(AES-128),24(AES-192),或者32(AES-256)
        if len(key) < 16:
            key = key.center(16, "*")
        elif len(key) < 24:
            key = key.center(24, "*")
        elif len(key) < 32:
            key = key.center(32, "*")
        else:
            key = key[:32]
        self.key = key.encode()
        self.mode = mode
        self.iv = Random.new().read(AES.block_size)  # 随机生成16字节的字节流

    # 对明文进行加密
    def encrypt(self, plain_str: str) -> bytes:
        cipher_obj = AES.new(self.key, self.mode, self.iv)
        encrypt_bytes = b2a_hex(cipher_obj.encrypt(plain_str.encode()))
        return encrypt_bytes

    # 对密文进行解密
    def decrypt(self, encrypt_bytes: bytes) -> str:
        cipher_obj = AES.new(self.key, self.mode, self.iv)
        decrypt_str = cipher_obj.decrypt(a2b_hex(encrypt_bytes)).decode()
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
    except Exception as e:
        hex_encrypt_str = ""
    return hex_encrypt_str

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
    except Exception as e:
        plain_str = ""
    return plain_str

public_key_server = b"-----BEGIN PUBLIC KEY-----\n" \
                    b"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA9CwF74Q6OuxB42BsscZy\n" \
                    b"8Nf4QvnWKkMfbSvz4a7WKLXjxVOfFooAnaom/TVfWxQw0Uud4rTZa3T3Yf3fldZJ\n" \
                    b"9He6Z8r0V/79oVPAydBGdj9U6BPWyVY1O76cEquc6Ymfg18ytxuRzd7T11hDe1Zo\n" \
                    b"sUPYmTA70BUbEsK9EwmPDAI9KBTnWBOy4rx+Gcc7Op/tr+WD+yDVaARyOS/7RwNT\n" \
                    b"QvO+D+38Q0yL/IM/hhnMN+lKXGVBJ6BpFaZXQ7QATwPU2oLO/DhXDpGdtO0GF31b\n" \
                    b"STh/GLGnrs02rquGPzX+b1/vaEyVEwKuvITIclQsxVpvDUjfSgzRnTlNquOlHCz4\n" \
                    b"9wIDAQAB\n" \
                    b"-----END PUBLIC KEY-----"

private_key_server = b"-----BEGIN RSA PRIVATE KEY-----\n" \
                     b"MIIEowIBAAKCAQEA9CwF74Q6OuxB42BsscZy8Nf4QvnWKkMfbSvz4a7WKLXjxVOf\n" \
                     b"FooAnaom/TVfWxQw0Uud4rTZa3T3Yf3fldZJ9He6Z8r0V/79oVPAydBGdj9U6BPW\n" \
                     b"yVY1O76cEquc6Ymfg18ytxuRzd7T11hDe1ZosUPYmTA70BUbEsK9EwmPDAI9KBTn\n" \
                     b"WBOy4rx+Gcc7Op/tr+WD+yDVaARyOS/7RwNTQvO+D+38Q0yL/IM/hhnMN+lKXGVB\n" \
                     b"J6BpFaZXQ7QATwPU2oLO/DhXDpGdtO0GF31bSTh/GLGnrs02rquGPzX+b1/vaEyV\n" \
                     b"EwKuvITIclQsxVpvDUjfSgzRnTlNquOlHCz49wIDAQABAoIBACqNJXepJnCwTYcv\n" \
                     b"faG5gLxiFrytR1pUGjzvRPAWhPHRSOFRgk7uO88+IM9NptF7gkpnEBu7AozMdHQa\n" \
                     b"RwWYs4ir+Msvvkc7g73Cl71T04O147kSBANQR7SishY62/yC5E6Dn5XzcwRaibZk\n" \
                     b"hlYPJ+2EclG36ySHGRG66DJSHyCrSA1a/81W//DFFJReMKwG+yiY7e2tNbQ+yRUM\n" \
                     b"X9UqUA8T6XZpQacdhZJ0IypiR6O9iLvoYvDc71Rg99TRHe0HxWJMRfo1xsvs8iXe\n" \
                     b"x4smEeZ4g5sddejdnbrKojkCozP9Fmr4VEjItRpAXmW7//C56XE3Acebg0XGb3Jh\n" \
                     b"Xn6J+IkCgYEA9G8+jflmQtwUpVA9DvYTi/Mz6kJiqREm/q/SN5BcfPW8o5z41Gab\n" \
                     b"D4VR2N/esQyZ3svrVly5+4ycZUOo25vZdp8mgTsc8+5DGhcSNRj8oSKJs00FR3z1\n" \
                     b"O9sL1fcymfpIB29ocjFYL9ZmyzpMdmDCosmPqZFGVmGtm/UE0blqH4UCgYEA/7mZ\n" \
                     b"JyzmB2BQiHy6rYHFZqfHWn+JfWGXPZw0+N6RvV4YIuRnzmVlxp1OAseNQYr+zkT6\n" \
                     b"9nzPPyEpaTrFh1JoSoFY73G4FtrqhRPkmjbAF8QMVN7nXv/YxfxX6nptaO0kC766\n" \
                     b"9FiCfNwtQvL7xcxPTfQ6+DOf4rzoiBFZe4tG2UsCgYAfepQbxJqe0aj3ATZbzuUF\n" \
                     b"iPSOnq4GB+d1tT7lWPoQPbVlfLmu4OfnP8wimfIb6vuF7c0I+jgZZSpfAC+m2JNQ\n" \
                     b"634R9oLsBystGPuHSwh91+zT4n9jjXwnkTYdABDMM6dDDd3tlt08i+gBFCj0tdFb\n" \
                     b"FYoi1EqypTGufAd62t4H4QKBgAU8ibRRqQwxnrSMyU3QQHiPqvdhcTFOFEjAsB0A\n" \
                     b"gb9888WTI8UIMoNUqUpJR801yW3z36e4eo3yYeSzvWO9/kC4UVfl3j0pkm/TLnUx\n" \
                     b"9dEGxLHgNqCtYIT9W9eDVkY1xO0wpKdoQJPJ9mtOinVMb7tK6wI2HGoKMEDJCioL\n" \
                     b"ehHtAoGBAKLQj/1cma2pkbZ+sYatuOVkSZexLxS0m3fls+PB7XgeJqgYixLgulgb\n" \
                     b"jF/fsA942iNnRGN351xS4MeqRKo49FxnPSvWJ4+0tIjtLZIym+LyvYtk9qS8AWRc\n" \
                     b"fbYo+lmllrt/gYVV/RzgUOBmTi+mCC5BGDkz/jRYERaFvTI4/hrW\n" \
                     b"-----END RSA PRIVATE KEY-----"

public_key_client = b"-----BEGIN PUBLIC KEY-----\n" \
                    b"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAskf++tlor1gVM2Xh51wH\n" \
                    b"fOxfY3whdsWr11FeDC5IfSOZeAKPKh9kXHH9z4IL3c7HmKQuWilcyIkLCOLYR0Q0\n" \
                    b"YkRxS82gT/wWFWkXRZwCZrGFvEtdKLjUtIJzw6EEHKWJVOetc7zg9KcREYxpHCPx\n" \
                    b"2V6/MCChfn86GYhuOl66VoMvdHzzQ2ssOV711T6q/ZGmLSmZTcePI/bgGAeSQ7rl\n" \
                    b"CdCtj5IDeZeKZh/8rvKD8vSHMH94AuZp/lRgNvx5uxG5GyNi2iFV1dvFdftUpLQG\n" \
                    b"k49T65a1cMPJ29us7yih+F3PdfvTVXngGK1XGe9eDN9knnHZDQ86Kw85njuilP2k\n" \
                    b"CwIDAQAB\n" \
                    b"-----END PUBLIC KEY-----"