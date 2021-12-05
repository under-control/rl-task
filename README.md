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

Note: if you are on windows run docker commands on PowerShell (in order to use `$(pwd)` instead of typing your path)

*  Run docker with 'FrozenLake8x8-v1' env for 100000 total learning timesteps:

```commandline
docker run -it --rm  --network host --ipc=host --name rl-rask --mount src=$(pwd),target=/root/code/,type=bind rl-task bash -c "python /root/code/main.py"
```

### Other options


[Example] Run docker with 'CarRacing-v0' env for 1000000 total learning timesteps :

```commandline
docker run -it --rm --network host --ipc=host --name rl-rask --mount src=$(pwd),target=/root/code/,type=bind rl-task bash -c "python /root/code/main.py -e 'CarRacing-v0' -s 1000000"
```

[Example] You can also get inside docker:

```commandline
docker run -it --rm --network host --ipc=host --name rl-rask --mount src=$(pwd),target=/root/code/,type=bind rl-task bash
```
And make experiments there:
```commandline
python /root/code/main.py -e 'CarRacing-v0' -s 1000000
```


[Optionally] See results on tensorboard (`examples` folder contains previous runs performed by two above command)
```commandline
tensorboard --logdir . --port 6006
```


