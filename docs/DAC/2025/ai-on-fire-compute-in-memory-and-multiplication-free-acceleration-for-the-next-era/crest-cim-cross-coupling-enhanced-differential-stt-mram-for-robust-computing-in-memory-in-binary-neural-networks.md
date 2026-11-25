---
title: "CREST-CiM: Cross-Coupling-Enhanced Differential STT-MRAM for Robust Computing-in-Memory in Binary Neural Networks"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# CREST-CiM: Cross-Coupling-Enhanced Differential STT-MRAM for Robust Computing-in-Memory in Binary Neural Networks


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133247">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133247</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 二值神经网络，存内计算，交叉耦合，自旋转移矩磁性随机存取存储器，隧穿磁阻，同或</p>
</div>


---

## 研究概要
本文提出CREST-CiM交叉耦合STT-MRAM存内计算单元，面向二值神经网络BNN。采用双MTJ互补存储±1权重，交叉耦合晶体管大幅提升高低电流比至8150。64×64阵列仿真显示读出裕度提升3.4倍、读扰动裕度提升27.6%，ResNet-18推理精度达86.7%，仅小幅面积开销，时延能耗增幅不足1%。

## 背景和动机
1. STT-MRAM基CiM受限于TMR比值低，阵列寄生电阻、工艺偏差加剧高低电流区分度差，产生计算误差、推理精度暴跌。
2. BNN仅±1权重，适合差分CiM，但现有2T-2MTJ差分单元零态电流IL偏大，阵列IR压降严重，读出裕度不足。
3. 现有优化方案（伪列、PWA部分字线激活）仅事后补偿，无法从单元底层抑制IL，鲁棒性提升有限。
4. 传统MRAM CiM读电流易扰动存储状态，读扰动裕度低，阵列大规模部署稳定性差。

## 相关工作
1. 1T-1MTJ单单元CiM：结构面积小，但IL极高，依赖伪列抵消误差，读出裕度极低，推理精度损失严重。
2. 2T-2MTJ差分CiM：双MTJ存互补权重，但无交叉耦合，IL仍达微安级，抗工艺偏差能力弱。
3. SOT-MRAM协同设计：换存储器件，无法改进STT-MRAM单元底层电流区分问题。
4. PWA/伪列补偿策略：软件/外围电路折中，带来时延、ADC成本开销，无法根除单元固有IL缺陷。

## 本文解决方案
### 1. 交叉耦合CREST存储单元
单元集成左右互补MTJ+交叉耦合M1/M2晶体管、读写独立门控管；MTJ分别存储+1/-1，读时耦合管自动关断低阻支路，将IL压低至nA级，I_H/I_L最高8150。
### 2. 专用读写电路机制
写通路通过M4控制双向电流切换MTJ平行/反平行态；读通路选择0.66V最优读电压，耦合管自调节支路导通状态，大幅抑制读扰动电流。
### 3. 64×64完整CiM阵列架构
字线、位线、屏蔽线分层布线，采用PWA8部分字线激活；配套电流减法器、3bit Flash ADC，输入映射0/1简化XNOR矩阵乘。
### 4. BNN适配编码方案
输入映射In'=(In+1)/2，阵列并行完成XNOR点积；通过移位+预存权重和简化输出转换，无需额外加法树硬件。
### 5. 多非理想仿真评估框架
整合线阻、驱动电阻、MTJ氧化层/尺寸/阈值电压工艺偏差，蒙特卡洛量化单元与系统推理误差。

## 实验分析
1. 仿真环境：45nm工艺，STT-MRAM器件校准模型，对比1T-1MTJ、2T-2MTJ两类基线。
2. 单元电路：最优读压下I_H/I_L=8150，最差读出裕度6.56μA，较2T-2MTJ提升3.4倍；读扰动裕度提升27.6%。
3. 硬件开销：单元层面面积是2T-2MTJ的1.5倍，但含外围整体阵列仅增加7.9%面积，CiM时延、能耗增幅均<1%。
4. 工艺鲁棒性：千次蒙特卡洛仿真输出电流重叠极小，抵抗阈值、MTJ尺寸、氧化层工艺偏差能力更强。
5. 系统推理：CIFAR-10上BNN ResNet-18精度86.7%，相比2T-2MTJ提升10.7%，仅比纯软件低1.35%。

## 研究启发
1. MRAM CiM鲁棒性短板根源是单元零态大电流IL，仅靠外围补偿治标，必须从存储单元电路改造。
2 交叉耦合晶体管是低成本提升电流区分度的方案，小幅写性能损耗可被CiM推理的高频使用收益抵消。
3 差分双MTJ架构适配BNN±1权重天然需求，搭配耦合电路可同时提升读出与读扰动两类裕度。
4 单元面积开销可被阵列+外围分摊，整体硬件代价可控，适合边缘BNN低功耗推理场景。
5 器件-单元-阵列-网络四层联合仿真，才能完整评估存内计算实际推理精度损失。
