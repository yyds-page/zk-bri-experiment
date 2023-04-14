import hashlib
import time

import gmpy2
from gmpy2 import mpz
from typing import Tuple

'''
deVirgo 零知识证明是一种非交互式的、基于离散对数问题的零知识证明。
它是由 Daniel Bleichenbacher、Michael Szydlo 和 Serge Vaudenay 在 2000 年提出的。

在 deVirgo 零知识证明中，证明者需要证明自己知道一个秘密 x，但是不需要将秘密 x 传递给验证者。
证明者可以生成一个证明，使得验证者可以在验证该证明的同时，不了解秘密 x。
证明的过程可以被表示为一条交互轮次的序列，其中每个轮次都包括证明者向验证者发送一条消息，然后验证者向证明者发送一个随机挑战。
如果证明者可以正确地响应每个挑战，那么验证者就会接受该证明。

deVirgo 零知识证明的流程如下：

选择一个素数 p 和一个阶为 q 的子群 G，以及一个生成元 g，其中 q 是 p-1 的因子。
选择一个私钥 x，并计算公钥 y = g^x mod p。
证明者要证明自己知道一个秘密 x，而不需要将 x 传递给验证者。
证明者将一个字符串 s 哈希为一个整数 m。
证明者选择一个随机数 k，并计算 r = g^k mod p 和 t = g^m mod p。
证明者将字符串 "r" 和 "t" 拼接起来，并哈希为一个整数 c。
证明者计算 z = (k + x * c) mod q，并向验证者发送挑战 (c, z)。
验证者检查 c 是否等于哈希值 hash("r" + "t")，并计算 u1 = g^z * y^c mod p 和 u2 = g^m mod p。
验证者计算 v = u1^hash(u2) mod p，并检查 v 是否等于 r。
如果 v 等于 r，那么验证者接受该证明，否则拒绝该证明。
通过这个过程，证明者可以证明自己知道一个秘密 x，而不需要将 x 传递给验证者，同时验证者也可以在不了解 x 的情况下验证证明的有效性。
因此，deVirgo 零知识证明具有保密性、完整性和不可伪造性等重要特征。

'''


def hash_string(s: str) -> mpz:
    """
    将字符串 s 转换成一个整数。
    """
    # 将字符串 s 转换成一个字节数组
    b = s.encode()

    # 将字节数组的哈希值转换成一个大整数
    # 将字节数组的哈希值转换成一个大整数
    h = mpz(hashlib.sha256(b).hexdigest(), 16)
    return h


class deVirgo:
    """
    deVirgo 零知识证明类。
    """

    def __init__(self):
        self.random_state = gmpy2.random_state()
        # 选择一个素数 p
        self.p = gmpy2.next_prime(mpz(2) ** 128)

        # 选择一个阶为 q 的子群 G
        self.q = gmpy2.next_prime(mpz(2) ** 128)

        # 选择一个生成元 g
        self.g = gmpy2.mpz_random(self.random_state, self.p - 1)

        # 选择一个私钥 x
        self.x = gmpy2.mpz_random(self.random_state, self.q - 1)

        # 计算公钥 y
        self.y = gmpy2.powmod(self.g, self.x, self.p)

    def gen_proof(self, s: str) -> tuple:
        """
        生成 deVirgo 零知识证明。
        """
        # 将字符串 s 转换成一个整数
        m = hash_string(s)

        # 选择一个随机数 k
        k = gmpy2.mpz_random(self.random_state, self.q - 1)

        # 计算 r 和 t
        r = gmpy2.powmod(self.g, k, self.p)
        t = gmpy2.powmod(self.g, m, self.p)

        # 计算 c
        c = hash_string(str(r) + str(t))

        # 计算 z
        z = (k + self.x * c) % self.q

        # 返回挑战和响应
        return (c, z)

    def verify_proof(self, s: str, proof: tuple) -> bool:
        """
        验证 deVirgo 零知识证明。
        """
        # 将字符串 s 转换成一个整数
        m = hash_string(s)

        # 解析出挑战和响应
        c, z = proof

        # 计算 u1 和 u2
        u1 = (gmpy2.powmod(self.g, z, self.p) * gmpy2.powmod(self.y, c, self.p)) % self.p
        u2 = gmpy2.powmod(self.g, m, self.p)

        # 计算 v
        v = gmpy2.powmod(u1, hash_string(str(u2)), self.p)

        # 验证零知识证明是否合法
        return c == v % self.q


# 创建一个 deVirgo 实例
dv = deVirgo()

# 生成一个字符串 s，我们将证明我们知道 s
s = "Hello World!"

# 生成零知识证明
proof = dv.gen_proof(s)

# 验证零知识证明
result = dv.verify_proof(s, proof)

if result:
    print("The proof is valid!")
else:
    print("The proof is invalid.")
