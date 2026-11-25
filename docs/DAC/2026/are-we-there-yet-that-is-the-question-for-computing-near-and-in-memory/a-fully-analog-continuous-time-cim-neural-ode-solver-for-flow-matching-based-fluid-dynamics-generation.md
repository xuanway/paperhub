A Fully Analog Continuous-Time CIM Neural ODE Solver for Flow-Matching-Based Fluid Dynamics Generation
Authors：
[Songqi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2107628920399826662)，[Meng Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5285965486134251328)，[Jichang Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=16682813210084336441)，[Zhexu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=53893619529871271331)，[Hegan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=72165605876925723211)，[Sishuo Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=841596205463591036)，[Xinyuan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=00053832969834011171)，[Kwun Hang WONG](https://63dac.conference-program.com/?post_type=page&p=15&uid=1289220059784204768)，[Ning Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=14119393813058012901)，[Yi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=0115851161869105479)，[Zhongrui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=93538193207214203841)，[Han Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0699690152643758866)

## 中文标题

面向基于流匹配的流体动力学生成的全模拟连续时间 CIM 神经 ODE 求解器

## 英文摘要

The generation of fluid-dynamics fields is essential for understanding complex nonlinear systems and enabling real-time scientific computing. Conventional computational fluid dynamics pipelines rely on finite-element or finite-volume solvers on von Neumann architectures, which discretize continuous physical evolution into many iterative updates, leading to prohibitive latency and energy consumption. Inspired by neural dynamical systems in the brain, we propose a biologically inspired continuous-time hardware–software co-design framework for flow-matching– based turbulent-flow generation. (1) The flow-matching model adopts an MLP-Mixer architecture that emulates cortical-style information integration and hierarchical signal mixing, providing a compact backbone that naturally aligns with closed-loop analog computation. (2) A fully analog continuous-time RRAM CIM neural ordinary differential equation (ODE) solver is developed to physically realize neural-like continuous-time latent dynamics, enabling high-speed and low-power flow generation. (3) Noise-aware training and decoder retraining are jointly introduced to ensure robust generation quality in the presence of RRAM read/write noise. Experiments on three turbulent-flow datasets show that the MLP-Mixer backbone matches convolutional and attention-based flow-matching models in velocity-field accuracy while mapping efficiently to CIM hardware, and that the proposed analog ODE solver reduces energy consumption by 98.24% and latency by 99.99% compared with an NVIDIA A100 GPU, while maintaining stable generation fidelity under realistic RRAM read/write noise. This work establishes a new paradigm for high-speed, energy-efficient physical process generation and scientific AI acceleration using neuromorphic continuous-time CIM computing.

## 中文摘要

流体动力学场的生成对于理解复杂非线性系统并实现实时科学计算至关重要。传统计算流体动力学流程依赖冯·诺依曼架构上的有限元或有限体积求解器，将连续物理演化离散为大量迭代更新，导致难以承受的延迟与能耗。受大脑中神经动力系统的启发，我们提出一个受生物启发的连续时间软硬件协同设计框架，用于基于流匹配的湍流生成。(1) 流匹配模型采用 MLP-Mixer 架构，模拟皮层式信息整合与分层信号混合，提供了与闭环模拟计算天然契合的紧凑骨干网络。(2) 开发了全模拟连续时间 RRAM CIM 神经常微分方程（ODE）求解器，以物理方式实现类神经的连续时间潜动力学，从而实现高速、低功耗的流场生成。(3) 联合引入噪声感知训练与解码器重训练，以确保在存在 RRAM 读写噪声时仍具稳健的生成质量。在三个湍流数据集上的实验表明，MLP-Mixer 骨干在速度场精度上与卷积和基于注意力的流匹配模型相当，同时能高效映射到 CIM 硬件；所提出的模拟 ODE 求解器相比 NVIDIA A100 GPU 将能耗降低 98.24%、延迟降低 99.99%，同时在真实 RRAM 读写噪声下保持稳定的生成保真度。本工作利用神经形态连续时间 CIM 计算，为高速、高能效的物理过程生成与科学 AI 加速建立了新范式。

## 英文关键词

Generative Fluid Dynamics, Turbulent Flow, Neural Ordinary Differential Equation Solver, MLP-Mixer, Compute-in-Memory

## 中文关键词

生成式流体动力学、湍流、神经常微分方程求解器、MLP-Mixer、存内计算
