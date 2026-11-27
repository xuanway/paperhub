RM-CIMA: An Analog Computing-in-Memory Accelerator for a Robust UAV Trajectory Tracking Framework
Authors：
[Pingdan Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=84008097891551243931)，[Yiliu Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=36962322762500150621)，[Bingqian Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=24395242378815130171)，[Sichun Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=50182337597276595731)，[Wanli Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=432143)，[Hong Qinghui](https://63dac.conference-program.com/?post_type=page&p=15&uid=1542478120166475813)

## 中文标题

RM-CIMA：面向鲁棒无人机轨迹跟踪框架的模拟存内计算加速器

## 英文摘要

Unmanned aerial vehicles (UAVs) are widely used in automation, demanding high robustness, real-time performance, and energy efficiency for trajectory tracking. However, when existing control frameworks are deployed on traditional architectures, their computational latency results in excessively low control frequencies, failing to respond promptly to fast, sudden disturbances in the real world. To address these challenges, we propose a framework for algorithm-hardware co-design. Algorithmically, we integrate reinforcement learning (RL) with model predictive controller (MPC), endowing the controller with real-time online learning capabilities to adapt to unknown models and disturbances. Hardware-wise, we design a dedicated analog compute-in-memory (ACIM) accelerator, RM-CIMA, which maps both the online learning of RL and the optimization solving of MPC entirely to the analog domain. In the experiment, RM-CIMA endows the UAV with an excellent ability to counter fast dynamic disturbances. Specifically, under sudden strong wind disturbances, its recovery times are improved by 7.9× compared to the traditional NMPC scheme. Furthermore, compared to traditional architectures, its computational latency and energy consumption are reduced by 2995.6× and 983.1×, respectively.

## 中文摘要

无人机（UAV）在自动化领域得到广泛应用，其轨迹跟踪对高鲁棒性、实时性与能效提出了很高要求。然而，当现有控制框架部署于传统架构时，其计算延迟导致控制频率过低，无法及时响应现实世界中快速突发的扰动。为应对这些挑战，我们提出一种算法—硬件协同设计的框架。在算法层面，我们将强化学习（RL）与模型预测控制器（MPC）相融合，赋予控制器实时在线学习能力，以适应未知模型与扰动。在硬件层面，我们设计专用模拟存内计算（ACIM）加速器 RM-CIMA，将强化学习的在线学习与 MPC 的优化求解全部映射到模拟域。实验表明，RM-CIMA 使无人机具备优异的抵御快速动态扰动的能力。具体而言，在突发强风扰动下，其恢复时间相较传统 NMPC 方案提升 7.9×。此外，与传统架构相比，其计算延迟与能耗分别降低 2995.6× 和 983.1×。

## 英文关键词

Analog CIM, RRAM, UAV trajectory, Circuit design

## 中文关键词

模拟存内计算、RRAM、无人机轨迹、电路设计
