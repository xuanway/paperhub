---
title: "Reinforcement Learning-Driven Window Selection for Enhanced Window-Based Rip-up and Reroute in Chip Detailed Routing"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Reinforcement Learning-Driven Window Selection for Enhanced Window-Based Rip-up and Reroute in Chip Detailed Routing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132699">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132699</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 强化学习，窗口选择，拆线重绕，详细布线 </p>
</div>


---

## 研究概要
本文提出基于Maskable PPO强化学习的窗口重布线优化方案，面向详细布线RUR流程。采用SE-ResNet提取版图多层密度特征，动态调整窗口尺寸与撕裂模式，缓解DRV扩散问题。基于ISPD2018基准测试，全部电路实现无DRV布线，总线长平均优化0.07%，通孔数降低2.42%，整体运行时间仅小幅增加0.61%。

## 背景和动机
1. 先进工艺设计规则严苛，详细布线的撕裂重布线(RUR)耗时占物理设计大头，固定网格窗口策略易产生DRV扩散、难以消除密集区域违规。
2. 主流TritonRoute采用固定7×7网格单调平移窗口，高密度区域无法自适应扩大窗口，局部违规持续残留。
3. 固定窗口撕裂模式无法区分迭代阶段，前期全局重构、后期局部修复无自适应切换，资源开销高。
4. 现有AI布线方案未针对RUR窗口生成做定制强化学习，不能结合金属/通孔密度动态调整窗口边界。
5. DRV扩散现象缺少统一量化建模，静态窗口易将违规推至相邻区域，迭代收敛速度慢。

## 相关工作
1. TritonRoute：经典窗口式详细布线，采用固定GCell网格、单调平移窗口，撕裂模式固定，高密度电路易残留DRV。
2. 路径式RUR：重布线规模大、多线程并行性差，整体运行开销远高于窗口方案。
3. 各类RL布线工作：多针对布局、斯坦纳树、定制单元布线，无面向R窗口自适应生成的强化学习框架。
4. PPO/Maskable PPO：稳定强化学习算法，可屏蔽非法动作，此前未应用于版图窗口规划。
5. SE-ResNet图像特征网络：擅长多通道特征加权，未落地多层版图密度特征提取场景。

## 本文解决方案
### 1 瓦片式版图分层特征建模
将版图切分细粒度瓦片，分别计算金属层DRV密度、金属密度、通孔层密度，构建3D多层密度图作为RL环境状态，精细表征局部拥塞。
### 2 Maskable PPO强化学习智能体
以违规瓦片为核心，智能体决策窗口四向扩展幅度与两种撕裂模式(RM0局部修复/RM1全局重构)，动作掩码过滤越界、尺寸非法窗口。
### 3 SE-ResNet多通道特征提取器
分3D金属、3D通孔、2D辅助三大分支提取特征，SE模块自适应加权拥塞、违规通道，融合窗口位置注意力特征辅助决策。
### 4 分阶段复合奖励函数
窗口形态奖励约束长宽比；DRV消除奖励鼓励违规置于窗口中心；撕裂模式惩罚抑制高开销RM1，实现收敛速度与布线质量平衡。
### 5 分阶段动态窗口策略
迭代前期生成大窗口、选用RM1打散高密度DRV；中后期缩小窗口、优先RM0局部修复，兼顾消除率与运行耗时，支持批量GPU并行推理。

## 实验分析
1. 测试环境：基于TritonRoute二次开发，ISPD2018全套10组工业基准，训练集4组衍生版图。
2. DRV消除能力：基线TritonRoute在18_4、18_10存在残留违规，本文方案所有电路均可实现零DRV。
3. 布线质量：总线长平均减少0.07%，通孔总数平均下降2.42%，布线资源利用率更优。
4. 运行效率：平均总耗时仅增加0.61%，半数测试案例速度优于基线；批量GPU推理缓解RL推理开销。
5. 消融对比：标准ResNet无通道自适应，无法动态切换撕裂模式；SE-ResNet可随迭代自适应调整窗口大小与RM选择。

## 研究启发
1. 固定网格窗口无法适配多变拥塞版图，基于密度感知动态窗口是解决DRV扩散的核心思路。
2. 多层版图密度属于多通道特征，SE注意力网络能有效区分拥塞/违规区域，提升RL决策精度。
3. RUR迭代存在阶段差异，强化学习需设计分阶段偏好，前期全局打散、后期局部修复可平衡速度与质量。
4. Maskable PPO适配版图几何约束，能自动剔除非法窗口，降低搜索空间，提升训练稳定性。
5. 强化学习可轻量化嵌入开源布线工具，在几乎不增加运行成本前提下彻底消除顽固设计违规。