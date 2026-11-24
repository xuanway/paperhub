# Resi-DINC: Resilient Distributed In-Network Computing with Closed-Loop Runtime Assurance

**中文标题**：Resi-DINC：具有闭环运行时保障的弹性分布式网内计算

**所属 Session**：[Session 8: Data Center Networking](index.md) · [ATC 2026](../index.md)

**作者**：Xiaoying Huang (Pengcheng Laboratory), Kun Huang (Pengcheng Laboratory), Mengqian Pang (Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences; Pengcheng Laboratory; University of Chinese Academy of Sciences)

## 英文摘要
Distributed In-Network Computing (DINC) deploys application logic across programmable network devices, but existing frameworks lack integrated Day-2 operational assurance for runtime disturbances such as device/link failures and service-level agreement (SLA) violations. We present Resi-DINC, an automated closed-loop framework built around an integer linear programming (ILP)-guided multi-expert architecture. An ILP oracle generates expert demonstrations for two-phase deep reinforcement learning (DRL) training—general pre-training and deployment-specific fine-tuning—yielding scenario-specific experts for fault recovery and SLA assurance. At runtime, detected anomalies trigger the corresponding expert, which produces a re-planning decision within milliseconds and drives automated data-plane re-deployment. We evaluate our prototype on Fat-Tree and wide-area network (WAN) backbone topologies. Resi-DINC achieves near-ILP decision quality, with average optimality gaps under 8% for fault recovery and under 7% for SLA assurance, while reducing closed-loop response time by over 480× and over 150×, respectively, compared with the manual baseline at the largest evaluated timing scale for each scenario.

## 中文摘要
分布式网内计算（DINC）将应用逻辑部署到可编程网络设备上，但现有框架缺乏针对设备/链路故障和违反服务等级协议（SLA）等运行时扰动的集成式 Day-2 运维保障。我们提出 Resi-DINC，一个围绕整数线性规划（ILP）引导的多专家架构构建的自动化闭环框架。ILP 预言机为两阶段深度强化学习（DRL）训练——通用预训练与面向部署的微调——生成专家示范，从而产生面向具体场景的故障恢复专家与 SLA 保障专家。在运行时，检测到的异常会触发相应的专家，该专家在毫秒级时间内给出重规划决策，并驱动自动化的数据面重新部署。我们在 Fat-Tree 和广域网（WAN）骨干拓扑上评估了原型。Resi-DINC 达到接近 ILP 的决策质量，故障恢复的平均最优性差距低于 8%，SLA 保障的平均最优性差距低于 7%，同时在各场景所评估的最大时间尺度上，相较人工基线分别将闭环响应时间缩短 480× 以上和 150× 以上。

## 英文关键词
Distributed In-Network Computing, Runtime Assurance, Deep Reinforcement Learning

## 中文关键词
分布式网内计算，运行时保障，深度强化学习

[返回 Session 8](index.md) · [返回 ATC 2026](../index.md)
