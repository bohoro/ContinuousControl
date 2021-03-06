from unityagents import UnityEnvironment
import numpy as np
from collections import deque
import torch
from ddpg_agent import Agent
import datetime
import sys
import time

env = UnityEnvironment(file_name="Reacher.app")

# Environments contain brains which are responsible for deciding the actions of
# their associated agents. Here we check for the first brain available, and set
# it as the default brain we will be controlling from Python.
# get the default brain
brain_name = env.brain_names[0]
brain = env.brains[brain_name]

# reset the environment
env_info = env.reset(train_mode=True)[brain_name]

# Examine the State and Action Spaces
# number of agents
num_agents = len(env_info.agents)
print("Number of agents:", num_agents)

# size of each action
action_size = brain.vector_action_space_size
print("Size of each action:", action_size)

# examine the state space
states = env_info.vector_observations
cstate_size = states.shape[1]
print(
    "There are {} agents. Each observes a state with length: {}".format(
        states.shape[0], cstate_size
    )
)
print("The state for the first agent looks like:", states[0])


# Take Random Actions in the Environment
env_info = env.reset(train_mode=False)[brain_name]  # reset the environment
states = env_info.vector_observations  # get the current state (for each agent)
scores = np.zeros(num_agents)  # initialize the score (for each agent)
time.sleep(3)
for _ in range(100):
    actions = np.random.randn(
        num_agents, action_size
    )  # select an action (for each agent)
    actions = np.clip(actions, -1, 1)  # all actions between -1 and 1
    env_info = env.step(actions)[brain_name]  # send all actions to the env
    next_states = env_info.vector_observations  # get next state for each agent
    rewards = env_info.rewards  # get reward (for each agent)
    dones = env_info.local_done  # see if episode finished
    scores += env_info.rewards  # update the score (for each agent)
    states = next_states  # roll over states to next time step
    #print(actions, env_info.rewards)
    if np.any(dones):  # exit loop if episode finished
        break

print("Total score (averaged over agents) this episode: {}".format(np.mean(scores)))
