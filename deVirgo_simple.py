import hashlib
import random

'''这里给出使用 Python 实现 deVirgo 零知识证明的示例代码。
为了简化代码，这里采用了 Python 自带的大数计算库 pow() 进行运算。
但是实际应用中，为了保证安全性，应该使用专门的大数计算库。

这个例子中，证明者选择了一个字符串 s 并将其哈希为整数 m，然后使用随机数 k 计算出 r 和 t，
并将它们拼接起来哈希为整数 c，然后根据随机数 k 和秘密值 x 计算出挑战的整数 z 并发送给验证者。
验证者检查 c 是否等于哈希值 hash("r" + "t")，如果是，则根据 z、y
'''

# 选择一个素数 p 和一个阶为 q 的子群 G，以及一个生成元 g，其中 q 是 p-1 的因子。
p = 953
q = 7
g = 5

# 选择一个私钥 x，并计算公钥 y = g^x mod p。
x = 3
y = pow(g, x, p)

# 证明者要证明自己知道一个秘密 x，而不需要将 x 传递给验证者。
# 证明者将一个字符串 s 哈希为一个整数 m。
s = 'hello'
m = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)

# 证明者选择一个随机数 k，并计算 r = g^k mod p 和 t = g^m mod p。
k = random.randint(1, q)
r = pow(g, k, p)
t = pow(g, m, p)

# 证明者将字符串 "r" 和 "t" 拼接起来，并哈希为一个整数 c。
c = int(hashlib.sha256((str(r) + str(t)).encode('utf-8')).hexdigest(), 16)

# 证明者计算 z = (k + x * c) mod q，并向验证者发送挑战 (c, z)。
z = (k + x * c) % q

# 验证者检查 c 是否等于哈希值 hash("r" + "t")，并计算 u1 = g^z * y^c mod p 和 u2 = g^m mod p。
if c == int(hashlib.sha256((str(r) + str(t)).encode('utf-8')).hexdigest(), 16):
    u1 = (pow(g, z, p) * pow(y, c, p)) % p
    u2 = pow(g, m, p)

    # 验证者计算 v = u1^hash(u2) mod p，并检查 v 是否等于 r。
    v = pow(u1, int(hashlib.sha256(str(u2).encode('utf-8')).hexdigest(), 16), p)
    if v == r:
        print('Proof is valid.')
    else:
        print('Proof is invalid.')
else:
    print('Proof is invalid.')
