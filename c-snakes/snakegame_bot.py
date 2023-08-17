import gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# Initialize the gym environment
env = gym.make('Snakes-v0')

# Wrap the environment in a vectorized wrapper
vec_env = make_vec_env(env, n_envs=1)

# Define the PPO agent
model = PPO(MlpPolicy, vec_env)

# Train the agent
model.learn(total_timesteps=10000)

# Save the trained agent
model.save("snakes_agent")
