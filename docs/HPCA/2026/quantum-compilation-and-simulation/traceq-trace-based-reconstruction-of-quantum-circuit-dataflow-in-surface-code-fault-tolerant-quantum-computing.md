---
title: "TraceQ: Trace-Based Reconstruction of Quantum Circuit Dataflow in Surface-Code Fault-Tolerant Quantum Computing"
description: "HPCA 2026 · Quantum Compilation and Simulation"
tags:
  - "HPCA2026"
  - "Quantum Compilation and Simulation"
---

# TraceQ: Trace-Based Reconstruction of Quantum Circuit Dataflow in Surface-Code Fault-Tolerant Quantum Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Compilation and Simulation。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Compilation and Simulation</p>
</div>

**论文链接**：
**作者**：Theodoros Trochatos Yale University , Christopher Kang University of Chicago , Andrew Wang Cornell University , Frederic T. Chong University of Chicago , Jakub Szefer Northwestern University
**会议**：HPCA 2026

---

## 中文标题

TraceQ：表面码容错量子计算中基于迹的量子线路数据流重建

## 英文摘要

Practical applications of quantum computing depend on fault-tolerant devices that employ error correction. A promising quantum error-correcting code for large-scale quantum computing is the surface code. For this code, Fault-Tolerant Quantum Computing (FTQC) can be performed via lattice surgery, i.e. merging and splitting of encoded qubit patches on a 2D grid. Lattice surgery operations result in space-time patterns of activity that are defined in this work as access traces. This work demonstrates that the access traces reveal when, where, and how logical qubits interact. Leveraging this formulation, this work further introduces TraceQ, a trace-based reconstruction framework that is able to reconstruct the quantum circuit dataflow just by observing the patch activity at each trace entry. The framework is supported by heuristics for handling inherent ambiguity in the traces, and demonstrates its effectiveness on a range of synthetic fault-tolerant quantum benchmarks. The access traces can have applications in a wide range of scenarios, enabling analysis and profiling of execution of quantum programs and the hardware they run on. As one example use of TraceQ, this work investigates whether such traces can act as a side channel through which an observer can recover the circuit’s structure and identify known subroutines in a larger program or even whole programs. The findings show that indeed the minimal access traces can be used to recover subroutines or even whole quantum programs with very high accuracy. Only a single trace per program execution is needed and the processing can be done fully offline. Along with the custom heuristics, advanced subgraph matching algorithms used in this work enable a high rate of locating the subroutines while executing in minimal time.

## 中文摘要

量子计算的实际应用依赖采用纠错的容错设备。表面码是大规模量子计算中一种有前景的量子纠错码。对该码而言，容错量子计算（FTQC）可通过晶格手术实现，即在 2D 网格上合并与拆分编码量子比特块。晶格手术操作会产生时空范围的活动模式，本文将其定义为访问迹。本文表明，访问迹揭示了逻辑量子比特在何时、何处以及如何相互作用。基于这一形式化，本文进一步提出 TraceQ，一个基于迹的重建框架，仅通过观察每个迹条目处的块活动即可重建量子线路的数据流。该框架辅以处理迹中固有歧义的启发式方法，并在多个合成的容错量子基准上验证有效。访问迹可应用于广泛场景，支持分析量子程序及其运行硬件的执行过程。作为 TraceQ 的一个示例用途，本文研究此类迹能否充当侧信道，使观察者恢复线路结构并识别更大程序乃至整个程序中的已知子程序。结果表明，确实可以用最小的访问迹以很高的准确率恢复子程序甚至完整的量子程序；每次执行仅需一条迹，且处理可完全离线完成。配合定制启发式方法，先进子图匹配算法可在极短时间内以高比率定位子程序。
