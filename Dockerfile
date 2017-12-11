FROM nvidia/cuda:cudnn

MAINTAINER Henry "henry2423@gmail.com"

# Configure environment
ENV CONDA_DIR /opt/miniconda
ENV USER dockeruser
ENV USERGROUP 1000
ENV HOME /home/$USER

# TensorBoard
EXPOSE 6006

# Flask Server
EXPOSE 4567

# Basic setups
# Jupyter
EXPOSE 8888
RUN apt-get -y update && \
    apt-get install -y wget python-pip python-dev libgtk2.0-0 unzip

# Create local user
RUN useradd -m -s /bin/bash -N -u $USERGROUP $USER

# Install conda
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -q -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh && \
    chown $USER $CONDA_DIR -R

# Switch to local user
USER $USER
ENV PATH $CONDA_DIR/bin:$PATH
WORKDIR $HOME

# prepare default python 3.5 environment
RUN conda install -y python=3.5.2 && \
    pip install --upgrade pip && \
    pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp35-cp35m-linux_x86_64.whl && \
    pip install h5py jupyter keras moviepy pandas pillow sklearn flask-socketio eventlet && \
    conda install -y -c menpo opencv3=3.1.0 && \
    conda install -y matplotlib=1.5.3 && \
    conda install -y seaborn

