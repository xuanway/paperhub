---
title: "Hardwired-Neuron Language Processing Units as General-Purpose Cognitive Substrates"
description: "ASPLOS 2026 · Session 6A · 硬连线神经元语言处理单元作为通用认知基底"
tags:
  - "ASPLOS2026"
  - "Session 6A"
  - "Neural Network Acceleration"
---

# Hardwired-Neuron Language Processing Units as General-Purpose Cognitive Substrates

**中文标题：** 硬连线神经元语言处理单元作为通用认知基底

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yang Liu (Institute of Computing Technology, Chinese Academy of Sciences), Yi Chen (University of Science and Technology of China), Yongwei Zhao (Institute of Computing Technology, Chinese Academy of Sciences), Yifan Hao (Institute of Computing Technology, Chinese Academy of Sciences), Zifu Zheng (Institute of Computing Technology, Chinese Academy of Sciences), Weihao Kong (Institute of Computing Technology, Chinese Academy of Sciences), Zhangmai Li (University of Science and Technology of China), Dongchen Jiang (Institute of Computing Technology, Chinese Academy of Sciences), Ruiyang Xia (Institute of Computing Technology, Chinese Academy of Sciences), Zhihong Ma (Institute of Computing Technology, Chinese Academy of Sciences), Zisheng Liu (Institute of Computing Technology, Chinese Academy of Sciences), Zhaoyong Wan (Institute of Computing Technology, Chinese Academy of Sciences), Yunqi Lu (Institute of Computing Technology, Chinese Academy of Sciences), Ximing Liu (Institute of Computing Technology, Chinese Academy of Sciences), Hongrui Guo (Institute of Computing Technology, Chinese Academy of Sciences), Zhihao Yang (Institute of Software, Chinese Academy of Sciences), Zhe Wang (Institute of Computing Technology, Chinese Academy of Sciences), Tianrui Ma (Institute of Computing Technology, Chinese Academy of Sciences), Mo Zou (Institute of Computing Technology, Chinese Academy of Sciences), Rui Zhang (Institute of Computing Technology, Chinese Academy of Sciences), Ling Li (Institute of Software, Chinese Academy of Sciences), Xing Hu (Institute of Computing Technology, Chinese Academy of Sciences), Zidong Du (Institute of Computing Technology, Chinese Academy of Sciences), Zhiwei Xu (Institute of Computing Technology, Chinese Academy of Sciences), Qi Guo (Institute of Computing Technology, Chinese Academy of Sciences), Tiashi Chen (Cambricon Technologies), Yunji Chen (Institute of Computing Technology, Chinese Academy of Sciences)

**单位：** Institute of Computing Technology, Chinese Academy of Sciences；University of Science and Technology of China；Institute of Software, Chinese Academy of Sciences；Cambricon Technologies

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790169) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The rapid advancement of Large Language Models (LLMs) has established language as a core general-purpose cognitive substrate, driving the demand for specialized Language Processing Units (LPUs) tailored for LLM inference. To overcome the growing energy consumption of LLM inference systems, this paper proposes a Hardwired-Neurons Language Processing Unit (HNLPU), which physically hardwires LLM weight parameters into the computational fabric, achieving several orders of magnitude computational efficiency improvement by extreme specialization. However, a significant challenge A straightforward hardwiring of gpt-oss 120 B would require fabricating photomask sets valued at over 6 billion dollars, rendering this straightforward solution economically impractical. Addressing this challenge, we propose the novel MetalEmbedding methodology. Instead of embedding weights in a 2D grid of silicon device cells, Metal-Embedding embeds weight parameters into the 3D topology of metal wires. This brings two benefits: (1) a 15× increase in density, and (2) 60 out of 70 photomask layers are homogeneous across chips, including all EUV photomasks. In total, Metal-Embedding reduced the photomask cost by 112×, bringing the NonRecurring Engineering (NRE) cost of HNLPU into an economically viable range. Experimental results show that HNLPU achieved 249,960 tokens/s (5,555×/85× that of GPU/WSE), 36 tokens/J (1,047×/283× that of GPU/WSE), 13,232 mm2 total die area, $ 59.46 M–123.5 M estimated NRE at 5 nm technology. Analysis shows that HNLPU achieved 41.7–80.4× improvement in cost-effectiveness and 357× reduction in carbon footprint compared to OpenAI-scale H100 clusters, Hardwired-Neuron Language Processing Units as General-Purpose Cognitive Substrates under an annual weight updating assumption.

## 中文摘要

大语言模型（LLMs）的快速发展已使语言成为核心的通用认知基底，推动了对专为 LLM 推理定制的专用语言处理单元（LPUs）的需求。为克服 LLM 推理系统不断增长的能耗，本文提出硬连线神经元语言处理单元（HNLPU），它将 LLM 权重参数物理地硬连线到计算结构中，通过极致的专用化实现数个数量级的计算效率提升。然而，一个重大挑战是：对 gpt-oss 120 B 进行直接硬连线将需要制造价值超过 60 亿美元的光罩套件，使这一直接方案在经济上不可行。为应对这一挑战，我们提出新颖的 MetalEmbedding 方法。Metal-Embedding 不是将权重嵌入硅器件单元的 2D 网格，而是将权重参数嵌入金属连线的 3D 拓扑中。这带来两个好处：（1）密度提升 15 倍；（2）70 层光罩中有 60 层在各芯片间是均质的，包括所有 EUV 光罩。总体而言，Metal-Embedding 将光罩成本降低 112 倍，使 HNLPU 的一次性工程（NRE）成本进入经济可行的范围。实验结果表明，HNLPU 实现了 249,960 tokens/s（为 GPU/WSE 的 5,555 倍/85 倍）、36 tokens/J（为 GPU/WSE 的 1,047 倍/283 倍）、13,232 mm2 的总裸片面积，在 5 nm 工艺下估计 NRE 为 5,946 万–1.235 亿美元。分析表明，在年度权重更新假设下，与 OpenAI 规模的 H100 集群相比，HNLPU 的成本效益提升了 41.7–80.4 倍，碳足迹降低了 357 倍——硬连线神经元语言处理单元作为通用认知基底。

## 英文关键词

Large Language Models, Language Processing Unit, Hardwired-Neurons, Metal-Embedding, Sustainable AI

## 中文关键词

大语言模型；语言处理单元；硬连线神经元；Metal-Embedding；可持续 AI

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790169)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 6A](index.md) · [返回 ASPLOS 2026](../index.md)
