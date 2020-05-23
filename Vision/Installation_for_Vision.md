# Installation Guide
Author : Eunbin Seo <br/>
Date : 2020.02.04.

## check the graphic card for driver
1. graphic driver install
refer: [Link](https://codechacha.com/ko/install-nvidia-driver-ubuntu/)

## Install Cuda
1. Check driver version and select cuda version. (our driver version is 430, select cuda 10.1) <br/>
~~~bash
nvidia-smi
~~~
2. Download Cuda 10.1 runfile 
[Link](https://developer.nvidia.com/cuda-10.1-download-archive-base?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=runfilelocal)

3. Run the cuda 10.1 in cuda file. If not working, you make it executable.
[reference](http://blog.naver.com/PostView.nhn?blogId=angelkim88&logNo=221630554860&parentCategoryNo=&categoryNo=73&viewDate=&isShowPopularPosts=true&from=search)

4. modify bashrc file
~~~bash
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDADIR=/usr/local/cuda-10.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
~~~
5. After modifying bashrc file, execute this command to verify the cuda version.
~~~bash
source ~/.bashrc
~~~

## Install Cudnn
1. GOTO [Link](https://developer.nvidia.com/rdp/cudnn-download), and download cuDNN Runtime Library for Ubuntu18.04 (Deb)
2. Execute the file!
~~~ bash
sudo dpkg -i libcudnn7_7.6.4.38-1+cuda10.0_amd64.deb 
~~~

## Make Virtual Environment
1. make virtual environment
~~~ bash
python3 -m venv ./(venv name)
~~~
we named virtual environment 'tensorflow'
2. activate the virtual environment
~~~ bash
# source (virtual environment name)/bin/activate
source tensorflow/bin/activate 
~~~
check always that the venv 
## Install Tensorflow
first, check the version.
~~~ bash
pip3 install tensorflow-gpu==(version)
~~~
## Install Keras
first, check the version.
~~~ bash
pip3 install keras==(version)
~~~
## Install torch
refer: [Link](https://pytorch.org/get-started/previous-versions/)
first, check the version.
~~~ bash
pip3 install torch===1.2.0 torchvision===0.4.0 -f https://download.pytorch.org/whl/torch_stable.html
~~~
## Install OpenCV
refer: [Link](https://webnautes.tistory.com/1186)

## Install Ros, Ros2, ... and so on...
