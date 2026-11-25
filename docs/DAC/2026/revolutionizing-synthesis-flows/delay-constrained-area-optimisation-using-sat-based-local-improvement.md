Delay-Constrained Area Optimisation Using SAT-Based Local Improvement
Authors：
[Franz-Xaver Reichl](https://63dac.conference-program.com/?post_type=page&p=15&uid=46170222539314861301)，[Christoph Scholl](https://63dac.conference-program.com/?post_type=page&p=15&uid=0103256112972674627)

## 中文标题

基于 SAT 局部改进的时延约束面积优化

## 英文摘要

This paper presents a new approach for minimising Boolean circuits subject to delay constraints. The proposed approach extends the efficient but purely area-based Boolean circuit minimiser eSLIM. The eSLIM minimiser reduces circuits by iteratively computing optimal replacements for small subcircuits on the fly. We extend the SAT encoding used, for synthesising these replacements, to take account for delay. While the additional constraints on delay restrict the set of possible candidates for the replacement, we can still harness the flexibility of making use of Boolean relations and multi-output circuits. We implemented the proposed method as part of the industrial-strength tool ABC. Surprisingly, in an experimental evaluation our implementation showed only a rather small deterioration in terms of area improvement, but substantial improvements in terms of delay compared to the purely area-based eSLIM approach on different benchmark sets.

## 中文摘要

本文提出一种在时延约束下最小化布尔电路的新方法。该方法扩展了高效但仅以面积为目标的布尔电路最小化工具 eSLIM。eSLIM 通过迭代地即时计算小子电路的最优替换来缩减电路规模。我们扩展了用于综合这些替换的 SAT 编码，以将时延纳入考量。尽管额外的时延约束收窄了可行替换候选的集合，我们仍能利用布尔关系与多输出电路带来的灵活性。我们将所提方法实现于工业级工具 ABC 之中。令人惊讶的是，在实验评估中，与纯面积导向的 eSLIM 方法相比，我们的实现在不同基准集上面积改善仅有小幅退化，但在时延方面取得了显著改善。

## 英文关键词

Boolean Circuit Optimisation, Exact Synthesis, SAT, AIG, LUT

## 中文关键词

布尔电路优化、精确综合、SAT、AIG、LUT
