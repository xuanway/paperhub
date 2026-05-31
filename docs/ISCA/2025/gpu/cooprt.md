---
title: "CoopRT: 通过协作线程加速BVH遍历"
description: "ISCA 2025论文解读：CoopRT让多个GPU线程协作执行单个光线的BVH遍历，通过负载均衡解决光线遍历路径差异导致的warp分歧问题。"
tags: ["ISCA2025", "GPU", "光线追踪", "BVH遍历", "协作线程", "NCSU"]
---

# CoopRT: Accelerating BVH Traversal for Ray Tracing via Cooperative Threads

**作者**：Yavuz Selim Tozlu, Huiyang Zhou  
**机构**：NC State University (NCSU)  
**会议**：ISCA 2025 · Session 1C: GPUs & Ray Tracing  

---

## 一句话总结

> GPU 光线追踪中不同光线的 BVH 遍历路径长度差异巨大，导致严重的 warp 分歧；CoopRT 让 warp 内线程协作遍历同一根光线的 BVH，消除分歧。

## 主要贡献

1. **协作遍历模型**：warp 内线程分组共同遍历同一光线的 BVH 路径
2. **动态协作组**：根据遍历深度动态调整协作组大小
3. **warp 分歧消除**：协作执行消除了不同光线路径长度导致的 divergence

## 实验结果

- 典型光线追踪场景性能提升 **1.4–2.1×**

## 关键词

光线追踪 · BVH遍历 · GPU · 协作线程 · Warp分歧 · NCSU · ISCA 2025
