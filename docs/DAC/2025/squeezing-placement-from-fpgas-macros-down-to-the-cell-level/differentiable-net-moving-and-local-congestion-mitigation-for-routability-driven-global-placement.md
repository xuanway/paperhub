---
title: "Differentiable Net-Moving and Local Congestion Mitigation for Routability-Driven Global Placement"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Differentiable Net-Moving and Local Congestion Mitigation for Routability-Driven Global Placement

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieda.oscc.cc/res/papers/25-DAC25-DCGP.pdf">https://ieda.oscc.cc/res/papers/25-DAC25-DCGP.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 可布线性驱动的全局布局，消除拥塞，单元移动 </p>
</div>


---

## 研究概要
本文提出兼顾全局/局部拥塞的可微分析式全局布局框架，融合泊松方程拥塞模型、动量单元膨胀、电源轨引脚可访问密度调整。通过虚拟单元引导网线远离拥塞区，在ISPD2015基准测试，相较Xplace-Route布线违规平均下降40%，总线长与过孔数基本持平。

## 背景和动机
1. 现有单元膨胀方法仅利用当前迭代拥塞，易出现单元反复往返拥塞区，或过度膨胀浪费布线资源。
2. 传统包围盒拥塞惩罚将盒内全部区域同等加权，包含无关拥塞网格，梯度引导效果差。
3. 全局布线拥塞与单元局部密度拥塞两类问题缺少统一可微建模方案，无法同步优化。
4. 引脚可访问性优化仅在细节布局阶段执行，全局阶段未预留M1电源轨布线空间，后期产生大量DR违规。
5. 主流可布性布局缺少自适应拥塞权重，轻拥塞场景过度牺牲线长，高拥塞场景优化力度不足。

## 相关工作
1. 静态单元膨胀布局：仅单次拥塞更新，无历史动量，单元反复回流拥塞区域。
2. BB式拥塞惩罚布局：整个包围盒统一施加代价，无法区分盒内真实拥塞位置。
3. NTplace4dr动量膨胀：仅解决局部密度问题，未建模全局网线拥塞。
4. Xplace-Route：电源轨密度一次性全局调整，无法随迭代动态适配拥塞变化。
5. 深度学习驱动布局：依赖预测网络，缺少解析可微梯度，迭代稳定性弱。

## 本文解决方案
### 1 泊松方程可微全局拥塞模型
以布线供需比值构建电荷密度，求解泊松电势场得到连续拥塞梯度；双引脚网线插入虚拟单元标记拥塞峰值，推导单元偏移梯度；多引脚高负载单元叠加拥塞力，动态平衡线长与拥塞损失权重。
### 2 动量感知动态单元膨胀
引入迭代历史膨胀动量项，单元移出拥塞区时施加收缩修正因子，设置膨胀上下限；区分拥塞增减趋势自动膨胀/收缩，避免过度膨胀与区域回流。
### 3 动态电源轨密度调整
预筛选长有效M2电源轨，仅在拥塞网格抬高单元密度，非拥塞区域不额外压缩布线通道，改善底层引脚可访问性。
### 4 统一多目标解析布局目标
加权平均WA线长项+静电密度项+可微拥塞项，采用Nesterov梯度下降迭代求解，GPU全局路由实时更新拥塞热力图。
### 5 完整可布性布局流水线
初始线长布局→GPU拥塞预估→动量膨胀+电源密度修正→拥塞梯度更新→梯度优化迭代，收敛后合法化与细节布局。

## 实验分析
1. 实验环境：Xeon+A800，ISPD2015无围栏基准，对比Xplace、Xplace-Route，后端统一Innovus布线评估。
2. 布线违规：相较Xplace-Route平均DRVs降低40%，原始Xplace降幅达80%，总线长、过孔数量几乎无损失。
3. 运行开销：布局耗时为Xplace-Route的1.59倍，但全局+详细总布线时间缩短7%~37%。
4. 消融实验：动量膨胀、可微拥塞、电源密度三项技术叠加后违规数最优，单一模块优化效果有限。
5. 大规模电路：Superblue系列高复杂度设计依旧稳定，无拥塞优化失效情况。

## 研究启发
1. 全局网线拥塞不能仅靠单元密度调控，需通过虚拟单元建立网线级可微梯度引导布线路径。
2. 单元膨胀引入历史动量与自动收缩机制，可解决单元在拥塞区来回震荡的经典缺陷。
3. 引脚可访问优化应嵌入全局布局，仅动态抬高拥塞电源轨区域密度，兼顾线长与布线通道。
4. 自适应拥塞权重能根据当前拥塞规模自动调整优化优先级，避免线长与可布性失衡。
5. 解析泊松电势场是稳定连续拥塞梯度的高效方案，相比深度学习预测更易工业工具集成。
