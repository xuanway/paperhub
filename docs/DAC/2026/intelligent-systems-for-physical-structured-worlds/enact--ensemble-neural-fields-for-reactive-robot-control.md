ENACT: Ensemble Neural Fields for Reactive Robot Control
Authors：
[Hammad Omar](https://63dac.conference-program.com/?post_type=page&p=15&uid=05400526634102869341)，[Ismail Mohamed](https://63dac.conference-program.com/?post_type=page&p=15&uid=2647967438436287045)，[Mohamed Ibrahim](https://63dac.conference-program.com/?post_type=page&p=15&uid=446843)

## 中文标题

ENACT：用于反应式机器人控制的集成神经场

## 英文摘要

Tracking moving targets through clutter and occlusions demands real-time sensorimotor control that adapts to dynamic uncertainty. Model predictive control (MPC) incurs high computational cost, while reinforcement learning requires task-specific retraining. We introduce ENACT (Ensemble Neural Attractor Components for Tracking), a modular framework decomposing reactive control into coordinated Dynamic Neural Fields (DNFs). Each DNF module— attention, gating, memory, context—addresses a distinct sensorimotor primitive through continuous attractor dynamics, enabling runtime reconfiguration without retraining. We benchmark ENACT on both simulation and a Cortex-M7 microcontroller, showing up to 86% lower tracking RMS error, ∼2.8× faster disturbance-recovery times, predictable sub-millisecond control latency, and ∼9× lower SRAM footprint compared to MPC baseline.

## 中文摘要

在杂乱环境与遮挡条件下跟踪移动目标，需要能够适应动态不确定性的实时感知—运动控制。模型预测控制（MPC）的计算开销高昂，而强化学习需要针对特定任务重新训练。我们提出 ENACT（Ensemble Neural Attractor Components for Tracking，用于跟踪的集成神经吸引子组件），这是一个模块化框架，将反应式控制分解为相互协同的动态神经场（DNF）。每个 DNF 模块——注意力、门控、记忆、上下文——通过连续吸引子动力学处理一种不同的感知运动基元，从而无需重新训练即可在运行时重构。我们在仿真环境与 Cortex-M7 微控制器上对 ENACT 进行了基准测试，结果显示：与 MPC 基线相比，跟踪 RMS 误差最高降低 86%，扰动恢复时间约快 2.8×，控制时延可预测且低于 1 毫秒，SRAM 占用约降低 9×。
