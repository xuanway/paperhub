Dataflowgen: An MLIR-Based Compiler for Efficient Dataflow Accelerator Generation
Authors：
[Jiangnan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=3035944067988884177)，[Kaixiang Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=63830813151715256551)，[Zhengyi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=64007306854796863301)，[Lingli Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=25253654954830750101)

## 中文标题

DataFlowGen：面向高效数据流加速器生成的基于 MLIR 的编译器

## 英文摘要

High-level synthesis (HLS) has been widely adopted to map high-level languages to hardware, significantly improving hardware design productivity. Existing HLS tools have gaps in generating custom hardware due to data dependencies and differences in intermediate representation (IR) levels. Appropriate IRs can be created for each by separating the algorithmic behaviour and the microarchitecture description, which is an effective way to reduce development costs and achieve competitive hardware designs. In this paper, we propose DataFlowGen, an open-source framework built on MLIR for efficient dataflow accelerator generation. DataFlowGen explicitly introduces a two-level IR to perform operations at suitable abstraction levels, capturing dataflow characteristics and multi-level hierarchy. Leveraging these representations, we develop an automated optimizer that outlines the application kernel and performs dataflow transformations to derive a hardware-oriented control dataflow graph (H-CDFG). It enables concise representation and resource efficiency of hardware architectures. Experiments show that DataFlowGen achieves a performance improvement with significant resource reduction compared to state-of-the-art HLS tools. The results show that our optimizer effectively leverages the expressive power of IRs thus capturing kernel parallelism.

## 中文摘要

高层次综合（HLS）已被广泛用于将高层语言映射到硬件，显著提升了硬件设计生产率。由于数据依赖以及中间表示（IR）层次的差异，现有 HLS 工具在生成定制硬件方面仍存在不足。通过分离算法行为与微架构描述，可以为二者分别构建合适的 IR，这是降低开发成本、获得有竞争力硬件设计的有效途径。本文提出 DataFlowGen，这是一个基于 MLIR 构建的开源框架，用于高效生成数据流加速器。DataFlowGen 显式引入两级 IR，以在合适的抽象层次上执行操作，捕捉数据流特征与多级层次结构。借助这些表示，我们开发了一个自动化优化器，它勾勒出应用内核并执行数据流变换，从而导出面向硬件的控制数据流图（H-CDFG）。这使得硬件架构的表示简洁且资源高效。实验表明，与最先进的 HLS 工具相比，DataFlowGen 在提升性能的同时显著减少了资源占用。结果表明，我们的优化器有效利用了 IR 的表达能力，从而捕捉到内核并行性。

## 英文关键词

MLIR, Hardware-software codesign, Intermediate Representation, Dataflow Optimization

## 中文关键词

MLIR、软硬件协同设计、中间表示、数据流优化
