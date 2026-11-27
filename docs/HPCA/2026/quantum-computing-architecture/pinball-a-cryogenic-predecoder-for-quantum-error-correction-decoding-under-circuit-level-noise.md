---
title: "Pinball: A Cryogenic Predecoder for Quantum Error Correction Decoding Under Circuit-Level Noise"
description: "HPCA 2026 · Quantum Computing Architecture"
tags:
  - "HPCA2026"
  - "Quantum Computing Architecture"
---

# Pinball: A Cryogenic Predecoder for Quantum Error Correction Decoding Under Circuit-Level Noise

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Computing Architecture。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Computing Architecture</p>
</div>

**论文链接**：
**作者**：Alexander Knapen University of Michigan , Guanchen Tao University of Michigan , Jacob Mack University of Michigan , Tomas Bruno University of Michigan , Mehdi Saligane Brown University , Dennis Sylvester University of Michigan , Qirui Zhang University of Michigan , Gokul Subramanian Ravi University of Michigan
**会议**：HPCA 2026

---

## 中文标题

Pinball：面向电路级噪声下量子纠错译码的低温预译码器

## 英文摘要

Scaling fault tolerant quantum computers, especially cryogenic systems based on the surface code, to millions of qubits is very challenging due to poorly-scaling data processing and power consumption overheads. One key challenge is the design of decoders for real-time quantum error correction (QEC), which demands high data rates for error processing; this is particularly apparent in systems with cryogenic qubits and room temperature (RT) decoders. In response, cryogenic predecoding using lightweight logic has been proposed to handle common, sparse errors within the cryogenic domain. However, prior work only accounts for a subset of the error sources present in real-world quantum systems with limited accuracy, often degrading performance below a useful level in practical scenarios. Furthermore, prior reliance on SFQ logic precludes detailed architecture-technology co-optimization. To address these shortcomings, this paper introduces Pinball1, a comprehensive design in cryogenic CMOS of a QEC predecoder for the surface code, tailored to realistic, circuit-level noise. By accounting for error generation and propagation through QEC circuits, our design achieves higher predecoding accuracy, outperforming logical error rates of the current state-of-the-art cryogenic predecoder by nearly six orders of magnitude. Remarkably, despite operating under much stricter power and area constraints, Pinball also reduces logical error rates by 32.58× and 5×, respectively, compared to the state-of-the-art RT predecoder and an RT ensemble configuration. By increasing cryogenic coverage, we also reduce syndrome bandwidth up to 3780.72×. Through co-design with 4 K-characterized 22 nm FDSOI technology, we achieve a peak power consumption under 0.56 mW. Voltage/frequency scaling and body biasing enable 22.2× lower typical power consumption, yielding up to 67.4× total energy savings. Assuming a 4 K power budget of 1.5 W, our predecoder can support up to 2,668 logical qubits at d = 21.

## 中文摘要

将容错量子计算机（尤其是基于表面码的低温系统）扩展到数百万量子比特极具挑战，原因是数据处理与功耗开销的扩展性很差。关键挑战之一是为实时量子纠错（QEC）设计译码器，其错误处理需要高数据率；这在具有低温量子比特与室温（RT）译码器的系统中尤为明显。已有工作提出用轻量逻辑进行低温预译码，以在低温域内处理常见的稀疏错误。但此前工作只考虑了真实系统中部分错误源，精度有限，在实际场景中常把性能降到可用水平以下；其依赖 SFQ 逻辑的做法也妨碍了细致的架构—工艺协同优化。为此本文提出 Pinball，一个在低温 CMOS 中实现的、面向表面码且针对真实电路级噪声的 QEC 预译码器完整设计。通过考虑 QEC 线路中的错误产生与传播，我们的设计获得更高的预译码精度，逻辑错误率优于当前最先进的低温预译码器近六个数量级。尽管功耗与面积约束严格得多，Pinball 相比最先进的 RT 预译码器与一种 RT 集成配置仍分别将逻辑错误率降低 32.58 倍与 5 倍；扩大低温覆盖范围还可将校验子带宽最多降低 3780.72 倍。借助与 4 K 表征的 22 nm FDSOI 工艺协同设计，峰值功耗低于 0.56 mW；电压/频率缩放与体偏置使典型功耗降低 22.2 倍，总能耗最多节省 67.4 倍。在 4 K 下 1.5 W 的功耗预算内，预译码器在 d = 21 时可支持多达 2,668 个逻辑量子比特。
