Epicell: Electro-Physical Co-Modeling for Standard Cell PPA Prediction
Authors：
[Wenbo An](https://63dac.conference-program.com/?post_type=page&p=15&uid=0189458218851304998)，[Kairong Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1135162009302194174)，[Haoyi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0033616857435554483)，[Yibo Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=227143)

## 中文标题

EPiCell：面向标准单元 PPA 预测的电-物理协同建模

## 英文摘要

In advanced process nodes, the pursuit of extreme PPA optimization has driven an explosion in the demand for customized standard cells. To satisfy this demand, automated layout synthesis has been increasingly adopted to explore vast design spaces. However, this paradigm shifts the bottleneck from design creation to verification, as characterizing the massive volume of generated variants via SPICE is computationally prohibitive. Meanwhile, conventional geometric heuristics fail to proxy PPA at advanced nodes due to dominant layout effects. Existing learning-based surrogates often lack the fidelity to capture these complex dependencies. To bridge this gap, we propose EPiCell, an electro-physical co-modeling framework for rapid PPA estimation. EPiCell features a Heterogeneous Graph Transformer (HGT) that explicitly models transistors, routing metals, and supply rails as distinct entities, unifying circuit topology with fine-grained layout geometry. By employing relation-aware attention, it effectively captures the nonlocal electro-physical interactions governing cell performance. Validated on a dataset of over 18,000 auto-generated layouts based on ASAP7, EPiCell achieves high fidelity against SPICE simulations, with low average prediction errors of 1.82% for leakage power, 4.01% for internal power, 3.06% for delay, and 3.29% for transition. Crucially, it demonstrates superior ranking consistency with SPICE, improving median Spearman’s 𝜌from 0.25 to 0.9 for internal power, from 0.17 to 0.81 for delay, and from 0.14 to 0.70 for transition. This offers a high-fidelity and scalable surrogate model to enable efficient design space exploration.

## 中文摘要

在先进工艺节点下，对极致 PPA 优化的追求导致定制标准单元的需求激增。为满足这一需求，自动布局综合被越来越多地采用，以探索广阔的设计空间。然而，这一范式将瓶颈从设计创建转移到验证环节，因为通过 SPICE 对海量生成的变体进行表征在计算上难以承受。同时，由于版图效应占据主导，传统的几何启发式方法在先进节点无法代理 PPA。现有的基于学习的代理模型往往缺乏捕捉这些复杂依赖关系所需的保真度。为弥合这一差距，我们提出 EPiCell，一种用于快速 PPA 估计的电-物理协同建模框架。EPiCell 采用异构图 Transformer（HGT），将晶体管、布线金属与电源轨显式建模为不同实体，从而将电路拓扑与细粒度版图几何统一起来。通过采用关系感知注意力，它有效捕捉了支配单元性能的非局部电-物理相互作用。在基于 ASAP7 生成的 18000 多个自动布局数据集上验证，EPiCell 相对 SPICE 仿真达到高保真度，漏电功耗、内部功耗、延迟与转换时间的平均预测误差分别低至 1.82%、4.01%、3.06% 与 3.29%。关键在于，它与 SPICE 的排序一致性更优，将内部功耗、延迟与转换时间的中位 Spearman’s 𝜌 分别从 0.25 提升至 0.9、从 0.17 提升至 0.81、从 0.14 提升至 0.70。这为高效的设计空间探索提供了一种高保真且可扩展的代理模型。

## 英文关键词

Standard Cell Layout, PPA Prediction, Graph Transformer

## 中文关键词

标准单元版图、PPA 预测、图 Transformer
