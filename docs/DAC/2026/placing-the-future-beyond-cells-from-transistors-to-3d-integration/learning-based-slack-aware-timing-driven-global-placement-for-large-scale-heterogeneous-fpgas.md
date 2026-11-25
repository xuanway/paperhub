Learning-Based Slack-Aware Timing-Driven Global Placement for Large-Scale Heterogeneous FPGAs
Authors：
[Yi Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=95299066169654331961)，[Shikai Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=3574330272611439529)，[Huijiang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3555311105260957475)，[Ning Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1334060446430045422)，[Zhixiong Di](https://63dac.conference-program.com/?post_type=page&p=15&uid=136343)，[Xiaochen Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=18909643294039381)，[He Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5142727456254908165)

## 中文标题

面向大规模异构 FPGA 的基于学习的松弛感知时序驱动全局布局

## 英文摘要

Timing optimization during placement is key to circuit timing closure. As design scales increase, dense interconnections among heterogeneous instances introduce severe Resistive-Capacitive effects, weaken the linear relationship between delay and wirelength. This leaves existing placers unable to handle delay variations from dense heterogeneous interconnects and limits their scalability across designs of different sizes. To address these challenges, we propose LS-Placer, a timing-driven global placement framework with slack awareness. Specifically, LS-Placer employs a graph-based representation to jointly model net and logic delays and integrates the learned timing model into a dynamic-programming-like global placement flow. During global placement, pin-level slack-guided timing terms are incorporated into a quadratic objective function for joint wirelength-timing optimization. In addition, LS-Placer employs an adaptive weighting scheme for timing terms to promote stable improvements in both total timing slack and wirelength. Experiments on seven large-scale open-source FPGA designs (100K–700K instances) show that, on average, LS-Placer improves Worst Negative Slack and Total Negative Slack by ∼11% and ∼19%, respectively, over state-of-the-art placers, and achieves 3% shorter Critical Path Delay than Vivado 2021.2. The source code is available at https://anonymous.4open.science/r/LS-Placer-2D06.

## 中文摘要

布局阶段的时序优化是电路时序收敛的关键。随着设计规模增大，异构实例之间的密集互连引入严重的阻容效应，削弱了延迟与线长之间的线性关系。这使现有布局器无法处理密集异构互连带来的延迟变化，也限制了其在不同规模设计上的可扩展性。为应对这些挑战，我们提出 LS-Placer，一种具备松弛感知能力的时序驱动全局布局框架。具体而言，LS-Placer 采用基于图的表示联合建模线网与逻辑延迟，并将学习得到的时序模型集成到类动态规划的全局布局流程中。在全局布局过程中，引脚级松弛引导的时序项被纳入二次目标函数，以实现线长与时序的联合优化。此外，LS-Placer 对时序项采用自适应加权方案，以促进总时序松弛与线长的稳定改善。在七个大规模开源 FPGA 设计（10 万至 70 万实例）上的实验表明，相较最先进布局器，LS-Placer 平均将最差负松弛（WNS）与总负松弛（TNS）分别改善约 11% 与 19%，且关键路径延迟较 Vivado 2021.2 缩短 3%。源码见 https://anonymous.4open.science/r/LS-Placer-2D06。

## 英文关键词

FPGA, Timing Driven, Analytical Placement

## 中文关键词

FPGA、时序驱动、解析布局
