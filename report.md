This report contains additional details on the project.

### Learning Algorithm

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

For this project, I solved the configuration which contains 20 identical agents, each with its own copy of the environment. This version is useful for algorithms like PPO, A3C, and D4PG that use multiple (non-interacting, parallel) copies of the same agent to distribute the task of gathering experience.

The barrier for solving this version of the environment is to take into account the presence of many agents. In particular, your agents must get an average score of +30 (over 100 consecutive episodes, and over all agents). Specifically,

After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 20 (potentially different) scores. We then take the average of these 20 scores. This yields an average score for each episode (where the average is over all 20 agents).

The learning algorith for this project was Deep Deterministic Policy Gradient for a Continuous Action-space. This work was introduced in the following paper: 

Continuous control with deep reinforcement learning
Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval Tassa, David Silver, Daan Wierstra
https://arxiv.org/abs/1509.02971

The team above summarized their work in this way:

"We adapt the ideas underlying the success of Deep Q-Learning to the continuous action domain. We present an actor-critic, model-free algorithm based on the deterministic policy gradient that can operate over continuous action spaces. Using the same learning algorithm, network architecture and hyper-parameters, our algorithm robustly solves more than 20 simulated physics tasks, including classic problems such as cartpole swing-up, dexterous manipulation, legged locomotion and car driving. Our algorithm is able to find policies whose performance is competitive with those found by a planning algorithm with full access to the dynamics of the domain and its derivatives. We further demonstrate that for many of the tasks the algorithm can learn policies end-to-end: directly from raw pixel inputs."

### Plot of Rewards

![Plot of Rewards](https://github.com/bohoro/ContinuousControl/blob/master/plot/Plot.jpeg?raw=true)

Problem solved in Episode 97 with an Average Score: 30.37

The agent is able to receive an average reward (over 100 episodes, and over all 20 agents) of at least +30.

### Ideas for Future Work

Ideas for future work include:

* Evolving the current work:
    * Utilizing the recent Distributed Distributional Deterministic Policy Gradients (D4PG) algorithm (https://openreview.net/forum?id=SyZipzbCb) as another method for adapting DDPG for this continuous control problem.
* Utilizing other algorthm approches such as:
    * Proximal Policy Optimization Algorithms (https://arxiv.org/pdf/1707.06347.pdf)
    * Asynchronous Methods for Deep Reinforcement Learning (https://arxiv.org/pdf/1602.01783.pdf)
    
    
