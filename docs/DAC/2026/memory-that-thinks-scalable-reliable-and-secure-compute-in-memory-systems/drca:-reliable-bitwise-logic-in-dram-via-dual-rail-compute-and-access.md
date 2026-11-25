DRCA: Reliable Bitwise Logic in DRAM via Dual-Rail Compute and Access
Authors：
[Yuxuan Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=54462240312505533561)，[Chuxiong Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=945343)，[Shuo Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=9122622970262177689)，[Guoming Rao](https://63dac.conference-program.com/?post_type=page&p=15&uid=6157737341288822659)，[Weiguang Sheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=6387309076479857656)，[Weifeng He](https://63dac.conference-program.com/?post_type=page&p=15&uid=408243)

## 中文标题

DRCA：通过双轨计算与访存实现 DRAM 中的可靠按位逻辑

## 英文摘要

DRAM-based processing-in-memory (PIM) emerged as a promising approach to alleviate the memory wall by executing massively parallel bitwise operations inside DRAM arrays. However, most prior designs operate on a single bitline and leave the dual-rail complementary signals naturally available on each bitline pair underutilized. We present DRCA, a novel dual-rail compute-and-access scheme that exploits both rails of a bitline pair for computation and data access. DRCA integrates two dual-contact compute cells, DRCA-OR and DRCA-XOR, which leverage full-swing dual-rail signaling on the bitline pair, to perform bitwise logic with high reliability. Furthermore, the design enables concurrent operations on a single bitline pair, improving the efficiency of complex bitwise logic processing. Our evaluation shows that DRCA reduces the failure rate by 2.29x compared with the most robust prior PIM design, while delivering superior average performance on basic bitwise operations.

## 中文摘要

基于 DRAM 的存内处理（PIM）通过在 DRAM 阵列内部执行大规模并行按位操作，成为缓解存储墙问题的有前景途径。然而，既有设计大多在单条位线上操作，未能充分利用每条位线对上天然可得的双轨互补信号。本文提出 DRCA，一种新颖的双轨计算与访存方案，同时利用位线对的两条轨完成计算与数据访问。DRCA 集成了两种双接触计算单元 DRCA-OR 与 DRCA-XOR，利用位线对上的全摆幅双轨信号实现高可靠性的按位逻辑。此外，该设计支持在单条位线对上并发操作，提升了复杂按位逻辑处理的效率。评估结果表明，与最稳健的已有 PIM 设计相比，DRCA 将失败率降低 2.29 倍，同时在基本按位操作上具有更优的平均性能。

## 英文关键词

Bulk bitwise operations, Processing-in-Memory, DRAM, Process variation

## 中文关键词

批量按位操作、存内处理、DRAM、工艺偏差
