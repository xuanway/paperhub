---
title: "DANN: Diffractive Acoustic Neural Network for in-sensor computing system target at multi-biomarker diagnosis"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# DANN: Diffractive Acoustic Neural Network for in-sensor computing system target at multi-biomarker diagnosis


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/abstract/document/11133358">https://ieeexplore.ieee.org/abstract/document/11133358</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>衍射神经网络，传感器内计算，有限元分析方法，声表面波生物传感器，多生物标志物方法 </p>
</div>

---

## 研究概要
本文首次提出基于声表面波SAW的衍射声学神经网络DANN，面向多生物标志物片上传感计算。设计FEA有限元协同梯度训练流水线，通过金属长度调控SAW相位实现网络权重。在抑郁症、前列腺癌诊断任务验证，诊断精度接近临床标准，系统功耗相比传统方案降低66%。

## 背景和动机
1. 传统生物检测流程需传感、ADC、数字处理器分离，存在冯诺依曼瓶颈，模数转换带来大量功耗与延迟，难以实现片上实时诊断。
2. 光学衍射神经网络DONN难以微型化集成微流控芯片，激光、光学元件体积大、成本高，流体信噪比差。
3. SAW传感器生物检测灵敏度高，但尚无衍射神经网络落地方案；SAW基板各向异性、机械损耗复杂，解析传播矩阵误差极大，常规梯度训练失效。
4. 现有片上衍射网络训练直接跑有限元，单轮耗时数百秒，训练效率极低，无法兼顾精度与速度。

## 相关工作
1. 光学衍射神经网络DONN：依靠光衍射完成计算，但光路难以微型化，不兼容微流控生物传感场景。
2. SAW生物传感器：仅实现单一标志物信号采集，无片上神经网络分类计算能力。
3. 电磁/超声衍射网络：仅适用于成像识别，未适配多标志物生化相位信号输入。
4. 片上衍射网络直接FEA训练：无预提取传播矩阵流程，每轮仿真耗时数百秒，训练效率差。

## 本文解决方案
### 1. SAW基DANN片上传感计算硬件架构
41°Y切LN衬底搭建SH型SAW系统，金属覆盖区调控声波相位作为网络权重；传感区捕获生物标志物引发相位偏移，衍射层直接完成模拟矩阵乘，无ADC。
### 2. 三阶段FEA协同训练流水线
1）物理参数提取：仿真标定机电耦合系数K²，拟合相位-金属长度映射关系；
2）FEA辅助训练：有限元提取精准传播矩阵构建可微模型，梯度反向传播更新权重；
3）模型精调：随机扰动衍射层位置补偿平均化误差，输出金属版图参数。
### 3. 相位权重硬件映射模型
推导金属长度与SAW相位偏移公式，将训练后网络权重转换为可流片金属布线尺寸。
### 4. 随机区域微调优化算法
迭代扰动衍射单元、输出IDT位置，补偿传播矩阵平均引入计算偏差，优先优化输出层降低仿真开销。

## 实验分析
1. 仿真平台：COMSOL FEA，120MHz SAW，两类网络分别适配3标志物抑郁症、2标志物前列腺癌任务。
2. 精度对比：传统解析训练分类准确率仅50%；FEA协同训练+精调后抑郁症74.07%、前列腺癌86.0%，接近临床诊断水平。
3. 训练效率：纯FEA单轮330s，Python可微模型仅0.003s，协同训练速度提升10万倍以上。
4. 功耗测试：传统方案含ADC、相位检测功耗高，DANN整体功耗仅原34%，能耗节省66%。
5. 消融实验：仅FEA训练无精调时癌症任务精度不足50，证明位置微调对补偿硬件非理想至关重要。

## 研究启发
1. SAW是微流控生物传感适配的衍射计算载体，相比光学方案更易片上集成、信噪比更高。
2. 各向异性介质无法用理想波传播公式，必须通过FEA提取传播矩阵才能保证训练有效。
3. 分离数值建模与硬件仿真，先轻量Python训练再有限元精调，可平衡精度与巨大仿真耗时。
4. 衍射网络权重可通过声波相位物理实现，传感与计算一体化能彻底消除模数转换功耗瓶颈。
5. 生物多分类衍射网络输出层误差最大，微调算法优先优化输出单元可大幅降低迭代计算成本。