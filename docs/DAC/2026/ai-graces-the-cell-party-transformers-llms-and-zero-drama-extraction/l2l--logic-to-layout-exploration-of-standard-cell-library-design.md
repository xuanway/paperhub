L2L: Logic to Layout Exploration of Standard Cell Library Design
Authors：
[Byeonggon Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9225425004061057727)，[Alan Mishchenko](https://63dac.conference-program.com/?post_type=page&p=15&uid=876243)，[Masahiro Fujita](https://63dac.conference-program.com/?post_type=page&p=15&uid=54935056644033350971)，[Bill Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=306243)，[Chung-Kuan Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=963143)

## 中文标题

L2L：标准单元库设计从逻辑到版图的探索

## 英文摘要

We present L2L, exploring end-to-end design optimization from logic to layout. The L2L framework includes logic, circuit, and layout stages. Logic exploration introduces two-stage transistor network synthesis. At the circuit stage, we propose two SMT models for transistor network synthesis: Connected-Diffusion (arbitrary, stack-height-bounded, multi-solution) and Grid-Scaffold (series-parallel). At the layout stage, an ILP-based flow co-optimizes circuit topology and double-height layouts, producing two 3-input P-class libraries (area-and metal-optimized). Block-level experiments demonstrate that full inclusion of 3-input P-class functions achieves up to 1.3% lower power, 5.6% higher performance, and 4.1% smaller area, outperforming the best prior baseline (average improvements: 0.8%, 0.6%, and 2.6%, respectively).

## 中文摘要

我们提出 L2L，探索从逻辑到版图的端到端设计优化。L2L 框架包括逻辑、电路与版图三个阶段。逻辑探索引入了两阶段晶体管网络综合。在电路阶段，我们提出两种用于晶体管网络综合的 SMT 模型：Connected-Diffusion（任意、堆叠高度受限、多解）与 Grid-Scaffold（串并联）。在版图阶段，一个基于 ILP 的流程对电路拓扑与双高度版图进行协同优化，产出两个 3 输入 P 类单元库（分别针对面积与金属优化）。模块级实验表明，完整纳入 3 输入 P 类功能可最高实现功耗降低 1.3%、性能提升 5.6%、面积减小 4.1%，优于此前最佳基线（平均改进分别为 0.8%、0.6% 与 2.6%）。

## 英文关键词

Standard cell, transistor network synthesis, cell layout, SMT, ILP

## 中文关键词

标准单元、晶体管网络综合、单元版图、SMT、ILP
