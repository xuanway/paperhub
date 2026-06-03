---
title: "ZK-Hammer: Leaking Secrets from Zero-Knowledge Proofs via Rowhammer"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "zero-knowledge-proof"
  - "rowhammer"
  - "fault-injection"
  - "zk-snark"
---

# ZK-Hammer: Leaking Secrets from Zero-Knowledge Proofs via Rowhammer

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC3。首次证明 zk-SNARK 方案可通过 Rowhammer 故障注入攻击泄漏秘密——通过 Rowhammer 注入故障到 QAP（二次算术程序）的指数变量中，利用双线性配对分析"错误证明"恢复秘密，已在 libsnark 上验证，发现 3 个 CVE。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Zero-Knowledge Proof · Rowhammer · Fault Injection · zk-SNARK · CVE</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | ZK-Hammer: Leaking Secrets from Zero-Knowledge Proofs via Rowhammer（ZK-Hammer：通过 Rowhammer 泄漏零知识证明中的秘密） |
| 作者 | Junkai Liang, Xin Zhang, Daqi Hu, Qingni Shen, Yuejian Fang, Zhonghai Wu |
| 机构 | 北京大学 |
| 领域 | 硬件安全 / ZKP 安全 |
| 投稿方向 | Security（Session: SEC3） |
| 关键词 | 零知识证明(ZKP)、Rowhammer、故障注入(Fault Injection)、zk-SNARK、双线性配对(Bilinear Pairing) |
| 核心资源 | [IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133021) |

---

## 一、一句话核心摘要

> 零知识证明的数学安全性是密码学可证明的——但其**物理实现的可靠性**完全是另一回事。ZK-Hammer 揭示了 zk-SNARK 的一个致命物理攻击面：通过 Rowhammer（反复激活 DRAM 行导致邻近行比特翻转）注入故障到证明生成的 QAP 指数变量中，攻击者收集"错误证明"后通过双线性配对导数分析恢复原始秘密（witness），已在 libsnark 上实际验证并发现 3 个 CVE。

---

## 二、核心方法

### 2.1 攻击流程

1. **Rowhammer 故障注入**：在证明生成过程中对存储 QAP 指数变量的 DRAM 区域实施 Rowhammer，触发比特翻转
2. **收集错误证明**：受害者产生含有故障的 zk-SNARK 证明
3. **双线性配对分析**：利用正确/错误证明的配对差异，通过代数攻击恢复秘密输入

### 2.2 为什么这是"悖论式"攻击？

ZKP 的核心安全假设是**"验证者从证明中学不到任何秘密"**。ZK-Hammer 打破了这一假设的实现层前提——不是从数学上攻破了 ZKP，而是从物理上让 ZKP 的计算过程**产生了不该有的信息泄露**。

### 2.3 结果

| 指标 | 结果 |
|------|------|
| 目标库 | libsnark |
| CVE 发现 | **3 个** |
| 攻击类型 | 首个 zk-SNARK Rowhammer 攻击 |

---

## 三、总结

ZK-Hammer 将两个看似不相关的领域——DRAM 故障注入和零知识证明——进行了交叉攻击。这提醒我们：密码协议的数学安全性不等于系统安全性。

**相关资源**：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133021)
