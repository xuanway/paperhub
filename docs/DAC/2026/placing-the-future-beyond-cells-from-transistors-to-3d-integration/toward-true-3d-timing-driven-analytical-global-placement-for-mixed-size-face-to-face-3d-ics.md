Toward True-3D Timing-Driven Analytical Global Placement for Mixed-Size Face-to-Face 3D ICs
Authors：
[Qiyuan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=915843)，[Fuxing Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=615843)，[Lixin Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=92235313980172470011)，[Hao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=715843)，[Hao Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=020843)，[Xiqiong Bai](https://63dac.conference-program.com/?post_type=page&p=15&uid=265843)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)，[Ziran Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=127643)

## 中文标题

面向混合尺寸面对面 3D IC 的真 3D 时序驱动解析全局布局

## 英文摘要

Face-to-face (F2F) three-dimensional integrated circuit (3D IC) design leverages advanced vertical interconnect technologies, such as hybrid bonding and micro-bump soldering, to vertically stack dies and preserve transistor-density scaling beyond Moore’s law. In this work, we present the first timing-driven analytical GP framework that moves toward true3D optimization for mixed-size F2F 3D ICs. We propose a comprehensive timing-driven net weighting formulation that integrates drive-strength-based cell delay, L-shaped RC-based net delay, and static timing analysis (STA)-based incremental timing criticality into the analytical GP model, serving as a foundational backbone for timing optimization and flexibly adapting to both true-3D and multi-die 2D GP environments. To steer macros away from central congestion and provide an effective 3D initialization, we introduce a macro-boundary-aware true-3D initial placement approach that models macro-to-boundary interactions using a differentiable function. Then, we develop the first timing-driven mixed-size true-3D GP algorithm that jointly optimizes standard cells and macros within a unified 3D design space, enabling cross-die timing refinement and improving 3D timing closure. After die partitioning based on true3D GP result, we further introduce a timing-driven multi-die 2D GP guided by 3D-aware STA, in which cross-die RC-trees are reconstructed to enable realistic 3D parasitic estimation for STA. Experimental results on the OpenROAD benchmark suites demonstrate that, compared with existing open-source placement flows and a wirelength-driven 3D GP baseline, our timing-driven 3D GP framework achieves at least 33.2% and 43.2% average improvements in total negative slack (TNS) and worst negative slack (WNS), respectively.

## 中文摘要

面对面（F2F）三维集成电路（3D IC）设计借助混合键合、微凸点焊接等先进垂直互连技术，将多个裸片垂直堆叠，从而在摩尔定律之外延续晶体管密度的缩放。本文提出首个时序驱动的解析全局布局（GP）框架，向面向混合尺寸 F2F 3D IC 的真 3D 优化迈进。我们提出一种全面的时序驱动线网加权公式，将基于驱动强度的单元延时、基于 L 形 RC 的线网延时以及基于静态时序分析（STA）的增量时序关键度统一纳入解析 GP 模型，作为时序优化的基础骨架，并可灵活适配真 3D 与多裸片 2D GP 两种环境。为引导宏单元远离中心拥塞区域并提供有效的 3D 初始化，我们引入一种宏单元边界感知的真 3D 初始布局方法，利用可微函数对宏单元与边界之间的相互作用建模。随后，我们提出首个时序驱动的混合尺寸真 3D GP 算法，在统一的三维设计空间中联合优化标准单元与宏单元，实现跨裸片的时序精化并改善 3D 时序收敛。在基于真 3D GP 结果完成裸片划分之后，我们进一步引入由 3D 感知 STA 引导的时序驱动多裸片 2D GP，其中重建跨裸片 RC 树，以实现贴近实际的 3D 寄生估计以用于 STA。在 OpenROAD 基准测试集上的实验结果表明，与现有开源布局流程以及线长驱动的 3D GP 基线相比，我们的时序驱动 3D GP 框架在总负松弛（TNS）与最差负松弛（WNS）上分别取得至少 33.2% 与 43.2% 的平均改善。

## 英文关键词

3D Integration, Mixed-Size Global Placement, Timing-Driven

## 中文关键词

3D 集成、混合尺寸全局布局、时序驱动
