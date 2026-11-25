Design Technology Co-Optimization for Network on Chip in High Performance CPUs at 3nm Node Using Monolithic 3D and Backside Interconnect Technologies
Authors：
[Tianchi Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5904480455541916664)，[Hu Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=2145472869061473163)，[Zexu Leng](https://63dac.conference-program.com/?post_type=page&p=15&uid=1817434956464451069)，[Zhiyong Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=56955970526490903241)，[Lianmao Peng](https://63dac.conference-program.com/?post_type=page&p=15&uid=25177249654566186211)，[Rongmei Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=1207865574063506308)

## 中文标题

3nm 节点高性能 CPU 片上网络的设计工艺协同优化：采用单片 3D 与背面互连技术

## 英文摘要

With the rapidly growing demand of cloud computing and large-scale AI models, many-core systems are facing challenges of longer global interconnect distances in Network-on-Chip (NoC). Though conventional 2D NoCs can apply relative high metal layer for global routing, the extensive repeater insertion for long-distance transmission results in a large number of stacked vias, leading to performance degradation. Targeting high-performance CPU clusters at 3nm node, this work adopts a design–technology co-optimization (DTCO) framework to evaluate long-distance NoC interconnects across four implementation schemes: conventional frontside 2D (F2D), frontside 3D (F3D) with M3D integration, F2D with backside power delivery network (BSPDN), and backside 2D (B2D) leveraging wafer backside signal routing & PDN. Based on post-layout extraction of the ARM Neoverse CSS N2 computing tile, we incorporate realistic PDN characteristics, technology-dependent RC modeling, and IR-drop-aware circuit simulation. Results show that F3D and B2D reduce delay by 53% and 68%, and energy–delay product (EDP) by 32% and 63%, respectively, compared with F2D. F2D-BSPDN achieves performance comparable to F3D. System-level NoC evaluations further demonstrate that F3D/B2D enable 2.1×/3.1× feasible link frequencies of F2D, and lower average NoC latency of F2D by 23%/35%. The DTCO analysis indicates that while F2D remains adequate for small cores (Cortex-A76), B2D is the optimal choice for mid-core (Cortex-A720, X4) and large-core (Cortex-X925, CSS N2) clusters, with F3D providing secondary benefits through repeater relocation. These findings identify backside interconnect as a momentous technology for ultra-large many-core processors.

## 中文摘要

随着云计算与大规模 AI 模型需求的迅猛增长，众核系统在片上网络（NoC）中面临全局互连距离变长的挑战。尽管传统 2D NoC 可采用较高的金属层进行全局布线，但长距离传输所需的大量中继器插入会引入众多堆叠通孔，从而导致性能退化。本文面向 3nm 节点的高性能 CPU 簇，采用设计工艺协同优化（DTCO）框架，评估四种实现方案下的长距离 NoC 互连：传统正面 2D（F2D）、基于单片 3D（M3D）集成的正面 3D（F3D）、带背面供电网络（BSPDN）的 F2D，以及利用晶圆背面信号布线与 PDN 的背面 2D（B2D）。基于对 ARM Neoverse CSS N2 计算芯粒的版图后提取，我们纳入了真实的 PDN 特性、与工艺相关的 RC 建模以及感知 IR-drop 的电路仿真。结果表明，相比 F2D，F3D 与 B2D 分别将延迟降低 53% 和 68%，将能量延迟积（EDP）降低 32% 和 63%；F2D-BSPDN 的性能与 F3D 相当。系统级 NoC 评估进一步表明，F3D/B2D 可分别达到 F2D 链路频率的 2.1/3.1 倍，并将 F2D 的平均 NoC 延迟降低 23%/35%。DTCO 分析表明：F2D 对小核（Cortex-A76）仍然适用，而 B2D 是中核（Cortex-A720、X4）与大核（Cortex-X925、CSS N2）簇的最优选择，F3D 则通过中继器重定位带来次级收益。上述发现表明，背面互连是超大规模众核处理器的重要技术。

## 英文关键词

Design Technology Co-Optimization (DTCO), Network-on-Chip (NoC), 3D integration, Backside interconnect

## 中文关键词

设计工艺协同优化 (DTCO)、片上网络 (NoC)、3D 集成、背面互连
