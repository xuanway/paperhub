---
title: "Unified Memory Protection with Multi-granular MAC and Integrity Tree for Heterogeneous Processors"
description: "ISCA 2025论文解读：为异构处理器（CPU+GPU+加速器）设计统一内存保护方案，通过多粒度MAC和完整性树保证所有处理器对内存访问的安全性。"
tags: ["ISCA2025", "内存保护", "MAC", "完整性树", "异构处理器", "KAIST"]
---

# Unified Memory Protection with Multi-granular MAC and Integrity Tree for Heterogeneous Processors

**作者**：Sunho Lee, Seonjin Na, Jeongwon Choi, Jinwon Pyo, Jaehyuk Huh  
**机构**：KAIST  
**会议**：ISCA 2025 · Session 10C: Security  

---

## 一句话总结

> CPU、GPU、加速器共享内存时各自的安全粒度不同；本文设计统一的多粒度 MAC 和完整性树方案，在统一框架内支持异构处理器的内存安全保护。

## 主要贡献

1. **多粒度 MAC**：不同处理器按访问粒度生成不同尺寸的 MAC，共享验证树
2. **统一完整性树**：设计跨异构处理器的 Merkle 树结构，支持并发更新
3. **低开销实现**：缓存 MAC 和树节点减少验证延迟

## 关键词

内存保护 · MAC · 完整性树 · 异构处理器 · KAIST · ISCA 2025
