---
title: "Area Bloating and the Future of Specialization"
description: "HPCA 2026 · Accelerator Design and Modeling"
tags:
  - "HPCA2026"
  - "Accelerator Design and Modeling"
---

# Area Bloating and the Future of Specialization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Accelerator Design and Modeling。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Accelerator Design and Modeling</p>
</div>

**论文链接**：
**作者**：Qixuan Yu Princeton University , David Wentzlaff Princeton University
**会议**：HPCA 2026

---

## 中文标题

面积膨胀与专用化的未来

## 英文摘要

Throughout history, technology trends have greatly influenced the development of computer architecture. For the past decade, continuing transistor density scaling combined with stalling voltage scaling created great opportunities for specialization. As a step forward from multi-core processors, hardware accelerators make use of vastly available transistors by dedicating them to specific applications, in exchange for performance and energy efficiency. Unfortunately, the scaling of transistor size is now also slowing down. The complete failure of Moore’s Law will raise challenges and demand new approaches with specialization. In this work, we model technology scaling, accelerator scaling, and chip scaling to determine future demands of hardware acceleration in a collection of benchmarks for the next eight technology nodes. We show that if current approaches continue, area is becoming a major limiting factor of achievable performance. In a phenomenon we call area bloating, the area and hence manufacturing cost of chips can increase by at least 78.4× and 117.4× respectively from 3nm to A1.8 to match performance gain expectations like those in the past. 3D stacking can deliver more area under the same footprint, at the cost of multiplied power density. But for a limited number of layers, different from the dark silicon prediction, power density plateaus and silicon can be kept bright under liquid cooling. Architectural innovation is required to combat area bloating. We present several directions for future studies. Reduced levels of integration and reduced levels of specialization can help future accelerators adapt to these new trends. By adding limited generality to accelerators, reconfigurable specialization can combat area bloating in platform-specific SoCs, saving significant amounts of area. Future architectures must also consider longevity as chip lifetime increases as a result of slow adoption.

## 中文摘要

历史上，技术趋势深刻影响了计算机体系结构的发展。过去十年，晶体管密度持续微缩而电压微缩停滞，为专用化创造了巨大机遇。作为多核处理器的演进，硬件加速器把大量可用晶体管专用于特定应用，以换取性能与能效。遗憾的是，晶体管尺寸微缩如今也在放缓，摩尔定律的彻底失效将带来挑战，并要求专用化采用新方法。本工作对工艺、加速器与芯片微缩建模，在未来八个技术节点的一组基准上判断硬件加速的未来需求。我们表明，若沿用当前方法，面积正成为可达成性能的主要限制因素。我们将此现象称为面积膨胀：从 3nm 到 A1.8，为匹配以往那样的性能增益预期，芯片面积与制造成本至少分别增加 78.4 倍与 117.4 倍。3D 堆叠可在相同占位面积下提供更多面积，代价是功率密度成倍上升；但在层数有限时，与暗硅预测不同，功率密度趋于平台，硅片可在液冷下保持“明亮”。抵御面积膨胀需要架构创新，我们给出了若干未来研究方向：降低集成度与专用化程度有助于加速器适应新趋势；为加速器增加有限通用性（可重构专用化）可在特定平台 SoC 中节省大量面积；由于采用缓慢使芯片寿命延长，未来架构还须考虑长寿命。
