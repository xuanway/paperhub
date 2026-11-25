Jsplace: A Shape-Controllable and Length-Matching Placement for Rapid Single-Flux-Quantum Circuits
Authors：
[Rongliang Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=172843)，[Minglei Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=2603136284660754339)，[Huilong Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6474497932284261079)，[Da Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3079317117622893514)，[Fei Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1718447505323599323)，[Huawei Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=45937566660175133671)，[Junying Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=572843)

## 中文标题

JSPlace：面向快速单磁通量子电路的形状可控且长度匹配的布局算法

## 英文摘要

Superconducting Rapid Single Flux Quantum (RSFQ) logic is a promising candidate for high-performance computing due to its ultra-high speed and ultra-low power. Since most RSFQ logic gates require synchronization with a single clock pulse, RSFQ circuits have a clock-driven gate-level pipelined architecture in nature. However, the gate-level pipelined architecture leads to layouts with a high width-to-height ratio, especially in large circuits, because the layout width increases with the number of logic stages while the height is determined by the tallest column. To address this, we propose JSPlace, a shape-controllable and length-matching placement algorithm for RSFQ circuits. Our algorithm folds the multi-stage pipelined placement into three segments and merges columns via mixed-integer linear programming (MILP) to achieve the target width-to-height ratio. Subsequently, dynamic programming determines the vertical positions of nodes within each column, followed by connectivity-driven repositioning to minimize total vertical wirelength. Experimental results on ISCAS85 and EPFL benchmarks demonstrate that JSPlace achieves effective control of layout width-to-height ratio while significantly outperforming the state-of-the-art in layout area and wirelength.

## 中文摘要

超导快速单磁通量子（RSFQ）逻辑凭借超高速与超低功耗，成为高性能计算的有力候选技术。由于多数 RSFQ 逻辑门都需要与单一时钟脉冲同步，RSFQ 电路本质上具有时钟驱动的门级流水架构。然而，这种门级流水架构会导致版图呈现很高的宽高比，在大规模电路中尤为明显：版图宽度随逻辑级数增长，而高度则取决于最高的列。为解决该问题，我们提出 JSPlace，一种面向 RSFQ 电路的形状可控且长度匹配的布局算法。该算法将多级流水布局折叠为三段，并借助混合整数线性规划（MILP）合并列，以达成目标宽高比；随后通过动态规划确定各列内节点的垂直位置，再以连接性驱动的重新定位最小化总垂直线长。在 ISCAS85 与 EPFL 基准上的实验结果表明，JSPlace 在有效控制版图宽高比的同时，在版图面积与线长方面显著优于现有最先进方法。
