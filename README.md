# CarND-Project-3
Udacity-CarND-Term1

# How to run the docker up
docker run -it --rm -p <outside port>:8888 -u root -v <mount file location>:/home/dockeruser/ henry2423/carnd-term1 sh -c "jupyter notebook --ip=* --no-browser --allow-root"


# How to run the bash make a fine tune
docker exec -it <docker ID> /bin/bash
