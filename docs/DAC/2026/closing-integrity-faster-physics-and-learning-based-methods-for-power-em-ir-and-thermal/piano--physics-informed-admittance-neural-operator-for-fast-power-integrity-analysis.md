PIANO: Physics-Informed Admittance Neural Operator for Fast Power Integrity Analysis
Authors：
[Xiangqiao Meng](https://63dac.conference-program.com/?post_type=page&p=15&uid=9893933195371201872)，[Siyuan Miao](https://63dac.conference-program.com/?post_type=page&p=15&uid=22410464848665300021)，[Yiming Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=86151706451234207771)，[Min Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=37325956085452896661)，[Zhen Zhuang](https://63dac.conference-program.com/?post_type=page&p=15&uid=76656129445126695571)，[Wei Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=693843)，[Chen Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03136600854360412471)，[Lei He](https://63dac.conference-program.com/?post_type=page&p=15&uid=66261377779751363971)

## 中文标题

PIANO：用于快速电源完整性分析的物理信息导纳神经算子

## 英文摘要

Design of large-scale integrated circuits requires rigorous power integrity (PI) analysis to ensure reliable and robust operation. In particular, Direct Current (DC) PI analysis entails solving massive symmetric positive definite (SPD) systems derived from Kirchhoff’s current law. Traditional PI evaluation methods are computationally expensive, making it difficult to satisfy the stringent turnaround-time requirements of modern design iterations. To address these challenges, we introduce PIANO, a physics-informed admittance neural operator for fast and high-fidelity DC PI analysis in 3D IC. PIANO first extracts an equivalent resistive network from the PDN layout and represents it as a graph. A graph neural network then learns the equivalent port admittance matrix between voltage-source ports and current sinks. The resulting reduced SPD system, formed from the predicted admittance matrix, is efficiently solved by a lightweight numerical solver to obtain port voltages. Experiments on industrial-scale PDNs show that PIANO achieves a 12.6× speedup over commercial simulators with only 1.95% voltage error, and a 17.2× acceleration when integrated into a PI-constrained design space exploration flow.

## 中文摘要

大规模集成电路的设计需要严格的电源完整性（PI）分析，以确保可靠且稳健的运行。特别是，直流（DC）PI 分析需要求解由基尔霍夫电流定律导出的大规模对称正定（SPD）方程组。传统的 PI 评估方法计算代价高昂，难以满足现代设计迭代严苛的交付周期要求。为应对这些挑战，我们提出 PIANO，一种物理信息导纳神经算子，用于 3D IC 中快速、高保真的 DC PI 分析。PIANO 首先从 PDN 版图中提取等效电阻网络，并将其表示为图。随后，图神经网络学习电压源端口与电流汇之间的等效端口导纳矩阵。由预测得到的导纳矩阵构成的降阶 SPD 系统由轻量级数值求解器高效求解，从而获得端口电压。在工业规模 PDN 上的实验表明，PIANO 相比商用仿真器实现了 12.6× 的加速，电压误差仅为 1.95%；当集成到 PI 约束的设计空间探索流程中时，加速可达 17.2×。

## 英文关键词

Power Integrity, 3D IC, Power Delivery Network

## 中文关键词

电源完整性、3D IC、供电网络
