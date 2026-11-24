---
title: "DNA data storage: A generative tool for Motif-based DNA storage"
description: "FAST 2025 · Storage Diversity and Heterogeneity · 用 MDP 生成 DNA motif 集合，2.54 秒产出全部合规序列"
tags:
  - "FAST2025"
  - "Storage Diversity and Heterogeneity"
  - "DNA data storage"
  - "motif assembly"
---

# DNA data storage: A generative tool for Motif-based DNA storage

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">以 motif 而非单个碱基编码数据能提高 DNA 写入带宽、降低成本，但多 motif 拼接的化学过程容易生成二级结构或错误退火。本文把 motif 设计建模为马尔可夫决策过程，用逐碱基奖励统一 GC 含量、同聚物、发夹等约束，2.54 秒生成合规集合，对比方案均超时。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Storage Diversity and Heterogeneity</p>
</div>

**中文标题**：DNA 数据存储：面向基序编码 DNA 存储的生成式工具

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/brunmayr](https://www.usenix.org/conference/fast25/presentation/brunmayr)

**论文 PDF**：[fast25-brunmayr.pdf](https://www.usenix.org/system/files/fast25-brunmayr.pdf)

**作者**：Samira Brunmayr、Omer S. Sella、Thomas Heinis（Imperial College London）

**会议**：FAST 2025 · Santa Clara, CA · 第 573–581 页

**Session**：Storage Diversity and Heterogeneity · 2025-02-27 10:50–12:10 · Chair：Avani Wildani（Cloudflare and Emory University）

**所属 Session**：[Storage Diversity and Heterogeneity](index.md) · [FAST 2025](../index.md)

**关键词**：DNA data storage, motif assembly, Markov decision process, constrained sequence design, DNA synthesis, write bandwidth

---

## 英文摘要

DNA possesses extremely high information density and durability. In order to become a commercially viable medium such as magnetic tape and hard disk drives, the cost per bit has to decrease considerably, while the write bandwidth needs to increase. Both are governed by DNA synthesis, the process of writing data to DNA, which is currently very expensive and slow. Assembly of DNA strands from motifs, i.e. short DNA sequences, is an economical and faster way of representing data using DNA. Each motif carries a letter in an alphabet. Trading the quaternary alphabet {A,C,T,G} for longer fragments, namely motifs, allows an increase in write bandwidth and reduces cost. The success of the underlying chemistry, specifically with the assembly of motifs into polymers that faithfully represent the source binary data, is sensitive to the formation of secondary structures and the correct annealing of the motifs in a unique way. In this work, we develop a mathematical framework and a method to generate a set of motifs that agree with a predefined set of constraints regardless of the order they are combined. The set of constraints can also be easily adjusted to align with technological advances and their evolving requirements. We show that our approach generates motifs that always conform to the constraints in a more efficient manner than previous works and randomly generated motifs.

## 中文摘要

DNA 具有极高的信息密度与耐久性。要成为像磁带与硬盘那样可商用的介质，每比特成本必须大幅下降、写入带宽必须提升；这两者都由 DNA 合成——即把数据写入 DNA 的过程——决定，而该过程目前非常昂贵且缓慢。用 motif（短 DNA 序列）拼装 DNA 链是一种更经济、更快速的 DNA 数据表示方式：每个 motif 承载字母表中的一个字符，用更长的片段（即 motif）替代 {A,C,T,G} 四元字母表，即可提高写入带宽并降低成本。拼接化学的成功——特别是把 motif 拼装成能忠实表示源二进制数据的聚合物——对二级结构的形成以及 motif 以唯一方式正确退火十分敏感。本文提出一套数学框架与生成方法，生成一组无论以何种顺序组合都满足预定义约束的 motif；约束集合也可随技术进步及其不断变化的需求轻松调整。本文表明，该方法总能生成符合约束的 motif，且比已有工作与随机生成的 motif 更高效。

## 一句话总结

> 把 motif 设计写成逐碱基的奖励采样：越接近约束边界惩罚越重，于是键与载荷无论怎么拼接都合法。

## 研究背景与问题

- **写入成本卡住 DNA 存储**：DNA 密度可达 10¹⁸ 字节/mm³、半衰期 500 年，适合长期归档；但按 2 bit/base 计算，用当前合成技术写入 1 TB 数据要超过 4 亿美元（400 million USD）。
- **motif 拼接是更便宜的写路径**：把 {A,C,T,G} 四元字母表换成更长的 motif，用 PCR 预先批量生产，靠桥接退火与连接把 motif 拼成聚合物，合成只用于起池，写入带宽更高、成本更低。
- **化学过程对序列敏感**：拼接要求载荷可唯一识别、键只与指定桥接互补，同时要满足 GC 含量上下界、避免二级结构与发夹、避免同聚物、避开保留字与限制性位点；随机生成几乎不可能同时满足，已有编码方案也难以在任意组合下保证合法。
- **切入点**：把约束做成可加权的逐碱基奖励，用随机采样生成键与载荷，再用独立校验器验证任意拼接顺序下的合法性。

## 核心贡献

- **MDP 形式化**：把 motif（键与载荷）的构造写成马尔可夫决策过程，每添加一个碱基是一次动作。
- **统一奖励函数**：为每类生物约束定义一个非正 log score，加权求和后经归一化得到四种碱基的采样概率。
- **生成工具**：按给定约束批量生成键与载荷，并保证无论以何种顺序拼接都满足约束。
- **可校验、可演进**：配套校验工具遍历拼接组合验证约束；约束集合以参数表描述，可随合成与测序技术进步调整。

## 方法与技术要点

- **逐碱基构造**：载荷从空串开始，每一步对 A/T/C/G 计算奖励并归一化为类别分布，按概率采样下一个碱基，达到设定长度后提交并开始下一条，直到无法再构造合规载荷。
- **奖励设计**：log score 非正且随违反程度单调上升；同聚物项按最长同聚物长度与 maxHom 的比值衰减，GC 项同时考虑当前组合可达到的最大与最小 GC 含量。
- **约束参数**：依据商用合成与测序能力取 maxHom = 5、发夹环长 6 到 7、maxHairpin = 1、GC 含量 25% 到 65%、键长 20 bp、载荷 60 bp，使 motif 最长 100 bp 且载荷占比不低于 60%。
- **工具与校验**：生成器与校验器分别发布，校验器对给定 motif 集合检查任意两条或多条拼接后的序列是否仍满足全部约束。
- **参数调优**：用两轮网格搜索确定超参数，在四核 Intel 机器上给 5 分钟预算生成一组 motif。

## 评估与主要结果

- **约束内生成时间**：在 5 分钟预算内，只有本文工具成功生成满足全部约束的 motif 集合，耗时 2.54 秒；DNA Fountain、Euclid、Preuss 等人的 shortmer 方案与随机生成均超过 5 分钟仍未生成。
- **无约束生成对照**：不加约束时本文工具耗时 2.3×10⁻² 秒，DNA Fountain 为 1.22×10⁻¹ 秒，Preuss 方案为 5.30×10⁻¹ 秒，随机生成为 2.1×10⁻³ 秒，但这些序列无法直接用于拼接。
- **设计余量**：键 20 bp、载荷 60 bp 使单个 motif 最多 100 bp，处于可合成、可测序范围内，且载荷仍占总 DNA 的 60% 以上。

[返回 Storage Diversity and Heterogeneity](index.md) · [返回 FAST 2025](../index.md)
