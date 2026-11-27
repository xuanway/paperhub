TOB-Sched: Topological Order Balancing-Driven Static Scheduling for Processor-Based Emulation
Authors：
[shunyang bi](https://63dac.conference-program.com/?post_type=page&p=15&uid=67424593689685242841)，[qiwang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=8001303523051580108)，[Jing Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9877415014318987833)，[zhengguang tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7010551455750515878)，[Haonan Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=06977766675389552171)，[Hailong You](https://63dac.conference-program.com/?post_type=page&p=15&uid=3735223745328947019)，[Cong Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=3194780417086781933)

## 中文标题

TOB-Sched：面向基于处理器仿真的拓扑序均衡驱动静态调度

## 英文摘要

The efficiency of processor-based emulation (PBE) heavily depends on the computations of scheduling. In the scheduling process, the challenge in accurate modeling time step stems from the complex instruction execution process, which is influenced by both the inter-processor communication latency, the execution sequence of the allocated nodes, and scheduling constraints. Therefore, existing works struggle with the inability to optimize the time step directly. In this paper, inspired by the key insight of the inherent connection between the time step and the topological order balancing of the netlist graph, we propose the topological order balancing-driven scheduling algorithm. Our approach introduces the mobility-prioritized node selection and efficient forward and backward propagation. Besides, a theorem is presented to reduce the time complexity of gain calculation to 𝑂(1). Experiments demonstrate significant improvements over the SOTA scheduling algorithm, achieving 72% better TOB metric, 22.5% reduction in time steps, and 55% faster runtime on public and open-source chip benchmarks, thus proving TOB as a critical metric for the scheduling process and enhancing the efficiency and performance of PBE emulation.

## 中文摘要

基于处理器的仿真（PBE）的效率在很大程度上取决于调度的计算。在调度过程中，准确建模时间步的难点源于复杂的指令执行过程，该过程同时受到处理器间通信延迟、所分配节点的执行顺序以及调度约束的影响。因此，现有工作难以直接优化时间步。本文基于“时间步与网表图的拓扑序均衡之间存在内在联系”这一关键洞察，提出拓扑序均衡驱动的调度算法。该方法引入以移动性为优先的节点选择机制以及高效的前向与后向传播。此外，文中给出一个定理，将增益计算的时间复杂度降至 O(1)。实验表明，在公开与开源芯片基准上，相较于最先进的调度算法，本方法在 TOB 指标上提升 72%，时间步减少 22.5%，运行时间加快 55%，从而证明 TOB 是调度过程中的关键指标，并提升了 PBE 仿真的效率与性能。
