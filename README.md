# ContinuousControl

Continuous Control, controlling a double-jointed arm to reach target locations using reinforcement learning.

##### Watch the trained agent in action.

The trained agent is controlling a double-jointed arm to reach target locations using reinforcement learning.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/IvAdnRBBOrM/0.jpg)](https://www.youtube.com/watch?v=IvAdnRBBOrM "Click to Play")

Click the image above to play the video of a trained agent.

# Project Details

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to the position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

For this project, I solved the configuration which contains 20 identical agents, each with its own copy of the environment.
This version is useful for algorithms like PPO, A3C, and D4PG that use multiple (non-interacting, parallel) copies of the same agent to distribute the task of gathering experience.

The barrier for solving this version of the environment is to take into account the presence of many agents. In particular, your agents must get an average score of +30 (over 100 consecutive episodes, and over all agents). Specifically,

After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 20 (potentially different) scores. We then take the average of these 20 scores.
This yields an average score for each episode (where the average is over all 20 agents).

# Getting Started

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
2. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.
	```bash
	git clone https://github.com/bohoro/ContinuousControl.git
	cd ContinuousControl/python
	pip install .
	```
3. Download the environment from one of the links below.  You need only select the environment that matches your operating system:

    - **_Version 1: One (1) Agent_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)

    - **_Version 2: Twenty (20) Agents_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux_NoVis.zip) (version 1) or [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux_NoVis.zip) (version 2) to obtain the "headless" version of the environment.  You will **not** be able to watch the agent without enabling a virtual screen, but you will be able to train the agent.  (_To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above._)

2. Place the file in the DRLND GitHub repository, in the `continuous-control/` folder, and unzip (or decompress) the file. 

# Instructions

##### Training the agent

```python continuous_control.py```

Output will contain

```
2018-11-14 22:04:43.691891 Training started
2018-11-14 22:05:58.591721 Episode 0	Average Score: 0.62
2018-11-14 22:18:33.173686 Episode 10	Average Score: 8.52
2018-11-14 22:31:04.626603 Episode 20	Average Score: 26.58
2018-11-14 22:43:36.006260 Episode 30	Average Score: 19.64
2018-11-14 22:56:10.468169 Episode 40	Average Score: 22.99
2018-11-14 23:08:44.066877 Episode 50	Average Score: 21.27
2018-11-14 23:21:18.404145 Episode 60	Average Score: 19.38
2018-11-14 23:33:48.686031 Episode 70	Average Score: 20.29
2018-11-14 23:46:20.157513 Episode 80	Average Score: 20.98
2018-11-14 23:58:52.266138 Episode 90	Average Score: 27.89
Problem solved in Episode 97 with an Average Score: 30.37
Saving agents!!!!
Training Complete
```

##### To Watch a trained agent

```python run_trained_agent.py```
