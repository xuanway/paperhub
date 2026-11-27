Adana: Accelerating Large Language Models via Adaptive Nonuniform Asymmetric Quantization
Authors：
[Xinkuang Geng](https://63dac.conference-program.com/?post_type=page&p=15&uid=07076846487607270501)，[Siting Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2045291533381948683)，[Hui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=26491562959622173821)，[Leibo Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=411243)，[Jie Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=273343)，[Honglan Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=91048570719084638371)

## 中文标题

Adana：基于自适应非均匀非对称量化的 LLM 加速

## 英文摘要

We propose Adana, a hardware-software co-design that enables efficient low-bit group-wise quantization for LLMs based on the adaptive nonuniform asymmetric numeric type. First, Adana introduces a novel numeric type that precisely captures the nonuniformity and asymmetry of data within small groups. In addition, an approximate metric for quantization error is proposed to facilitate efficient implementation of online adaptive activation quantization. Finally, a dedicated LLM acceleration microarchitecture is developed for Adana. Compared to state-of-the-art designs, Adana achieves 1.42×–2.10× speedups and 18.9%–48.5% power savings on LLMs, while maintaining superior accuracy.

## 中文摘要

我们提出 Adana，一种软硬件协同设计，基于自适应非均匀非对称数值类型为 LLM 实现高效的低比特分组量化。首先，Adana 引入一种新颖的数值类型，能够精确刻画小组内数据的非均匀性与非对称性。此外，提出一种量化误差的近似度量，以支持在线自适应激活量化的高效实现。最后，为 Adana 设计了专用的 LLM 加速微架构。与最先进设计相比，Adana 在保持更优精度的同时，在 LLM 上实现 1.42–2.10 倍加速和 18.9%–48.5% 的功耗节省。

## 英文关键词

large language model, low-bit quantization, group-wise quantization, adaptive numeric type, accelerator

## 中文关键词

大语言模型、低比特量化、分组量化、自适应数值类型、加速器
