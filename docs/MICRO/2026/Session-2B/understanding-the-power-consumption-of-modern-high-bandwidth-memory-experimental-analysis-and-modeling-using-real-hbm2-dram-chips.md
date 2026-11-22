---
title: "Understanding the Power Consumption of Modern High Bandwidth Memory: Experimental Analysis and Modeling Using Real HBM2 DRAM Chips"
description: "MICRO 2026 · Session 2B · 理解现代高带宽内存的功耗：基于真实 HBM2 DRAM 芯片的实验分析与建模"
tags:
  - "MICRO2026"
  - "DRAM"
  - "Energy Efficiency"
---

# Understanding the Power Consumption of Modern High Bandwidth Memory: Experimental Analysis and Modeling Using Real HBM2 DRAM Chips

**中文标题：** 理解现代高带宽内存的功耗：基于真实 HBM2 DRAM 芯片的实验分析与建模

**所属 Session：** [Session 2B](index.md) · [MICRO 2026](../index.md)

**作者：** Ataberk Olgun, Spiros Galanopoulos, Andreas Kosmas Kakolyris, İsmail Emir Yüksel, Haocong Luo, F. Nisa Bostanci, Onur Mutlu

**来源：** MICRO 2026，pp. 553–571；[DOI](https://doi.org/10.1109/MICRO67795.2026.00052)

## 英文摘要

We perform the first comprehensive experimental characterization of power consumed by real HBM2 DRAM chips. Our extensive characterization of 36 HBM2 chips yields 1) the empirical basis for developing new, accurate HBM power models or validating existing power models and 2) key insights into structural and data-pattern-dependent variation of power in HBM2 chips. Out of our 12 new findings and 6 key takeaway messages, we highlight: 1) read operation consumes higher current than any other tested operation including refresh (by 3.1X), 2) HBM2 read current significantly varies across bank groups (by 8.1%) and banks (by 5.3%), and 3) the toggled data bus signals in a data transfer burst both significantly affect current draw. For example, toggling all HBM2-internal bank group bus signals causes 29.4% higher current consumption than keeping them constant. Leveraging our empirical insights into HBM2 power consumption, we carefully engineer an access pattern that yields 23.6% (35.4%) higher power consumption on average (maximum) across all tested HBM2 chips than the highest-power-consuming JEDEC-specified current measurement loop. Our results have important implications for HBM-based system design and validation. For example, relying solely on JEDEC-or vendor-specified test loops to bound HBM power could cause errors or system failures, thermal throttling, and thermal shutdowns in real-world high-power, high-performance computing or AI/ML workloads. To improve 3D-stacked DRAM power modeling fidelity in open source architectural simulation infrastructure, we develop a new HBM power model, guided by our characterization and built on DRAMPower, that captures structural and data-pattern-dependent power variation. Our model predicts the power of 36 real HBM2 chips across diverse workloads (including a real LLM decode workload) with 8.6% mean absolute percentage error, substantially more accurately than state-of-the-art HBM power models (with error between 20-21%). We validate our model against real HBM3E GPU memory power consumption. The power consumption predicted by our model for a power-intensive microbenchmark closely matches (7% error) the average memory power consumed by three tested NVIDIA H200 GPUs. We use the power model to project the read energy of future HBM4 chips. We publicly release our power model at https://github.com/CMU-SAFARI/HBM-Power.

## 中文摘要

我们首次对真实 HBM2 DRAM 芯片的功耗进行了全面的实验表征。我们对 36 个 HBM2 芯片进行了广泛的表征，得出 1) 开发新的、准确的 HBM 功耗模型或验证现有功耗模型的经验基础，以及 2) 对 HBM2 芯片中结构和数据模式相关的功耗变化的关键见解。在我们的 12 个新发现和 6 个关键要点中，我们强调：1) 读取操作消耗的电流比任何其他测试操作（包括刷新）消耗的电流更高（3.1 倍），2) HBM2 读取电流在存储体组（8.1%）和存储体（5.3%）之间存在显着差异，3）数据传输突发中的切换数据总线信号都会显着影响电流消耗。例如，切换所有 HBM2 内部组总线信号会导致比保持它们恒定的电流消耗高 29.4%。利用我们对 HBM2 功耗的经验洞察，我们精心设计了一种访问模式，在所有测试的 HBM2 芯片上，该模式的平均功耗（最大值）比最高功耗的 JEDEC 指定电流测量环路高出 23.6%（35.4%）。我们的结果对于基于 HBM 的系统设计和验证具有重要意义。例如，仅依靠 JEDEC 或供应商指定的测试循环来限制 HBM 功率可能会导致现实世界的高功率、高性能计算或 AI/ML 工作负载中出现错误或系统故障、热节流和热关闭。为了提高开源架构仿真基础设施中 3D 堆叠 DRAM 功率建模的保真度，我们开发了一种新的 HBM 功率模型，该模型以我们的特性为指导并以 DRAMPower 为基础构建，可捕获结构和数据模式相关的功率变化。我们的模型预测了 36 个真实 HBM2 芯片在不同工作负载（包括真实 LLM 解码工作负载）中的功率，平均绝对百分比误差为 8.6%，比最先进的 HBM 功率模型（误差在 20-21% 之间）准确得多。我们根据真实的 HBM3E GPU 内存功耗验证我们的模型。我们的模型针对功耗密集型微基准测试预测的功耗与三个测试的 NVIDIA H200 GPU 消耗的平均内存功耗非常匹配（误差为 7%）。我们使用功耗模型来预测未来 HBM4 芯片的读取能量。我们在 https://github.com/CMU-SAFARI/HBM-Power 公开发布我们的电源模型。

## 中文关键词

高带宽内存；HBM2；功耗测量；实验分析；功耗建模

## 代码与研究制品

- 代码仓库：[https://github.com/CMU-SAFARI/HBM-Power](https://github.com/CMU-SAFARI/HBM-Power)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21531486](https://doi.org/10.5281/zenodo.21531486)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2B](index.md) · [MICRO 2026 主页](../index.md)
