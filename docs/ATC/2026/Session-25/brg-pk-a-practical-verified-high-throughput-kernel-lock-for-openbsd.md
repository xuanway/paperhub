# brg-pk: A Practical Verified High-Throughput Kernel Lock for OpenBSD

**中文标题**：brg-pk：一个面向 OpenBSD 的实用且经过验证的高吞吐内核锁

**所属 Session**：[Session 25: Formal Methods and Verification](index.md) · [ATC 2026](../index.md)

**作者**：David Gwynne (University of Queensland), Robert Colvin (University of Queensland), Brijesh Dongol (University of Surrey), Roger Su (Australian National University), Daniel Wright (University of Surrey)

## 英文摘要
Operating system kernels make extensive use of locks to handle concurrent accesses to shared data, hence the efficiency of kernel lock mechanisms is crucial to system performance. In this paper we present a new locking algorithm, brg-pk, its verification, and an empirical evaluation. As a result of our efforts brg-pk is the default kernel lock (mutex) implementation in OpenBSD. The algorithm uses concepts of barging and parking from current practice and adapts them for use in a cross-platform operating system kernel. Our empirical analysis is focussed on behaviour under various workloads corresponding to those experienced by the OpenBSD kernel, and we find that brg-pk overall outperforms five established lock algorithms across four different architectures. Much of its performance comes from having a relatively weak fairness guarantee: it is a “mostly-fair” algorithm that sometimes allows threads waiting to acquire the lock to be overtaken. Both experimental and real-world evidence suggest this does not manifest as a problem on the workload profile of the OpenBSD kernel. Given its importance in the kernel, we rigorously verify the correctness of the core algorithm underlying brg-pk via machine-assisted theorem proving; additionally, we validate correctness of the brg-pk implementation via a combination of testing and model checking. Weak memory effects are taken into account in a generic way to support portability across different software and hardware models.

## 中文摘要
操作系统内核大量使用锁来处理对共享数据的并发访问，因此内核锁机制的效率对系统性能至关重要。在本文中，我们提出一种新的加锁算法 brg-pk、对它的验证以及一项实证评估。得益于这些工作，brg-pk 成为 OpenBSD 中默认的内核锁（互斥锁）实现。该算法借鉴了当前实践中的插队（barging）与停泊（parking）概念，并对其加以调整以用于跨平台的操作系统内核。我们的实证分析聚焦于与 OpenBSD 内核所经历的各种工作负载相对应的行为，发现在四种不同架构上 brg-pk 总体上优于五种已有锁算法。其性能很大程度上来自一个相对较弱的公平性保证：它是一种“大致公平”的算法，有时允许正在等待获取锁的线程被后来者超越。实验证据和真实世界证据都表明，在 OpenBSD 内核的工作负载特征下这并不会表现为问题。鉴于它在内核中的重要性，我们通过机器辅助的定理证明严格验证了 brg-pk 底层核心算法的正确性；此外，我们通过测试与模型检查相结合的方式验证了 brg-pk 实现的正确性。弱内存效应以通用方式被纳入考虑，以支持跨不同软件和硬件模型的可移植性。

## 英文关键词
OpenBSD, kernel lock, locks, mutual exclusion, operating systems, verification, model checking, weak memory models

## 中文关键词
OpenBSD，内核锁，锁，互斥，操作系统，验证，模型检查，弱内存模型

[返回 Session 25](index.md) · [返回 ATC 2026](../index.md)
