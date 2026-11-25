Dynamic-Cost Area Recovery for Fracturable LUT-Based FPGAs
Authors：
[Xianfeng Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=9939460935055903777)，[Jiangnan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=3035944067988884177)，[Lingli Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=25253654954830750101)

## 中文标题

面向可拆分 LUT 型 FPGA 的动态代价面积恢复

## 英文摘要

Fracturable LUTs (FLUTs) creates variable logic consumption for LUT implementations since two LUTs can be merged to one FLUT under certain constraints. Traditional technology mapping algorithms fail to exploit this feature due to their static-cost area models. To bridge this gap, we introduce merging probability, a quantitative, mapping-stage metric that predicts the likelihood of LUT merging during the subsequent packing phase. Based on this, we present a dynamic-cost LUT area model, enabling area recovery better suited for FLUTs. Experimental results on EPFL benchmarks demonstrate that our method reduces the usage of FLUTs by at most of 10.3% on mainstream commercial FPGAs, compared to the state-of-the-art technology mapping algorithm, without any performance degradation.

## 中文摘要

可拆分 LUT（FLUT）使 LUT 实现的逻辑资源消耗变得可变，因为在特定约束下两个 LUT 可合并为一个 FLUT。传统工艺映射算法由于采用静态代价面积模型，无法利用这一特性。为弥合这一差距，我们引入合并概率，一种在映射阶段预测后续装箱阶段中 LUT 合并可能性的定量指标。在此基础上，我们提出动态代价 LUT 面积模型，使面积恢复更适合 FLUT。在 EPFL 基准上的实验结果表明，与最先进的工艺映射算法相比，我们的方法在主流商用 FPGA 上最多将 FLUT 使用量减少 10.3%，且无任何性能退化。

## 英文关键词

Fracturable LUT, FPGA, Area Recovery, Technology Mapping

## 中文关键词

可拆分 LUT、FPGA、面积恢复、工艺映射
