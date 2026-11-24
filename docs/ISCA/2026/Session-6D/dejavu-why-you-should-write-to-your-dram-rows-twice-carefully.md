---
title: "DejaVu: Why You Should Write to Your DRAM Rows Twice, Carefully"
description: "ISCA 2026 · Session 6D · DejaVu: Why You Should Write to Your DRAM Rows Twice, Carefully"
tags:
  - "ISCA2026"
  - "Session 6D"
  - "Rowhammer and Security"
---

# DejaVu: Why You Should Write to Your DRAM Rows Twice, Carefully

**中文标题：** DejaVu: 为何应当谨慎地对 DRAM 行写入两次

**所属 Session：** [Session 6D](index.md) · [ISCA 2026](../index.md)

**作者：** Haocong Luo, İsmail Emir Yüksel, Ataberk Olgun, Nisa Bostanci, Orhun Ecemiş, Abdullah Giray Yaglikci, Onur Mutlu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

We provide the first experimental demonstration of DejaVu, a phenomenon where the data previously written to DRAM cells affects DRAM’s vulnerability to read disturbance. Our experimental characterization using 112 commercial-off-the-shelf DDR4 DRAM chips from all three major manufacturers shows that, compared to the baseline where we initialize the victim row by writing to it only once, 1) initializing the victim row by overwriting the victim row with the opposite data (compared to what was previously written) reduces ACmin (the minimum aggressor row activation count to induce at least one bitflip; a lower ACmin means higher vulnerability to read disturbance), and 2) initializing the victim row by writing the same data twice increases ACmin. We provide two hypotheses to explain DejaVu. First, we hypothesize that overwriting the victim row with the opposite data values causes the under-restoration of charge in the DRAM cells. Second, we hypothesize that the process of overwriting the victim row changes the charge trap states in the active region, affecting the read-disturbance-induced cell leakage current. We conduct controlled experimental characterization to provide insight into these two hypotheses. To further investigate DejaVu’s potential impact on the current passing capability of the DRAM cell access transistors, we characterize the reliability of Processing-Using-DRAM (PUD) operations with DRAM rows initialized with DejaVu patterns. Our experimental characterization of 32-row MAJ-3 operation shows that by overwriting the DRAM rows used in the operation, the number of bitlines that fail to reliably perform MAJ-3 reduces by 32.7% on average compared to the baseline where the rows are written only once. We hypothesize that DejaVu’s effects make the distribution of the current passing capabilities of the access transistors of DRAM cells more uniform compared to the baseline. Based on our observations, we describe two major implications of DejaVu. We provide an example of how DRAM testing and characterization methodologies should take DejaVu into consideration to 1) accurately characterize the read disturbance vulnerability of DRAM rows under fixed data patterns, and 2) rigorously study the effect of different data patterns on read disturbance by avoiding unintended interference from DejaVu. We also evaluate the additional performance overhead of read disturbance mitigation techniques when their read disturbance thresholds need to be lowered to be secure against DejaVu and show that they induce higher performance overheads (e.g., 6.3% performance overhead when reducing the read disturbance threshold by 20% as a guardband to mitigate DejaVu).

## 中文摘要

我们首次通过实验展示了 DejaVu 现象：先前写入 DRAM 单元的数据会影响 DRAM 对读干扰的易感性。我们使用来自三大厂商的 112 颗商用 DDR4 DRAM 芯片进行的实验表征表明，与仅写入一次来初始化受害行的基线相比，1) 用相反数据（相对于此前写入的内容）覆盖受害行来初始化，会降低 ACmin（诱发至少一个位翻转所需的最小攻击行激活次数；ACmin 越低意味着对读干扰的易感性越高），2) 通过将相同数据写入两次来初始化受害行会提高 ACmin。我们提出两种假设来解释 DejaVu。第一，我们假设用相反数据值覆盖受害行会导致 DRAM 单元中电荷的欠恢复。第二，我们假设覆盖受害行的过程会改变有源区中的电荷陷阱态，从而影响读干扰引起的单元漏电流。我们进行了受控实验表征，以深入探究这两种假设。为进一步研究 DejaVu 对 DRAM 单元访问晶体管电流通过能力的潜在影响，我们表征了使用 DejaVu 模式初始化的 DRAM 行的存内处理（PUD）操作的可靠性。我们对 32 行 MAJ-3 操作的实验表征显示，通过覆盖操作中使用的 DRAM 行，无法可靠执行 MAJ-3 的位线数量相比仅写入一次的基线平均减少 32.7%。我们假设 DejaVu 效应使 DRAM 单元访问晶体管电流通过能力的分布相比基线更加均匀。基于我们的观察，我们描述了 DejaVu 的两个主要影响。我们给出了一个示例，说明 DRAM 测试与表征方法应如何考虑 DejaVu，以便 1) 在固定数据模式下准确表征 DRAM 行的读干扰易感性，2) 通过避免 DejaVu 的意外干扰来严格研究不同数据模式对读干扰的影响。我们还评估了当读干扰缓解技术的读干扰阈值需要降低以抵御 DejaVu 时的额外性能开销，并表明这会带来更高的性能开销（例如，当把读干扰阈值降低 20% 作为缓解 DejaVu 的保护带时，性能开销为 6.3%）。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [实验材料归档（Zenodo 19444878）](https://zenodo.org/records/19444878)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6D](index.md) · [返回 ISCA 2026](../index.md)
