SpArC: Sparse Tensor Accelerator Compilation with Scheduling and Mapping
Authors：
[Xingyan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=55906089571378102461)，[Zihan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=752843)，[Lei Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=852843)，[Qianyu Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=452843)，[Cheng Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9722161818012809504)，[teng wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=652843)，[Wenqi Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=425843)，[Xuehai Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=513843)

## 中文标题

SpArC：面向稀疏张量加速器的调度与映射编译

## 英文摘要

Sparse tensor computation is widely used in deep learning and scientific computing, but its irregular computation and memory access patterns pose significant challenges for general-purpose accelerators such as GPUs and NPUs. FPGAs, owing to their reconfigurability, are inherently well-suited for handling sparse workloads. However, existing point-based manual design paradigms severely limit the performance potential of reconfigurable hardware across diverse sparse scenarios. To address this, we propose SpArC—an automated compilation framework for sparse tensor computation that automatically generates high-performance FPGA accelerators. SpArC consists of: (1) a primitive-based DSL serving as the design specification for sparse accelerators, providing a unified abstraction of data formats, iteration pattern, and hardware mapping strategies; (2) a two-stage mapping mechanism centered around sparse meta-operations, enabling arbitrary sparse dataflows to be efficiently mapped to hardware micro-architectures; and (3) a heuristic design space exploration method for joint software–hardware optimization. Experimental results show that SpArC can automatically generate FPGA accelerators for typical sparse workloads such as SpMSpV, Plus3, and SpMM. On the SuiteSparse benchmark dataset, for SpMSpV workloads, SpArC achieves 31.7×–130.4× performance improvement over automated frameworks such as ScaleHLS and Allo. On the same SuiteSparse SpMSpV workloads running on CPU platforms, SpArC further achieves 10.8×–34.7× speedup over TACO and 1.03×–1.89× speedup over MKL.

## 中文摘要

稀疏张量计算广泛应用于深度学习与科学计算，但其不规则的计算与访存模式给 GPU、NPU 等通用加速器带来了重大挑战。FPGA 凭借其可重构性，天然适合处理稀疏负载。然而，现有的基于点的手工设计范式严重限制了可重构硬件在多样稀疏场景下的性能潜力。为此，我们提出 SpArC——一个面向稀疏张量计算的自动化编译框架，可自动生成高性能 FPGA 加速器。SpArC 由以下部分组成：(1) 基于原语的 DSL，作为稀疏加速器的设计规范，提供数据格式、迭代模式与硬件映射策略的统一抽象；(2) 以稀疏元操作为中心的两阶段映射机制，使任意稀疏数据流都能高效映射到硬件微架构；(3) 一种启发式设计空间探索方法，用于软硬件联合优化。实验结果表明，SpArC 可为 SpMSpV、Plus3、SpMM 等典型稀疏负载自动生成 FPGA 加速器。在 SuiteSparse 基准数据集上，对于 SpMSpV 负载，SpArC 相比 ScaleHLS 与 Allo 等自动化框架取得 31.7×–130.4× 的性能提升。在 CPU 平台上运行相同的 SuiteSparse SpMSpV 负载时，SpArC 进一步相比 TACO 取得 10.8×–34.7× 的加速，相比 MKL 取得 1.03×–1.89× 的加速。

## 英文关键词

FPGA, Sparse tensor algebra, Compiler, High-Level Synthesis

## 中文关键词

FPGA、稀疏张量代数、编译器、高层次综合
