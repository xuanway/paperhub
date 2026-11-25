Disentangled Differentiable Timing-Power Co-Optimization with Quad-Gradient Gate Sizing
Authors：
[Zixuan Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=70551413387135013901)，[Zizheng Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=978243)，[Yufan Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=21735547392757712)，[Runsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=214343)，[Yibo Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=227143)

## 中文标题

基于四梯度门尺寸调整的解耦可微时序—功耗协同优化

## 英文摘要

Co-optimizing timing and power in modern VLSI designs remains challenging under realistic static timing analysis and standard-cell libraries. Classical gate sizing often scales poorly, while learning-based sizers behave as expensive black boxes with limited generality. Recent differentiable physical optimization enables gradient-based design flows, but existing approaches still struggle to stay aligned with library-based implementations and to provide controlled timing–power trade-offs. We propose a library-native quad-gradient gate sizing framework that leverages differentiable timing to derive structured guidance for timing and power, enabling more systematic and interpretable co-optimization in the standard-cell sizing space. On the ICCAD 2025 contest benchmarks, our framework achieves, on average, 40.4% larger reduction in TNS and 16.2% better total power change than the 1st-place contest flow.

## 中文摘要

在现代 VLSI 设计中，如何在贴近实际的静态时序分析与标准单元库条件下协同优化时序与功耗仍然十分困难。经典的门尺寸调整方法往往扩展性较差，而基于学习的尺寸调整器则表现为代价高昂的黑盒，泛化能力有限。近期的可微物理优化使基于梯度的设计流程成为可能，但现有方法仍难以与基于库的实现保持一致，也难以提供可控的时序—功耗折中。我们提出一种库原生的四梯度门尺寸调整框架，利用可微时序分析为时序与功耗导出结构化引导，从而在标准单元尺寸调整空间中实现更系统、更具可解释性的协同优化。在 ICCAD 2025 竞赛基准上，与竞赛第一名流程相比，我们的框架平均取得 40.4% 更大的 TNS 降幅和 16.2% 更优的总功耗变化。
