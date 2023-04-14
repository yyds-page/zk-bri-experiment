#   

系统建议: ubuntu
CPU要求：x86_64/amd64

## libff

```bash
export http_proxy=http://127.0.0.1:1087
export https_proxy=http://127.0.0.1:1087

git clone https://github.com/scipr-lab/libff
cd libff
git submodule init && git submodule update

sudo apt-get install build-essential git libboost-all-dev cmake libgmp3-dev libssl-dev pkg-config libsodium-dev

mkdir build && cd build
# cmake -G Ninja 
cmake -DCMAKE_BUILD_TYPE=Release -DUSE_ASM=ON -DCURVE=BN128 ..
make -j 7
sudo make install

```

## libsnark

```shell
# git clone --recursive https://github.com/meilof/libsnark

git clone --recursive https://github.com/scipr-lab/libsnark
cd libsnark/

sudo apt install build-essential cmake git libgmp3-dev libprocps-dev python3-markdown libboost-program-options-dev libssl-dev python3 pkg-config
  
mkdir build
cd build/

cmake .. -DCURVE=BN128

make -j 7
sudo make install

```

```text

https://github.com/meilof/python-libsnark

```

```shell
git clone --recurse-submodules https://github.com/sunblaze-ucb/Virgo.git
cd Virgo

sudo apt install -y  cmake make git clang++-7 libgmp-dev g++ parallel



```

https://github.com/TAMUCrypto/virgo-plus.git

```shell
git clone https://github.com/TAMUCrypto/virgo-plus.git

cd virgo-plus
mkdir build
cd build/
cmake .. -DCMAKE_BUILD_TYPE=Release 
make

```

