# A^2: Characterizing and Mitigating Imbalanced Reclaim in MGLRU via Active Aging at Production Scale

**中文标题**：A²：在生产规模下刻画并通过主动老化缓解 MGLRU 中的不均衡回收

**所属 Session**：[Session 9: Memory Tiering and Management](index.md) · [ATC 2026](../index.md)

**作者**：Fei Zeng (Central South University), Zicheng Wang (Honor Device Co., Ltd), Ligeng Chen (Honor Device Co., Ltd), Yinggang Guo (Honor Device Co.,Ltd), Hao Wu (Nanjing University), Lu Liu (Honor Device Co.,Ltd), Tao Wang (Honor Device Co.,Ltd), Jun Xiao (Honor Device Co.,Ltd), Borui Li (Southeast University), Feng Lyu (Central South University)

## 英文摘要
Multi-generational LRU (MGLRU) has been adopted by some major smartphone manufacturers to replace the dual-list LRU, delivering lower kswapd CPU consumption, fewer low-memory kills, and reduced rendering latency under memory pressure. However, our production deployment revealed a regression: cold anonymous pages are shielded from reclaim by MGLRU’s aging gate, forcing hot file pages to be evicted first; swappiness, the canonical parameter for balancing anonymous and file reclaim, is thereby bypassed. The root cause is an asymmetry: anonymous pages must age through multiple generations before becoming reclaimable, yet at default priority, aging is deferred; file pages are reclaimed from the oldest generation immediately. We propose an Active Aging mechanism, A2, which decouples aging from reclaim by triggering it when pages turn cold. On Android, the foreground-to-background transition provides this moment: userspace invokes the kernel’s existing page-table scan, opening the aging gate before reclaim runs. The approach is not Android-specific; servers running MGLRU can apply the same aging primitive via a BPF hook to correct the generational imbalance. A2 deployed across 300 users over 30K device-hours, A2 improves Android keep-alive by 15.4%, and input method editor (IME) dismiss latency by 47.2%. In server workload measurements, it improves fio random-read bandwidth by 31.83%. Code and benchmark specifications are available at https://github.com/ccfeiker/mglru-active-aging.

## 中文摘要
多代 LRU（MGLRU）已被一些主流智能手机厂商采用以替代双链表 LRU，在内存压力下带来更低的 kswapd CPU 消耗、更少的低内存杀死以及更低的渲染延迟。然而，我们的生产部署揭示了一种性能回退：冷的匿名页被 MGLRU 的老化门限屏蔽而无法被回收，迫使热的文件页先被逐出；作为平衡匿名页与文件页回收的规范参数的 swappiness 因此被绕过。根本原因是一种不对称性：匿名页必须经过多个代才能变为可回收，而在默认优先级下老化被推迟；文件页则立即从最老的代中被回收。我们提出主动老化（Active Aging）机制 A²，它通过在被页面变冷时触发老化，将老化与回收解耦。在 Android 上，前台到后台的切换提供了这一时机：用户态调用内核已有的页表扫描，在回收运行之前打开老化门限。该方法并非 Android 专属；运行 MGLRU 的服务器可以通过 BPF 钩子应用相同的老化原语，以纠正代际不均衡。A² 部署在 300 名用户、超过 3 万设备小时上，将 Android 保活率提升 15.4%，将输入法编辑器（IME）消失延迟改善 47.2%。在服务器工作负载测量中，它将 fio 随机读带宽提升 31.83%。代码与基准测试规范见 https://github.com/ccfeiker/mglru-active-aging。

## 英文关键词
Multi-generational LRU, Memory Management, Android System

## 中文关键词
多代 LRU，内存管理，Android 系统

## 代码与研究制品

- [code](https://github.com/ccfeiker/mglru-active-aging)

[返回 Session 9](index.md) · [返回 ATC 2026](../index.md)
