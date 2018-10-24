# This Dockerfile is used to build an ROS + VNC + Tensorflow image based on Ubuntu 16.04
FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04

MAINTAINER Henry Huang "https://github.com/henry2423"
ENV REFRESHED_AT 2018-10-22

# Install sudo
RUN apt-get update && \
    apt-get install -y sudo \
    xterm \
    curl

# Install VScode
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/ && \
    sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

RUN sudo apt-get install -y apt-transport-https && \
    sudo apt-get update && \
    sudo apt-get install -y code

# Configure user
ARG user=hscc
ENV USER=$user
RUN groupadd $USER && \
    useradd --create-home --no-log-init -g $USER $USER && \
    usermod -aG sudo $USER && \
    echo "$USER:$USER" | chpasswd && \
    chsh -s /bin/bash $USER

### VNC Installation
LABEL io.k8s.description="VNC Container with ROS with Xfce window manager, firefox and chromium" \
      io.k8s.display-name="VNC Container with ROS based on Ubuntu" \
      io.openshift.expose-services="6901:http,5901:xvnc,6006:tnesorboard" \
      io.openshift.tags="vnc, ros, zed, tensorflow, ubuntu, xfce" \
      io.openshift.non-scalable=true

## Connection ports for controlling the UI:
# VNC port:5901
# noVNC webport, connect via http://IP:6901/?password=vncpassword
ENV DISPLAY=:1 \
    VNC_PORT=5901 \
    NO_VNC_PORT=6901
EXPOSE $VNC_PORT $NO_VNC_PORT

## Envrionment config
ENV VNCPASSWD=hscc2018
ENV HOME=/home/$USER \
    TERM=xterm \
    STARTUPDIR=/dockerstartup \
    INST_SCRIPTS=/home/$USER/install \
    NO_VNC_HOME=/home/$USER/noVNC \
    DEBIAN_FRONTEND=noninteractive \
    VNC_COL_DEPTH=24 \
    VNC_RESOLUTION=1920x1080 \
    VNC_PW=$VNCPASSWD \
    VNC_VIEW_ONLY=false
WORKDIR $HOME

## Add all install scripts for further steps
ADD ./src/common/install/ $INST_SCRIPTS/
ADD ./src/ubuntu/install/ $INST_SCRIPTS/
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +

## Install some common tools
RUN $INST_SCRIPTS/tools.sh
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

## Install xvnc-server & noVNC - HTML5 based VNC viewer
RUN $INST_SCRIPTS/tigervnc.sh
RUN $INST_SCRIPTS/no_vnc.sh

## Install firefox and chrome browser
RUN $INST_SCRIPTS/firefox.sh
RUN $INST_SCRIPTS/chrome.sh

## Install xfce UI
RUN $INST_SCRIPTS/xfce_ui.sh
ADD ./src/common/xfce/ $HOME/

## configure startup
RUN $INST_SCRIPTS/libnss_wrapper.sh
ADD ./src/common/scripts $STARTUPDIR
RUN $INST_SCRIPTS/set_user_permission.sh $STARTUPDIR $HOME

### ZED Installation
# Setup the ZED SDK
RUN apt-get update
RUN apt-get install lsb-release wget less udev sudo apt-transport-https -y
RUN wget -O ZED_SDK_Linux_Ubuntu16.run https://download.stereolabs.com/zedsdk/2.6/ubuntu 
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | sudo debconf-set-selections
#switch to user to install ros env
USER $USER
RUN chmod +x ZED_SDK_Linux_Ubuntu16.run ; ./ZED_SDK_Linux_Ubuntu16.run silent

# Install some other packages
USER root
RUN apt-get install -y cmake usbutils

### ROS Installation
# Install other utilities
RUN apt-get update && \
    apt-get install -y vim \
    tmux \
    git

# Install ROS
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu xenial main" > \
                /etc/apt/sources.list.d/ros-latest.list' && \
    apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116 && \
    apt-get update && apt-get install -y ros-kinetic-desktop && \
    apt-get install -y python-rosinstall && \
    rosdep init

# Setup ROS
USER $USER
RUN rosdep fix-permissions && rosdep update
RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"

###Tensorflow Installation
# Configure environment
ENV CONDA_DIR /opt/miniconda
ENV HOME /home/$USER

# Basic setups
EXPOSE 8888
EXPOSE 6006
EXPOSE 4567

# Install pip
USER root
RUN apt-get install -y wget python-pip python-dev libgtk2.0-0 unzip libblas-dev liblapack-dev libhdf5-dev && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py

# Install conda
# RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -q -O /tmp/miniconda.sh && \
#     bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
#     rm /tmp/miniconda.sh && \
#     chown $USER $CONDA_DIR -R

# # Switch to local user
# USER $USER
# ENV PATH $CONDA_DIR/bin:$PATH
# WORKDIR $HOME

# RUN conda install -y python=2.7
# # prepare default python 2.7 environment
USER root
RUN pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.11.0-cp27-none-linux_x86_64.whl && \
    pip install jupyter keras==2.2.4 matplotlib pandas scipy cprint h5py termcolor testresources

### Switch to user to install additional software
USER $USER

ENTRYPOINT ["/dockerstartup/vnc_startup.sh"]
CMD [sh -c "jupyter notebook --ip=* --no-browser --allow-root"]
CMD ["--wait"]


# RUN pip install --upgrade pip && \
#     pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.11.0-cp27-none-linux_x86_64.whl && \
#     pip install h5py jupyter keras matplotlib pandas sklearn&& \
#     conda install -y -c menpo opencv3&& \
#     conda install -y seaborn
