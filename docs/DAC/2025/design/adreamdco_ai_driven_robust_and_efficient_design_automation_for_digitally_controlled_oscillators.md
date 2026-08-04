---
title: "AdreamDCO: AI-Driven Robust and Efficient Design Automation for Digitally Controlled Oscillators"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# AdreamDCO: AI-Driven Robust and Efficient Design Automation for Digitally Controlled Oscillators


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES4: Digital and Analog Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132798">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132798</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>人工智能，贝叶斯优化，互补金属氧化物半导体，设计自动化，差分进化，数字控制振荡器，频率调谐，射频集成电路，残差神经网络 </p>
</div>


---

## 研究概要
本文提出AdreamDCO人机协同AI全自动化DCO设计流程，分主谐振腔、精细调谐两步完成有源无源协同设计。采用迁移学习残差代理模型替代耗时EM/电路仿真，差分进化逆设计快速生成版图，单次训练后80秒输出GDSII，覆盖1–20GHz。22nm流片FoM超192.4dBc/Hz，分辨率低于1.5kHz，优于人工设计。

## 背景和动机
1. 传统DCO全人工设计，迭代周期长达数周，3D电磁、非线性电路仿真算力消耗极大，极易陷入局部最优。
2. 现有AI射频工具仅优化无源器件，缺少有源-无源协同端到端自动化流程，无法联合晶体管与谐振腔整体优化。
3. 高精度亚kHz频率调谐无源结构推导复杂，人工难以设计满足严苛分辨率的耦合辅助线圈。
4. 工艺偏差验证依赖海量蒙特卡洛EM仿真，传统方法耗时数十小时，量产鲁棒性评估成本极高。

## 相关工作
1. 单无源AI优化：CNN/GNN等模型仅预测无源S参数，不兼容晶体管有源核心协同仿真。
2. 专用振荡器人工设计：依靠集总模型反复迭代，定制电容面积开销大，无自动化生成能力。
3. 贝叶斯模拟射频工具：仅小规模参数寻优，无法完成完整版图GDSII自动合成。
4. 单一频段DCO设计：不具备1–20GHz宽频适配能力，缺少工艺变异快速验证机制。

## 本文解决方案
### 1. 两步式人机协同自动化设计框架
步骤一：Class-F₂主谐振腔+晶体管核心设计，优化相位噪声、功耗与FoM；步骤二：双辅助耦合线圈精细调谐，实现亚1.5kHz分辨率，分阶段解耦两大核心指标优化。
### 2. 迁移学习残差代理仿真模型
简化金属堆叠预训练、完整PDK数据集微调缩减3倍采样开销；3/40层残差网络分别适配主腔、调谐线圈，R²>0.97，替代海量3D EM与HB仿真。
### 3. DE差分进化逆设计求解
构造含FoM、频率、相位噪声约束的损失函数，预筛无法起振电路；对比贝叶斯优化，DE收敛更快、精度更高，40秒内完成参数寻优。
### 4. 双弱耦合辅助线圈调谐结构
双辅助线圈分层粗/细21bit电容阵列，复用标准PDK电容无需定制；AI自动优化线圈几何，规避调谐死区，蒙特卡洛仿真仅需15秒完成工艺鲁棒性校验。

## 实验分析
1. 设计效率：一次性数据集采集77h、模型训练1h，任意规格从指标到GDSII仅需80秒，远优于人工数周周期。
2. 频率适配：覆盖1–20GHz全频段，1.6~20GHz多频段设计FoM均高于189dBc/Hz。
3. 流片实测：22nm SOI两款原型，7.1–8.6GHz、3.8–4.6GHz调谐区间，分辨率<1.5kHz，FoM最高193.3dBc/Hz，直流功耗低至0.45mW。
4. 对比SOTA：无需定制电容，相位噪声、FoM、功耗全面领先同类人工DCO，工艺变异仿真速度提升上万倍。
5. 算法对比：差分进化DE相比贝叶斯优化，频率精度、相位噪声、FoM指标更优，寻优耗时更短。

## 研究启发
1. 射频自动化不能仅单独优化无源，有源晶体管与谐振腔端到端协同建模是全局最优关键。
2. 迁移学习可大幅降低EM数据集采集成本，残差网络适合高精度射频电路代理建模。
3. 分阶段解耦核心性能指标（FoM/调谐分辨率）能大幅降低逆设计优化难度。
4. 弱耦合多层辅助线圈可在标准器件下实现超高频率分辨率，AI可辅助人工推导难以解析的无源拓扑。
5. AI代理模型可将工艺变异蒙特卡洛仿真提速上万倍，为射频芯片量产鲁棒性快速验证提供可行路径。