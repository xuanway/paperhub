---
title: "DJFS : Directory-Granularity Filesystem Journaling for CMM-H SSDs"
description: "FAST 2025 · File Systems · 把日志事务粒度改成目录，让不同目录并行提交，在 CMM-H SSD 上最高提速 4.5 倍"
tags:
  - "FAST2025"
  - "File Systems"
  - "journaling file system"
  - "CMM-H SSD"
---

# DJFS : Directory-Granularity Filesystem Journaling for CMM-H SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">分析八个流行应用可以发现，文件更新几乎都集中在所属目录。DJFS 以目录为单位组织日志事务，用路径选择、合并与冲突消解处理多链接文件、跨目录更新与提交顺序，相比 FastCommit 在 Varmail、MDTest、Exim 上分别提升 4.5 倍、2.5 倍与 3.7 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · File Systems</p>
</div>

**中文标题**：DJFS：面向 CMM-H SSD 的目录粒度文件系统日志

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/yoo](https://www.usenix.org/conference/fast25/presentation/yoo)

**论文 PDF**：[fast25-yoo.pdf](https://www.usenix.org/system/files/fast25-yoo.pdf)

**作者**：Seung Won Yoo（Korea Advanced Institute of Science and Technology (KAIST)）；Joontaek Oh（University of Wisconsin–Madison）；Myeongin Cheon、Bonmoo Koo（Korea Advanced Institute of Science and Technology (KAIST)）；Wonseb Jeong、Hyunsub Song、Hyeonho Song、Donghun Lee（Samsung Electronics）；Youjip Won（Korea Advanced Institute of Science and Technology (KAIST)）

**会议**：FAST 2025 · Santa Clara, CA · 第 35–51 页

**Session**：File Systems · 2025-02-25 10:45–12:25 · Chair：Yu Hua（Huazhong University of Science and Technology）

**所属 Session**：[File Systems](index.md) · [FAST 2025](../index.md)

**关键词**：journaling file system, CMM-H SSD, CXL, per-directory transaction, transaction lock-up, crash consistency

---

## 英文摘要

In this paper, we propose DJFS, Journaling Filesystem with per-Directory Transaction . By analyzing the file access patterns in eight popular applications, we find that most file update operations are centered around the associated directory. Based upon this observation, we propose that the journaling filesystem defines the transaction in per-directory basis. DJFS consists of three key ingredients: path-based transaction selection, transaction coalescing and transaction conflict resolution. Per-directory journal transaction successfully addresses the fundamental issues associated with improving the performance of the journaling filesystem: reduce the lock contention, reduce the transaction conflict, reduce the transaction lock-up, and parallelize the journal commit. DJFS improves the throughput by 4.5× in Varmail, 2.5× in MDTest, and 3.7× in Exim, compared to the state-of-the-art journaling filesystem, FastCommit.

## 中文摘要

本文提出 DJFS（Journaling Filesystem with per-Directory Transaction，按目录划分事务的日志文件系统）。通过分析八个流行应用的文件访问模式，本文发现大多数文件更新操作都围绕所属目录进行。基于这一观察，本文提出日志文件系统应以目录为单位定义事务。DJFS 由三个关键部分组成：基于路径的事务选择、事务合并与事务冲突消解。按目录的日志事务成功解决了提升日志文件系统性能所面临的根本问题：降低锁竞争、减少事务冲突、减少事务锁定，并让日志提交并行化。相比最先进的日志文件系统 FastCommit，DJFS 在 Varmail 中吞吐提升 4.5 倍、MDTest 中提升 2.5 倍、Exim 中提升 3.7 倍。

## 一句话总结

> 日志变慢的根因不是提交延迟而是事务锁定窗口；把事务边界从全局挪到目录，多核与 CMM-H SSD 的并行度才真正用得上。

## 研究背景与问题

- 现代服务器有上百个核、同时跑数百个 VM 镜像并共享同一文件系统分区，日志模块成为瓶颈；CXL 让 CPU 能以 cache line 粒度访问存储，设备变快之后，加锁与串行提交的代价更加暴露。
- 已有工作分别针对全局日志结构的锁竞争、事务冲突与串行提交，但事务锁定（transaction lock-up）在块设备上被长写延迟掩盖，在 CMM-H SSD 上不可忽略；只有 CJFS 专门处理，而其 trylock 方案会拉长提交延迟。
- 把日志粒度做细并不自动带来吞吐：在 JBD 中实现 64 字节 cache line 粒度日志后，提交延迟下降 50%，但基准吞吐提升不到 20%，事务锁定时间反而延长 70%。
- CMM-H SSD 的吞吐高度依赖内置 DRAM 缓存命中率，cache line 粒度随机写吞吐随工作集大小最多相差 74 倍；而既有 PM 文件系统按几十 GB 的分区随机访问，与只有几 GB 缓存的 CMM-H 并不匹配。

## 核心贡献

- 用八个流行应用归纳出三条更新规律（各自使用专属目录、在目录内连续更新一批文件、更新内容伴随文件创建与删除），论证目录是比文件、核或分区更合适的日志事务单元。
- 提出按目录定义事务的 DJFS，并给出三条实现技术：路径式事务选择、事务合并与事务冲突消解。
- 路径式事务选择（path-based transaction selection）处理一个文件有多个硬链接时的归属问题；事务合并（transaction coalescing）把涉及多个目录的更新并入同一事务，保持原子性。
- 事务冲突消解（transaction conflict resolution）在维持提交顺序的前提下允许不同目录的事务并行提交，并消解提交期间对页缓存条目的阻塞。

## 方法与技术要点

- 双模通路：利用 CMM-H 的 CXL.mem（cache line 粒度、低延迟）与 CXL.io（块粒度、高带宽）两条访问通路，元数据日志走 cache line 粒度。
- 事务边界：以目录为事务单位，同一目录内连续的文件更新落入同一个 running transaction，减少多个线程争用同一全局事务。
- 归属与合并：多链接文件按路径确定归属事务；一次操作触及多个目录时用合并机制保持单个事务，避免原子性被目录边界切断。
- 提交并行化：不同目录的事务可并发提交，用冲突消解维持提交顺序，避开 JBD 式串行提交以及提交期间对后续文件操作的阻塞。
- 实现与语义：在 EXT4 上基于 Linux 5.18 实现，fsync 严格遵循 POSIX，只刷新该文件描述符相关的数据。

## 评估与主要结果

- 基线为当前最优日志方案 FastCommit：Varmail 吞吐提升 4.5 倍、MDTest 2.5 倍、Exim 3.7 倍，RocksDB-fillsync 的吞吐与之相当。
- 崩溃恢复用 CrashMonkey 与 xfstests 的 35、106、321 三个场景（分别覆盖 rename、跨目录 link、以及 creat()、unlink()、append()、mkdir()、rmdir() 的重复执行），每个场景生成的 1,000 个用例全部通过；Varmail 80 线程下强制关机后恢复耗时 2.5 秒。
- 全部访问 cache miss、由闪存服务时，DJFS 在 Varmail（80 线程）上仍比块粒度 JBD 高 1.24 倍；退化为纯块粒度日志时则高 1.96 倍。
- 内存开销：日志记录（被更新元数据的影子副本）总量小于 250 KB；四个基准中 EXIM 使用的目录最多，为 352 个，事务结构的内存压力可忽略。

[返回 File Systems](index.md) · [返回 FAST 2025](../index.md)
