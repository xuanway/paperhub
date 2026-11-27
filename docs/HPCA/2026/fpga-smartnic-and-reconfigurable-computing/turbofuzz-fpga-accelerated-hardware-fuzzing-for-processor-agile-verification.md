---
title: "TurboFuzz: FPGA Accelerated Hardware Fuzzing for Processor Agile Verification"
description: "HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing"
tags:
  - "HPCA2026"
  - "FPGA, SmartNIC, and Reconfigurable Computing"
---

# TurboFuzz: FPGA Accelerated Hardware Fuzzing for Processor Agile Verification

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: FPGA, SmartNIC, and Reconfigurable Computing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing</p>
</div>

**论文链接**：
**作者**：Yang Zhong Institute of Computing, Chinese Academy of Sciences , Haoran Wu University of Cambridge , Xueqi Li State Key Lab of Processors, Institute of Computing Technology, CAS , Sa Wang SKLP, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences , David Boland The University of Sydney , Yungang Bao State Key Lab of Processors, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences , Kan Shi Institute of Computing, Chinese Academy of Sciences
**会议**：HPCA 2026

---

## 中文标题

TurboFuzz：面向处理器敏捷验证的 FPGA 加速硬件模糊测试

## 英文摘要

Verification is a critical process for ensuring the correctness of modern processors. The increasing complexity of processor designs and the emergence of new instruction set architectures (ISAs) like RISC-V have created demands for more agile and efficient verification methodologies, particularly regarding verification efficiency and faster coverage convergence. While simulation-based approaches now attempt to incorporate advanced software testing techniques such as fuzzing to improve coverage, they face significant limitations when applied to processor verification, notably poor performance and inadequate test case quality. Hardware-accelerated solutions using FPGA or ASIC platforms have tried to address these issues, yet they struggle with challenges including host-FPGA communication overhead, inefficient test pattern generation, and suboptimal implementation of the entire multi-step verification process. In this paper, we present TurboFuzz, an end-to-end hardware-accelerated verification framework that implements the entire Test Generation-Simulation-Coverage Feedback loop on a single FPGA for modern processor verification. TurboFuzz enhances test quality through optimized test case (seed) control flow, efficient inter-seed scheduling, and hybrid fuzzer integration, thereby improving coverage and execution efficiency. Additionally, it employs a feedback-driven generation mechanism to accelerate coverage convergence. Experimental results show that TurboFuzz achieves up to 2.23× more coverage collection than software-based fuzzers within the same time budget, and up to 571× performance speedup when detecting real-world issues, while maintaining full visibility and debugging capabilities with moderate area overhead.

## 中文摘要

验证是确保现代处理器正确性的关键环节。处理器设计复杂度不断提升，加之 RISC-V 等新指令集架构（ISA）的出现，对更敏捷、更高效的验证方法学提出需求，尤其在验证效率与覆盖率收敛速度方面。基于仿真的方法如今尝试引入模糊测试等先进软件测试技术以提升覆盖率，但在处理器验证中面临明显局限，特别是性能差、测试用例质量不足。使用 FPGA 或 ASIC 平台的硬件加速方案试图解决这些问题，却仍受制于主机与 FPGA 之间的通信开销、测试激励生成低效以及整个多步验证流程实现不佳等挑战。本文提出 TurboFuzz，一个端到端的硬件加速验证框架，在现代处理器验证中将完整的测试生成—仿真—覆盖率反馈闭环实现在单块 FPGA 上。TurboFuzz 通过优化的测试用例（种子）控制流、高效的种子间调度和混合模糊器集成来提升测试质量，从而改善覆盖率与执行效率；同时采用反馈驱动的生成机制加速覆盖率收敛。实验结果表明，在相同时间预算内，TurboFuzz 的覆盖率收集量最高为基于软件的模糊器的 2.23 倍；在检测真实问题时性能加速最高达 571 倍，同时以适中的面积开销保持完整的可见性与调试能力。
