FROM tensorflow/tensorflow:1.15.2-py3

RUN apt-get update && apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev ffmpeg libsm6 libxext6 xvfb python-opengl -y

RUN pip install gym[box2d] stable-baselines pyvirtualdisplay
