---
title: "InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference"
description: "HPCA 2025 · Viva Las Learning Models"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models"
---

# InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models</p>
</div>

**论文链接**：
**作者**：Xiurui Pan (Peking University), Endian Li (Peking University), Qiao Li (Xiamen University), Shengwen Liang (Institute of Computing Technology, Chinese Academy of Sciences), Yizhou Shan (Huawei Cloud), Ke Zhou (Wuhan National Laboratory for Optoelectronics (WNLO) of Huazhong University of Science and Technology (HUST)), Yingwei Luo (Peking University), Xiaolin Wang (Peking University), Jie Zhang (Peking University)
**会议**：HPCA 2025

---

## 中文标题

InstAttention：面向经济高效长上下文 LLM 推理的存储内注意力卸载

## 英文摘要

The widespread of Large Language Models (LLMs) marks a significant milestone in generative AI. Nevertheless, the increasing context length and batch size in offline LLM inference escalate the memory requirement of the key-value (KV) cache, which imposes a huge burden on the GPU VRAM, especially for resource-constrained scenarios (e.g., edge computing). Several cost-effective solutions leverage host memory or SSDs to reduce storage costs for offline inference scenarios and improve the throughput. Nevertheless, they suffer from significant performance penalties imposed by intensive KV cache accesses due to limited PCIe bandwidth. To address these issues, we propose InstAttention, a novel LLM inference system that offloads the most performance-critical computation (i.e., attention in decoding phase) and data (i.e., KV cache) parts to Computational Storage Drives (CSDs), which minimize the enormous KV transfer overheads. InstAttention designs a dedicated flash-aware in-storage attention engine with KV cache management mechanisms to exploit the high internal bandwidths of CSDs instead of being limited by the PCIe bandwidth. The optimized P2P transmission between GPU and CSDs further reduces data migration overheads. Experimental results demonstrate that for a 13B model using an NVIDIA A6000 GPU, InstAttention improves throughput for long-sequence inference by up to 11.1×, compared to existing SSD-based solutions such as FlexGen.

## 中文摘要

大语言模型（LLM）的广泛应用标志着生成式 AI 的一个重要里程碑。然而，离线 LLM 推理中不断增长的上下文长度和批大小加剧了键值（KV）缓存的内存需求，给 GPU 显存带来巨大负担，在资源受限的场景（如边缘计算）中尤为突出。若干经济高效的方案利用主机内存或 SSD 来降低离线推理场景的存储成本并提升吞吐。然而，受限于有限的 PCIe 带宽，密集的 KV 缓存访问会带来显著的性能损失。为解决这些问题，我们提出 InstAttention，一种新颖的 LLM 推理系统，它将对性能最关键的计算（即解码阶段的注意力）和数据（即 KV 缓存）卸载到计算存储盘（CSD），从而最大限度地减少庞大的 KV 传输开销。InstAttention 设计了专用的闪存感知存储内注意力引擎及 KV 缓存管理机制，以利用 CSD 的高内部带宽，而不受 PCIe 带宽的限制。GPU 与 CSD 之间优化的 P2P 传输进一步降低了数据迁移开销。实验结果表明，对于使用 NVIDIA A6000 GPU 的 13B 模型，与 FlexGen 等现有基于 SSD 的方案相比，InstAttention 将长序列推理的吞吐最高提升 11.1 倍。
