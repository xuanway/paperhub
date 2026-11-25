Analytically-Derived Hybrid Net–pin Weighting for Timing-Driven Global Placement
Authors：
[Junjin Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=4918864129874763465)，[Qiang Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0831988578220356493)，[Hao Ai](https://63dac.conference-program.com/?post_type=page&p=15&uid=3411397556741948786)，[Wenxing Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=732843)

## 中文标题

面向时序驱动全局布局的解析推导混合线网—引脚加权方法

## 英文摘要

Timing-driven global placement is critical in modern VLSI physical design for achieving timing closure. Among existing approaches, weighting is a mainstream technique, but traditional weights are often manually designed based on heuristics, which can lead to suboptimal timing performance. To address this, we present an analytically-derived model of interconnect and cell-delay contributions of pin pairs along critical paths, from which we obtain explicit and differentiable formulations approximating Total Negative Slack (TNS) and Worst Negative Slack (WNS). The formulations include three wirelength components: net wirelength, linear pin-to-pin wirelength, and quadratic pin-to-pin wirelength, where net and linear pin-to-pin wirelength are smoothed via the weighted-average (WA) model. Based on these formulations, we derive a hybrid net-and-pin weighting scheme and propose a novel timing-driven global placement framework that directly optimizes TNS and WNS. The weighting scheme features dynamic and cumulative updates, ensuring that consistently critical paths are prioritized throughout optimization. Experimental results on the ICCAD’15 benchmark demonstrate that our method achieves average improvements of 39% in TNS and 6% in WNS compared with state-of-the-art timing-driven placers, while maintaining competitive wirelength and runtime, validating the effectiveness of the analytically-derived weighting framework.

## 中文摘要

时序驱动全局布局是现代超大规模集成电路（VLSI）物理设计中实现时序收敛的关键环节。在现有方法中，加权是一种主流技术，但传统权重往往基于启发式手工设计，可能导致时序性能欠佳。为此，我们提出一种解析推导的模型，用于刻画关键路径上引脚对的互连与单元延时贡献，并由此得到可显式表达且可微的公式，用以近似总负松弛（TNS）与最差负松弛（WNS）。该公式包含三个线长分量：线网线长、线性引脚间线长与二次引脚间线长，其中线网线长与线性引脚间线长通过加权平均（WA）模型进行光滑化。基于这些公式，我们推导出一种混合的线网与引脚加权方案，并提出一种新颖的时序驱动全局布局框架，直接优化 TNS 与 WNS。该加权方案具有动态与累积更新特性，确保始终关键的关键路径在整个优化过程中被优先处理。在 ICCAD'15 基准上的实验结果表明，与先进的时序驱动布局器相比，我们的方法在 TNS 与 WNS 上分别取得 39% 与 6% 的平均改善，同时保持具有竞争力的线长与运行时间，验证了解析推导加权框架的有效性。

## 英文关键词

physical design, timing-driven global placement, hybrid weighting

## 中文关键词

物理设计、时序驱动全局布局、混合加权
