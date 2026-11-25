---
title: "SSDTrain: An Activation Offloading Framework to SSDs for Faster Large Language Model Training"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# SSDTrain: An Activation Offloading Framework to SSDs for Faster Large Language Model Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2408.10013">https://arxiv.org/abs/2408.10013</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/K-Wu/FlashTrain">https://github.com/K-Wu/FlashTrain</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 激活值卸载，SSD存储，大语言模型训练，训练加速 </p>
</div>


---

## 研究概要
本文提出SSDTrain面向大模型训练的激活卸载框架，基于NVMe SSD借助GDS直连通路异步搬运激活张量，配套张量去重、数据转发优化，IO与计算完全重叠。兼容PyTorch/Megatron/DeepSpeed，在BERT/GPT/T5测试，激活峰值内存最高降低47%，训练时延几乎无损失，可提升微批次大小、减少流水线气泡。

## 背景和动机
1. LLM模型规模增速远超GPU显存扩容速度，训练中激活张量占80%以上显存，显存成为核心性能瓶颈。
2. 现有缓解手段（缩小微批次、梯度累积、激活重计算）会造成GPU利用率下降、算力浪费，重计算额外引入大量重复前向运算。
3. CPU内存容量、带宽受限，无法承载海量激活离线存储；SSD容量弹性更大、可独占带宽，但缺少面向训练的激活卸载方案。
4. 现有卸载方案同步读写IO阻塞计算关键路径，带来显著训练时延；且大多仅适配推理，不支持训练反向传播重取激活。
5. 主流分布式训练框架缺少原生SSD卸载接口，现有方案兼容性差，难以对接ZeRO、流水线并行等主流训练策略。

## 相关工作
1. 激活重计算方案：仅降低显存上限，但引入重复前向计算，吞吐量大幅下滑。
2. ZeRO-Infinity等CPU卸载方案：依赖CPU内存与中转缓冲区，带宽受限、同步IO拖慢训练。
3. 推理侧SSD卸载（FlexGen）：仅缓存KV缓存，无训练所需前向激活异步读写逻辑，不支持反向复用。
4. FlashNeuron等DNN SSD卸载：未针对Transformer多层级激活、分布式训练做优化，不兼容LLM并行范式。
5. 通用张量交换框架：同步读写为主，无法将SSD传输与GPU计算完全重叠，存在固定IO开销。

## 本文解决方案
### 1 GDS直连异步SSD传输架构
基于kvikio与CUDA钩子实现GPU与NVMe SSD直连，绕过CPU内存缓冲区；分离读写线程池，前向异步落盘、反向预取激活，IO完全掩盖在GPU计算间隙。
### 2 钩子驱动张量缓存管理器
基于PyTorch前向/反向钩子追踪张量生命周期，自定义唯一张量ID解决地址复用冲突；区分权重与激活，仅卸载中间激活张量。
### 3 张量去重与数据转发优化
结合张量存储时间戳生成全局唯一标识，避免重复落盘；预取时若张量仍在内存直接复用，跳过SSD读取减少IO请求。
### 4 自适应卸载阈值调度
根据模型隐藏维度、SSD带宽动态调整单次卸载激活总量，最后一层激活常驻GPU无需预取，平衡显存节省与IO次数。
### 5 分布式框架兼容设计
无侵入式monkey patch改造调度器，原生适配张量/数据/流水线并行、ZeRO优化，单进程逻辑隔离不干扰多卡分布式通信。

## 实验分析
1. 实验环境：2×A100 40GB、7块Optane SSD，PyTorch+Megatron-DeepSpeed，测试BERT/GPT/T5，对比无卸载、激活重计算基线。
2. 显存优化：各类模型激活峰值内存降低28%~47%，同等显存预算可翻倍微批次尺寸。
3. 训练时延：SSD IO完全被计算掩盖，单步训练时延与无卸载基线几乎持平，远优于重计算方案。
4. 吞吐量对比：ROK曲线验证同等显存下SSDT吞吐量显著高于重计算；更大批次可削减流水线并行气泡。
5. 硬件仿真：主流数据中心SSD顺序写入寿命超2年，单GPU所需PCIe带宽低于12.1GB/s，硬件成本可控。

## 研究启发
1. 激活是LLM显存主要矛盾，相比重计算、CPU卸载，NVMe SSD异步卸载可兼顾显存释放与无损耗训练速度。
2. GPU-GDS直连是SSD卸载关键，CPU中转会引入不可掩盖的传输延迟，必须规避缓冲区开销。
3. 张量生命周期精准追踪+数据转发可大幅减少重复SSD读写，是降低IO压力的轻量化手段。
4. 训练卸载方案需全分布式生态兼容，不能割裂ZeRO、流水线并行等主流优化策略。
5. 增大微批次尺寸可减少梯度累积开销与流水线气泡，显存释放带来的吞吐量增益具备工程落地价值。
