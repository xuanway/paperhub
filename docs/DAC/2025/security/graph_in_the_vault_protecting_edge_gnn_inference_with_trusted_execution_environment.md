---
title: "Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "graph-neural-network"
  - "trusted-execution-environment"
  - "intel-sgx"
  - "edge-computing"
  - "privacy"
---

# Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.15012">https://arxiv.org/abs/2502.15012</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 可信执行环境，图神经网络，分区-预训练策略，GNN修正器 </p>
</div>

---


## 研究概要
本文提出GNNVault，首款面向边缘GNN的TEE安全推理框架，采用训练前拆分策略，构建公共主干与TEE私有校正器。公共主干基于替代图运行于不可信区，真实邻接矩阵与轻量化校正器置于SGX飞地。多图数据集测试精度损失低于2%，可抵御链路窃取攻击，飞地内存占用符合SGX限制，推理开销可控。

## 背景和动机
1. 边缘本地部署GNN存在双重隐私风险：攻击者窃取模型权重、通过中间嵌入实施链路窃取攻击，还原用户私有图连接关系。
2. 现有TEE安全方案仅适配CNN/LLM，未考虑GNN消息传递依赖邻接矩阵，大图完整放入飞地超出SGX EPC内存上限。
3. 噪声加密、模型水印等被动防护精度损失大，同态加密计算开销极高，无法满足边缘实时推理需求。
4. 直接将完整GNN放入TEE受硬件内存约束，大图稠密邻接矩阵存储成本极高，频繁换页造成巨大延迟。
5. 缺乏分拆式GNN安全架构，未区分公开节点特征与私有边结构，难以平衡安全、精度与内存开销。

## 相关工作
1. TEE保护DNN方案：对CNN/大模型分层拆分，仅处理图像张量，无图结构消息传递逻辑，不适配GNN邻接矩阵保护。
2. 模型水印/非迁移学习：被动防御模型窃取，无法阻止基于中间嵌入的链路推理攻击。
3. 同态加密GNN：全密文图运算，推理速度下降数千倍，边缘设备无法落地。
4. 链路窃取攻击研究：证明GNN中间嵌入可反推节点连接，但未提出针对性TEE防御方案。
5. 图隐私扰动方法：随机修改边结构，会造成严重分类精度衰减，商用场景可用性差。

## 本文解决方案
### 1 训练前分层拆分架构
训练阶段分离公共主干、私有校正器；主干采用KNN/余弦相似度生成替代邻接矩阵，仅使用公开节点特征训练，无私有边信息泄露。
### 2 三类轻量化TEE校正器
并行、级联、串行三种校正器结构：并行逐层修正嵌入精度最优；串行仅传入最后层嵌入，飞地内存最小；级联汇聚多层特征，表达能力更强。
### 3 单向安全数据流约束
仅允许不可信区向TEE单向传输嵌入，logits、真实邻接矩阵、校正权重全程隔离在飞地，仅输出最终分类标签。
### 4 邻接矩阵内存优化
真实图采用CO稀疏格式存储，搭配预计算度矩阵压缩，大幅降低TEE内存占用，适配SGX 96MB EPC限制。
### 5 端到端SGX部署流水线
PyTorch实现公共主干，C+++Eigen开发飞地校正器；GPU加速不可信主干，TEE仅执行轻量化校正模块，兼顾速度与安全。

## 实验分析
1. 实验配置：Cora/Citeseer等6类标准图，Intel i7+SGX硬件，对比无防护GNN、纯DNN基线，评估精度、内存、链路窃取AUC。
2. 精度表现：并行校正器效果最优，整体精度损失小于2%；替代图中KNN、余弦相似度主干性能显著优于随机图、纯DNN。
3. 内存开销：校正器参数仅几十MB，全部模型飞地内存峰值41.6MB，远低于SGX 96MB上限；主干占用内存超128MB，不适合放入TEE。
4. 推理时延：串行校正器开销最低，相比原生GNN仅增加52%~131%；并行因传输中间嵌入延迟更高。
5. 安全验证：多种相似度链路窃取攻击下，GNNVault的AUC降至DNN基线水平，私有边结构无法被攻击者还原。

## 研究启发
1. GNN安全不能照搬CNN的TEE分拆思路，图的私有邻接矩阵是核心泄露源，必须隔离在可信硬件内。
2. 训练阶段解耦公开图近似与私有真实拓扑，是解决TEE内存瓶颈的核心手段，轻量化校正器可大幅降低飞地资源需求。
3. 单向数据流+仅输出标签能阻断基于中间嵌入的链路窃取，仅开放最终结果可彻底屏蔽图结构信息。
4. 校正器存在精度、内存、时延三角权衡，可根据边缘硬件内存限制选择并行/串行结构。
5. 单纯扰动图边会大幅降低精度，基于TEE硬件隔离的主动防护方案，在隐私与推理性能间平衡更优。

### 相关阅读

- **TEE for ML**：Slalom (USENIX ATC 2023)、Graviton (ASPLOS 2020)
- **链路窃取攻击**：He et al., "LinkTeller: Recovering Private Edges from GNN" (USENIX 2022)
- **图神经网络综述**：Wu et al., "A Comprehensive Survey on GNN" (IEEE TNNLS 2020)
