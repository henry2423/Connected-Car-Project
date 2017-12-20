FROM nvidia/cuda:cudnn

MAINTAINER Henry Huang "henry2423@gmail.com"

# Configure environment
ENV CONDA_DIR /opt/miniconda
ENV USER dockeruser
ENV USERGROUP 1000
ENV HOME /home/$USER

# Basic setups
EXPOSE 8888
EXPOSE 6006
EXPOSE 4567
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

RUN conda install -y python=3.5
# prepare default python 3.5 environment
RUN pip install --upgrade pip && \
    pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.3.0-cp35-cp35m-linux_x86_64.whl && \
    pip install h5py jupyter keras matplotlib moviepy pandas pillow sklearn flask-socketio eventlet && \
    conda install -y -c menpo opencv3&& \
    conda install -y seaborn
