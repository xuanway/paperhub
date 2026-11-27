---
title: "Compression-Aware Gradient Splitting for Collective Communications in Distributed Training"
description: "HPCA 2026 · Distributed and Multi-GPU Training"
tags:
  - "HPCA2026"
  - "Distributed and Multi-GPU Training"
---

# Compression-Aware Gradient Splitting for Collective Communications in Distributed Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Distributed and Multi-GPU Training。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Distributed and Multi-GPU Training</p>
</div>

**论文链接**：
**作者**：Pranati Majhi Texas A&M University , Sabuj Laskar Texas A&M University , Abdullah Muzahid Texas A & M University , Eun Jung Kim
**会议**：HPCA 2026

---

## 中文标题

面向分布式训练集合通信的压缩感知梯度拆分

## 英文摘要

While distributed training is crucial for scaling deep learning models, it incurs significant overhead due to the collective communication of gradients. To alleviate the burden, compression techniques are commonly used to improve network bandwidth utilization. However, compression poses challenges for synchronized AllReduce collective communications, even more so in scalable systems. Non-uniform data sizes resulting from compression can cause bandwidth under-utilization, as faster nodes remain idle while waiting for slower nodes to complete data exchanges, increasing overall communication and consequently, training time. However, the inherent similarity in gradients across consecutive batches presents an opportunity to mitigate these inefficiencies. By leveraging the quantization of gradients and consistent distribution of zeros, the gradients can be partitioned logically to speedup communication. Splitting them into groups with and without zeros can allow different compression approaches for both. The bandwidth under-utilization due to nonuniform data size can also be solved by partitioning the gradients into variable-sized chunks, leading to more balanced compressed data sizes and reduced idle waiting time. We propose two novel strategies in OSCAR, where gradient splitting is designed to improve communication and training. OSCAR-SW is a novel software-based technique supporting direct AllReduce that splits gradients into probable zeros and non zeros to apply count sketch compression. OSCAR-HW, a novel hardware/software codesigned gradient splitting technique is proposed with ASC (Adaptive Stepwise Coding), an encoding technique for gradient compression in distributed training. OSCAR-HW dynamically splits fixed-point quantized gradients for AllReduce communications and maximizes bandwidth utilization for state-of-the-art hardware compression techniques. ASC is a variant of Adaptive Arithmetic Coding (AAC) that generates a distinct probability table for each timestep of AllReduce to adapt to its unique value ranges and avoids sending the probability table during the communication of gradients. Our experimental results show that OSCAR-SW achieves 1.22× speedup and 7% better accuracy over the SOTA CountSketch algorithm. OSCAR-HW achieves an average AllReduce speedup of 3.77×, and an average end-to-end training speedup of 1.38×. ASC achieves an average AllReduce speedup of 1.05× over Atalanta and 4.66× over no compression.

## 中文摘要

分布式训练对扩展深度学习模型至关重要，但梯度的集合通信带来显著开销。压缩技术可提高网络带宽利用率，却给同步 AllReduce 通信带来挑战：压缩后数据大小非均匀造成带宽利用不足，较快节点空等较慢节点完成交换，延长通信与训练时间。相邻批次梯度的相似性提供了缓解机会：借助梯度量化与零值分布特性，可按逻辑划分梯度，拆成含零与不含零两组分别压缩；划分为变长块还能均衡压缩后大小、减少空闲等待。我们在 OSCAR 中提出两种梯度拆分策略：OSCAR-SW 是支持直接 AllReduce 的软件技术，把梯度拆为可能为零与非零的部分以应用 count sketch 压缩；OSCAR-HW 是软硬件协同设计的技术，配合编码方法 ASC（自适应逐步编码），动态拆分定点量化梯度以最大化最先进硬件压缩的带宽利用率；ASC 是自适应算术编码 AAC 的变体，为每个时间步生成不同概率表并免于在通信中发送该表。实验表明 OSCAR-SW 相比最先进的 CountSketch 算法取得 1.22 倍加速与 7% 更高精度；OSCAR-HW 取得平均 3.77 倍的 AllReduce 加速与 1.38 倍端到端训练加速；ASC 相对 Atalanta 与无压缩分别取得 1.05 倍与 4.66 倍加速。
