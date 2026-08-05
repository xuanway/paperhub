---
title: "Security of Approximate Neural Networks against Power Side-channel Attack"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "approximate-computing"
  - "side-channel"
  - "neural-network"
  - "cpa"
---

# Security of Approximate Neural Networks against Power Side-channel Attack

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133333">https://ieeexplore.ieee.org/document/11133333</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 神经网络硬件，功耗侧信道攻击，近似计算，人工智能 </p>
</div>

---

## 研究概要
本文探究近似神经网络PE的功耗侧信道安全性，对比过频、电压缩放、位级近似三种方案。随近似程度提升功耗迹SNR显著下降，MTD成倍增长；电压缩放防护效果最优。提出SPD安全-功耗-时延综合指标，同等误差下电压缩放SPD最高，可作为轻量级抗CPA防御手段。

## 背景和动机
1. 边缘AI硬件广泛采用近似计算降低能耗，但近似电路对功耗侧信道攻击的防护能力缺乏系统性验证。
2. CPA功耗攻击可通过采集电流迹逆向窃取神经网络权重，造成模型IP泄露，边缘设备物理接触攻击风险极高。
3. 现有近似计算研究仅关注精度、功耗折中，未量化不同近似手段的侧信道泄露差异。
4. 缺少统一评价指标兼顾安全强度、硬件功耗与时延，难以对比各类近似方案的综合安全收益。
5. 业界不清楚电压/频率/位级近似哪一种更适合兼顾能效与模型权重防护。

## 相关工作
1. DNN功耗侧信道攻击：FPGA/嵌入式加速器CPA、EMA攻击，可完整逆向权重与网络架构，但未结合近似电路场景。
2. 位级近似硬件：近似加法/乘法单元，通过舍弃低位降低功耗，仅评估推理精度，无安全分析。
3. 电压/频率缩放(VFS)：动态调压超频降低算力能耗，现有研究仅分析时序误差，未研究侧信道噪声增益。
4. 神经网络硬件防护：掩码、随机化等专用防御，面积功耗开销大，无法适配低功耗边缘终端。
5. 近似与安全交叉少量工作：仅定性描述噪声抑制，未量化SNR、MTD、综合SPD指标。

## 本文解决方案
### 1 三类典型近似PE标准化建模
统一4bit乘加神经元处理单元，分别实现：①超频过频；②降压电压缩放；③低位舍弃位级近似；匹配25%、37.5%两组近似误差用于公平对比。
### 2 基于汉明距离的CPA攻击评估流程
以权重汉明距离构建功耗假设模型，采集硬件电流迹做相关性分析，用相关系数区分真实权重与猜测值。
### 3 SNR泄露量化指标
定义SNR为真实权重相关系数与最优错误权重系数比值，SNR越低代表功耗迹有效泄露越少，攻击难度越高。
### 4 MTD攻击难度度量
测量成功恢复权重所需最小功耗迹数量，MTD数值越大，攻击者采集成本越高、防护效果越好。
### 5 SPD综合评价指标
SPD=MTD/(功耗×时延)，统一融合安全强度、硬件能耗、推理延迟，横向对比三类近似方案综合收益。

## 实验分析
1. 仿真平台：45nm CMOS工艺，Cadence电路仿真，基础精确PE作为对照组。
2. SNR表现：近似程度越高SNR衰减越快；同误差下电压缩放<超频<位级近似，噪声抑制能力最强。
3. MTD结果：精确PE仅需48条迹；25%误差电压缩放MTD=570、超频≈600、位级200；37.5%下两种缩放MTD超1024。
4. SPD综合收益：25%误差电压缩放SPD是精确PE的20倍，37.5%达35倍，三类方案中综合性能最优。
5. 功耗迹特征：电压缩放整体电流基线大幅降低，超频瞬时峰值更高，位级近似电流变化幅度最接近精确电路。

## 研究启发
1. 各类近似计算天然引入功耗噪声，可作为零额外硬件开销的轻量级功耗侧信道防御。
2. 电压缩放抗CPA能力显著优于超频、位近似，低功耗边缘AI应优先采用调压近似方案。
3. 仅靠推理精度无法衡量近似电路安全，必须配套SNR、MTD等侧信道专用量化指标。
4. SPD指标可统一权衡安全、功耗、时延，为近似AI硬件选型提供标准化评价依据。
5. 无需额外掩码电路，适度可控近似就能大幅提升权重窃取攻击门槛，适合资源受限IoT神经网络设备。