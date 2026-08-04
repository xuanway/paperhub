---
title: "PUFiM: A Robust and Efficient FeFET-Based Security Solution Merging Physical Unclonable Function with Compute-in-Memory for Edge AI"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PUFiM: A Robust and Efficient FeFET-Based Security Solution Merging Physical Unclonable Function with Compute-in-Memory for Edge AI

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132800">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132800</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 硬件安全，存内计算，物理不可克隆函数，铁电场效应晶体管</p>
</div>


---

## 研究概要
本文提出基于FeFET的PUFiM一体化架构，将PUF物理密钥生成与存内计算CiM融合在同一MLC阵列。设计四类配套优化抵御建模攻击与密钥泄露，VGG/ResNet测试下密钥泄露95%时推理精度下降超60%，存储密度、能效相较主流安全CiM分别提升9.7倍、1.2倍以上。

## 背景和动机
1. 边缘AI存内计算权重明文存储，极易被窃取，传统AES/软件加密开销巨大，不兼容CiM原位运算。
2. 现有轻量XOR加密依赖外部寄存器链传输密钥，存在密钥劫持、探针窃取漏洞，PUF与CiM分块设计面积冗余。
3. 传统安全CiM采用互补单元存储密文，单元数量翻倍，存储密度大幅降低，能效损耗严重。
4. 现有FeFET PUF抗建模攻击能力弱，百万级样本即可破解，无法保障模型长期知识产权安全。

## 相关工作
1. 分离式安全CiM（XOR-CIM/SRA）：权重成对互补存储，单元翻倍，无原生PUF，密钥通过寄存器传输易泄露。
2. 独立FeFET PUF：仅实现质询响应生成，未和推理阵列融合，需额外硬件对接密钥。
3. 分立PUF-CIM架构：PUF与CiM阵列物理隔离，存在密钥传输攻击面，存储利用率低。
4. 各类PUF原语（仲裁PUF/XOR PUF）：线性结构居多，攻击者海量样本即可完成建模破解。

## 本文解决方案
### 1 MLC FeFET混合存储计算阵列
利用FeFET多级单元特性，MSB存互补PUF比特、LSB存储权重，单单元同时支持PUF异或密钥生成与CiM乘累加，省去互补冗余单元。
### 2 上电混淆+非线性后处理PUF加固
上电随机双稳态电路选择PUF行增加熵；复用CiM加法器构造多层非线性质询输出，抵御LR、XGB等建模攻击。
### 3 块内本地密钥生成解密
阵列块内完成质询-PUF异或生成临时密钥，不对外传输密钥，消除寄存器链劫持攻击；原位完成权重解密与乘累加。
### 4 权重感知分层映射
MSB优先计算提前截断无效ReLU通路降低能耗；同权重比特打散至不同加密块，单块密钥泄露无法完整还原权重。

## 实验分析
1. 仿真平台：28nm FeFET阵列，VGG8、ResNet18，对比SRAM/RRAM/STT-MRAM/FeFET四类安全CiM。
2. 安全指标：百万级训练样本下建模攻击识别准确率仅50.26；95%密钥泄露时模型精度暴跌60%以上。
3. 硬件指标：存储密度10.52Mb/mm²，算力密度0.444TOPS/mm²，相较SOTA提升9.7倍，能效提升1.2倍。
4. 电路可靠性：PUF/CiM单元读出错误率均低于2%，27~85℃宽温下密钥生成电路稳定。
5. 消融实验：权重映射平均减少34.6%计算量，PUF非线性机制是抗攻击核心。

## 研究启发
1. 将密钥生成PUF与推理CiM集成至同一存储阵列，可彻底消除密钥传输攻击面，同时削减冗余存储单元。
2. FeFET循环间随机阈值波动是优质硬件熵源，配合多层非线性变换可大幅提升PUF抗建模能力。
3. 结合ReLU计算特征做权重分层映射，能同步实现推理节能与防权重窃取双重收益。
4. 安全存内计算无需额外互补存储单元，MLC多比特复用是提升密度与能效关键路线。
5. 边缘AI硬件安全需端到端设计，从密钥生成、传输、解密到原位计算全链路消除漏洞。
