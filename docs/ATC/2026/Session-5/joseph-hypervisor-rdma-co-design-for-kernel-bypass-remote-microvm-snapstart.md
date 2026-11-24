# Joseph: Hypervisor–RDMA Co-Design for Kernel-Bypass Remote MicroVM SnapStart

**中文标题**：Joseph：面向内核旁路远程 MicroVM SnapStart 的 hypervisor–RDMA 协同设计

**所属 Session**：[Session 5: VM, Containers and Migration](index.md) · [ATC 2026](../index.md)

**作者**：Xingguo Pang (Unversity of Macau), Muhan Song (University of Macau), Chuang Hu (University of Macau), Kanye Ye Wang (University of Macau), Dazhao Cheng (WuHan University), Xiaobo Zhou (University of Macau)

## 英文摘要
Modern serverless platforms such as AWS Lambda increasingly use MicroVM SnapStart to pair lightweight isolation with fast startup. However, restoring snapshots from remote disaggregated memory to local DRAM induces layered copies and fault-driven stalls along the NIC →kernel →VMM → guest datapath, inflating latency and limiting scalability under high concurrency. We present Joseph, a hypervisor–RDMA co-designed system that treats the hypervisor as a first-class RDMA endpoint for fast remote MicroVM SnapStart. Joseph’s key principle is a network-to-guest placement contract: each RDMA read targets the guest frame of the faulting page, and the EPT mapping is installed only after the corresponding RDMA completion. This couples network transfer with guest-memory visibility in a single VMM/RNIC operation. Joseph builds a kernel-bypass RNIC→guest data path to place snapshot data directly into guest pages, bypassing kernel buffers and coalescing remote page fetches to amortize latency. By integrating RNIC-driven data placement into the hypervisor’s memory path, Joseph (i) enables direct access to remote snapshot pages, (ii) pipelines scatter–gather page fetches within the VMM pager, and (iii) uses RNIC-offloaded guest-memory fetch for in-situ page mapping, enabling zero-copy restoration and reducing CPU contention. Implemented on Firecracker/KVM, Joseph achieves up to 77% (87%) lower SnapStart latency, 2× (3×) higher concurrency, and 81% (56%) higher memory efficiency under high-concurrency workloads, compared to FaaSnap (TrEnv).

## 中文摘要
AWS Lambda 等现代无服务器平台越来越多地采用 MicroVM SnapStart，以兼顾轻量隔离与快速启动。然而，将快照从远程解耦内存恢复到本地 DRAM，会在 NIC → 内核 → VMM → 客户机这条数据通路上引入分层拷贝和由缺页驱动的停顿，从而抬高延迟并限制高并发下的可扩展性。我们提出 Joseph，一个 hypervisor–RDMA 协同设计的系统，它把 hypervisor 作为快速远程 MicroVM SnapStart 的一等 RDMA 端点。Joseph 的核心原则是一条网络到客户机的放置契约：每次 RDMA 读都指向发生缺页的页面所属的客户机帧，并且只有在相应的 RDMA 完成之后才安装 EPT 映射。这把网络传输与客户机内存可见性耦合在单次 VMM/RNIC 操作中。Joseph 构建了一条内核旁路的 RNIC → 客户机数据通路，把快照数据直接放入客户机页面，绕过内核缓冲区，并合并远程页取回以摊销延迟。通过把 RNIC 驱动的数据放置集成到 hypervisor 的内存路径中，Joseph（i）实现了对远程快照页的直接访问，（ii）在 VMM 分页器内以流水线方式执行分散–聚集式页取回，（iii）利用 RNIC 卸载的客户机内存取回进行就地页映射，从而实现零拷贝恢复并减少 CPU 争用。Joseph 在 Firecracker/KVM 上实现，在高并发工作负载下，与 FaaSnap（TrEnv）相比，SnapStart 延迟最多降低 77%（87%），并发度提高 2×（3×），内存效率提高 81%（56%）。

## 英文关键词
MicroVM SnapStart, RDMA, Kernel Bypass

## 中文关键词
MicroVM SnapStart，RDMA，内核旁路

[返回 Session 5](index.md) · [返回 ATC 2026](../index.md)
