# Install_CARLA
## Building CARLA
확인할것!
1. Ubuntu 버전확인: Ubuntu 18.04인지 확인하자. Ubuntu 16.04에서는 기본 컴파일러로인해 동작 불가능
2. 50GB정도의 여유공간이 있는지 확인하자.
3. 4GB 이상의 GPU
4. 2개의 TCP ports와 좋은 인터넷상태.
### Dependencies
CARLA를 실행시키기 위한 Dependencies download

```
sudo apt-get update
sudo apt-get install wget software-properties-common
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -
sudo apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-8 main"
sudo apt-get update

sudo apt-get install build-essential clang-8 lld-8 g++-7 cmake ninja-build libvulkan1 python python-pip python-dev python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev
pip2 install --user setuptools && pip3 install --user setuptools 

'''
CARLA dependencies와 Unreal Engine사이의 호환성 문제를 피하기 위해서 동일한 컴파일러 버전과 C++runtime libr
sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-8/bin/clang++ 180 && sudo update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-8/bin/clang 180

```
