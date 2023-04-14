
sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev curl

curl -O https://www.python.org/ftp/python/3.9.16/Python-3.9.16.tar.xz
tar -xf Python-3.9.16.tar.xz
cd Python-3.9.16/
./configure --enable-optimizations
make -j 7
make altinstall
which python3.9

