---
title: "Let-Me-In: (Still) Employing In-pointer Bounds metadata for Fine-grained GPU Memory Safety"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# Let-Me-In: (Still) Employing In-pointer Bounds metadata for Fine-grained GPU Memory Safety

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Jaewon Lee (Georgia Institute of Technology), Euijun Chung (Georgia Institute of Technology), Saurabh Singh (Georgia Institute of Technology), Seonjin Na (Georgia Institute of Technology), Yonghae Kim (Intel), Jaekyu Lee (Arm), Hyesoon Kim (Georgia Institute of Technology)
**会议**：HPCA 2025

---

## 中文标题

Let-Me-In：仍采用指针内边界元数据实现细粒度 GPU 内存安全

## 英文摘要

The importance of ensuring the robustness of GPU systems has grown significantly, especially as GPUs have become vital in critical decision-making systems such as autonomous driving and medical diagnostics. However, GPU programming languages, primarily based on C/C++, inherit memory vulnerabilities that threaten the robustness of GPU applications. The heterogeneous GPU memory hierarchy makes it more difficult to find effective universal solutions. While several studies have proposed advanced GPU memory safety mechanisms, they still grapple with significant challenges, including substantial metadata storage and access overhead, elevated hardware implementation costs, and limited security coverage, particularly regarding fine-grained memory safety. We address this issue with Let-Me-In (LMI), a fine-grained memory safety mechanism specifically designed for GPUs. LMI features an efficient hardware bounds-checking mechanism that ensures negligible impact on performance and hardware costs, even in scenarios where thousands of concurrent threads perform memory operations across buffers in heap and local memory. This is achieved by aligning memory allocation to powers of two and performing static analysis to identify and mark pointer arithmetic instructions. This approach also enables storing metadata inside the unused upper bits of pointers, which are shrinking due to the expansion of the virtual memory address space. The unique characteristics of GPU programs make this approach feasible, unlike in CPU programs, where the inherent complexity of programs poses challenges. Our evaluation shows that LMI incurs only negligible hardware and performance overhead, making it a practical and efficient solution for enhancing GPU memory safety.

## 中文摘要

随着 GPU 在自动驾驶、医学诊断等关键决策系统中变得至关重要，确保 GPU 系统健壮性的重要性显著提升。然而，主要基于 C/C++ 的 GPU 编程语言继承了内存漏洞，威胁 GPU 应用的健壮性；GPU 异构的内存层次结构更使寻找有效的通用方案难上加难。已有研究提出了多种先进的 GPU 内存安全机制，但它们仍面临元数据存储与访问开销可观、硬件实现成本高昂，以及安全覆盖范围有限（尤其在细粒度内存安全方面）等重大挑战。为此，我们提出 Let-Me-In（LMI），一种专为 GPU 设计的细粒度内存安全机制。LMI 具备高效的硬件边界检查机制，即使在数千个并发线程对堆内存与本地内存中的缓冲区执行内存操作的场景下，也能将性能与硬件成本的影响控制在可忽略的水平。这通过将内存分配对齐到 2 的幂，并借助静态分析识别和标记指针算术指令来实现。该方法还允许将元数据存放在指针未使用的最高位中，而这些位正随着虚拟内存地址空间的扩展而不断减少。GPU 程序的独特特性使该方案可行，而在 CPU 程序中，程序固有的复杂性则带来挑战。评测表明，LMI 的硬件与性能开销均可忽略，是增强 GPU 内存安全的一种实用而高效的解决方案。
