---
title: "HR-DCIM: High-Reliability Floating-Point Digital CIM Architecture with Unified Low-Cost Iterative Error Correction"
description: "HPCA 2026 · Memory System Reliability"
tags:
  - "HPCA2026"
  - "Memory System Reliability"
---

# HR-DCIM: High-Reliability Floating-Point Digital CIM Architecture with Unified Low-Cost Iterative Error Correction

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Memory System Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Memory System Reliability</p>
</div>

**论文链接**：
**作者**：Zhen He Tsinghua University , Yiqi Wang Tsinghua University , Zhiheng Yue Tsinghua University , Zihan Wu Tsinghua University , Huiming Han Tsinghua University , Shaojun Wei Tsinghua University , Yang Hu Tsinghua University , Fengbin Tu The Hong Kong University of Science and Technology , Shouyi Yin Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

HR-DCIM：具有统一低成本迭代纠错的高可靠浮点数字存内计算架构

## 英文摘要

Digital computing-in-memory (CIM) is a promising computing paradigm for the neural network (NN) acceleration. However, during the actual deployment process of digital CIM chips, we find that existing digital CIM designs face severe computing reliability issues, which are crucial for real product development but remain underexplored. Therefore, this work pioneers a systematic computing reliability analysis for digital CIM across off-memory and in-memory levels. We find that both the off-memory floating-point (FP) exponent alignment and the in-memory random cell bit-flip errors impair digital CIM’s computing reliability, causing significant truncation and bit-flip accuracy loss. Critically, existing reliability solutions are incompatible with the unique multi-row accumulation structure of digital CIM, which either severely damage digital CIM’s performance or result in prohibitive overhead. To address above challenges, we propose HR-DCIM: a high-reliability FP digital CIM architecture featuring unified low-cost iterative error correction. Specifically, for the off-memory reliability, we propose an exponent-mantissa joint-alignment mechanism to repurpose inherent invalid bits of aligned mantissas as compensation bits to reduce alignment truncation loss, without damaging digital CIM’s performance. Then, for the in-memory reliability, we propose a remainder aliasing-based unified multiply-accumulation (MAC) error correction mechanism to correct possible MAC errors caused by various cell error cases with low-cost iteration. Experimental results show that the proposed techniques enable digital CIM to maintain high performance and efficiency across various operating voltage conditions without significant accuracy loss.

## 中文摘要

数字存内计算（CIM）是加速神经网络（NN）的一种颇具前景的计算范式。然而在数字 CIM 芯片的实际部署过程中，我们发现现有数字 CIM 设计面临严重的计算可靠性问题，这对真实产品研发至关重要却仍研究不足。因此，本工作率先对数字 CIM 开展跨内存外与内存内的系统性计算可靠性分析。我们发现，内存外的浮点（FP）指数对齐与内存内的单元随机位翻转错误都会损害数字 CIM 的计算可靠性，造成显著的截断与位翻转精度损失。关键在于，现有可靠性方案与数字 CIM 特有的多行累加结构不兼容，要么严重损害其性能，要么带来难以承受的开销。为应对上述挑战，我们提出 HR-DCIM：一种具备统一低成本迭代纠错的高可靠浮点数字 CIM 架构。具体而言，针对内存外可靠性，我们提出指数—尾数联合对齐机制，将已对齐尾数中固有的无效位重新用作补偿位，以降低对齐截断损失且不损害数字 CIM 的性能。随后针对内存内可靠性，我们提出基于余数混叠的统一乘累加（MAC）纠错机制，以低成本迭代纠正各类单元错误情形可能导致的 MAC 错误。实验结果表明，所提技术使数字 CIM 在多种工作电压条件下均能保持高性能与高效率，且无显著精度损失。
