# install ROS

## For TX2

#################
### Setup ROS ###
#################

### Setup sources.lst
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
### Setup keys
```
$ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116
```
### Installation
```
$ sudo apt-get update
$ sudo apt-get install ros-kinetic-desktop

$ sudo apt-get install python-rosdep
$ sudo rosdep init
$ rosdep update

$ echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

### Setup bashrc for ROS 
```
$ Add to .bashrc: source /opt/ros/kinetic/setup.bash
```

### Create ROS workspace
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
$ cd ~/catkin_ws/
$ catkin_make
```

### Setup bashrc for ROS workspace
```
$ Add to .bashrc: source ~/catkin_ws/devel/setup.bash
```

####################
### Setup ZED For ROS ###
####################

### Install ZED SDK
```
$ wget https://download.stereolabs.com/zedsdk/2.4/tegrax2
$ chmod 755 (filename)
$ ./(filename)...

$ sudo apt-get install libpcl1.7 ros-kinetic-pcl-ros ros-kinetic-image-view ros-kinetic-tf2-geometry-msgs
$ cd ~/catkin_ws/src
$ git clone https://github.com/stereolabs/zed-ros-wrapper.git
```

### Check cuda version 
```
$ cat /usr/local/cuda/version.txt
```
#### And may be necessary to do this: in zed-ros-wrapper/CMakeLists.txt put in: SET(CUDA_VERSION "9.0")

### Run up ZED on ros
```
$ cd ~/catkin_ws
$ catkin_make
```

### Test that it works
```
$ roslaunch zed_wrapper zed.launch
$ rosrun image_view image_view image:=/camera/right/image_rect_color
```

########################
### Setup the model_car ###
#######################

### Put ros/bdd_car_simple/ into catkin_ws/src/

### Re-Compile ROS
```
$ catkin_make
$ source devel/setup.bash  # make sure ros can find .laun
$ roslaunch bair_car bair_car.launch use_zed:=true
$ rosrun image_view image_view image:=/bair_car/zed/right/image_rect_color
```

### And rostopic echo all the topics to check
```
$ rostopic list 
$ rostopic echo /bair_car/...
```

###########################
### Running experiments ###
###########################

### Go into bair_car.launch and change the bagpath to where you want to record data to (e.g. flash drive)
### In this step, you should put the bair_car and zed_wrapper into workspace you create(normally ~/catkin_ws/src), then use catkin_make to build it  


###########################
### Install Tensorflow and Keras ###
###########################

### Install pip and other dev package
```
$ sudo apt-get install libblas-dev liblapack-dev python-dev python-pip
```
### Updating pip
```
$ sudo pip install --upgrade pip
```

### Download Tensorflow install package from GitHub(https://github.com/peterlee0127/tensorflow-nvJetson) -> using 1.7.0 currently, and using cat to merge two files
```
$ cat tensorflow-1.7.0-cp27-cp27mu-linux_aarch64.whl.part-* > tensorflow-1.7.0-cp27-cp27mu-linux_aarch64.whl
```


### Compile and install bazel
```
$ sudo apt-get install  build-essential python zip openjdk-8-jdk
$ mkdir bazel && cd bazel

$ bazel_version="0.11.1"
$ wget https://github.com/bazelbuild/bazel/releases/download/$bazel_version/bazel-$bazel_version-dist.zip

$ unzip bazel-$bazel_version-dist.zip && ./compile.sh
$ sudo cp output/bazel /usr/local/bin
```

### Compile tensorflow
```
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/extras/CUPTI/lib64 
$ sudo apt-get install python-numpy python-dev python-pip python3.5-numpy python-wheel
$ git clone https://github.com/tensorflow/tensorflow # You may wish to check out a speicfic branch here

$ cd tensorflow
$ ./configure (lots of config)

#build a whl file
$ bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package
$ bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg  #put the whl in /tmp/tensorflow_pkg
$ pip3 install /tmp/tensorflow_pkg/tensorflow-... #depending on your tensorflow/python version this file may have a different name
```

### Using pip to install Tensorflow(about -H, because directory owner issue and tf won't install w/o it)
### TX2 BUG -> have to move out enum34 first
```
$ sudo mv /usr/lib/python2.7/dist-packages/enum34-1.1.2.egg-info ~/Desktop/
$ sudo -H pip install tensorflow-1.7.0-cp27-cp27mu-linux_aarch64.whl
```

### Using pip to install keras
```
$ sudo -H pip install keras
```

### If you need .h5 file load and save, install libhdf5-dev
```
$ sudo apt-get install libhdf5-dev
$ sudo -H pip install h5py
```

## For Desktop
### Remind: Use the GUI ubuntu to preprocessing the data

### Install ros
```
$ sh -c 'echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list'
$ apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 0xB01FA116
$ apt-get update && apt-get install -y ros-kinetic-desktop-full
$ sudo apt-get install -y python-rosinstall

$ rosdep init
$ rosdep update
$ echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```

### Install ZED camera SDK(seems like not able to install on docker)
```
$ cd ~/
$ wget https://download.stereolabs.com/zedsdk/2.4/ubuntu
$ chmod 777 ZED_SDK_Linux_Ubuntu16_v2.4.0.run
$ ./ZED_SDK_Linux_Ubuntu16_v2.4.0.run
```

