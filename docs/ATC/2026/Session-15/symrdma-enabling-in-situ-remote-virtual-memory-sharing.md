# SymRDMA: Enabling In-Situ Remote Virtual Memory Sharing

**中文标题**：SymRDMA：实现原位远程虚拟内存共享

**所属 Session**：[Session 15: Remote Memory and RDMA](index.md) · [ATC 2026](../index.md)

**作者**：Huijun Shen (Hunan University), Bojie Li (Pine AI), Haixin Pang (Hunan University), Peihao Huang (Hunan university), Xingtong Lin (Hunan University), Xingyu Zhang (Hunan University), Guo Chen (Hunan University)

## 英文摘要
Data-intensive distributed applications, including in-memory analytics, distributed storage, and graph systems, increasingly demand in-situ remote virtual memory sharing, which refers to application-managed virtual memory (typically unpinned and dynamically changing) that remote peers access directly (e.g., the live JVM heap used by Spark). Realizing this on RDMA forces a dilemma: either copy into small pinned buffers, sacrificing zero-copy, or pin the entire heap—which disables OS elasticity and, for managed runtimes, is often architecturally impossible. Hardware-based On-Demand Paging (ODP) bridges the gap but suffers throughput collapse. This paper presents SymRDMA, the first system to enable high-performance in-situ remote virtual memory sharing on commodity RDMA hardware, transparently and with no hardware modifications. SymRDMA handles page faults optimistically via three mechanisms: (1) Optimistic Fault Suppression, using a hardware-enforced Sentinel Page to trap faults without breaking connections; (2) lightweight Remote Seqlocks to detect host-side changes without blocking the OS; and (3) Server-Initiated Repair, converting faults into targeted reverse-RDMA operations that avoid head-of-line blocking and timeouts. As a user-space library compatible with unmodified applications and hardware, SymRDMA achieves 11–14× lower graph-traversal latency than gRPC and 5–7× than ODP, runs Spark 1.5–1.7× faster than production, and expands storage capacity 5× with only 9% latency increase (vs. 45% for copying, 6× for ODP).

## 中文摘要
数据密集型分布式应用，包括内存分析、分布式存储和图系统，日益需要原位远程虚拟内存共享，即由应用管理的虚拟内存（通常未固定且动态变化）被远端对等方直接访问（例如 Spark 使用的活跃 JVM 堆）。在 RDMA 上实现这一点面临两难：要么拷贝到小的固定缓冲区，牺牲零拷贝；要么固定整个堆，这会破坏操作系统弹性，而且对托管运行时而言在体系结构上往往不可行。基于硬件的按需分页（ODP）弥合了这一差距，但会出现吞吐崩溃。本文提出 SymRDMA，首个在商用 RDMA 硬件上透明地、无需任何硬件修改地实现高性能原位远程虚拟内存共享的系统。SymRDMA 以乐观方式处理缺页，通过三种机制：(1) 乐观缺页抑制，使用硬件强制的哨兵页在不破坏连接的情况下捕获缺页；(2) 轻量级远程顺序锁，在不阻塞操作系统的情况下检测宿主侧变化；(3) 服务器发起的修复，将缺页转换为有针对性的反向 RDMA 操作，从而避免队头阻塞和超时。作为一个与未修改的应用和硬件兼容的用户态库，SymRDMA 的图遍历延迟比 gRPC 低 11–14 倍、比 ODP 低 5–7 倍，运行 Spark 比生产版本快 1.5–1.7 倍，并把存储容量扩展 5 倍，而延迟仅增加 9%（拷贝方式为 45%，ODP 为 6 倍）。

## 英文关键词
RDMA, Remote Memory Sharing, Virtual Memory

## 中文关键词
RDMA，远程内存共享，虚拟内存

[返回 Session 15](index.md) · [返回 ATC 2026](../index.md)
