---
title: "DeepPUFSCA: Deep learning for Physical Unclonable Function attack based on Side Channel Analysis support"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "physical-unclonable-function"
  - "side-channel-analysis"
  - "deep-learning"
  - "puf-attack"
  - "fpga"
---

# DeepPUFSCA: Deep Learning for PUF Attack Based on Side Channel Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://pureadmin.qub.ac.uk/ws/portalfiles/portal/633404316/DAC_2025_camera_ready.pdf">https://pureadmin.qub.ac.uk/ws/portalfiles/portal/633404316/DAC_2025_camera_ready.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 人工智能与机器学习，FPGA系统，安全与隐私 </p>
</div>

---

## 研究概要
本文提出DeepPUFSCA深度学习混合攻击框架，针对宣称抗建模的4×4仲裁PUF，同时输入激励与功耗侧信道轨迹双特征。推导PUF激励、功耗与响应数学关联，双分支网络分别提取两类特征融合预测。FPGA实测最高建模准确率81.11%，相比传统机器学习提升显著，证明侧信道信息可有效强化PUF建模攻击能力。

## 背景和动机
1. 4×4仲裁PUF采用多路并行MUX结构，复杂度更高，现有方案声称其可抵御传统机器学习建模攻击，安全边界缺乏验证。
2. 传统PUF建模仅使用激励-响应对(CRP)，忽略电路开关跳变带来功耗泄露，丢失大量内部时序特征。
3. 单一机器学习/深度学习模型仅依赖CRP，面对高复杂度多比特PUF拟合能力不足，预测准确率偏低。
4. 现有混合攻击未独立设计双特征提取网络，无法充分挖掘功耗轨迹携带的内部路径信息。
5. 缺少针对4×4 APUF的专用深度学习攻击方案，该PUF的实际安全脆弱性有待实验验证。

## 相关工作
1. 传统机器学习PUF攻击：LR、SVM、集成树等仅利用CRP，线性拟合能力有限，对高维复杂PUF效果差。
2. 纯深度学习PUF攻击：CNN/MLP仅输入激励，未引入侧信道辅助信息，建模精度存在明显上限。
3 单一侧信道PUF攻击：仅依靠功耗/时序轨迹，无激励特征协同，特征信息不完整，泛化性弱。
4. 早期混合攻击：简单拼接激励与侧信道编码，无分支特征提取，无法分离两类数据的独有特征。
5. PUF防护设计：XOR、iPUF、4×4 APUF等通过增加非线性提升抗建模能力，但未完成全面攻防验证。

## 本文解决方案
### 1 理论关联推导
建立4×4 APUF数学模型，证明激励直接决定电路稳态路径；推导CMOS门动态功耗公式，证实功耗轨迹包含开关噪声与路径隐含信息，可补充CRP缺失的内部特征。
### 2 双分支深度融合网络架构
设计双输入分支：MLP分支提取二进制激励全局特征；CNN分支对一维功耗时序轨迹做卷积池化提取局部跳变特征，两路特征拼接后送入多层MLP完成多分类。
### 3 标准化数据集构建
基于FPGA+PICOscope采集系统，同步捕获激励、6比特响应、功耗轨迹；采用MinMax归一化消除采样噪声，划分4:1训练/测试集。
### 4 超参优化训练策略
多层堆叠网络，CNN核最优尺寸11，隐藏层神经元64；SGD优化+交叉熵损失，早停策略防止过拟合。
### 5 分层评测指标体系
设计整体准确率、Top-k准确率、平均秩、汉明距离、类别置信度多维度指标，全面评估模型建模效果与鲁棒性。

## 实验分析
1. 实验平台：CW305 FPGA开发板、1GS/s PICO示波器，采集50万组样本，对比LR、LGBM、XGBoost等十余种主流算法。
2. 精度对比：DeepPUFSCA整体准确率81.11%，比LGBM高11%、比逻辑回归高35%；引入功耗特征相比纯CRP提升2.54%。
3. 细粒度性能：6路输出单比特准确率近95%，Top-3准确率达90%；错误样本汉明距离多为1~2，误判程度低。
4. 消融实验：最优配置为MLP/CNN分类层各15层、隐藏层64、卷积核11，50万样本达到性能峰值。
5. 鲁棒性验证：各类正确类别置信度显著高于随机猜测，最优/次优置信度差值普遍大于0.2，模型区分度强。

## 研究启发
1. 高复杂度4×4仲裁PUF无法完全抵御深度学习建模，仅增加多路非线性不足以规避机器学习攻击风险。
2. 功耗侧信道包含PUF内部路径独有信息，将时序轨迹与激励融合可显著提升建模攻击准确率。
3. 双分支异构网络分别处理离散激励与时序功耗，相比简单特征拼接能更充分挖掘两类数据特征。
4. 评估PUF抗建模安全性，不能仅用传统机器学习，需结合深度学习+侧信道混合攻击做完整验证。
5. 新型多路仲裁PUF防护设计需同步兼顾机器学习建模与功耗侧信道两类威胁，单一维度加固存在安全漏洞。

## 相关资源

- **PUF 综述**：Gao et al., "Physical Unclonable Functions" (Nature Electronics, 2020)
- **CRP 建模攻击**：Rührmair et al., "PUF Modeling Attacks on Simulated and Silicon Data" (IEEE TIFS, 2013)
- **Arbiter PUF**：Lim et al., "Extracting Secret Keys from Integrated Circuits" (IEEE TVLSI, 2005)
- **XOR Arbiter PUF**：Suh & Devadas, "Physical Unclonable Functions for Device Authentication" (DAC 2007)
