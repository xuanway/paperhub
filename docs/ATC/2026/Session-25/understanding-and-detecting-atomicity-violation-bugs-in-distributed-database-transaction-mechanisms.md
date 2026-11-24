# Understanding and Detecting Atomicity Violation Bugs in Distributed Database Transaction Mechanisms

**中文标题**：理解与检测分布式数据库事务机制中的原子性违反缺陷

**所属 Session**：[Session 25: Formal Methods and Verification](index.md) · [ATC 2026](../index.md)

**作者**：Zhiyong Wu (School of Software, Tsinghua University), Jie Liang (Beihang University), Jingzhou Fu (Tsinghua University), Chi Zhang (Tsinghua University), Heyuan Shi (Central South University), Yu Jiang (Tsinghua University)

## 英文摘要
Atomicity is a cornerstone of distributed transactions, guaranteeing that all operations within a transaction are either fully committed or entirely aborted across multiple nodes in DDBMSs. However, implementation errors of the distributed database transaction mechanism can lead to atomicity violations, which cause data inconsistency or even system unavailability. We refer to such errors as atomicity violation bugs (AVBs). Despite their severity, the characteristics, root causes, and trigger conditions of AVBs remain limited understood. Moreover, existing testing tools (e.g., Mallory, Jepsen) are hard to detect AVBs, especially for those that preserve liveness while silently breaking distributed transactional semantics (e.g, data inconsistency). This paper presents a systematic study of 52 atomicity violation bugs (AVBs) across 4 DDBMSs. It reveals that atomicity violations primarily manifest as data inconsistency, partition-node crash, and system unavailability, often stemming from flawed distributed transaction management mechanisms, and are typically triggered by cross-partition transactions executed under perturbations during the transaction execution. Based on these findings, we design and implement Davis to detect AVBs. It first generates cross-partition transactional workloads that stress multiple-node interactions. Then, it constructs the distributed transaction communication model, monitors transaction progress, and introduces perturbation during critical execution phases to trigger AVBs. Finally, it verifies correctness by reconstructing an operation commit history execution and comparing it against the observed multi-node state. We applied Davis to six popular DDBMSs and discovered 41 previously unknown AVBs, and 12 have been assigned CVEs due to the severity.

## 中文摘要
原子性是分布式事务的基石，它保证事务内的所有操作在 DDBMS 的多个节点上要么全部提交、要么全部中止。然而，分布式数据库事务机制中的实现错误可能导致原子性违反，进而造成数据不一致甚至系统不可用。我们把此类错误称为原子性违反缺陷（AVB）。尽管后果严重，人们对 AVB 的特征、根本原因和触发条件仍了解有限。此外，现有测试工具（例如 Mallory、Jepsen）难以检测 AVB，尤其是那些在保持活性的同时悄然破坏分布式事务语义（例如数据不一致）的缺陷。本文对 4 个 DDBMS 中的 52 个原子性违反缺陷（AVB）开展了系统性研究。研究揭示，原子性违反主要表现为数据不一致、分区节点崩溃和系统不可用，往往源于有缺陷的分布式事务管理机制，并且通常由事务执行期间在扰动下执行的跨分区事务触发。基于这些发现，我们设计并实现了 Davis 来检测 AVB。它首先生成对多节点交互施加压力的跨分区事务工作负载。然后，它构建分布式事务通信模型，监控事务进展，并在关键执行阶段引入扰动以触发 AVB。最后，它通过重构操作提交历史的执行并与观测到的多节点状态进行比较来验证正确性。我们把 Davis 应用于六个流行的 DDBMS，发现了 41 个此前未知的 AVB，其中 12 个因严重性已被分配 CVE。

## 英文关键词
Distributed Transactions, Atomicity Violation, Bug Detection

## 中文关键词
分布式事务，原子性违反，缺陷检测

[返回 Session 25](index.md) · [返回 ATC 2026](../index.md)
