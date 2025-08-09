---
title: "Hierarchical safe reinforcement learning control for leader-follower systems with prescribed performance"
collection: publications
permalink: /publication/tan2025hierarchical
date: 2025-10-01 00:00:00 +0500
venue: 'IEEE Transactions on Automation Science and Engineering'
paperurl: 'https://ieeexplore.ieee.org/document/11121383/'
doi: '10.1016/j.ins.2025.122117'
pubtype: 'journal'
image: '../images/IEEE Transactions on Automation Science and Engineering.jpg'
citation: 'Tan, Junkai and Xue, Shuangsi and Li, Huan and Guo, Zihang and Cao, Hui and Chen, Badong (2025). Hierarchical safe reinforcement learning control for leader-follower systems with prescribed performance. IEEE Transactions on Automation Science and Engineering.'
authors: 'J. Tan, S. Xue, H. Li, Z. Guo, H. Cao, B. Chen'
excerpt_separator: ""
---
This paper proposes a hierarchical safe reinforcement learning with prescribed performance control (HSRL-PPC) scheme to address the challenges of interconnected leader-follower systems operating in complex environments. The framework consists of two levels: at the higher level, the leader agent detects and avoids moving obstacles while planning optimal paths; at the lower level, the follower agent tracks the leader within strict prescribed performance bounds. We formulate the optimal prescribed performance safe control problem and solve it using the Hamilton-Jacobi-Bellman (HJB) equation. Due to system nonlinearity and obstacle complexity, we approximate the leader’s optimal value function using a state-following neural network that efficiently extrapolates training data to neighboring states, while employing a regular critic neural network for the follower’s value function approximation. Lyapunov stability analysis demonstrates the closed-loop system’s theoretical guarantees. Experimental results from two simulation examples and hardware tests with a quadcopter-vehicle system validate the effectiveness of the proposed approach in achieving safe navigation and precise tracking performance in dynamic environments.

[Download paper here](https://ieeexplore.ieee.org/document/11121383/)
[DOI](10.1109/TASE.2025.3596912)