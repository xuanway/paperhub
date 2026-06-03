---
title: "zkVC: Fast Zero-Knowledge Proof for Private and Verifiable Computing"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "zero-knowledge-proof"
  - "matrix-multiplication"
  - "zksnark"
  - "verifiable-computing"
---

# zkVC: Fast Zero-Knowledge Proof for Private and Verifiable Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC1。针对可验证计算中矩阵乘法 ZKP 的证明生成效率瓶颈，提出 zkVC——通过约束缩减多项式电路（CRPC）和前缀和查询（PSQ）两个模块，相比此前 zkSNARK 方法实现 >12× 证明生成加速。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Zero-Knowledge Proof · Matrix Multiplication · zkSNARK · Verifiable Computing</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | zkVC: Fast Zero-Knowledge Proof for Private and Verifiable Computing（zkVC：面向隐私可验证计算的快速零知识证明） |
| 作者 | Yancheng Zhang, Mengxin Zheng, Yan Solihin, Qian Lou (UCF), Xun Chen (Samsung), Jingtong Hu (Pitt), Weidong Shi (UH), Lei Ju (山东大学) |
| 机构 | UCF / Samsung Research America / Pitt / Houston / 山东大学 |
| 领域 | AI/ML 安全 / ZKP |
| 投稿方向 | Security（Session: SEC1） |
| 关键词 | 零知识证明(ZKP)、矩阵乘法(Matrix Multiplication)、zkSNARK、可验证计算(Verifiable Computing) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132681) · [GitHub: UCF-Lou-Lab-PET/zkformer](https://github.com/UCF-Lou-Lab-PET/zkformer) |

---

## 一、一句话核心摘要

> 在客户端-服务器场景中，客户端将矩阵乘法外包给不可信服务器，需要零知识证明来验证计算结果——但矩阵乘法的 ZKP 证明生成极为昂贵。zkVC 通过两个创新模块大幅加速：**CRPC**（约束缩减多项式电路）将矩阵乘法的 R1CS 约束数显著压缩；**PSQ**（前缀和查询）加速验证阶段的求和聚合。两者结合实现 >12× 于此前 zkSNARK 方法的证明生成加速。

---

## 二、核心方法

### 2.1 CRPC：约束缩减多项式电路

- 针对矩阵乘法中大量重复的同构约束（矩阵每个元素乘法产生相同形式的 R1CS 约束）
- 通过多项式电路将多组约束"折叠"为单组 → 约束数大幅降低 → 证明生成加速

### 2.2 PSQ：前缀和查询

- 矩阵乘法的验证需要累加大量点积结果
- PSQ 用 O(logN) 的查询复杂度替代 O(N) 的逐元素验证

### 2.3 实验结果

| 指标 | 结果 |
|------|------|
| **证明生成加速** | **>12×** vs 此前 zkSNARK 方法 |
| 引用 | FWCI=5.67（前 10%），已被 2 篇论文引用 |
| 代码 | GitHub 开源 |

---

## 三、总结

zkVC 将矩阵乘法的 ZKP 证明生成从"昂贵到不可用"推进到"可实用"——对 zkML（零知识机器学习推理）和 zkRollup 等需要大规模矩阵运算证明的场景具有直接的应用价值。

**核心资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11132681) · [GitHub](https://github.com/UCF-Lou-Lab-PET/zkformer)
