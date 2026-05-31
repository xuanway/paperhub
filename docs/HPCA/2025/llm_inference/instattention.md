---
title: "InstAttention: 存储卸载超长上下文LLM推理"
description: "HPCA 2025论文解读：InstAttention将LLM的KV Cache卸载到NVMe SSD，通过In-Storage计算减少主机-存储数据传输，实现超长上下文（100K+ tokens）的高效LLM推理。"
tags: ["HPCA2025", "LLM推理", "KV Cache", "长上下文", "In-Storage计算", "NVMe", "北京大学"]
---

# InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">InstAttention 将超长上下文 LLM 推理的 KV Cache 卸载到 NVMe SSD，并在 SSD 内部的计算单元上直接执行 Attention Score 计算，避免将大量 KV Cache 数据传输到 GPU，使 100K+ tokens 的长上下文推理吞吐提升 2×+。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · 长上下文 LLM · KV Cache · In-Storage Attention · NVMe · 北京大学</p>
</div>

**作者**：Xiurui Pan, Endian Li, Qiao Li, Shengwen Liang, Yizhou Shan, Ke Zhou, Yingwei Luo, Xiaolin Wang, Jie Zhang  
**机构**：Peking University; Xiamen University; ICT CAS; Huawei Cloud; HUST  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> 长上下文 LLM 推理（100K+ tokens）的 KV Cache 超过 GPU HBM 容量，需卸载到 SSD；但 KV Cache 数据传输量巨大（每 Token 需读取全量 KV Cache）；InstAttention 通过在 SSD 内直接计算 Attention，将传输量减少 90%+。

## 背景与动机

- **KV Cache 内存压力**：LLaMA-2-70B 处理 100K tokens 的 KV Cache 约为 320GB，远超单 GPU HBM 容量（80GB A100）
- **SSD 卸载的带宽瓶颈**：NVMe SSD 读带宽约 7GB/s，将 320GB KV Cache 全量传回 GPU 需要 45s，不可接受
- **In-Storage 计算的机会**：现代 CSD（Computational Storage Drive）配备 ARM 核心，可在 SSD 内部执行 Attention Score 计算（$QK^T$），只将最终 Attention 输出（远小于 KV Cache）传回 GPU

## InstAttention 设计

### KV Cache 分层存储

- GPU HBM：存储当前层最新的 KV Cache（约 4K tokens）
- Host DRAM：存储近期 KV Cache（约 16K tokens）
- NVMe SSD：存储全量历史 KV Cache（100K+ tokens）

### In-Storage Attention 计算

- SSD ARM 核心执行：$\text{Score} = \text{softmax}(Q \cdot K^T / \sqrt{d_k})$（Flash Attention 分块实现）
- 只将最终 Attention Output $O = \text{Score} \cdot V$ 传回 GPU
- 数据传输量从 O(seq_len × d_model) 降低到 O(batch × d_model)

### 前缀感知优化

- 对相同前缀的多个请求共享 SSD 中的 KV Cache
- 引用计数管理 KV Cache 生命周期，避免冗余写入

## 实验结果

| 指标 | GPU+DRAM (OOM) | Offload-GPU | InstAttention | 
|------|----------------|-------------|---------------|
| 100K tokens 推理吞吐 | 不可行 | 基线 | 2.3× |
| 主机-SSD 数据传输量 | — | 320GB | 28GB | 
| 端到端延迟（单请求） | — | 基线 | 0.43× |

## 核心亮点

1. 首次在商用 CSD 上实现 LLM In-Storage Attention，无需专用硬件
2. 数据传输量减少 91%，真正突破 SSD 带宽瓶颈
3. 前缀共享优化对 RAG（检索增强生成）等场景效果显著

## 局限性

- SSD ARM 核心计算能力有限，对很长的 Attention（>512K tokens）SSD 成为计算瓶颈
- 写放大问题：频繁追加 KV Cache 对 SSD 寿命有一定影响
