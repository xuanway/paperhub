---
title: "Forest: 访问感知的GPU统一虚拟内存管理"
description: "ISCA 2025论文解读：Forest通过分析GPU内存访问模式实现访问感知的UVM（统一虚拟内存）管理策略，降低页面迁移开销。"
tags: ["ISCA2025", "GPU", "UVM", "统一虚拟内存", "页面迁移", "Rutgers"]
---

# Forest: Access-aware GPU UVM Management

**作者**：Mao Lin, Rachata Ausavarungnirun, Chris Rossbach, Feng Cheng, Ketan Bhardwaj, Hyesoon Kim  
**机构**：Rutgers University, Georgia Tech 等  
**会议**：ISCA 2025 · Session 1C: GPUs & Ray Tracing  

---

## 一句话总结

> GPU UVM 自动管理 CPU-GPU 数据迁移，但当前策略忽视访问模式，导致大量不必要的页面迁移；Forest 利用访问模式分析优化迁移决策。

## 主要贡献

1. **访问模式分类**：识别 GPU 工作负载的访问热度分布（热/冷/间歇）
2. **动态迁移策略**：根据访问模式自适应调整迁移阈值和预取策略
3. **减少抖动**：通过稳定迁移决策避免页面在 CPU 和 GPU 之间频繁来回

## 关键词

GPU · UVM · 统一虚拟内存 · 页面迁移 · 访问感知 · ISCA 2025
