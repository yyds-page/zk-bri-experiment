import os

os.system('mkdir -p LOG')


def exec_system(*args, **kwargs):
    print("exec: %s" % (args))
    return os.system(*args, **kwargs)


for i in range(8):
    exec_system('./zk_proof SHA256_64_merkle_' + str(i + 1) + '_circuit.txt SHA256_64_merkle_' + str(
        i + 1) + '_meta.txt LOG/SHA256_' + str(i + 1) + '.txt')
    print("\n")
