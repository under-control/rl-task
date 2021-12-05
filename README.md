### To reproduce results:

*  Clone repository and get into it

```commandline
git clone https://github.com/under-control/rl-task.git
cd rl-task
```

*  Build docker:

```commandline
docker build -t rl-task .
```

*  Run docker with default parameters - 'FrozenLake8x8-v1' env for 100000 total learning timesteps:

```commandline
docker run -it --rm  --network host --ipc=host --name rl-rask --mount src=$(pwd),target=/root/code/,type=bind rl-task bash -c "python /root/code/main.py"
```

Note: if you are on windows run docker commands on PowerShell (in order to use `$(pwd)` instead of typing your path)

### Other options:


Run docker with parameters for 'CarRacing-v0' env with 1000000 total learning timesteps :

```commandline
docker run -it --rm --network host --ipc=host --name rl-rask --mount src=$(pwd),target=/root/code/,type=bind rl-task bash -c "python /root/code/main.py -e 'CarRacing-v0' -s 1000000"
```

You can also get inside docker:

```commandline
docker run -it --rm --network host --ipc=host --name rl-rask --mount src=$(pwd),target=/root/code/,type=bind rl-task bash
```
And make experiments while being inside:
```commandline
python /root/code/main.py -e 'CarRacing-v0' -s 1000000
```


See results on tensorboard (`examples` folder contains run on default parameters)
```commandline
tensorboard --logdir exp --port 6006
```


