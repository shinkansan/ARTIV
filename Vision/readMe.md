# Tensorflow Installation

## Install Cuda
1. Check driver version and select cuda version. (our driver version is 430, select cuda 10.1) <br/>
~~~bash
nvidia-smi
~~~
2. Download Cuda 10.1 runfile [Link] (https://developer.nvidia.com/cuda-10.1-download-archive-base?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=runfilelocal)
3. Run the cuda 10.1 in cuda file. If not working, you make it executable.
4. modify bashrc file
~~~bash
export PATH=$PATH:/usr/local/cuda-10.0/bin
export CUDADIR=/usr/local/cuda-10.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-10.0/lib64
~~~
5. After modifying bashrc file, execute this command to verify the cuda version.
~~~bash
source .bashrc
~~~

## Install Cudnn
1. GOTO [Link](https://developer.nvidia.com/rdp/cudnn-download), and download 
--> Minimum system requirement!!


--> 
