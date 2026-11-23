---
title: "SpecEE: Accelerating Large Language Model Inference with Speculative Early Exiting"
description: "ISCA 2025 · Session 4A · SpecEE: 利用推测早退加速LLM推理"
tags:
  - "ISCA2025"
  - "Session 4A"
  - "LLMs"
---

# SpecEE: Accelerating Large Language Model Inference with Speculative Early Exiting

**中文标题：** SpecEE: 利用推测早退加速LLM推理

**所属 Session：** [Session 4A](index.md) · [ISCA 2025](../index.md)

**作者：** Jiaming Xu, Jiayi Pan, Yongkang Zhou, Siming Chen, Jinhao Li, Yaoxiu Lian, Junyi Wu, Guohao Dai

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730996) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Early exiting has recently emerged as a promising technique for accelerating large language models (LLMs) by effectively reduc- ing the hardware computation and memory access. In this paper, we identify that the LLM vocabulary serves as the runtime search space of the early exiting predictor and significantly influences the predictor workload (e.g., ∼20% overall inference latency with ∼3 ×104 vocabulary size in Llama2). We propose a novel para- digm using speculative models to reduce this search space, while addressing three critical challenges for further predictor optimiza- tion. (1) Time-consuming predictor with high computational complexity. Current predictor designs leverage basic models with high-dimensional input that ignore inherent data variation and GPU parallelization opportunities, resulting in∼15% overall in- ference latency. (2) Under-utilization of layer-wise predictor deployment. Current early exiting systems treat the predictor in each layer equally without considering the activation frequencies of layer-wise predictors, leading to∼20% inference overhead. (3) Exponential mapping complexity of predictor in speculative decoding. Each token in the token tree of speculative decoding is treated as an independent search space when applying the current early exiting mapping, leading to exponential mapping complexity and failing to incorporate the high-throughput benefits To address the above challenges, we present SpecEE, a fast LLM inference engine with speculative early exiting. (1) At the algo- rithm level, we propose the speculation-based lightweight pre- dictor design by exploiting the probabilistic correlation between the speculative tokens and the correct results and high parallelism of GPUs. (2) At the system level, we point out that not all layers need a predictor and design the two-level heuristic predictor scheduling engine based on skewed distribution and contextual similarity. (3) At the mapping level, we point out that different decoding methods share the same essential characteristics, and pro- pose the context-aware merged mapping for predictor with efficient GPU implementations to support speculative decoding, and form a framework for various existing orthogonal accelera- tion techniques (e.g., quantization and sparse activation) on cloud and personal computer (PC) scenarios, successfully pushing the Pareto frontier of accuracy and speedup. It is worth noting that SpecEE can be applied to any LLM by negligible training overhead in advance without affecting the model’s original parameters. Ex- tensive experiments show that SpecEE achieves 2.25×and 2.43× speedup with Llama2-7B on cloud and PC scenarios respectively. The code is open-sourced in [https://github.com/infinigence/SpecEE](https://github.com/infinigence/SpecEE)

## 中文摘要

提前退出是一种前景良好的技术，通过有效削减计算量与访存开销来加速大语言模型（LLM）推理。本文发现，LLM词表是提前退出预测器的运行时搜索空间，会显著影响预测器负载（例如Llama2在词表规模约3万时，预测器开销约占总推理延迟的20%）。本文提出一种基于推测模型的新范式，以此缩小该搜索空间，同时解决制约预测器优化的三大关键问题：
（1）预测器计算复杂度高、耗时久。现有预测器采用基础模型，输入维度很高，没有利用数据本身的变化特征与GPU并行潜力，带来约15%的总推理延迟；
（2）分层部署的预测器利用率低。现有提前退出系统对每一层的预测器同等对待，没有考虑各层预测器的激活频率，引入约20%的推理开销；
（3）推测解码下预测器映射复杂度呈指数增长。在现有提前退出映射方式下，推测解码的token树中每个token都被视作独立搜索空间，造成指数级映射复杂度，无法发挥高吞吐优势。

针对以上问题，本文提出SpecEE，一款支持推测式提前退出的高速LLM推理引擎。
（1）算法层面：利用推测token与正确结果之间的概率相关性以及GPU高并行特性，设计基于推测机制的轻量预测器；
（2）系统层面：并非所有层都需要部署预测器，基于负载偏态分布与上下文相似度，设计两级启发式预测器调度引擎；
（3）映射层面：指出不同解码方式具备共通本质特征，提出面向预测器的上下文感知合并映射方案，并在GPU上高效实现，支持推测解码；同时搭建框架，兼容各类正交加速技术（例如量化、稀疏激活），适配云端与个人电脑场景，推动精度-加速比的帕累托前沿。

值得注意的是，SpecEE仅需极小的预训练开销即可适配任意LLM，不会改动模型原有参数。大量实验表明，在Llama2-7B模型上，SpecEE在云端与PC场景下分别实现2.25倍、2.43倍加速。代码开源：https://github.com/infinigence/SpecEE

## 英文关键词

Large Language Model, Machine Learning and System, GPU

## 中文关键词

大语言模型, 机器学习与系统, GPU

## 代码与研究制品

- [代码仓库](https://github.com/infinigence/SpecEE)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730996)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2025](../index.md)
