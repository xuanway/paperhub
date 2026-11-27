GenDSE: Generative CPU Design Space Exploration via Sequential Decision Making
Authors：
[Meng Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=76837822111641146731)，[Mingyu Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=069143)，[Duo Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3693251015799447899)，[Shijun Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=05241801909679106501)，[Guangyu Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=470243)，[Xiaochun Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=280243)

## 中文标题

GenDSE：基于序列决策的生成式 CPU 设计空间探索

## 英文摘要

The prevailing surrogate-guided paradigm for CPU design space exploration (DSE) suffers from a fundamental credit assignment problem, leading to high sample complexity. This work introduces GenDSE, which reformulates DSE as a sequential decision process. Its contributions are: (1) A Markov decision process that decomposes design configuration generation into context-dependent steps. (2) A GFlowNet-based configuration generator for implicit credit assignment, linking individual decisions to final outcomes. (3) Progressive Sketching, a training paradigm to overcome GFlowNet’s data hunger. Experiments show GenDSE reduces simulation costs by 90% on average while achieving superior solution quality.

## 中文摘要

当前主流的代理模型引导式 CPU 设计空间探索（DSE）范式存在根本性的信用分配问题，导致样本复杂度高。本文提出 GenDSE，将 DSE 重新表述为序列决策过程。其贡献包括：（1）一个马尔可夫决策过程，将设计配置的生成分解为依赖上下文的多个步骤；（2）一个基于 GFlowNet 的配置生成器，通过隐式信用分配将单个决策与最终结果关联起来；（3）渐进式草图（Progressive Sketching），一种克服 GFlowNet 数据饥渴问题的训练范式。实验表明，GenDSE 平均降低 90%的仿真成本，同时获得更优的解质量。

## 英文关键词

Generative, Multi-object Optimization, Design Space Exploration

## 中文关键词

生成式、多目标优化、设计空间探索
