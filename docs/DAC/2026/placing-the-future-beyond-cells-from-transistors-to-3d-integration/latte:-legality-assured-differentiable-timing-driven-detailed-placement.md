LATTE: Legality-Assured Differentiable Timing-Driven Detailed Placement
Authors：
[Jing Mai](https://63dac.conference-program.com/?post_type=page&p=15&uid=587182915407512375)，[Yi-Chen Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=57683330628874433401)，[Yibo Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=227143)，[Haoxing Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=172643)

## 中文标题

LATTE：合法性保证的可微时序驱动详细布局

## 英文摘要

Differentiable techniques for timing optimization have become the dominant paradigm in global placement, surpassing weight-tuning heuristics by directly leveraging gradients that encompass full-chip context. However, in detailed placement, state-of-the-art flows still rely on rule-based or enumeration-centric methods that ignore existing gradient landscape, sacrificing significant wirelength only for marginal timing gains. To overcome this issue, we present LATTE, the first legality-assured, end-to-end differentiable timing-driven detailed placer that fuses continuous gradient smoothness with detailed discrete granularity. Particularly, at each iteration, LATTE relaxes local density constraints around selected timing-critical cells, steering relocation from exact timing and wirelength gradients with step sizes in annealed schedules, and enforces end-of-place legality via incremental legalization and bad-move filtering. Across input placements from mainstream commercial and academic placers, LATTE consistently delivers significant timing improvement with minimal routed wirelength impact while ensuring legal final solutions. On 15 designs in a 7𝑛𝑚technology node, LATTE on average improves state-of-the-art timing-driven detailed placers including DREAMPlace-4.0 TCAD and Rsyn by 29.7% in TNS and 44.4% in routed wirelength, with all metrics verified by an industry-leading commercial tool.

## 中文摘要

面向时序优化的可微技术已成为全局布局的主流范式，它直接利用蕴含全芯片上下文的梯度，优于权重调优类的启发式方法。然而在详细布局中，最先进的流程仍依赖基于规则或以枚举为中心的方法，忽视了既有梯度所刻画的地形，仅为微弱的时序收益而牺牲可观的线长。为解决这一问题，我们提出 LATTE，首个融合连续梯度平滑性与详细离散粒度的、合法性保证的端到端可微时序驱动详细布局器。具体而言，LATTE 在每次迭代中松弛所选时序关键单元周围的局部密度约束，依据精确的时序与线长梯度、以退火调度中的步长引导单元迁移，并通过增量合法化与坏移动过滤保证布局结束时的合法性。在主流的商用与学术布局器给出的输入布局上，LATTE 始终在保证最终解合法性的同时，以极小的布线线长影响带来显著的时序改善。在 7nm 工艺节点的 15 个设计上，LATTE 相较包括 DREAMPlace-4.0 TCAD 与 Rsyn 在内的最先进时序驱动详细布局器，平均将 TNS 改善 29.7%、布线线长改善 44.4%，所有指标均经业界领先的商用工具验证。
