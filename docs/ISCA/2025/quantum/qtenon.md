---
title: "Qtenon: 低延迟架构集成加速混合量子-经典计算"
description: "ISCA 2025论文解读：Qtenon提出低延迟经典-量子接口架构，通过紧耦合集成减少混合量子-经典算法中的通信开销。"
tags: ["ISCA2025", "量子计算", "混合量子-经典", "低延迟", "PKU"]
---

# Qtenon: Towards Low-Latency Architecture Integration for Accelerating Hybrid Quantum-Classical Computing

**作者**：Chenning Tao, Liqiang Lu, Size Zheng, Li-Wen Chang, Minghua Shen, Hanyu Zhang, Fangxin Liu, Kaiwen Zhou, Jianwei Yin  
**机构**：Peking University, ICTS 等  
**会议**：ISCA 2025 · Session 3A: Quantum I  

---

## 一句话总结

> VQE、QAOA 等混合量子-经典算法需要频繁的量子-经典数据交换；Qtenon 设计低延迟紧耦合接口架构，最小化量子测量到经典参数更新的往返延迟。

## 主要贡献

1. **紧耦合接口设计**：量子控制器与经典处理器共享片上互联，消除 PCIe 通信延迟
2. **流水线执行**：重叠量子电路执行与经典参数优化计算
3. **延迟分解分析**：识别混合算法瓶颈（测量延迟 vs. 经典优化延迟）
4. **系统实现**：在超导量子平台上验证

## 关键词

混合量子经典 · 低延迟接口 · VQE · QAOA · PKU · ISCA 2025
