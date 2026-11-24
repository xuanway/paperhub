# Astragalus: Automatic Configuration Repair for Production Networks

**中文标题**：Astragalus：面向生产网络的自动配置修复

**所属 Session**：[Session 27: Performance Diagnosis and Operational Repair](index.md) · [ATC 2026](../index.md)

**作者**：Zhenrong Gu (Xi'an Jiaotong University), Peng Zhang (Xi'an Jiaotong University), Xing Feng (Xi'an Jiaotong University), Xu Liu (Xi'an Jiaotong University)

## 英文摘要
Network configurations are prone to errors, which can lead to catastrophic service outages. A tool that can achieve automatic configuration repair (ACR) is highly desired by operators. Existing tools for ACR follow a semantics-driven approach: they model network semantics as a set of SMT constraints, and solve them for a location or fix of the error. Due to the complex semantics of networks, constructing and solving these constraints can be prohibitively expensive, making these tools neither general nor scalable. Inspired by automatic program repair (APR), we explore another direction, i.e., a syntax-driven approach, which generates and validates syntactically-valid candidate updates without modeling program semantics, often drawing on existing code in the same repository. Following this direction, we propose Astragalus, a syntax-driven method for ACR. It uses multiple iterations of a “localize-fix-validate” pipeline to search for repairs, and proves quite effective on configurations of our production network. Specifically, we show that Astragalus can repair every incident in multiple sizes of a synthesized network, and 97.5% of the incidents on a real network, both with 15 types of errors injected, within an average time of 6.93 seconds. It has also provided valid repairs in under 6 minutes for 7 recent network incidents or undesired changes, in a real production network with O(1,000)∼O(10,000) devices.

## 中文摘要
网络配置容易出错，而这些错误可能导致灾难性的服务中断。运维人员非常需要一种能够实现自动配置修复（ACR）的工具。现有的 ACR 工具遵循语义驱动的方法：它们将网络语义建模为一组 SMT 约束，并求解以获得错误的位置或修复方案。由于网络语义复杂，构造和求解这些约束的代价可能高得难以承受，使这些工具既不具备通用性也不具备可扩展性。受自动程序修复（APR）的启发，我们探索了另一个方向，即语法驱动的方法：它在不建模程序语义的情况下生成并验证语法上合法的候选更新，通常借鉴同一代码库中已有的代码。沿着这一方向，我们提出 Astragalus，一种语法驱动的 ACR 方法。它使用多轮“定位—修复—验证”流水线来搜索修复方案，并在我们生产网络的配置上表现得相当有效。具体而言，我们展示 Astragalus 能够修复一个合成网络在多种规模下的每一起故障，以及真实网络中 97.5% 的故障（两者均注入 15 种类型的错误），平均耗时 6.93 秒。在一个设备规模为 O(1,000)∼O(10,000) 的真实生产网络中，它还在 6 分钟内为最近 7 起网络故障或非预期变更提供了有效修复。

## 英文关键词
network configuration, automatic configuration repair, automatic program repair, network verification

## 中文关键词
网络配置，自动配置修复，自动程序修复，网络验证

[返回 Session 27](index.md) · [返回 ATC 2026](../index.md)
