G-Matcher: GPU-Accelerated Multi-Level, Multi-Stage Framework for Large-Scale Layout Pattern Matching
Authors：
[Nan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=83318436845195880671)，[Hanbin Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=38614088020971804831)，[Chengxuan Lv](https://63dac.conference-program.com/?post_type=page&p=15&uid=69543687847033508101)，[Jiaqi Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=301791953262832763)，[Tao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5015719775236880997)，[Jingyi Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2434541213894243641)，[Hao Geng](https://63dac.conference-program.com/?post_type=page&p=15&uid=64456419866376934351)

## 中文标题

G-Matcher：面向大规模版图图形匹配的 GPU 加速多级多阶段框架

## 英文摘要

Pattern matching has become one of the most predominant industrial solutions in IC design-to-manufacturing flow, with broad applications in layout verification, hotspot detection and Optical Proximity Correction (OPC). However, conventional CPU-based approaches, which rely on rule-based extraction, suffer from excessive false matches and high runtime overhead. These inefficiencies create bottlenecks in both verification and manufacturing workflows at advanced nodes. To address these limitations, we introduce the first fully GPU-accelerated pattern matching framework G-Matcher, with a novel multi-stage, multi-level architecture. Our GPU-oriented development exploits massive parallelism to process ultra-large-scale layout data. The multi-stage pipeline filters false matches, while the multi-level paradigm utilizes specialized pattern and layout representations to accelerate the search. On industrial datasets, our framework demonstrates a 407× speedup over the 64-thread commercial tool Calibre. On public benchmarks, it achieves 7.1× speedup over a state-of-the-art CPU implementation. Importantly, G-Matcher maintains 100% matching accuracy with zero false matches across all evaluations.

## 中文摘要

图形匹配已成为 IC 设计与制造流程中最重要的工业解决方案之一，在版图验证、热点检测和光学邻近效应校正（OPC）中有着广泛应用。然而，依赖规则提取的传统 CPU 方法存在误匹配过多和运行时间开销大的问题。这些低效在先进工艺节点的验证与制造流程中造成瓶颈。为应对这些限制，我们提出首个完全 GPU 加速的图形匹配框架 G-Matcher，采用新颖的多阶段、多层级架构。我们面向 GPU 的开发方式利用大规模并行性来处理超大规模版图数据。多阶段流水线用于过滤误匹配，而多层级范式利用专门的图形与版图表示来加速搜索。在工业数据集上，我们的框架相较 64 线程商用工具 Calibre 实现 407 倍加速。在公开基准上，相较最先进的 CPU 实现获得 7.1 倍加速。重要的是，G-Matcher 在所有评估中保持 100%的匹配精度且零误匹配。
