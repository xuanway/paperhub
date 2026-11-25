TRAC: Transparent Row Activation Counting for Efficient Rowhammer Monitoring
Authors：
[Sunggi Ahn](https://63dac.conference-program.com/?post_type=page&p=15&uid=97088661338775682951)，[Saeid Gorgin](https://63dac.conference-program.com/?post_type=page&p=15&uid=17164130674600935311)，[Jungrae Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=9871976239999900833)

## 中文标题

TRAC：面向高效 Rowhammer 监控的透明行激活计数

## 英文摘要

RowHammer is one of the most critical security threats in modern DRAM. The industry has introduced Per-Row Activation Counting (PRAC) to monitor activations, but this approach degrades performance by lengthening critical DRAM timing parameters. We propose TRAC (Transparent Row Activation Counting), a lightweight monitoring architecture that eliminates these drawbacks. TRAC leverages ACT-triggered update, robust in-subarray processing, and a Linear Feedback Shift Register (LFSR)-based counter to track activations transparently, without introducing timing overhead. Circuit-level simulations and system-level evaluations demonstrate TRAC’s correctness, stability, and negligible area cost, establishing it as a practical and scalable defense against RowHammer.

## 中文摘要

RowHammer 是现代 DRAM 中最严峻的安全威胁之一。业界已引入逐行激活计数（PRAC）来监控激活操作，但该方法因延长关键 DRAM 时序参数而损害了性能。我们提出 TRAC（Transparent Row Activation Counting），一种轻量级监控架构，可消除上述缺陷。TRAC 利用 ACT 触发的更新、稳健的子阵列内处理以及基于线性反馈移位寄存器（LFSR）的计数器，在不引入时序开销的前提下透明地跟踪激活次数。电路级仿真与系统级评估表明，TRAC 具备正确性与稳定性，且面积开销可忽略，使其成为应对 RowHammer 的实用且可扩展的防御方案。

## 英文关键词

RowHammer, Per-Row Activation Counting (PRAC), DRAM, Memory Security, Linear Feedback Shift Register (LFSR)

## 中文关键词

RowHammer、逐行激活计数（PRAC）、DRAM、存储安全、线性反馈移位寄存器（LFSR）
