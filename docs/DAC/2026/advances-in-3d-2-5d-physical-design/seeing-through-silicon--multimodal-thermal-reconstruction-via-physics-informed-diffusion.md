Seeing Through Silicon: Multimodal Thermal Reconstruction via Physics-Informed Diffusion
Authors：
[Jing Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=9782117615153333311)，[Yuquan Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=3261042766618983319)，[Wei Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=693843)，[Yuanqing Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=2241154245997635535)

## 中文标题

透视硅片：基于物理信息扩散的多模态热重构

## 英文摘要

Real-time thermal monitoring of 3D integrated circuits confronts a fundamental observability crisis: reconstructing high-resolution volumetric thermal fields from sparse, heterogeneous on-chip observations. We demonstrate that existing single-modality approaches are physically insufficient—performance counters capture heat generation but they are blind to thermal transport, while sparse thermal sensors capture local states and provide thermal responses, but lack spatial coverage. To bridge this gap, we introduce a Physics-Informed 3D Conditional Diffusion Architecture (PI-3D-CD) which synergistically fuses these complementary modalities, treating thermal reconstruction as a constrained inference problem over the heat equation. Our 3D architecture explicitly models vertical interlayer coupling, reducing estimation error by over 94% (0.48 𝐾vs. 13.08 𝐾RMSE) compared to single-source baselines. Furthermore, by leveraging deterministic sampling, we accelerate inference 158× over finite-element simulation (0.93s vs. 147.4s) while maintaining high physical fidelity (𝑅2 > 0.98). This work establishes a new, observability-driven paradigm for thermal monitoring, enabling practical closed-loop dynamic thermal management for next-generation 3D integrated circuits.

## 中文摘要

3D 集成电路的实时热监测面临根本性的可观测性危机：如何从稀疏、异构的片上观测中重构高分辨率的体热场。我们证明，现有单模态方法在物理上是不充分的——性能计数器能够捕捉热量产生，却对热传输“失明”；稀疏温度传感器能够捕捉局部状态并提供热响应，但缺乏空间覆盖。为弥合这一差距，我们提出一种物理信息 3D 条件扩散架构（PI-3D-CD），它协同融合这些互补模态，将热重构视为热方程上的约束推断问题。我们的 3D 架构显式建模层间垂直耦合，与单源基线相比将估计误差降低超过 94%（0.48 K 对 13.08 K RMSE）。此外，借助确定性采样，我们将推断速度较有限元仿真提升 158 倍（0.93 s 对 147.4 s），同时保持较高的物理保真度（R² > 0.98）。本工作确立了可观测性驱动的热监测新范式，使下一代 3D 集成电路的实用闭环动态热管理成为可能。

## 英文关键词

3D ICs, Thermal Reconstruction, Physics-Informed Diffusion, Multimodal

## 中文关键词

3D IC、热重构、物理信息扩散、多模态
