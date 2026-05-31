---
title: "Palermo: 高性能Oblivious Memory"
description: "HPCA 2025论文解读：Palermo通过协议-硬件协同设计改进Oblivious Memory（ORAM）的性能，将ORAM访问延迟降低3×以上，使隐私保护内存访问在实际系统中可行。"
tags: ["HPCA2025", "硬件安全", "ORAM", "Oblivious Memory", "协议硬件协同", "Michigan"]
---

# Palermo: Improving the Performance of Oblivious Memory using Protocol-Hardware Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Palermo 重新设计 ORAM 协议以适应硬件加速，通过批处理 ORAM 请求、流水线化 Eviction 操作和硬件辅助随机洗牌，将 Path ORAM 的访问延迟降低 3×+，使 ORAM 在实际系统中首次具备可用性。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Oblivious Memory · ORAM · 隐私保护 · 体系结构安全 · University of Michigan</p>
</div>

**作者**：Haojie Ye, Yuchen Xia, Yuhan Chen, Kuan-Yu Chen, Yichao Yuan, Shuwen Deng, Baris Kasikci, Trevor Mudge, Nishil Talati  
**机构**：University of Michigan; Tsinghua University; University of Washington and Google  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> Oblivious RAM（ORAM）是隐藏内存访问模式的关键技术，但标准 Path ORAM 带来 20～100× 的访问延迟开销；Palermo 通过协议与硬件协同重设计，将这一开销压缩至 3～7×。

## 背景与动机

- **ORAM 的必要性**：云计算中，即使数据已加密，攻击者仍可通过观察内存访问地址推断敏感信息（地址泄露攻击）
- **Path ORAM 的开销**：标准 Path ORAM 每次访问需要读写一条从根到叶的路径（O(log N) 次内存访问），同时维护随机位置映射表（Position Map）和临时存储区（Stash）
- **硬件加速的机会**：现有 ORAM 硬件加速（Intel SGX 的 PPML 等）只是直接实现 Path ORAM 协议，未对协议本身做硬件友好的改造

## 方法详解

### 协议层优化

**Batched Path Eviction**：
- 将多个 ORAM 请求的 Eviction 操作合批处理，每次 Eviction 覆盖多条路径
- 减少 Eviction 频率，降低总内存带宽消耗

**Lazy Position Update**：
- 延迟更新 Position Map，使多个逻辑地址的重映射操作合并完成
- 减少 Position Map 访问次数（原方案每次访问需读写两次 Position Map）

### 硬件层优化

- **并行路径读取**：多 Bank 内存控制器同时读写 ORAM 树的多条路径
- **硬件随机数生成器**：芯片内 TRNG 加速随机地址生成，消除软件伪随机数开销
- **Stash 管理单元**：专用硬件搜索和管理 Stash，避免 CPU 介入

## 实验结果

| 指标 | Path ORAM | Palermo | 改进 |
|------|-----------|---------|------|
| 访问延迟（N=1M） | 18μs | 5.2μs | 3.5× |
| 内存带宽放大 | 30× | 8× | 3.75× |
| SQLITE 吞吐 | 0.08× | 0.22× | 2.75× |

## 核心亮点

1. 首次通过协议-硬件协同设计大幅降低 ORAM 开销
2. Batched Eviction 策略对工作负载局部性自适应，热点数据几乎无额外开销
3. 兼容 Intel SGX 等现有可信执行环境

## 局限性

- 批处理策略引入延迟抖动，对实时应用不友好
- Stash 溢出概率需要仔细参数调整
