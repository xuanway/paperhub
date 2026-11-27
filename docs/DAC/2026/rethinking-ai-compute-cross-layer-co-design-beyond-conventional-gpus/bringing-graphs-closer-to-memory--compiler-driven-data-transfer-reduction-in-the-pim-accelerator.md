Bringing Graphs Closer to Memory: Compiler-Driven Data Transfer Reduction in the PIM Accelerator
Authors：
[Jisung Pack](https://63dac.conference-program.com/?post_type=page&p=15&uid=5026388360282929641)，[Junil Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=8441885127845898309)，[Mun Seong Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=7046277128122436041)，[Seok Young Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=1660840409574008115)，[Jaehan Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=5868290431921845943)，[Ilkon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=82164788887508293851)，[Seon Wook Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=7482602187392785365)

## 中文标题

让图更贴近内存：PIM 加速器中编译器驱动的数据传输削减

## 英文摘要

Processing-in-Memory (PIM) alleviates the memory bottleneck of modern AI workloads; however, its limited computational capability often necessitates hybrid architectures that integrate PIM with nearby processing units. In such heterogeneous systems, communication and host-side overheads remain dominant performance bottlenecks. Our profiling of SK hynix’s AiMX reveals that CPU–AiMX communication and CPU-side data reordering account for 50.07% of end-to-end LLM prefill and 78.36% of decode execution time. Notably, 54.03% of reordering operations occur adjacent to AiMX-executable nodes, indicating significant untapped potential for near-memory execution to eliminate unnecessary data movement. We propose a graph compiler that jointly optimizes computation and data movement for AiMX-based acceleration. The compiler performs (1) graph simplification to maximize AiMX-kernel coverage, (2) DMA-assisted tensor reordering and layout redefinition to offload host-side preprocessing, and (3) operator fusion to suppress redundant memory transfers. Integrated into the ONNX Runtime, our approach improves 2.00∼2.73× speedup in the prefill phase and 18.50∼38.29× in the decode phase, demonstrating the substantial benefits of graph-level co-optimization for PIM-enabled LLM inference and achieving performance comparable to hand-tuned AiMX execution.

## 中文摘要

存内计算（PIM）缓解了现代 AI 工作负载的内存瓶颈；然而其有限的计算能力往往需要将 PIM 与邻近的处理单元集成为混合架构。在此类异构系统中，通信与主机侧开销仍是主要的性能瓶颈。我们对 SK hynix 的 AiMX 进行剖析后发现，CPU 与 AiMX 之间的通信以及 CPU 侧的数据重排序分别占端到端 LLM 预填充执行时间的 50.07%和解码执行时间的 78.36%。值得注意的是，54.03%的重排序操作发生在 AiMX 可执行节点的相邻位置，表明近存执行在消除不必要数据搬移方面仍有巨大而未开发的潜力。我们提出一种图编译器，针对基于 AiMX 的加速联合优化计算与数据搬移。该编译器执行：(1) 图简化以最大化 AiMX 内核覆盖率；(2) DMA 辅助的张量重排序与布局重定义，以卸载主机侧预处理；(3) 算子融合以抑制冗余的内存传输。集成到 ONNX Runtime 后，我们的方法在预填充阶段取得 2.00∼2.73×加速，在解码阶段取得 18.50∼38.29×加速，展示了图级协同优化对 PIM 使能 LLM 推理的显著收益，并达到与手工调优 AiMX 执行相当的性能。

## 英文关键词

Processing-in-Memory, PIM Compiler, Data Reordering, Data Layout, Fusion

## 中文关键词

存内计算、PIM 编译器、数据重排序、数据布局、算子融合
