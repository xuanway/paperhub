SCOUT: Thermal-Aware SRAM Allocation for Real-Time DNN Tasks on Edge TPU
Authors：
[Changhun Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=6290284316514144047)，[Chihun Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=54070614821552457251)，[Namseok Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=4164550171340668597)，[Kilho Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=133343)，[Hoon Sung Chwa](https://63dac.conference-program.com/?post_type=page&p=15&uid=629243)，[Sangeun Oh](https://63dac.conference-program.com/?post_type=page&p=15&uid=07446695627260543621)

## 中文标题

SCOUT：面向边缘 TPU 上实时 DNN 任务的热感知 SRAM 分配

## 英文摘要

Specialized hardware accelerators facilitate timing guarantees for real-time DNNs, but high computational demands cause severe thermal stress. We present SCOUT, a real-time framework for Google Edge TPU that jointly satisfies timing/thermal constraints. The key idea couples task-level dynamic frequency scaling (DFS) with runtime on-chip SRAM allocation to offset DFS-induced performance loss. To this end, SCOUT provides i) a thermal model that reflects SRAM’s thermal impact and ii) an SRAM reallocation technique that safely adjusts allocations while mitigating write overheads. Our experiments show SCOUT schedules up to 46% more DNN task sets than prior approaches, while adhering to thermal constraints.

## 中文摘要

专用硬件加速器为实时 DNN 的时序保证提供了支撑，但高计算需求会带来严重的热压力。我们提出 SCOUT，一个面向 Google Edge TPU 的实时框架，可同时满足时序与热约束。其核心思想是将任务级动态频率调节（DFS）与运行时片上 SRAM 分配相耦合，以抵消 DFS 引起的性能损失。为此，SCOUT 提供：i) 反映 SRAM 热影响的热模型；ii) 一种 SRAM 重分配技术，可在安全调整分配的同时缓解写开销。实验表明，在遵守热约束的前提下，SCOUT 比现有方法多调度最多 46% 的 DNN 任务集。
