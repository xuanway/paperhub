# BPFFoundary: Scalable and Practical Multi eBPF Program Composition and Testing at Hyperscale

**中文标题**：BPFFoundary：超大规模下可扩展且实用的多 eBPF 程序组合与测试

**所属 Session**：[Session 24: Kernel Interfaces and Service Reliability](index.md) · [ATC 2026](../index.md)

**作者**：Prankur Gupta (Meta), Takshak Chahande (Meta), Miao Xu (Meta), Prashanth Kannan (Meta), Tejas Birajdar (Meta), Lilian Liu (Meta), Rajiv Krishnamurthy (Meta), Theophilus A. Benson (Carnegie Mellon University)

## 英文摘要
At scale, many eBPF programs developed by different teams must coexist on the same hosts (i.e., multi-tenancy) and share maps, across a fleet running varying kernel versions. Unfortunately, the interactions among these programs, their shared maps, and the kernel versions they run on can lead to failures and production incidents. More importantly, the kernel verifier does not check these interactions: they fall outside the notion of safety it enforces. We present BPFFoundary, a framework developed at Meta to provide two forms of safety: compositional safety, where BPFWeaver detects and arbitrates conflicts among programs and their shared maps, and emergent safety, where eBPF-CICD proactively exposes programs to a broad range of kernel versions, hardware, application traffic and edge cases to detect failures. Although these mechanisms provide fundamentally different forms of safety, managing eBPF programs at our scale requires both and so we developed BPFFoundary to address both. We have evaluated BPFFoundary across millions of hosts, and it is used by multiple teams. BPFWeaver has prevented 1,227 issues in a recent 30-day window, and eBPF-CICD has detected and prevented failures in 9.8–12.4% of eBPF releases in our host-networking pipelines.

## 中文摘要
在大规模场景下，不同团队开发的众多 eBPF 程序必须共存于同一批主机上（即多租户），并在运行不同内核版本的机群中共享 map。遗憾的是，这些程序、其共享 map 以及所运行的内核版本之间的交互可能导致故障和生产事故。更重要的是，内核验证器并不检查这些交互：它们落在验证器所施加的安全概念范围之外。我们提出 BPFFoundary，一个在 Meta 开发的框架，提供两种形式的安全：一是组合安全，由 BPFWeaver 检测并仲裁程序及其共享 map 之间的冲突；二是涌现安全，由 eBPF-CICD 主动让程序面对广泛的内核版本、硬件、应用流量和边界情况以检测故障。尽管这些机制提供的是根本不同形式的安全，但在我们的规模下管理 eBPF 程序二者皆需，因此我们开发了 BPFFoundary 以同时应对两者。我们在数百万台主机上评估了 BPFFoundary，它已被多个团队使用。BPFWeaver 在最近一个 30 天的窗口内阻止了 1,227 个问题，eBPF-CICD 在我们的主机网络流水线中检测并阻止了 9.8–12.4% 的 eBPF 发布中的故障。

## 英文关键词
eBPF, Network Management, Orchestration

## 中文关键词
eBPF，网络管理，编排

[返回 Session 24](index.md) · [返回 ATC 2026](../index.md)
