Throughput-Oriented Speculative Decoding via Intra-Device Parallelism
Authors：
[Zehua Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=3639264009112842391)，[Zijian Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6574881181297649131)，[Zhanhong Tan](https://63dac.conference-program.com/?post_type=page&p=15&uid=90327739536785674531)，[Fei Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=8926230268958860053)，[Kaisheng Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=908243)

## 中文标题

面向吞吐优化的设备内并行推测解码

## 英文摘要

Large Language Model (LLM) serving is crucial for applications like chatbots and code assistants, yet its implementation remains bottlenecked by low hardware utilization. Speculative decoding improves effective throughput, but still suffers from suboptimal resource partitioning. We introduce SmoothSpec, a speculative decoding system designed to maximize serving throughput by fully leveraging intra-device parallelism. SmoothSpec deploys draft and target models with the same parallelism configurations but allocates asymmetric compute resources at runtime. We design a novel scheduling strategy that dynamically adjusts both the draft parameters for the next step and the resource allocation ratio between the two models, based on the generation quality of draft tokens. We implement SmoothSpec on a single-node LLM serving system and demonstrate its effectiveness across diverse workloads.

## 中文摘要

大语言模型（LLM）推理服务对聊天机器人、代码助手等应用至关重要，但其实现仍受限于硬件利用率偏低。推测解码可提升有效吞吐，却仍存在资源划分次优的问题。我们提出 SmoothSpec，一种旨在通过充分利用设备内并行来最大化服务吞吐的推测解码系统。SmoothSpec 以相同的并行配置部署草稿模型与目标模型，但在运行时为二者分配非对称的计算资源。我们设计了一种新颖的调度策略，依据草稿 token 的生成质量，动态调整下一步的草稿参数以及两个模型之间的资源分配比例。我们在单节点 LLM 服务系统上实现了 SmoothSpec，并在多种工作负载上验证了其有效性。

## 英文关键词

AI and Machine Learning, Architecture & System Design, Cloud Computing, Compute/Storage Infrastructure

## 中文关键词

人工智能与机器学习、体系结构与系统设计、云计算、计算/存储基础设施
