GTX: Graph Transformer for Parasitic Extraction on Analog Circuits
Authors：
[Youngchang Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=4063043365090120149)，[Myungjun Kook](https://63dac.conference-program.com/?post_type=page&p=15&uid=08672359392344046421)，[Seokhyeong Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=775743)

## 中文标题

GTX：面向模拟电路寄生参数提取的图 Transformer

## 英文摘要

We present GTX, a graph-transformer–based framework for accurate parasitic prediction in analog circuits. GTX combines a customized parasitic modeling scheme with HGNNs and global attention to capture both local device interactions and long-range interconnect dependencies. Experiments show GTX achieves higher prediction accuracy than prior ML-based methods and generates predicted-parasitics netlists whose post-layout simulations closely match commercial parasitic-extracted netlists. Moreover, parasitic inference is 232.7× faster than commercial PEX, and simulations using predicted-parasitics netlists are up to 8.4× faster while closely matching the results of commercial parasitic-extracted netlists, demonstrating GTX’s effectiveness in accelerating layout-aware analog design.

## 中文摘要

我们提出 GTX，一个基于图 Transformer 的框架，用于模拟电路中寄生参数的准确预测。GTX 将定制的寄生建模方案与 HGNN 以及全局注意力机制相结合，从而同时捕获局部器件间的交互与长程互连依赖关系。实验表明，GTX 的预测精度高于已有基于机器学习的方法，其生成的寄生预测网表在后仿真中与商用寄生提取网表高度吻合。此外，GTX 的寄生参数推理速度比商用 PEX 快 232.7×；使用寄生预测网表进行仿真的速度最高提升 8.4×，且结果与商用寄生提取网表高度一致，表明 GTX 在加速版图感知的模拟设计方面行之有效。
