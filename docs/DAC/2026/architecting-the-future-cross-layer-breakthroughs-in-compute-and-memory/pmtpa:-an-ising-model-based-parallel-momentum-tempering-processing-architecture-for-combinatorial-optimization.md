PMTPA: An Ising Model-Based Parallel-Momentum Tempering Processing Architecture for Combinatorial Optimization
Authors：
[Jinsa Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=81694239704246602281)，[Xiangrui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=61843727252564969661)，[Dong Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3038164904167606743)，[Junyi Mai](https://63dac.conference-program.com/?post_type=page&p=15&uid=7981397643211086745)，[Zhanhong Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0102841917391452229)，[Enyi Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=3161479413500319301)

## 中文标题

PMTPA：一种面向组合优化的基于 Ising 模型的并行动量回火处理架构

## 英文摘要

CMOS-based Ising machines have emerged as a promising hardware paradigm for solving combinatorial optimization problems (COPs), which become increasingly intractable for conventional general-purpose processors as problem scale and complexity grow. However, existing Ising architectures still suffer from the algorithmic inefficiency of simulated annealing and parallel tempering, along with architectural bottlenecks and limited flexibility across computation scales. To address these challenges, this work proposes a Parallel-Momentum Tempering Processing Architecture (PMTPA) that features an elastic replica framework with time-division multiplexing and a system-level parallel pipeline design. Several architectural techniques are introduced to improve computational throughput and hardware utilization, including a similarity-driven local-field computation that halves local-field storage and simplifies arithmetic operations, and an adaptive processing scheme supporting spin networks of varying scales. In addition, a random-number-controlled shift mechanism is employed to implement nonlinear functions in the Metropolis criterion, achieving a balance between computational accuracy and hardware cost. A prototype FPGA implementation supports up to 2,048 fully-connected spins and 2–32 configurable replicas. Experimental results on large-scale Max-Cut and image-segmentation benchmarks demonstrate accuracy exceeding 99% and a 17, 000× speedup compared with a CPU-based software implementation.

## 中文摘要

基于 CMOS 的 Ising 机已成为求解组合优化问题（COP）的一种有前景的硬件范式，而随着问题规模与复杂度增长，这类问题对传统通用处理器而言愈发难以处理。然而，现有 Ising 架构仍受制于模拟退火与并行回火的算法低效性，以及架构瓶颈和跨计算规模的灵活性有限。为应对这些挑战，本工作提出并行动量回火处理架构（PMTPA），其特点是具有时分复用的弹性副本框架与系统级并行流水线设计。文中引入多项架构技术以提升计算吞吐量与硬件利用率，包括相似性驱动的局域场计算（将局域场存储减半并简化算术运算），以及支持不同规模自旋网络的自适应处理方案。此外，采用随机数控制的移位机制来实现 Metropolis 判据中的非线性函数，在计算精度与硬件成本之间取得平衡。原型 FPGA 实现最多支持 2,048 个全连接自旋与 2–32 个可配置副本。在大规模 Max-Cut 与图像分割基准上的实验结果表明，其准确率超过 99%，相比基于 CPU 的软件实现加速 17,000 倍。

## 英文关键词

Combinatorial optimization, hardware acceleration, Ising model, parallel tempering, momentum annealing

## 中文关键词

组合优化、硬件加速、Ising 模型、并行回火、动量退火
