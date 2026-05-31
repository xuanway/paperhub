---
title: "LIA: 基于AMX的CPU-GPU协作与CXL卸载的单GPU LLM推理加速"
description: "ISCA 2025论文解读：LIA利用Intel AMX指令集加速CPU端LLM计算，配合CXL内存扩展，构建CPU-GPU协作的高效单节点LLM推理系统。"
tags: ["ISCA2025", "LLM推理", "CPU-GPU协作", "CXL", "Intel AMX", "UIUC"]
---

# LIA: A Single-GPU LLM Inference Acceleration with Cooperative AMX-Enabled CPU-GPU Computation and CXL Offloading

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">LIA 利用 Intel AMX（Advanced Matrix Extensions）使 CPU 能高效参与 LLM 矩阵运算，并通过 CXL 扩展内存容纳超大模型，构建单节点 CPU+GPU+CXL 协同的高效 LLM 推理系统。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · CPU-GPU协作 · Intel AMX · CXL内存扩展 · LLM推理 · UIUC</p>
</div>

**作者**：Hyungyo Kim, Nachuan Wang, Qirong Xia, Jinghan Huang, Amir Yazdanbakhsh, Nam Sung Kim  
**机构**：University of Illinois Urbana-Champaign (UIUC), Google  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 4A: LLMs  

---

## 一句话总结

> 单 GPU 无法装载超大 LLM；LIA 让 CPU 的 AMX 单元分担矩阵乘法，同时用 CXL 内存扩展模型容量，实现超出 GPU 显存限制的高效 LLM 推理。

## 背景与动机

- **单 GPU 容量瓶颈**：A100 80GB 无法容纳 70B+ 参数模型，需多卡或 CPU 协作
- **CPU 算力被忽视**：Intel SPR 的 AMX 单元有 TMUL 指令，矩阵乘能力相当于小型 GPU，但未被 LLM 框架利用
- **CXL 内存潜力**：CXL 2.0 连接的扩展内存提供 100+ GB 低延迟空间，可用于 KV Cache 和权重存储

## 主要贡献

1. **AMX-GPU 协同调度**：profiling 各 Transformer 层，按算力匹配分配到 CPU（AMX）或 GPU
2. **CXL 感知内存管理**：热权重留在 GPU VRAM，冷权重存 CXL 内存，异步预取隐藏延迟
3. **端到端系统实现**：基于 llama.cpp 和 PyTorch 的完整实现，支持 Llama-2 70B/140B

## 实验结果

- Llama-2-70B 在单节点（A100 + Xeon SPR + CXL）推理吞吐量比纯 GPU offloading 提升 **2.3×**
- GPU 利用率从 45% 提升至 **85%**

## 关键词

CPU-GPU协作 · Intel AMX · CXL内存 · LLM推理 · UIUC · ISCA 2025
