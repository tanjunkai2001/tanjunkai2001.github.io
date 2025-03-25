---
title: "Prescribed Performance Robust Approximate Optimal Tracking Control Via Stackelberg Game"
collection: publications
permalink: /publication/tan2025prescribed
date: 2025-03-07 00:00:00 +0500
venue: 'IEEE Transactions on Automation Science and Engineering'
paperurl: 'https://ieeexplore.ieee.org/document/10916718/'
doi: '10.1109/TASE.2025.3549114'
pubtype: 'journal'
image: 'IEEE Transactions on Automation Science and Engineering.jpg'
authors: 'J. Tan, S. Xue, H. Li, Z. Guo, H. Cao, D. Li'
excerpt_separator: ""
---
Real-world applications of nonlinear systems tracking control are always challenging due to the existence of uncertainties and disturbances. To design a robust optimal tracking controller for uncertain nonlinear systems with disturbances and actuator saturation, this paper investigates the prescribed performance robust optimal tracking control problem. A prescribed performance mechanism is constructed to convert the dynamics of tracking error into transformed error dynamics, which keeps the system’s operating states within specific bounds, ensuring tracking with predefined error constraints. For the optimal tracking controller design, an optimal index is established to optimize the performance of tracking control, and a robust optimal index is established to optimize the disturbance effect on the tracking error. To achieve robust optimal tracking control that minimizes both optimal and robust optimal indexes, a Stackelberg game is constructed, which provides a hierarchical game structure for the optimal controller and the worst disturbance. The robust optimal controller is approximated online using reinforcement learning techniques. An actor-critic-identifier algorithm is designed to approximate the optimal value function, optimal controller, and drifted system parameters. Lyapunov theory is utilized to analyze the closed-loop system’s stability. To demonstrate the effectiveness of the proposed robust optimal control method, two numerical simulations and a hardware experiment on a quadcopter system are conducted. The experiment results demonstrate that our method successfully achieves prescribed performance tracking control when actuators are saturated and disturbances are present.

[Download paper here](https://ieeexplore.ieee.org/document/10916718/)
[DOI](10.1109/TASE.2025.3549114)