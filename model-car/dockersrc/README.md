# Docker container images with ROS, ZED, Xfce4 VNC Desktop, Tensorflow and Keras

This repository developed from ConSol/docker-headless-vnc-container, with provide the headless VNC environments for docker container

## Current Image Build:
* `henry2423/ros-vnc-mcar` : __Ubuntu 16.04 with `ROS Kinetic + ZED`__

  [![](https://images.microbadger.com/badges/version/henry2423/ros-vnc-mcar.svg)](https://hub.docker.com/r/henry2423/ros-vnc-mcar/) [![](https://images.microbadger.com/badges/image/henry2423/ros-vnc-mcar.svg)](https://microbadger.com/images/henry2423/ros-vnc-mcar)

## Usage
- Run command with mapping to local port `5901` (vnc protocol) and `6901` (vnc web access):

      docker run -d -p 5901:5901 -p 6901:6901 henry2423/ros-vnc-mcar

- If you want to get into the container use interactive mode `-it` and `bash`
      
      docker run -it -p 5901:5901 -p 6901:6901 henry2423/ros-vnc-mcar bash

- If you want to connect to tensorboard, run command with mapping to local port `6006`:
      
      docker run -it -p 5901:5901 -p 6901cu:6901 -p 6006:6006 henry2423/ros-vnc-mcar

- Build an image from scratch:

      docker build -t henry2423/ros-vnc-mcar .

## Connect & Control
If the container runs up, you can connect to the container throught the following 
* connect via __VNC viewer `localhost:5901`__, default password: `vncpassword`
* connect via __noVNC HTML5 full client__: [`http://localhost:6901/vnc.html`](http://localhost:6901/vnc.html), default password: `vncpassword` 
* connect via __noVNC HTML5 lite client__: [`http://localhost:6901/?password=vncpassword`](http://localhost:6901/?password=vncpassword) 
* connect to __Tensorboard__ if you do the tensorboard mapping above: [`http://localhost:6006`](http://localhost:6006)
* The default username and password in container is ros:ros

## Detail Environment setting

#### 1.1) Using root (user id `0`)
Add the `--user` flag to your docker run command:

    docker run -it --user root -p 5901:5901 henry2423/ros-vnc-mcar

#### 1.2) Using user and group id of host system
Add the `--user` flag to your docker run command (Note: uid and gui of host system may not able to map with container, which is 1000:1000. If that is the case, check with 3.1):

    docker run -it -p 5901:5901 --user $(id -u):$(id -g) henry2423/ros-vnc-ubuntu:kinetic

### 2) Override VNC and Container environment variables
The following VNC environment variables can be overwritten at the `docker run` phase to customize your desktop environment inside the container:
* `VNC_COL_DEPTH`, default: `24`
* `VNC_RESOLUTION`, default: `1920x1080`
* `VNC_PW`, default: `vncpassword`
* `USER`, default: `ros`
* `PASSWD`, default: `ros`

#### 2.1) Example: Override the VNC password
Simply overwrite the value of the environment variable `VNC_PW`. For example in
the docker run command:

    docker run -it -p 5901:5901 -p 6901:6901 -e VNC_PW=vncpassword henry2423/ros-vnc-mcar

#### 2.2) Example: Override the VNC resolution
Simply overwrite the value of the environment variable `VNC_RESOLUTION`. For example in
the docker run command:

    docker run -it -p 5901:5901 -p 6901:6901 -e VNC_RESOLUTION=800x600 henry2423/ros-vnc-mcar

### 3.1) Example: Mounting local directory to conatiner
You should run with following environment variable in order to mapping same UID, GID with container, and retrieve R/W permission in container:

      docker run -it -p 5901:5901 \
        --user $(id -u):$(id -g) \
        --env "UID=`id -u $who`" \
        --env "GID=`id -g $who`" \
        --volume /home/ros/Desktop:/home/ros/Desktop:rw \
        henry2423/ros-vnc-ubuntu:kinetic


## Contributors

* [ConSol](https://github.com/ConSol/docker-headless-vnc-container) - developed the ConSol/docker-headless-vnc-container
