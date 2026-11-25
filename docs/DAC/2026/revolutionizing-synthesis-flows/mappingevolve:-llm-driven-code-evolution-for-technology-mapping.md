Mappingevolve: LLM-Driven Code Evolution for Technology Mapping
Authors：
[Rongliang Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=172843)，[Yi Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3969423459093055325)，[Qiang Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=024143)，[Tsung-Yi Ho](https://63dac.conference-program.com/?post_type=page&p=15&uid=568743)

## 中文标题

MappingEvolve：面向工艺映射的 LLM 驱动代码演化

## 英文摘要

Technology mapping is a critical yet challenging stage in logic synthesis. While Large Language Models (LLMs) have been applied to generate optimization scripts, their potential for core algorithm enhancement remains untapped. We introduce MappingEvolve, an open-source framework that pioneers the use of LLMs to directly evolve technology mapping code. Our method abstracts the mapping process into distinct optimization operators and employs a hierarchical agent-based architecture, comprising a Planner, Evolver, and Evaluator, to guide the evolutionary search. This structured approach enables strategic and effective code modifications. Experiments show our method significantly outperforms direct evolution and strong baselines, achieving 10.04% area reduction versus ABC and 7.93% versus mockturtle, with 46.6%–96.0% 𝑆𝑜𝑣𝑒𝑟𝑎𝑙𝑙improve-ment on EPFL benchmarks, while explicitly navigating the area– delay trade-off. Our code and data are available at https://github. com/Flians/MappingEvolve.

## 中文摘要

工艺映射是逻辑综合中关键而富有挑战性的阶段。尽管大语言模型（LLM）已被用于生成优化脚本，但其在核心算法增强方面的潜力仍未被挖掘。我们提出 MappingEvolve，一个开源框架，率先利用 LLM 直接演化工艺映射代码。该方法将映射过程抽象为若干独立的优化算子，并采用包含规划器、演化器与评估器的分层智能体架构来引导演化搜索。这种结构化的方法使代码修改兼具策略性与实效性。实验表明，我们的方法显著优于直接演化与强基线：相较 ABC 实现 10.04% 的面积缩减，相较 mockturtle 实现 7.93% 的面积缩减，在 EPFL 基准上取得 46.6%–96.0% 的总体改进，同时显式地在面积与时延之间进行权衡。代码与数据见 https://github.com/Flians/MappingEvolve。
