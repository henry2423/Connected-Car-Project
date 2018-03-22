## Connected Car Project

### Introduction
#### This is the team project base on Udacity Self-Driving Car, aiming to create the smart city scenario with UGV and roadside monitoring.

### Environment Setup
#### How to run the docker up
```
docker run -it --rm -p (outside port):6006 -p (outside port):8888 -u root -v (mount file location):/home/dockeruser/ henry2423/carnd-term1 sh -c "jupyter notebook --ip=* --no-browser --allow-root"
```

- 6006 -> Tensorboard default port
- 8888 -> Jupyter default port 

#### How to run the bash make a fine tune
```docker exec -it (docker ID) /bin/bash```

#### How to monitor the GPU status
```watch -n 1 nvidia-smi ```

#### How to Run the Tensorboard
after using callbacks function provided by Keras, you can use

```tensorboard --logdir="Graph/"```

### Collaborators
* Joying Guo
* Danny Wang
* Michael Wu
