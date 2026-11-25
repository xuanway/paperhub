RAM-CGRA: Reachability-Aware Mapping for CGRAs
Authors：
[Anh Nguyen](https://63dac.conference-program.com/?post_type=page&p=15&uid=224843)，[Linyi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=8137230312509640377)，[Jason H. Anderson](https://63dac.conference-program.com/?post_type=page&p=15&uid=139443)

## 中文标题

RAM-CGRA：面向 CGRA 的可达性感知映射

## 英文摘要

Coarse-grained reconfigurable arrays (CGRAs) are programmable hardware devices having large coarse-grained processing elements (PEs) and word-wide configurable interconnect. The interconnect comprises a considerable fraction of total CGRA area, making it desirable to restrict interconnect connectivity richness. However, reducing interconnect richness makes application mapping more difficult, and impossible in some cases. We propose techniques for mapping applications onto CGRAs with restricted routing architectures. For a target CGRA having restricted interconnect, we precompute the reachability and distance between all PE pairs, as well as an estimate of the number of available routing paths between PE pairs. The values are stored in tables, and used during the placement stage of the mapping flow to assess the potential routability of an intermediate placement. For benchmark applications mapped onto CGRA variants with restricted interconnect, results demonstrate higher mapping success, and lower mapping runtimes vs. recent state-of-the-art CGRA mappers.

## 中文摘要

粗粒度可重构阵列（CGRA）是一种可编程硬件器件，具有大量粗粒度处理单元（PE）和字宽可配置互连。互连在 CGRA 总面积中占相当大的比例，因此有必要限制互连连接的丰富程度。然而，降低互连丰富度会使应用映射更加困难，在某些情况下甚至无法完成映射。我们提出将应用映射到互连受限 CGRA 上的技术。对于互连受限的目标 CGRA，我们预先计算所有 PE 对之间的可达性与距离，以及 PE 对之间可用布线路径数量的估计值。这些数值被存储在表中，并在映射流程的布局阶段用于评估中间布局结果的潜在可布线性。对于映射到互连受限 CGRA 变体上的基准应用，结果表明，与近期最先进的 CGRA 映射器相比，本方法具有更高的映射成功率和更短的映射运行时间。

## 英文关键词

CGRAs, coarse-grained reconfigurable arrays, reachability, placement, mapping

## 中文关键词

CGRA、粗粒度可重构阵列、可达性、布局、映射
