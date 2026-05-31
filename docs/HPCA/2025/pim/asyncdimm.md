---
title: "AsyncDIMM: DIMM近内存处理异步执行"
description: "HPCA 2025论文解读：AsyncDIMM提出DIMM近内存处理(NMP)的异步执行框架，解决主机CPU与DIMM处理单元之间的同步开销问题，实现更高效的计算卸载。"
tags: ["HPCA2025", "PIM", "近内存计算", "DIMM", "异步执行", "NMP", "上海交通大学"]
---

# AsyncDIMM: Achieving Asynchronous Execution in DIMM-Based Near-Memory Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">AsyncDIMM 识别出 DIMM-Based NMP 的核心瓶颈：主机 CPU 在每次卸载操作后必须同步等待 DIMM 完成，造成大量 CPU 空闲等待。AsyncDIMM 提出异步卸载执行模型，允许 CPU 在 DIMM 执行期间继续计算，大幅提升系统整体利用率。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · PIM · DIMM-Based NMP · 异步执行 · 计算卸载 · 上海交通大学</p>
</div>

**作者**：Liyan Chen, Dongxu Lyu, Jianfei Jiang, Qin Wang, Zhigang Mao, Naifeng Jing  
**机构**：Shanghai Jiao Tong University  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> DIMM 近内存处理（如三星 HBM-PIM、SK Hynix AiME）通常要求主机 CPU 在卸载操作后同步等待，造成 CPU 空转；AsyncDIMM 通过异步执行原语和依赖追踪，让 CPU 与 DIMM 真正并行工作。

## 背景与动机

- **DIMM-NMP 的部署现状**：商用 DIMM-NMP 产品（三星 HBM-PIM、SK Hynix AiME）已支持矩阵向量乘（GeMV）等操作下推到 DIMM 端执行
- **同步等待瓶颈**：现有 NMP 卸载模型为"请求-响应"式：CPU 发送卸载命令，等待 DIMM 返回完成信号，期间 CPU 空闲
- **并行化机会**：许多 DNN 工作负载中，DIMM-NMP 计算（访存密集操作）与 CPU 计算（计算密集操作）可以并行执行

## AsyncDIMM 设计

### 异步卸载原语

- **async_offload(op, args, tag)**：向 DIMM 卸载操作，立即返回标签，不等待完成
- **async_sync(tag)**：在依赖点等待指定标签完成
- **async_poll(tag)**：非阻塞查询指定标签是否完成

### 依赖追踪硬件

- CPU 侧维护卸载操作的 DAG（有向无环图）
- 自动检测 CPU 计算与 DIMM 操作之间的数据依赖
- 在依赖存在时才插入同步点，无依赖时允许完全并行

### 内存一致性

- 卸载操作期间，被操作的内存区域进入"DIMM-exclusive"状态
- CPU 尝试访问该区域时自动等待，保证数据一致性

## 实验结果

（以 BERT-Large 推理为代表工作负载）

| 指标 | 同步 DIMM-NMP | AsyncDIMM | 提升 |
|------|-------------|-----------|------|
| 端到端延迟 | 基线 | 0.62× | 1.61× |
| CPU 利用率 | 34% | 81% | 2.38× |
| DIMM 利用率 | 68% | 72% | 1.06× |

## 核心亮点

1. 将 DIMM-NMP 从"串行卸载"升级为"并行协同"，系统级效率提升显著
2. 硬件依赖追踪保证正确性，不引入程序员负担
3. 兼容现有商用 DIMM-NMP 硬件，仅需内存控制器扩展

## 局限性

- 对数据流不规则的工作负载（稀疏访存），依赖关系复杂，异步化收益有限
- 多 DIMM 场景下的异步调度开销需要进一步优化
