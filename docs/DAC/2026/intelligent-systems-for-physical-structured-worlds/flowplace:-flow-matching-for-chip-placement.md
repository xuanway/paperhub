Flowplace: Flow Matching for Chip Placement
Authors：
[Peng Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=40062715754023433431)，[Ke Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=5778742940083357572)，[Yunqi Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=39267230907048957061)，[Ruo-Tong Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=4940691652784141785)，[Chengrui Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=1804124812119649253)，[Siyuan Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=90130281886321181481)，[Chenjian Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=01747372684443936201)，[Mingxuan Yuan](https://63dac.conference-program.com/?post_type=page&p=15&uid=2371953237384098548)，[Chao Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=16501305373597700161)

## 中文标题

FlowPlace：面向芯片布局的流匹配

## 英文摘要

Chip placement plays an important role in physical design. While generative models like diffusion models offer promising learning-based solutions, current methods have the following limitations: they use random synthetic data for pretraining, require long sampling times, and often result in overlaps due to their dependence on gradient-based solvers during the sampling process. To overcome these issues, we propose FlowPlace, which features mask-guided synthetic data generation, flow-based efficient training with flexible prior injection, and hard constraint sampling for overlap-free layouts. Experiments on OpenROAD and ICCAD 2015 benchmarks show FlowPlace achieves better PPA metrics, 10-50× faster sampling efficiency, and zero overlaps.

## 中文摘要

芯片布局在物理设计中发挥着重要作用。尽管扩散模型等生成模型提供了有前景的基于学习的解决方案，但现有方法存在以下局限：使用随机合成数据进行预训练、采样时间长，并且由于采样过程依赖基于梯度的求解器而常常产生重叠。为克服这些问题，我们提出 FlowPlace，其特点是掩码引导的合成数据生成、带灵活先验注入的基于流的快速训练，以及用于无重叠布局的硬约束采样。在 OpenROAD 与 ICCAD 2015 基准上的实验表明，FlowPlace 取得了更好的 PPA 指标、10-50 倍的采样效率提升，且零重叠。
