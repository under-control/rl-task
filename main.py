import argparse
from pathlib import Path
from datetime import datetime

import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines import PPO2

LOG_DIR = 'exp'

parser = argparse.ArgumentParser(description='rl task')
parser.add_argument('-e', '--env-name', default='FrozenLake8x8-v1')  # 'CarRacing-v0'
parser.add_argument('-s', '--total-timesteps', default=200000, type=int)
args = vars(parser.parse_args())

ENV_NAME = args['env_name']
TOTAL_TIMESTEPS = args['total_timesteps']

BOX2D_ENV_NAMES = [
    'BipedalWalker-v2', 'BipedalWalkerHardcore-v2',
    'CarRacing-v0',
    'LunarLander-v2', 'LunarLanderContinuous-v2'
]

env = gym.make(ENV_NAME)

if env.spec.id in BOX2D_ENV_NAMES:
    IS_BOX2D = True
    from pyvirtualdisplay import Display
    display = Display(visible=False, size=(1400, 900))
    display.start()
else:
    IS_BOX2D = False

logs_path = Path(Path(__file__).parent, LOG_DIR, env.spec.id)

model = PPO2(MlpPolicy, env, verbose=1, tensorboard_log=logs_path)

model.learn(total_timesteps=TOTAL_TIMESTEPS)

model.save(logs_path/f'{datetime.now().strftime("%Y%m%d_%H%M%S")}.model')

obs = env.reset()
for i in range(2000):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    if not IS_BOX2D:
        env.render()
