From Fab to Mask Shop: A Differentiable MDP-ILT Framework for Co-Optimization of Wafer Pattern Fidelity and Mask Writability
Authors：
[Xu Jinchao](https://63dac.conference-program.com/?post_type=page&p=15&uid=91719676631673752211)，[Xinyun Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=21506297774650920451)，[Kun Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=5397185250506321492)，[Qi Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=073843)，[Cheng Zhuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=204443)

## 中文标题

从晶圆厂到掩模厂：面向晶圆图案保真度与掩模可写性协同优化的可微 MDP-ILT 框架

## 英文摘要

Inverse lithography technology (ILT) generates curvilinear masks for optimal wafer patterns and process windows. In practice, fabs employ ILT based on optical lithography (OL) models to improve wafer pattern fidelity, while mask shops perform mask data preparation (MDP) to ensure mask writability. The MDP process applies geometry-level mask process correction (MPC) guided by electron-beam lithography (EBL) simulations, followed by shot fracturing. However, this disjointed workflow, both between fabs and mask shops, as well as within MDP between MPC and shot fracturing, often results in suboptimal wafer patterns and inefficient mask preparation. This paper presents a novel, unified, end-to-end differentiable framework for co-optimizing wafer pattern fidelity and mask manufacturability. We achieve differentiability by formulating a physics-aware EBL simulator using the inherently differentiable error function (erf), which precisely captures energy deposition at the VSB shot level, enabling exact gradient computation. With OL simulation embedded in the optimization loop, the framework enables refinement of shot parameters to achieve wafer-level optimality. The proposed method unifies the workflow from fab to mask shop, aligning wafer-side lithography objectives with mask-side writability constraints within an end-to-end optimization flow, thereby improving mask manufacturability while preserving wafer pattern fidelity.

## 中文摘要

反向光刻技术（ILT）生成曲线掩模，以获得最优的晶圆图案与工艺窗口。在实践中，晶圆厂采用基于光学光刻（OL）模型的 ILT 来提升晶圆图案保真度，而掩模厂则执行掩模数据准备（MDP）以确保掩模的可写性。MDP 流程在电子束光刻（EBL）仿真的引导下施加几何级掩模工艺校正（MPC），随后进行曝光分割。然而，这种割裂的工作流——既存在于晶圆厂与掩模厂之间，也存在于 MDP 内部 MPC 与曝光分割之间——往往导致次优的晶圆图案和低效的掩模准备。本文提出一种新颖、统一、端到端的可微框架，用于协同优化晶圆图案保真度与掩模可制造性。我们通过使用本身可微的误差函数（erf）构建物理感知的 EBL 仿真器来实现可微性，该仿真器精确捕捉 VSB 曝光级别的能量沉积，从而支持精确的梯度计算。将 OL 仿真嵌入优化循环后，该框架能够细化曝光参数以实现晶圆级最优性。所提方法统一了从晶圆厂到掩模厂的工作流，在端到端优化流程中将晶圆侧的光刻目标与掩模侧的可写性约束对齐，从而在保持晶圆图案保真度的同时提升掩模可制造性。
