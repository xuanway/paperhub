---
title: "REMU: Memory-aware Radiation Emulation via Dual Addressing for In-orbit Deep Learning System"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# REMU: Memory-aware Radiation Emulation via Dual Addressing for In-orbit Deep Learning System

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132935">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132935</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>深度学习，星载人工智能，内存仿真 </p>
</div>

---

## 研究概要
本文面向星载COTS GPU深度学习场景，提出REMU内存感知辐射仿真器。设计双寻址+位图树架构打通DRAM硬件故障与运行时DNN映射，精准模拟SEU/MCU空间相关比特翻转。在10类卫星DNN、两类遥感任务验证，注入开销由百倍降至3倍，揭示轻量化模型更脆弱、MCU不能等效多SEU等辐射容错规律。

## 背景和动机
1. 星载算力普遍采用商用GPU替代昂贵抗辐芯片，但空间辐射引发SEU、MCU内存比特翻转，导致DNN推理静默错误，威胁卫星遥感任务可靠性。
2. 地面束流、在轨实测成本极高、周期漫长，现有软件故障注入工具存在缺陷：仅在模型静态权重注入，不匹配DRAM空间关联MCU故障，缺失虚实-物理-DRAM完整地址映射。
3. DNN推理运行时内存碎片化，传统遍历全物理地址搜索故障开销巨大，无法支持大规模容错评测。
4. 现有工具忽略TensorRT运行引擎内存区域，仅关注权重参数，难以定位推理中间缓存、内核逻辑等高危故障点位。
5. MCU是行/列/DQ三维邻域多比特错误，简单随机多SEU无法复现真实硬件故障对精度的破坏效果。

## 相关工作
1. 硬件级辐射测试：地面粒子束、在轨长期观测，数据真实但成本高、迭代慢，无法批量开展模型容错筛选。
2. 编译/微架构故障注入工具（LLFI、Sassifi）：面向通用程序，不兼容GPU统一内存与DNN推理流水线。
3. DNN专用注入框架（TensorFI、PyTorFI）仅静态修改模型权重，不覆盖运行时引擎，不支持空间关联MCU仿真。
4 DRAM仿真工具Ramulator：仅完成硬件寻址建模，缺少与DNN进程虚拟地址双向映射能力，无法对接AI推理负载。
5. 星载DNN可靠性研究：仅简单随机比特翻转评测，未区分SEU/MCU差异，容错分析结论片面。

## 本文解决方案
### 1 三层完整地址映射链路
依托Linux pagemap完成虚拟地址→物理地址转换；扩展Ramulator实现物理地址映射至DRAM通道/块/行/列单元，建立DNN推理引擎到存储单元一一对应关系。
### 2 位图树双寻址优化机制
构建DRAM分层位图索引树，仅保留DNN占用有效内存区域；深度优先遍历分层分配故障数量，规避海量无效地址检索，大幅降低注入耗时。
### 3 真实辐射故障仿真模型
支持独立SEU与行/列/DQ三维空间关联MCU，可配置多比特翻转数量、故障占比，贴合太空辐射实测统计分布。
### 4 运行时全内存注入机制
覆盖权重参数、激活缓存、TensorRT引擎内核、输出缓冲区全部内存区域，区分崩溃故障与静默推理错误。
### 5 轻量化库式集成方案
提供libREMU动态链接库，无需大规模源码插桩，原生兼容TensorRT部署的星载Jetson平台。

## 实验分析
1. 测试环境：Jetson Xavier NX 16GB LPDDR4，10种CNN/ViT/YOLO模型，RESISC45遥感分类、DOTA目标检测两大在轨任务，BER设1e-7/1e-6。
2. 性能开销：无优化注入耗时膨胀67~99倍，位图树优化后仅3.1~3.5倍，大规模批量评测效率大幅提升。
3. 模型容错规律：轻量化EfficientNet/MobileNet精度衰减最剧烈；ViT、MLPMixer鲁棒性更强；INT8量化比FP3容错表现更好。
4. MCU对比实验：同等误码率下，MCU比特数、占比越高推理精度下滑越严重，单纯叠加多个SEU无法等效MCU破坏效果。
5. 故障点位分析：引擎尾部内核、输出缓冲区易引发断崖式精度崩塌，仅评估权重参数会低估辐射风险。

## 研究启发
1. 星载DNN可靠性评测不能仅静态修改模型权重，必须覆盖GPU运行时完整内存空间，引擎辅助逻辑是高频静默故障源。
2. DRAM空间关联MCU故障不能简化为独立单比特错误，仿真工具需还原行/列/DQ三维邻域翻转特征。
3. 虚实-物理-硬件三层地址映射是连接上层AI负载与底层辐射故障的关键，分层位图索引树可解决海量内存检索瓶颈。
4. 轻量化嵌入式DNN虽省存储算力，但对空间辐射比特翻转更敏感，卫星选型需平衡开销与容错能力。
5. 面向在轨部署前验证，可使用REMU批量筛选高鲁棒模型，优先加固引擎尾部、输出缓存等高风险内存区域。