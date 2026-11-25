---
title: "High Energy-efficiency and Low latency In-Memory Computing using Analog Accumulator and In-Memory ADC with shared References"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# High Energy-efficiency and Low latency In-Memory Computing using Analog Accumulator and In-Memory ADC with shared References

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133014">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133014</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 存内计算，存内模数转换器，静态随机存取存储器，电荷共享，多位</p>
</div>

---

## 研究概要
本文提出基于双8T SRAM的存内计算宏，融合RWLUDC单元、电荷共享位切片累加BSCHA与共享参考可重构IMADC。65nm工艺下ADC面积开销仅3%，MAC线性度提升23倍，吞吐较PWM提升1.9倍；搭配噪声鲁棒训练，MLP/VGG8/GAT推理精度损失均低于0.8%，峰值能效1146 TOPS/W。

## 背景和动机
1. 冯诺依曼内存墙导致DNN访存时延、能耗极高，模拟SRAM存内计算是有效解决方案，但存在PVT失配、线性度差问题。
2. 传统逐列IMADC面积开销巨大，SAR/Flash ADC吞吐受限，难以兼顾精度与硬件成本。
3. PWM、传统位切片(BS)多比特输入方案循环数多，ADC反复触发带来大量能耗与时延开销。
4. 位线放电电流随电压变化，造成MAC非线性，复杂图神经网络等高精度任务推理精度大幅下滑。

## 相关工作
1. 单列独立IMADC：每列配置独立斜坡发生器，ADC阵列面积占比最高27%，硬件开销严重。
2. PWM多比特输入：输入编码周期随比特指数增长，位线电压摆幅大，MAC线性度极差。
3. 传统数字BS：每比特单独ADC采样，多次模数转换叠加能耗与延迟，数字累加引入额外开销。
4. 7T/8T基础SRAM IMC单元：无共源共栅稳压设计，放电电流波动大，信号裕度低。

## 本文解决方案
### 1 RWLUDC双8T存储单元
读写通路解耦支持三值权重，读字线欠压共源共栅结构稳定放电电流，大幅扩大位线有效电压摆幅，抑制非线性误差。
### 2 BSCHA电荷共享模拟累加
引入等容MOM电容实现二进制加权模拟求和，仅最后执行一次ADC，消除多轮模数转换带来的时延、能耗损耗。
### 3 共享参考可重构IMADC
单列全局斜坡参考源供全部MAC列复用，搭配差分灵敏放大器与纹波计数器，ADC阵列面积开销降至3%，支持1~7bit动态精度配置。
### 4 噪声鲁棒训练NRT
前向注入电路非理想噪声，反向使用理想梯度更新权重，补偿模拟硬件带来的推理精度衰减。

## 实验分析
1. 工艺与平台：65nm CMOS，256×128 IMC阵列，对比SAR/Flash/传统IMADC、PWM、标准BS方案；测试MLP(MNIST)、VGG8(CIFAR10)、GAT(Cora)。
2. 硬件指标：ADC面积开销3%，峰值能效1146 TOPS/W、面积效率27 TOPS/mm²；相较PWM吞吐提升1.9倍、MAC线性度提升23倍。
3. 时延能耗：7比特输入场景，相比传统BS吞吐提升6.6倍、能效提升1.7倍；电压缓冲功耗仅占总能耗2%。
4. 推理精度：NRT补偿后，MLP精度降0.1%、VGG8降0.8%、GAT降0.5%，接近浮点基线。
5. 消融验证：RWLUDC单元保障线性，BSCHA是时延能耗核心优化，共享ADC大幅削减硬件面积，三者缺一综合性能显著下滑。

## 研究启发
1. 模拟IMC非线性根源是单元放电电流漂移，读字线欠压共源共栅可低成本提升信号线性区间。
2. 多比特输入无需逐次数字量化，片上电容模拟加权累加能省去多次ADC，是低延迟关键思路。
3. 全局共享ADC斜坡参考可大幅降低外设面积，差分放大器搭配缓冲可解决长线驱动不足问题。
4. 模拟电路噪声无法单纯靠硬件消除，软硬件协同噪声感知训练可极小代价恢复推理精度。
5. 存储单元、模拟累加、模数转换外设需全链路协同设计，单一模块优化难以兼顾面积、时延、能效。
