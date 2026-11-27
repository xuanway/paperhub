---
title: "ER-DCIM: Error-Resilient Digital CIM with Run-Time MAC-Cell Error Correction"
description: "HPCA 2025 · Doubling Down with PIM"
tags:
  - "HPCA2025"
  - "Doubling Down with PIM"
---

# ER-DCIM: Error-Resilient Digital CIM with Run-Time MAC-Cell Error Correction

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Doubling Down with PIM。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Doubling Down with PIM</p>
</div>

**论文链接**：
**作者**：Zhen He (Tsinghua University), Yiqi Wang (Tsinghua University), Zihan Wu (Tsinghua University), Shaojun Wei (Tsinghua University), Yang Hu (Tsinghua University), Fengbin Tu (The Hong Kong University of Science and Technology), Shouyi Yin (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

ER-DCIM：具备运行时 MAC 单元纠错的容错数字存内计算

## 英文摘要

Digital computing-in-memory (CIM) is an emerging solution to break through the limitations of memory wall by integrating digital logic into SRAM, which is able to achieve high area and energy efficiency with no accuracy loss. Digital CIM’s SRAM cells are still prone to errors like conventional SRAM due to noise and variation, especially under low-voltage operation for high energy efficiency. The SRAM cell errors cause multiply-accumulation (MAC) result errors, which may seriously damage the neural network inference accuracy. However, traditional SRAM’s error correcting code (ECC) that corrects errors in one read-out row is incompatible with digital CIM, which reads out multiple rows simultaneously for computation. Detecting and correcting computational MAC errors and SRAM cell errors (i.e., MAC-cell errors) in digital CIM remain largely unexplored. To address digital CIM’s unique MAC-cell error resilience needs, we propose ER-DCIM, an error-resilient digital CIM with run-time MAC-cell error correction to guarantee computation correctness. The proposed residue code-based MAC error correction mechanism is the first to correct additive errors in the MAC result in real time during DCIM computation. Then, we propose a progressive cell error correction mechanism to correct underlying cell error in a timely manner, avoiding performance loss due to stalling computation. Further, we design a mode switcher to repurpose redundant error-resilient logic reserved for low-voltage mode to improve performance in high-voltage mode. Experimental results show that the proposed techniques enable digital CIM to maintain high throughput and energy efficiency without accuracy loss in both low-voltage and high-voltage modes.

## 中文摘要

数字存内计算（CIM）通过将数字逻辑集成进 SRAM，能够以无精度损失的方式实现高面积效率与高能效，是突破内存墙限制的新兴方案。数字 CIM 的 SRAM 单元与常规 SRAM 一样，仍会因噪声与工艺偏差而出错，尤其是在为追求高能效而采用低电压工作时。SRAM 单元错误会造成乘累加（MAC）结果错误，可能严重损害神经网络的推理精度。然而，传统 SRAM 中用于纠正单次读出整行错误的纠错码（ECC）与数字 CIM 不兼容，因为后者会同时读出多行以完成计算。如何检测并纠正数字 CIM 中的计算 MAC 错误与 SRAM 单元错误（即 MAC 单元错误）在很大程度上仍未被探索。为应对数字 CIM 独特的 MAC 单元容错需求，我们提出 ER-DCIM，一种具备运行时 MAC 单元纠错能力、以保证计算正确性的容错数字 CIM。所提出的基于余数码的 MAC 纠错机制首次在 DCIM 计算过程中实时纠正 MAC 结果中的加性错误。随后，我们提出渐进式单元纠错机制，及时纠正底层的单元错误，避免因停顿计算而造成性能损失。进一步，我们设计了模式切换器，将原本为低电压模式预留的冗余容错逻辑重新利用，以提升高电压模式下的性能。实验结果表明，所提出的技术使数字 CIM 在低电压与高电压模式下均能在无精度损失的情况下保持高吞吐与高能效。
