---
title: "TrustWeave: Integrity Measurement and Attestation For Multi-Cloud LLMs"
description: "EuroSys 2026 · Security, Privacy & Vulnerabilities · Jianchang Su (University of Connecticut), Wenhui Zhang (Independent Researcher),"
tags:
  - "EuroSys2026"
  - "Security, Privacy & Vulnerabilities"
---

# TrustWeave: Integrity Measurement and Attestation For Multi-Cloud LLMs

**中文标题：** TrustWeave：面向多云 LLM 的完整性度量与证明

**所属 Session：** [Session 8.2: Security, Privacy & Vulnerabilities](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security, Privacy & Vulnerabilities。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security, Privacy & Vulnerabilities</p>
</div>

**作者**：Jianchang Su (University of Connecticut), Wenhui Zhang (Independent Researcher), Yifan Zhang (University of Connecticut), Kexin Chu (University of Connecticut), Hao Guo (Tsinghua University), Youyou Lu (Tsinghua University), Wei Zhang (University of Connecticut)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803586)

## 英文摘要

Multi-cloud deployed multi-agent systems powered by Large Language Models (LLMs) introduce critical security challenges. While Intel Trust Domain Extensions (TDX)-based Confidential Virtual Machines (CVMs) provide strong isolation and boot-time attestation, they lack dynamic runtime integrity verification, a capability essential for trusted agent systems that frequently load new models and coordinate across distributed services. We present TrustWeave, a runtime integrity measurement and attestation framework that extends the Linux Integrity Measurement Architecture (IMA) with support for Intel TDX’s Runtime Measurement Registers (RTMRs). TrustWeave enables userspace attestation of dynamically loaded agent components throughout their lifecycle, providing runtime trust guarantees for secure and scalable LLM agent deployments.

Our key innovation is a workload-aware filtering mechanism that reduces measurement overhead by 99.95% while preserving security coverage for agent-critical operations. Our evaluation on production agent workloads using five models (0.6B-14B parameters) demonstrates practical performance: 0.8-12.8% boot overhead (reducible to <10% with filtering), Time-to-First-Token (TTFT) degradation around 25% of baseline, and stable QPS scaling up to 32 concurrent requests. TrustWeave introduces operationally acceptable overhead for security-sensitive deployments, maintaining model inference accuracy with bounded boot and runtime latency, while providing runtime attestation for dynamically loaded applications.

## 中文摘要

由大语言模型（LLM）驱动的多云部署多智能体系统带来了关键的安全挑战。虽然基于 Intel 信任域扩展（TDX）的机密虚拟机（CVM）提供了强隔离和启动时证明，但它们缺乏动态的运行时完整性验证，而这对于频繁加载新模型并跨分布式服务协调的可信智能体系统至关重要。我们提出 TrustWeave，一个运行时完整性度量与证明框架，它扩展了 Linux 完整性度量架构（IMA）以支持 Intel TDX 的运行时度量寄存器（RTMR）。TrustWeave 使动态加载的智能体组件在其整个生命周期内可进行用户空间证明，为安全且可扩展的 LLM 智能体部署提供运行时信任保证。

我们的关键创新是一种工作负载感知的过滤机制，它将度量开销降低 99.95%，同时保持对智能体关键操作的安全覆盖。我们在使用五种模型（0.6B–14B 参数）的生产智能体工作负载上进行评估，展示了实用的性能：启动开销 0.8–12.8%（通过过滤可降至 <10%），首令牌时间（TTFT）下降约基线的 25%，QPS 可稳定扩展至 32 个并发请求。TrustWeave 为安全敏感部署引入了在运营上可接受的开销，在保持模型推理准确率的同时限制了启动和运行时延迟，并为动态加载的应用提供运行时证明。

**英文关键词：** Trusted Execution Environment, Integrity Measurement Architecture, Runtime Attestation, LLM Security

**中文关键词：** 可信执行环境、完整性度量架构、运行时证明、LLM 安全

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
