AccDRC: FPGA Acceleration for VLSI DRC with Cell-Aware Layout Partitioning
Authors：
[Ruping Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=51141489296296022441)，[Zexu Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6488369790220333447)，[You Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3346321278693748308)，[Jiahao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3502418449269235076)，[Haodong Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67762242078220399721)，[Genggeng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=875243)，[Jianli Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=539243)，[Kun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=565843)

## 中文标题

AccDRC：基于单元感知版图划分的 VLSI DRC 的 FPGA 加速

## 英文摘要

Design Rule Checking (DRC) is a critical yet computation-intensive stage in modern very large scale integration design. As processes evolve, the high computational cost of DRC has become a significant bottleneck for design efficiency. Current acceleration approaches do not fully leverage the parallelism of DRC, resulting in limited performance gains. To address this challenge, we propose AccDRC, an FPGA-accelerated DRC based on software–hardware co-design. On the software, we design a cell-aware partitioning strategy with a data preparation and task encapsulation mechanism, which reorganize layouts into balanced task units tailored for FPGA processing. On the hardware, we implement an acceleration architecture consisting of a locality-preserving data-loading module, a unified and reconfigurable check core, and a sparse result writeback module. This architecture exploits DRC’s locality, structural commonality across rules, and sparse violation outcomes, enabling high-throughput dataflow execution with multi-level parallelism. Experimental results show that AccDRC achieves 522.11×∼1071.03× speedup over the CPU-based DRC tool KLayout, and 9.62×∼26.07× speedup over the state-of-the-art GPU-based DRC tool OpenDRC.

## 中文摘要

设计规则检查（DRC）是现代超大规模集成电路设计中关键但计算密集的阶段。随着工艺不断演进，DRC 的高计算开销已成为制约设计效率的显著瓶颈。现有加速方案未能充分挖掘 DRC 的并行性，性能收益有限。针对这一挑战，我们提出 AccDRC，一种基于软硬件协同设计的 FPGA 加速 DRC 方案。在软件侧，我们设计了单元感知的划分策略，并配合数据准备与任务封装机制，将版图重组为适合 FPGA 处理的均衡任务单元。在硬件侧，我们实现了一套加速架构，由局部性保持的数据加载模块、统一且可重构的检查核心以及稀疏结果回写模块组成。该架构充分利用了 DRC 的局部性、不同规则间的结构共性以及违例结果的稀疏性，从而以多级并行实现高吞吐的数据流执行。实验结果表明，AccDRC 相比基于 CPU 的 DRC 工具 KLayout 取得 522.11×~1071.03× 的加速，相比当前最先进的基于 GPU 的 DRC 工具 OpenDRC 取得 9.62×~26.07× 的加速。
