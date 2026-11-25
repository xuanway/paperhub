Accelerating AI+SAR Applications Through Enhanced Graph Optimization
Authors：
[Yang Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=9262200252510638717)，[Yaohua Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4430704124134866063)，[Zhe Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=57964508165223605301)

## 中文标题

通过增强图优化加速 AI+SAR 应用

## 英文摘要

Synthetic Aperture Radar (SAR), benefiting from its all-weather, all-time, and high-resolution characteristics, has become a vital tool in earth observation. A typical application of SAR first completes the imaging process of echo data and then conducts subsequent analysis. As AI excels in image classification and recognition, integrating AI with SAR has garnered significant interest. In order to leverage the acceleration capabilities of existing AI frameworks, particularly graph optimizations, while also reducing developing complexity, developers strive to streamline the entire SAR application within these frameworks. However, a key performance challenge arises: SAR imaging differs greatly from typical AI tasks in both the requirements of data layouts and the composition of operators, causing graph optimizations to fail in effectively accelerating the SAR imaging process. The fundamental reason is the failure of the two key graph optimizations: layout transformation and operator splitting. In this paper, we first address the issue of significant transpose overhead introduced by the layout transformation strategy. To this end, we propose a novel layout transformation strategy based on pseudo-transposition operators, which can completely eliminate transpose overhead while maintaining memory access efficiency. Subsequently, we design a tailored splitting strategy based on movable reverse-order operators to compensate for existing frameworks’ lack of capability in handling the core FFT operators. The proposed strategies were implemented in PyTorch and LiteRT, yielding a significant speedup of 3.45× for SAR imaging process.

## 中文摘要

合成孔径雷达（SAR）凭借全天候、全天时和高分辨率特性，已成为对地观测的重要工具。SAR 的典型应用首先完成回波数据的成像处理，随后再进行后续分析。由于 AI 在图像分类与识别方面表现优异，将 AI 与 SAR 相结合已引起广泛关注。为了利用现有 AI 框架的加速能力（尤其是图优化），同时降低开发复杂度，开发者希望在这类框架内统一实现整个 SAR 应用。然而，一个关键的性能挑战随之出现：SAR 成像在数据布局需求与算子构成上均与典型 AI 任务差异很大，导致图优化无法有效加速 SAR 成像过程。其根本原因在于两项关键图优化——布局变换与算子拆分——失效。本文首先解决布局变换策略引入的显著转置开销问题。为此，我们提出一种基于伪转置算子的新布局变换策略，可在保持访存效率的同时完全消除转置开销。随后，我们设计了基于可移动逆序算子的定制拆分策略，以弥补现有框架在处理核心 FFT 算子方面的能力不足。所提策略已在 PyTorch 与 LiteRT 中实现，使 SAR 成像过程获得 3.45 倍的显著加速。

## 英文关键词

SAR, graph optimization, AI framework, FFT

## 中文关键词

SAR、图优化、AI 框架、FFT
