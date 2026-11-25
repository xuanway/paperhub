---
title: "Garen: Reliable Cluster Management with Atomic State Reconciliation"
description: "EuroSys 2026 · Fault Tolerance, Reliability & Debugging · Mingi Kim (FriendliAI), Ahnjae Shin (FriendliAI), Jaewoo Maeng (Samsung Advanced"
tags:
  - "EuroSys2026"
  - "Fault Tolerance, Reliability & Debugging"
---

# Garen: Reliable Cluster Management with Atomic State Reconciliation

**中文标题：** Garen：基于原子状态协调的可靠集群管理

**所属 Session：** [Session 4.3: Fault Tolerance, Reliability & Debugging](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Fault Tolerance, Reliability & Debugging。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Fault Tolerance, Reliability & Debugging</p>
</div>

**作者**：Mingi Kim (FriendliAI), Ahnjae Shin (FriendliAI), Jaewoo Maeng (Samsung Advanced Institute of Technology), Myeongjae Jeon (POSTECH), Byung-Gon Chun (FriendliAI, Seoul National University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769383)

## 英文摘要

Modern cluster managers orchestrate large-scale services and resources through a set of controllers, each managing a specific part of the cluster by iteratively reconciling the cluster states into the desired states. However, controllers are prone to various state inconsistencies stemming from asynchrony, concurrency, and failures, posing significant challenges in reliable cluster operation. Our analysis of 51 consistency bugs in Kubernetes controllers reveals that many issues remain unresolved, and even proposed fixes are often rejected for backward incompatibility or performance loss.

We present Garen, a system that implements atomic state reconciliation (ASR), a technique that ensures atomicity and consistency of reconciliation to protect the cluster against state inconsistencies. To achieve full-fledged ASR, Garen addresses several challenges. First, to ensure high scalability, Garen detects conflicts within the minimal states involved in the reconciliation process. To pinpoint this dynamically changing set of states, Garen decomposes the reconciliation logic into smaller, conditionally executed blocks. It then confines conflict detection to the states relevant to the involved blocks in a given reconciliation. Moreover, Garen ensures that all state transitions within ASR comply with dynamic cluster constraints by leveraging the dry-run feature to verify state transitions in advance, allowing for atomic execution. For stateful checks that can introduce races, Garen proposes an ASR-based execution model to prevent such races. Lastly, Garen transpiler automatically instruments existing controllers to use Garen, enhancing usability. Through real-world case studies, Garen resolves 18 previously unresolved consistency bugs without manual code changes. It also maintains scalability across various API request rates and cluster sizes, with a latency overhead under 3%.

## 中文摘要

现代集群管理器通过一组控制器来编排大规模服务与资源，每个控制器通过迭代地将集群状态协调至期望状态来管理集群的特定部分。然而，控制器容易因异步、并发和故障而产生各种状态不一致，给集群的可靠运行带来重大挑战。我们对Kubernetes控制器中51个一致性缺陷的分析表明，许多问题仍未解决，甚至提出的修复方案也常因向后不兼容或性能损失而被拒绝。

我们提出Garen，一个实现了原子状态协调（ASR）的系统。ASR是一种确保协调原子性与一致性的技术，可保护集群免受状态不一致的影响。为实现完整的ASR，Garen解决了若干挑战。首先，为保证高可扩展性，Garen仅在协调过程所涉及的最小状态集合内检测冲突。为精确定位这一动态变化的状态集合，Garen将协调逻辑分解为更小的、按条件执行的代码块，然后将冲突检测限定在给定协调中相关代码块所涉及的状态上。此外，Garen利用dry-run特性预先验证状态转换，确保ASR内的所有状态转换都符合动态集群约束，从而实现原子执行。对于可能引入竞态的有状态检查，Garen提出一种基于ASR的执行模型来防止此类竞态。最后，Garen转译器自动为现有控制器插桩以使用Garen，提升了易用性。通过真实案例研究，Garen在无需人工修改代码的情况下解决了18个此前未解决的一致性缺陷。它还在各种API请求速率和集群规模下保持可扩展性，延迟开销低于3%。

**英文关键词：** cluster management, reliability, scalability

**中文关键词：** 集群管理、可靠性、可扩展性

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
