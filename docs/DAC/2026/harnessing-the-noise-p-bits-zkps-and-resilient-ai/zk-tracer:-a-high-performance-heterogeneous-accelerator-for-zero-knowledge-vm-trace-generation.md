ZK-Tracer: A High-Performance Heterogeneous Accelerator for Zero-Knowledge VM Trace Generation
Authors：
[Jieran Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=5054926489459491354)，[Zhengkai Wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=659749334194042412)，[Haowen Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=53757909892479366011)，[Yinan Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=80915366919317565321)，[Jia Xiong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1380754946707582248)，[Cheng Ni](https://63dac.conference-program.com/?post_type=page&p=15&uid=6400072404440362467)，[Mingchi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7426870888188238783)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)

## 中文标题

ZK-Tracer：面向零知识虚拟机踪迹生成的高性能异构加速器

## 英文摘要

Zero-knowledge virtual machines (zkVMs) are a key technology for driving the large-scale adoption of zero-knowledge proofs (ZKP), but their performance bottlenecks severely limit their practicality. While current hardware acceleration research has exclusively focused on backend proving, we identify that the frontend execution and trace generation phase is rapidly emerging as the new system bottleneck. To address this challenge, we propose ZK-Tracer, the first hardware accelerator architecture specifically designed for the zkVM frontend. ZK-Tracer features a novel heterogeneous design comprising a Main Trace Unit and parallel Permutation Trace Units. It exposes a fine-grained interface to the host software through a lightweight instruction set extension, enabling efficient task offloading. Our ASIC implementation results demonstrate that ZK-Tracer achieves up to 1829× speedup in trace generation over a high-performance multi-core CPU. When integrated with existing backend proving accelerators, it delivers a remarkable 963× end-to-end performance improvement for the entire ZKP system.

## 中文摘要

零知识虚拟机（zkVM）是推动零知识证明（ZKP）大规模应用的关键技术，但其性能瓶颈严重限制了其实用性。现有硬件加速研究几乎只关注后端证明环节，而我们发现前端的执行与踪迹生成阶段正迅速成为新的系统瓶颈。为应对这一挑战，我们提出 ZK-Tracer，这是首个专为 zkVM 前端设计的硬件加速器架构。ZK-Tracer 采用新颖的异构设计，由主踪迹单元（Main Trace Unit）和并行的置换踪迹单元（Permutation Trace Unit）组成。它通过轻量级指令集扩展向主机软件暴露细粒度接口，从而实现高效的任务卸载。我们的 ASIC 实现结果表明，ZK-Tracer 的踪迹生成速度相比高性能多核 CPU 最高提升 1829 倍。当与现有后端证明加速器集成时，它可为整个 ZKP 系统带来高达 963 倍的端到端性能提升。

## 英文关键词

Zero-Knowledge Virtual Machine, Hardware Acceleration

## 中文关键词

零知识虚拟机、硬件加速
