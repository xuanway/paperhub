# RS-Infer: A Fast and Secure LLM Inference System for Mobile Devices with Recallable Resource Isolation

**中文标题**：RS-Infer：面向移动设备的、具备可回收资源隔离的快速安全 LLM 推理系统

**所属 Session**：[Session 26: LLM Inference III](index.md) · [ATC 2026](../index.md)

**作者**：Yinpeng Wu (Shanghai Jiao Tong University), Yitong Cheng (Shanghai Jiao Tong University), Lixiang Wang (Shanghai Jiao Tong University), Jinyu Gu (Shanghai Jiao Tong University), Zhichao Hua (Shanghai Jiao Tong University), Yubin Xia (Shanghai Jiao Tong University)

## 英文摘要
The adoption of device-side Large Language Models (LLMs) has grown rapidly, offering stronger privacy and higher availability than their cloud-side counterparts. Attackers may compromise the OS kernel to steal valuable model weights and user data. ARM TrustZone is the de facto hardware-based isolation technology on mobile devices, used to protect sensitive applications from a compromised OS. However, protecting LLM inference with TrustZone incurs significant overhead for both the secure inference and the normal applications, due to two challenges: the inflexible resource isolation and the inefficient secure resource management. To address these challenges, this paper presents RS-Infer, a fast and secure LLM inference system for mobile devices. The key idea is to decouple the access permission from the management permission of secure resources, so that the normal-world OS cannot access them but can still manage them as usual. First, RS-Infer introduces a Recallable Resource Isolation mechanism to construct Recallable Secure Memory (RS-Memory) and a Recallable Secure NPU (RS-NPU). They can only be accessed by the secure world, but can be efficiently allocated and reclaimed by the normal-world OS. Based on them, RS-Infer further introduces the RS-Infer Framework to run secure LLM inference in the secure world. It cooperates with the normal-world OS to manage secure memory. We evaluate an RS-Infer prototype against a TrustZone-based Strawman and its optimized variant. RS-Infer achieves average TTFT speedups of 8.00× and 2.19×, respectively, and average response latency speedups of 14.15× and 2.94× for multi-model agent workflows.

## 中文摘要
端侧大语言模型（LLM）的采用迅速增长，相比云端对应方案，它提供更强的隐私性与更高的可用性。攻击者可能攻陷操作系统内核，以窃取有价值的模型权重和用户数据。ARM TrustZone 是移动设备上事实上的基于硬件的隔离技术，用于保护敏感应用免受已被攻陷的操作系统的侵害。然而，由于两项挑战——不灵活的资源隔离以及低效的安全资源管理——用 TrustZone 保护 LLM 推理会同时给安全推理和普通应用带来显著开销。为应对这些挑战，本文提出 RS-Infer，一个面向移动设备的快速、安全的 LLM 推理系统。其核心思想是将安全资源的访问权限与管理权限解耦，使得普通世界的操作系统无法访问这些资源，但仍能像往常一样管理它们。首先，RS-Infer 引入可回收资源隔离机制，构建可回收安全内存（RS-Memory）和可回收安全 NPU（RS-NPU）。它们只能由安全世界访问，但可被普通世界的操作系统高效分配与回收。在此基础上，RS-Infer 进一步引入 RS-Infer 框架，在安全世界中运行安全的 LLM 推理，并与普通世界的操作系统协作管理安全内存。我们针对基于 TrustZone 的 Strawman 方案及其优化变体评估了 RS-Infer 原型。在多模型智能体工作流中，RS-Infer 分别实现平均 TTFT 加速 8.00× 和 2.19×，平均响应延迟加速 14.15× 和 2.94×。

## 英文关键词
Large language model inference, Mobile computing, Arm TrustZone, Memory management

## 中文关键词
大语言模型推理，移动计算，Arm TrustZone，内存管理

[返回 Session 26](index.md) · [返回 ATC 2026](../index.md)
