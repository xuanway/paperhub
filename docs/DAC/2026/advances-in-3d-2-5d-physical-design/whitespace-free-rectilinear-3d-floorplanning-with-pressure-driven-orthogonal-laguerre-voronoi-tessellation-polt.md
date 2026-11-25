Whitespace-Free Rectilinear 3D Floorplanning with Pressure-Driven Orthogonal Laguerre-Voronoi Tessellation (POLT)
Authors：
[Tse-Han Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=17877861283852586961)，[Paul Franzon](https://63dac.conference-program.com/?post_type=page&p=15&uid=803143)

## 中文标题

基于压力驱动正交 Laguerre-Voronoi 剖分（POLT）的无空白区直角化 3D 布局规划

## 英文摘要

A major challenge in 3DIC design is determining the top-level floorplan of a chip stack while accounting for die-to-die (D2D) interfaces. Existing approaches often model modules as simple rectangles and optimize area, and wirelength under limited constraints, diverging from real scenarios where hard modules have fixed outlines and some have alignment constraints, while soft modules have undefined shapes. To address these issues, we propose a two-stage, whitespace-free rectilinear 3D floorplanning process. The first stage places hard modules and determines the spatial relationship of soft-modules using a force-directed algorithm; the second tessellates each soft module into a rectilinear shape with minimal area error using POLT. The method integrates constrained hard modules and flexible soft modules to generate rectilinear, whitespace-free floorplans that meet target areas and alignment constraints. Experimental results show that our method achieves an average 5.6% reduction in HPWL on 3D floorplans with alignment constraints and reduces area error by 98% compared to existing rectilinear floorplanners, while maintaining less than 0.16% area error across all 2D and 3D stacking scenarios.

## 中文摘要

3DIC 设计中的一大挑战是在考虑裸片间（D2D）接口的同时确定芯片堆叠的顶层布局规划。现有方法通常将模块建模为简单矩形，并在有限约束下优化面积与线长，这与真实场景存在偏差：硬模块具有固定轮廓，部分模块还带有对齐约束，而软模块的形状尚未确定。为解决这些问题，我们提出一种两阶段、无空白区的直角化 3D 布局规划流程。第一阶段放置硬模块，并使用力导向算法确定软模块之间的空间关系；第二阶段使用 POLT 将每个软模块剖分为面积误差最小的直角形状。该方法融合了受约束的硬模块与可灵活变形的软模块，生成满足目标面积与对齐约束的直角化、无空白区布局规划。实验结果表明，在带对齐约束的 3D 布局规划上，我们的方法平均将 HPWL 降低 5.6%，与现有直角化布局规划器相比将面积误差减少 98%，同时在所有 2D 与 3D 堆叠场景中面积误差均低于 0.16%。

## 英文关键词

floorplan, rectilinear, Voronoi, force-directed algorithms, 3DIC

## 中文关键词

布局规划、直角化、Voronoi、力导向算法、3DIC
