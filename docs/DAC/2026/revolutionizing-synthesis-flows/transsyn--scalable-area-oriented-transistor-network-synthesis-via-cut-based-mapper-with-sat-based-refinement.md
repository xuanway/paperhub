Transsyn: Scalable, Area-Oriented Transistor Network Synthesis via Cut-Based Mapper with SAT-Based Refinement
Authors：
[Jiun-Cheng Tsai](https://63dac.conference-program.com/?post_type=page&p=15&uid=145843)，[Wei-Min Hsu](https://63dac.conference-program.com/?post_type=page&p=15&uid=20032417576057353311)，[Hsuan-Ming Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=045843)，[Jen-Hang Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=624116570887815759)，[Heng-Liang Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=13691576309948615241)，[Yen-Ju Su](https://63dac.conference-program.com/?post_type=page&p=15&uid=007516258198424666)，[Hung-Pin (Charles) Wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=95982384704182032201)

## 中文标题

TransSyn：基于割映射器与 SAT 精化的可扩展、面向面积的晶体管网络综合

## 英文摘要

SAT-based transistor network synthesis delivers optimal, minimum-transistor designs but faces exponential complexity, making it impractical for large circuits. This paper introduces TransSyn, a scalable transistor network synthesizer that brings the benefits of SAT-based synthesis to the macro-cell scale through a novel two-stage framework. First, a cut-based global synthesis stage reformulates the task as a cut-based mapping problem, rapidly decomposing the design into smaller, manageable sub-problems. This ensures scalability and produces a high-quality network in seconds. Then, a SAT-based detailed synthesis stage refines this network by systematically identifying and re-optimizing merged subcircuits across cut boundaries using a SAT-based approach, recapturing lost optimization opportunities. Experiments demonstrate that TransSyn significantly outperforms previous methods, achieving 11.2% and 10% reductions in transistor count compared to graph-based and hybrid-based approaches, respectively. Furthermore, when integrated with a transistor-level placer, TransSyn breaks the library and cell boundaries, yielding up to a 48.8% area reduction compared to conventional cell-based designs. TransSyn demonstrates its capability for scalable, high-quality transistor-network synthesis, successfully bridging the gap between the optimality of SAT-based synthesis and the practical demands of large-scale cell design.

## 中文摘要

基于 SAT 的晶体管网络综合能够给出最优、晶体管数最少的设计，但面临指数级复杂度，难以适用于大规模电路。本文提出 TransSyn，一个可扩展的晶体管网络综合器，通过新颖的两阶段框架将 SAT 综合的优势拓展至宏单元规模。首先，基于割的全局综合阶段将任务重构为基于割的映射问题，快速把设计分解为更小、更易处理的子问题。这保证了可扩展性，并能在数秒内产生高质量网络。随后，基于 SAT 的详细综合阶段通过系统性地识别并重新优化跨越割边界的合并子电路，用基于 SAT 的方法精化该网络，从而找回此前丢失的优化机会。实验表明，TransSyn 显著优于已有方法，相较基于图的方法与混合方法分别减少 11.2% 与 10% 的晶体管数。此外，当与晶体管级布局器集成时，TransSyn 打破了标准单元库与单元边界，相较传统基于单元的设计可实现高达 48.8% 的面积缩减。TransSyn 展示了其可扩展、高质量晶体管网络综合的能力，成功弥合了 SAT 综合的最优性与大规模单元设计实际需求之间的差距。

## 英文关键词

Transistor-level synthesis, Complex cell, Transistor count reduction

## 中文关键词

晶体管级综合、复杂单元、晶体管数缩减
