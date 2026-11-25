COOL: A Cooling-Aware Point Transformer Framework for Thermal Prediction in Advanced 3D/3.5D IC Packaging
Authors：
[Yao Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6294307449303409391)，[Zhicheng Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1701010475988725104)，[Qijun Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7306866826013265809)，[Shang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7888404795171209433)，[Wenji Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0880747726699421348)，[Wenkai LI](https://63dac.conference-program.com/?post_type=page&p=15&uid=91566662620660660201)，[Zhiyao Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=263843)

## 中文标题

COOL：面向先进 3D/3.5D IC 封装热预测的散热感知点 Transformer 框架

## 英文摘要

Advanced 3D and 3.5D IC packaging significantly improves integration density but elevates thermal management challenges due to cross-layer heat coupling and complex cooling structures. Traditional solvers deliver high fidelity but are too slow for iterative design flows, while existing learning-based methods either fail to capture inter-die thermal coupling or treat cooling structures as static components, limiting their applicability in real packaging co-design scenarios. In this work, we introduce COOL, a cooling-aware point transformer framework that represents heterogeneous assemblies (dies, interposers, TIMs, heat spreaders) as annotated 3D point clouds embedding geometric, material and power attributes. COOL explicitly encodes geometric boundaries and cooling structures, and introduces a physics-informed boundary condition (PI-BC) loss to enforce thermal consistency at material interfaces and cooling boundaries. Extensive experiments demonstrate that COOL achieves a remarkable 2.4% NMAE on our constructed benchmark of multi-package thermal designs, substantially outperforming existing learning-based approaches while providing over 15.7× speedup compared to commercial FEM solvers.

## 中文摘要

先进的 3D 和 3.5D IC 封装显著提升了集成密度，但由于跨层热耦合和复杂的散热结构，也加剧了热管理挑战。传统求解器具有高保真度，但对于迭代设计流程而言过于缓慢；而现有的基于学习的方法要么无法捕获裸片间的热耦合，要么将散热结构视为静态部件，限制了其在实际封装协同设计场景中的适用性。本文提出 COOL，一个散热感知的点 Transformer 框架，它将异构组件（裸片、中介层、TIM、均热板）表示为带有标注的 3D 点云，并嵌入几何、材料与功耗属性。COOL 显式编码几何边界和散热结构，并引入物理信息边界条件（PI-BC）损失，以在材料界面和散热边界处强制热一致性。大量实验表明，在我们构建的多封装热设计基准上，COOL 取得了低至 2.4% 的 NMAE，显著优于现有的基于学习的方法，同时相比商用 FEM 求解器提供超过 15.7× 的加速。
