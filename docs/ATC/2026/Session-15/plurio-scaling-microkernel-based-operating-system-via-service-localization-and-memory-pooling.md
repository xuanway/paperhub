# Plurio: Scaling Microkernel-based Operating System via Service Localization and Memory Pooling

**中文标题**：Plurio：通过服务本地化与内存池化扩展基于微内核的操作系统

**所属 Session**：[Session 15: Remote Memory and RDMA](index.md) · [ATC 2026](../index.md)

**作者**：Zhenlin Qi (Shanghai Jiao Tong University), Shengan Zheng (Shanghai Jiao Tong University), Bowen Zhang (Shanghai Jiao Tong University), Linpeng Huang (Shanghai Jiao Tong University)

## 英文摘要
Microkernel-based operating systems offer strong isolation but often scale poorly on multicore platforms due to expensive IPC. We present Plurio, a microkernel-based operating system architecture that revisits service organization and memory management around two principles: localizing service execution and pooling memory resources. Plurio selects among pre-generated service combinations at runtime to turn frequent cross-service invocations into local function calls, and employs a global memory pool that exposes physical memory as capabilities for mapping in a shared virtual address space. Affinity-aware worker arrangement and proxy-managed request caches further shorten communication path and reduce data copying. We implement Plurio on the Genode framework and evaluate it with Filebench and YCSB on x86 and ARM platforms. For the evaluated metadata-intensive workload, Plurio improves throughput over unmodified Genode by up to 1.9× on x86 and 1.8× on ARM, demonstrating the benefits of service localization within these multicore configurations.

## 中文摘要
基于微内核的操作系统提供强隔离，但由于 IPC 开销高昂，在多核平台上往往扩展性较差。我们提出 Plurio，一种基于微内核的操作系统架构，围绕两条原则重新审视服务组织与内存管理：服务执行本地化与内存资源池化。Plurio 在运行时从预生成的服务组合中进行选择，将频繁的跨服务调用转变为本地函数调用，并采用全局内存池，把物理内存以能力的形式暴露出来，以便在共享虚拟地址空间中映射。亲和性感知的工作线程布置与代理管理的请求缓存进一步缩短通信路径并减少数据拷贝。我们在 Genode 框架上实现 Plurio，并在 x86 和 ARM 平台上用 Filebench 与 YCSB 对其进行评估。对于所评估的元数据密集型工作负载，Plurio 相比未修改的 Genode 在 x86 上最高提升 1.9 倍吞吐、在 ARM 上最高提升 1.8 倍，展示了在这些多核配置中服务本地化带来的收益。

## 英文关键词
Microkernel, Multi-core, Scalability, IPC

## 中文关键词
微内核，多核，可扩展性，IPC

[返回 Session 15](index.md) · [返回 ATC 2026](../index.md)
