---
title: "Augmenting the Branch Predictor with a Squashed-Branch Reuse Buffer"
description: "ISCA 2026 · Session 3D · Augmenting the Branch Predictor with a Squashed-Branch Reuse Buffer"
tags:
  - "ISCA2026"
  - "Session 3D"
  - "Microarchitexture"
---

# Augmenting the Branch Predictor with a Squashed-Branch Reuse Buffer

**中文标题：** 用被冲刷分支复用缓冲增强分支预测器

**所属 Session：** [Session 3D](index.md) · [ISCA 2026](../index.md)

**作者：** Rohit Singh, Jiayang Li, Eric Rotenberg

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

In high-performance superscalar processors, a single mispredicted branch may squash hundreds of instructions after it. Some squashed instructions may be control and data independent of the branch, including younger branches, some of which may have executed prior to the squash. Their squashed outcomes can be used to override the branch predictor when the same dynamic branches are refetched, eliminating mispredictions if the predictor is incorrect. The key challenge lies in associating each dynamic branch on the resolved path with its counterpart on the squashed path, if it exists. Multiple dynamic instances of a branch occur due to loops. A dynamic instance can be uniquely identified by a hierarchical loop iteration identifier, like {loopA.iterA, loopB.iterB} for a branch within a doubly-nested loop. We realize such an identifier compactly using an LFSR-based signature that is augmented as loops are entered and continued, and a small stack that saves and restores the signature before entering and after exiting loops, respectively. The signature plus branch PC identifies the dynamic branch being fetched. A key point is that signatures are invariant, in that the signature of a dynamic branch on the resolved path matches that of its counterpart on the squashed path (if it exists), despite arbitrary differences in control-flow observed on the two paths. We augment a 64KB TAGE-SC-L branch predictor with a Squashed-Branch Reuse Buffer (SBRB) accessed by a hash of signature and branch PC. With 11KB of storage for all components, the SBRB improves performance by 2.08% for the SPEC 2006 and 2017 integer benchmarks (maximum 14.1%), 7.25% for the GAPBS benchmarks (maximum 21.2%), and 4.43% for all benchmarks combined.

## 中文摘要

在高性能超标量处理器中，一条预测错误的分支可能冲刷掉其后的数百条指令。部分被冲刷的指令可能与分支在控制与数据上均无依赖，其中包括更年轻的分支，其中一些可能在冲刷之前就已经执行。当相同的动态分支被重新取指时，这些被冲刷指令的已解析结果可用于覆盖分支预测器的预测，从而在预测器出错时消除预测错误。关键挑战在于：对于已解析路径上的每条动态分支，如果被冲刷路径上存在与之对应的分支，则需要将二者关联起来。由于循环的存在，同一分支会出现多个动态实例。一个动态实例可以由分层的循环迭代标识符唯一确定，例如对于双重嵌套循环内的某条分支，可用 {loopA.iterA, loopB.iterB} 表示。我们使用一种基于 LFSR 的签名紧凑地实现这样的标识符，该签名在进入循环和继续循环时被更新，并用一个小型栈分别在进入循环之前保存、在退出循环之后恢复该签名。签名加上分支 PC 即可标识正在取指的动态分支。一个关键之处在于签名具有不变性：尽管两条路径上观察到的控制流可能存在任意差异，已解析路径上某条动态分支的签名仍与其在被冲刷路径上对应分支（若存在）的签名相同。我们用被冲刷分支复用缓冲（Squashed-Branch Reuse Buffer, SBRB）扩展一个 64KB 的 TAGE-SC-L 分支预测器，该缓冲通过签名与分支 PC 的哈希来访问。所有组件共使用 11KB 存储，SBRB 在 SPEC 2006 与 2017 整数基准上带来 2.08% 的性能提升（最高 14.1%），在 GAPBS 基准上提升 7.25%（最高 21.2%），在所有基准合计上提升 4.43%。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3D](index.md) · [返回 ISCA 2026](../index.md)
