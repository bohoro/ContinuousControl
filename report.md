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

#### Additional Details About the Learning Algorithm

Here are some additional details of the application of the algorithm to this project.
* During training the overall simulation is limted to 500 episodes of a maximum of 1000 time steps.  During each step the states, actions, rewards, next_states, and dones are added to a fixed size replay buffer.
* The project contains both a critic and and actor models.
    * The actor (policy) network maps states to actions.
    * The critic (value) network that maps (state, action) pairs to Q-values.
* In this sense the actor controls our actions and the critic can estimate how well we did.
* In this project, the weights are updated in the learn function after 20 stpes.  The learn function is called 10 times at this point so we see 10 weight updates (soft update) every 20 steps.
* Both the actor and critic have regular and target weights, the learn function mixes in the regualr network weights to the target weights. See the call to soft update model parameters using θ_target = τ*θ_local + (1 - τ)*θ_target.  This strategy leads to faster convergence.   

The following hyperparameters were used for the project:

```
BUFFER_SIZE = int(1e5)  # replay buffer size - orginal was 1e5
BATCH_SIZE = 256  # minibatch size - orginally was 128
GAMMA = 0.99  # discount factor
TAU = 1e-2  # for soft update of target parameters - orgial was 1e-2
LR_ACTOR = .00017  # learning rate of the actor - orgial was 1e-4
LR_CRITIC = .0015  # learning rate of the critic - orgial was 1e-2
WEIGHT_DECAY = 0  # L2 weight decay
```

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
    
    
