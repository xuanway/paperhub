---
title: "G-SpNN: GPU-Accelerated Passivity Enforcement for S-Parameter Modeling with Neural Networks"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# G-SpNN: GPU-Accelerated Passivity Enforcement for S-Parameter Modeling with Neural Networks

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133072">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133072</a></p> 
<p class="paper-seo-summary__meta"><strong>PPT链接:</strong> <a href="https://www.ssslab.cn/assets/slides/2025-li-GSpNN.pdf">https://www.ssslab.cn/assets/slides/2025-li-GSpNN.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 参数宏建模，无源性强制，神经网络，GPU加速 </p>
</div>


---

## 研究概要
本文提出GPU加速G-SpNN框架，将S参数无源宏建模的无源约束优化映射为神经网络训练任务。基于谱分解与PFE变换构造可微网络，搭配LBFGS二阶优化、QR化简损失。对比主流DAO算法，平均提速7.63倍，内存占用降低两个数量级，多端口射频互连建模精度更优。

## 背景和动机
1. 先进芯粒、多核电路多端口S参数宏建模需求激增，传统无源校正算法复杂度高，大规模场景内存溢出、迭代收敛缓慢。
2. VF+EPM/LC两步法先拟合再校正无源，会大幅牺牲拟合稳态误差，商用工具常放宽无源阈值引发时域仿真不收敛。
3. DAO三步优化框架虽兼顾精度与无源约束，但克罗内克积、完整海森矩阵计算内存开销爆炸，138端口直接内存超限。
4. 现有优化需手动推导复杂梯度，无自动微分机制，大规模矩阵求逆迭代耗时极高，难以GPU并行加速。
5. 一阶Adam类优化器在高维电路优化中震荡严重，易陷入伪收敛，无法逼近理论拟合下界。

## 相关工作
1. VF矢量拟合：快速生成有理宏模型，但输出系统不满足无源条件，需后置校正。
2. EPM/RPM/LC无源校正：扰动极点残量修复无源，拟合误差显著上升。
3. DAO交替域优化：转化无约束优化兼顾精度，但克罗内克运算内存随端口爆炸式增长，无法GPU加速。
4. 凸规划无源建模复杂度O(n⁶)，仅适用极小规模低阶电路。
5. Adam一阶优化器：无需海森矩阵，但高维射频建模收敛不稳定、损失下降缓慢。

## 本文解决方案
### 1 无源优化转神经网络映射
将DAO无约束优化问题等价构建前向网络层：SPF谱分解为网络输入参数L、Q，PFE部分作为网络前向变换，拟合误差定义为损失，依托PyTorch自动微分完成梯度回传，省去手工求导。
### 2 QR分解简化最小二乘损失
对频率特征矩阵做QR分解，重构损失函数规避重复矩阵范数运算，大幅降低每轮迭代矩阵计算量，适配GPU向量化并行。
### 3 LBFGS二阶近似优化
不存储完整海森矩阵，仅保存梯度/参数更新历史近似海森逆，稳定迭代方向，相比Adam收敛更平滑，避免震荡伪收敛。
### 4 GPU向量化计算流水线
全部矩阵克罗内克、谱分解、PFE变换迁移GPU显存，多频点并行计算，内存不随端口数剧烈膨胀。
### 5 完整G-SpNN迭代流程
VF+LC生成初始无源系统→SPF转换网络参数→前向传播算损失→LBFGS反向更新L/Q→循环至收敛，输出高精度无源宏模型。

## 实验分析
1. 实验环境：RTX4070 GPU，对比MATLAB实现DAO；测试11~138端口真实射频Touchstone工业文件。
2. 收敛效率：同等收敛阈值下平均提速7.63倍，DAO高端口案例内存溢出提前终止，G-SpNN可完整迭代。
3. 内存性能：DAO内存平均为G-SpNN的171.3倍，端口规模提升时G-SpNN内存保持平稳。
4. 拟合精度：稳态误差贴近VF理论下界，显著优于LC校正、原始DAO方案，全频点拟合偏差更小。
5. 消融对比：LBFGS优于Adam，一阶优化存在剧烈震荡、难以收敛至最优损失。

## 研究启发
1. 电路带约束数值优化可等价映射深度学习训练框架，借助自动微分与GPU并行解决传统算法算力瓶颈。
2. 克罗内克等高开销矩阵运算可通过QR代数化简，从数学层面降低迭代存储与计算开销。
3. 高维射频无源优化必须采用二阶类LBFGS优化器，一阶Adam难以稳定收敛至最优拟合点。
4. 传统DAO框架的内存瓶颈源于完整海森与克罗内克存储，网络式参数表示可规避大规模矩阵常驻显存。
5. 面向芯粒多端口互连场景，GPU驱动神经网络优化是兼顾无源约束、拟合精度与可扩展性的可行路线。