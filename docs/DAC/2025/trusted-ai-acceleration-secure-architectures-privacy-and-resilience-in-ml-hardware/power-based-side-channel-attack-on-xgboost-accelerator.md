---
title: "Exploiting Power Side-Channel Vulnerabilities in XGBoost Accelerator"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "xgboost"
  - "side-channel"
  - "fpga"
  - "model-extraction"
---

# Exploiting Power Side-Channel Vulnerabilities in XGBoost Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133048">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133048</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> XGBoost，硬件安全，侧信道攻击，高层次综合，现场可编程门阵列 </p>
</div>

---

## 研究概要
本文针对HLS实现的FPGA XGBoost加速器FAXID提出功耗侧信道窃取攻击。利用树节点分支判断产生差异化功耗轨迹，结合二分搜索逆向节点分割特征。Sakura-X板实测，单决策节点平均需36.7万条功耗迹即可还原模型内部特征，证实树型机器学习硬件存在严重模型提取漏洞。

## 背景和动机
1. FPGA搭载XGBoost多用于欺诈检测等高敏感场景，模型权重、分割特征属于商业机密，但现有侧信道研究集中于CNN，极少关注树类加速器。
2. 同类Bonsai决策树攻击无法适配XGBoost分层迭代、sigmoid输出的独特硬件计算流程，现有方法失效。
3. HLS综合生成流水线硬件，节点左右分支存储不同ID，汉明距离差异造成可区分功耗波形，形成天然泄露通道。
4. 业界普遍忽视ML加速器物理安全，缺少针对XGBoost硬件的侧信道风险验证与攻击范式。
5. 暂无量化XGBoost各节点攻击所需功耗样本量的系统性实验，漏洞危害缺乏数据支撑。

## 相关工作
1. 神经网络侧信道攻击：针对CNN/BNN加速器，利用功耗窃取权重、网络结构，不适用于树型分支运算。
2. Bonsai决策树SCA：依靠函数参数泄露建模，XGB无同类可调参数，攻击逻辑无法复用。
3. HLS硬件安全研究：多聚焦密码电路存储优化泄露，未覆盖机器学习推理流水线。
4. 硬件模型窃取：多为软件层面模型提取，缺乏物理功耗通道的硬件逆向方案。
5. 功耗统计分析方法：仅用于密码TVLA评估，未用于机器学习树节点特征逆向。

## 本文解决方案
### 1 XGBoost硬件泄露机理分析
HLS流水线get_leaf_single函数执行分支比较，左右子节点ID汉明距离不同，寄存器写入功耗存在显著差异，形成可观测功耗特征点POI。
### 2 二分搜索式节点特征逆向攻击
固定节点分割阈值区间，迭代更换输入样本采集功耗轨迹；通过POI分布区分分支走向，不断缩小区间精准还原节点分割特征。
### 3 KDE核密度分布区分POI
提取每条功耗迹峰值点构建概率密度曲线，依据分布重叠程度判断分支可区分度，量化攻击所需样本规模。
### 4 样本量量化统计模型
设定α=0.05、统计功效80%，基于Cohen效应量计算各节点最低采集迹数；输入与阈值差值越小，所需样本数量呈指数上升。
### 5 两类硬件防护思路
方案一统一所有子节点ID汉明距离，消除功耗差异；方案二硬件功耗均衡电路/软件掩码抹平分支功耗波动。

## 实验分析
1. 实验平台：Sakura-X FPGA(24MHz)+20dB放大器+250MS/s示波器，基于Vitis/Vivado综合FAXID加速器。
2. 轨迹区分效果：左右分支功耗波形峰值差异明显；节点ID汉明距离越小，密度分布重叠度越高、识别难度越大。
3. 样本规模：28节点树含14个决策点，平均367218条迹可完整逆向；最差节点需502万条，最优仅65条。
4. 相关性规律：输入值与节点分割阈值差值和所需样本量呈负相关，差值越小攻击成本越高。
5. 防护验证：统一ID汉明距离、硬件功耗均衡电路均可消除分支功耗差异，阻断攻击条件。

## 研究启发
1. 基于HLS生成的树型ML加速器天然存在分支功耗泄露，不能直接部署高隐私业务。
2. 神经网络侧信道方案无法迁移至XGBoost，需针对比较运算流水线设计专属攻击范式。
3. 节点ID汉明距离是功耗泄露核心诱因，硬件设计阶段应统一ID比特翻转数量。
4. 模型物理安全评估需量化各节点攻击成本，微小阈值差仍存在长期泄露风险。
5. 边缘FPGA机器学习硬件需配套功耗均衡电路或软件掩码作为标准安全加固手段。