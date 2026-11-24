# PAVE: Prebuilding Address Translations for Fast Nested MicroVM Restore

**中文标题**：PAVE：为嵌套 MicroVM 快速恢复预构建地址转换

**所属 Session**：[Session 5: VM, Containers and Migration](index.md) · [ATC 2026](../index.md)

**作者**：Muhan Song (University of Macau), Xingguo Pang (University of Macau), Li Li (University of Macau), Xiaobo Zhou (University of Macau)

## 英文摘要
Nested virtualization lets serverless platforms run MicroVM-based function runtimes on virtualized cloud infrastructure, but it makes snapshot restore substantially more expensive. Existing systems either overlap snapshot-page loading with execution to achieve data readiness, or reduce the cost of individual nested EPT faults. However, neither makes final nested translations ready before restored pages are first touched. Nested KVM still constructs these translations reactively, one page at a time, on the synchronous first-touch path, causing severe latency under high-concurrency same-snapshot restore bursts. We present PAVE, a nested-hypervisor extension that makes translation readiness a first-class restore objective. PAVE combines two mechanisms. Latency-hidden EPT prebuilding uses recorded working-set and snapshot metadata to construct validated final nested translations at L0 concurrently with MicroVM execution; if a MicroVM reaches a page first, the L0 fault handler installs the same translation directly, avoiding the normal nested fault path through L1. Cross-VM EPT sharing places clean, non-writable translations in a snapshot-scoped shared EPT hierarchy so that MicroVMs restored from the same snapshot can reuse them without repeated construction. PAVE preserves isolation with a simple invariant—shared EPT entries are append-only and non-writable—and routes writes through per-VM copy-on-write EPT overlays without cross-VM TLB shootdowns. Our evaluation on serverless benchmarks shows that PAVE reduces high-concurrency restore latency by 7.11× over FaaSnap-Nested and by 3.23× over FaaSnap+HT.

## 中文摘要
嵌套虚拟化使无服务器平台能够在虚拟化的云基础设施上运行基于 MicroVM 的函数运行时，但也使快照恢复的代价显著增加。现有系统要么将快照页加载与执行过程重叠以实现数据就绪，要么降低单次嵌套 EPT 缺页的代价。然而，两者都不能在恢复出的页面被首次访问之前就让最终的嵌套地址转换准备就绪。嵌套 KVM 仍然在同步的首次访问路径上以逐页方式被动地构建这些转换，在从同一快照进行高并发恢复的突发场景下造成严重延迟。我们提出 PAVE，一个嵌套 hypervisor 扩展，它把地址转换就绪作为恢复的一等目标。PAVE 结合了两种机制。延迟隐藏的 EPT 预构建利用记录下来的工作集与快照元数据，在 MicroVM 执行的同时于 L0 构建经过校验的最终嵌套转换；如果 MicroVM 先访问到某个页面，L0 缺页处理程序会直接安装同一转换，从而避开经由 L1 的正常嵌套缺页路径。跨 VM 的 EPT 共享把干净的、不可写的转换放入以快照为作用域的共享 EPT 层级，使从同一快照恢复的 MicroVM 可以复用它们而无需重复构建。PAVE 通过一条简单的不变量来保持隔离性——共享 EPT 条目只追加且不可写——并将写操作经由每 VM 的写时复制 EPT 覆盖层处理，且不引发跨 VM 的 TLB 击落（shootdown）。我们在无服务器基准上的评估表明，PAVE 将高并发恢复延迟相对 FaaSnap-Nested 降低 7.11×，相对 FaaSnap+HT 降低 3.23×。

## 英文关键词
Nested virtualization, Serverless computing, Memory virtualization

## 中文关键词
嵌套虚拟化，无服务器计算，内存虚拟化

[返回 Session 5](index.md) · [返回 ATC 2026](../index.md)
