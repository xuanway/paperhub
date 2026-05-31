---
title: "Heliostat: 利用光线追踪加速器优化页表遍历"
description: "ISCA 2025论文解读：Heliostat将GPU中的RT核（光线追踪加速器）复用为页表遍历的BVH遍历引擎，显著加速地址翻译。"
tags: ["ISCA2025", "GPU", "光线追踪", "页表遍历", "TLB", "硬件复用"]
---

# Heliostat: Harnessing Ray Tracing Accelerators for Page Table Walks

**作者**：Yuan Feng, Jaewon Lee, Yehia Arafa, Abdulrahman Mahmoud, Abdulaziz Alameldeen, Manoj Gupta, Nishkam Ravi  
**机构**：San Jose State University, Yonsei University, Meta 等  
**会议**：ISCA 2025 · Session 1C: GPUs & Ray Tracing  

---

## 一句话总结

> GPU 地址翻译（页表遍历）在虚拟化和大内存工作负载下成为瓶颈；Heliostat 将 RT Core 的 BVH 遍历硬件复用为页表树的遍历引擎，加速地址翻译。

## 主要贡献

1. **RT-Core 复用**：将 BVH 层次结构映射到多级页表结构，用 RT Core 执行 Page Table Walk
2. **RTX 架构适配**：在 NVIDIA RTX 硬件架构上验证可行性
3. **与 TLB 协同**：与现有 TLB/MMU 微架构无缝集成

## 关键词

GPU · RT Core · 页表遍历 · 地址翻译 · ISCA 2025
