---
title: "Meta’s Second Generation AI Chip: Model-Chip Co-Design and Productionization Experiences"
description: "ISCA 2025 · Session 9A · Meta 第二代 AI 芯片：模型—芯片协同设计与产品化经验"
tags:
  - "ISCA2025"
  - "Session 9A"
  - "Industry Track"
---

# Meta’s Second Generation AI Chip: Model-Chip Co-Design and Productionization Experiences

**中文标题：** Meta 第二代 AI 芯片：模型—芯片协同设计与产品化经验

**所属 Session：** [Session 9A](index.md) · [ISCA 2025](../index.md)

**作者：** Joel Coburn, Chunqiang Tang, Adam Hutchin, Ajit Mathews, Alex Mastro, Amin Firoozshahian, Amit Nagpal, Aravind Sukumaran-Rajam, Arushi Sharma, Ashwin Kamath, Ashwin Narasimha, Bhasker Jakka, Brian Dodds, Cao Gao, David Reiss, Deboleena Roy, Eleanor Ozer, Emmanuel Menage, Eran Tal, Erum Kazi, Feixiong Zhang, Guoqiang Jerry Chen, Hangchen Yu, Harikrishna Reddy, Harish Dixit, Indu Kalyanaraman, Jack Montgomery, Jian Huang, Jinghan Yang, Jiyuan Zhang, Jongsoo Park, Junhan Hu, Kaustubh Gondkar, Mahesh Maddury, Maxim Naumov, Mike Tsai, Mohammed Sourouri, Neeraj Agrawal, Olivia Wu, Siji Medaiyese, Pankaj Kansal, Pavan Shetty, Poorvaja Ramani, Pritesh Modi, Raviteja Chinta, Richard Wareing, Roman Levenstein, Sameer Abu Asal, Saritha Dwarakapuram, Sathish Sekar, Satish Nadathur, Shreya Varshini, Sterling Hughes, Tanmay Zargar, Truls Edvard Stokke, Tyler Graf, Xiaolong Xie, Xun Jiao, Zitong Zeng

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731409) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The rapid growth of AI workloads at Meta has motivated our in- house development of AI chips, aiming to significantly reduce the total cost of ownership and mitigate risks posed by unpredictable GPU supplies. At ISCA’23, we presented Meta’s first-generation AI chip, MTIA 1. This paper describes its successor, MTIA 2i, now deployed at scale and serving billions of users. MTIA 2i signifi- cantly improves upon MTIA 1, reducing total cost of ownership by 44% compared to GPUs while delivering competitive performance per watt. A key differentiator is its memory hierarchy: instead of costly HBM, it uses large SRAM alongside LPDDR. Although there has been a proliferation of publications on AI chips, they often focus on architectural design and overlook three critical aspects: (1) co-designing and optimizing ML models to work effectively with the AI chip; (2) demonstrating sufficient flexibility to support a wide range of models; and (3) during the productionization process, ad- dressing challenges unanticipated or decisions deferred at design time, such as dealing with memory errors, safe overclocking, re- ducing provisioned power, and implementing real-time firmware updates to mitigate silicon design defects. A key contribution of this paper is sharing our experience with these aspects, based on our journey of productionizing MTIA 2i at scale.

## 中文摘要

Meta 内部AI负载的快速增长，推动了自研AI芯片的研发，目标是大幅降低总拥有成本，同时缓解GPU供应不稳定带来的风险。我们在ISCA 2023上介绍了Meta第一代AI芯片MTIA 1。本文介绍其迭代版本MTIA 2i，该芯片现已大规模部署，服务数十亿用户。MTIA 2i相比MTIA 1实现了显著提升，对比GPU，总拥有成本降低44%，同时能效具备竞争力。它的一大特色在于存储层次：没有采用昂贵的高带宽内存（HBM），而是搭配大容量SRAM与LPDDR。

目前已有大量AI芯片相关论文，但大多聚焦架构设计，常常忽略三个关键环节：（1）协同设计与优化机器学习模型，使其能够在AI芯片上高效运行；（2）具备足够灵活性，支撑多样化模型；（3）在产品化阶段，处理设计阶段未预见或延后决策的各类问题，例如内存错误处理、安全超频、降低预留功耗、通过实时固件更新修复硅片设计缺陷。本文的核心贡献是基于MTIA 2i大规模落地的历程，分享这几方面的工程实践经验。

## 英文关键词

Accelerators, Artificial intelligence, Inference, Machine learning, Memory hierarchy, Productionization, Deep learning recommenda- tion models, Total Cost of Ownership

## 中文关键词

加速器, 人工智能, 推理, 机器学习, 存储层次, 产品化, 深度学习推荐模型, 总拥有成本

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731409)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 9A](index.md) · [返回 ISCA 2025](../index.md)
