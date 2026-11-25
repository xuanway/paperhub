---
title: "AutoClock: Automated Clock Management for Power-Efficient HLS Designs on FPGAs"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# AutoClock: Automated Clock Management for Power-Efficient HLS Designs on FPGAs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133279">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133279</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高层次综合，时钟管理，跨时钟域，时钟门控，时钟多路选择器 </p>
</div>


---

## 研究概要
本文提出AutoClock开源FPGA高层次综合时钟自动化管理框架，适配Vitis HLS。自定义时钟编译指令，ILP求解最优MMCM/PLL/BUFG资源分配；分层贪心门控降低动态功耗，自适应插入多类CDC同步电路，时钟多路复用解决跨域TDM冲突。在Alveo U28验证，时钟门控+多时钟协同优化下动态功耗最高下降74.38%。

## 背景和动机
1. 商用Vitis HLS缺少完整多时钟自动化流程，设计师需手动搭建时钟拓扑、CDC同步电路，开发周期冗长。
2. FPGA内置MMCM、PLL、BUFGCE时钟资源功耗差异大，多频率需求下资源组合空间庞大，无自动化最优分配方案。
3. 现有时钟门控方法仅适配流式数据流模块，未覆盖通用FSM控制模块，且未考虑FPGA门控硬件数量限制。
4. 跨时钟域(CDC)信号分单比特电平/脉冲、多比特数据流、共享存储等多类型，传统工具无法自适应生成对应同步单元。
5. 分时复用(TDM)模块跨多时钟域时会出现功能失效，缺乏时钟多路复用配套修复方案。

## 相关工作
1. 单一时钟生成优化：仅针对PLL/MMCM做频率规划，未统筹BUFGCE低功耗门控资源，无全局功耗目标。
2. 专用CDC同步方案：仅支持FIFO握手等单一跨域场景，无法兼容脉冲、复位、共享BRAM多类信号。
3. HLS时钟门控研究：局限流水线数据流模块，不支持通用FSM架构，未做分层功耗收益排序分配。
4. 多时钟HLS框架：缺少自动化资源绑定与TDM冲突修复，需人工划分时钟域，自动化程度低。
5. RTL级低时钟优化：位于后端阶段，无法在HLS高层完成时钟域规划，迭代成本高。

## 本文解决方案
### 1 自定义HLS时钟编译指令与解析器
新增inputclk、clkdomain两类pragma，支持顶层输入时钟与模块时钟频率配置；专用解析器提取时钟域信息并清洗原始指令，兼容原生Vitis编译流程。
### 2 ILP迭代约束时钟资源分配
以总功耗最小为目标建立整数规划模型，优先低成本BUFG分频资源，剩余频率由MMCM/PLL分组生成；不可行解迭代增加功耗约束重新求解，输出最优时钟资源绑定方案。
### 3 分层贪心时钟门控策略
自上而下遍历模块层级，扣除上层已门控空闲周期计算净功耗收益；优先给收益高模块分配有限BUFGCE，区分数据流连续模块不插入门控，基于ap_start/ap_done控制门控使能。
### 4 自适应多类型CDC自动插入
针对不同信号匹配同步单元：电平/脉冲双触发器同步器、复位专用同步、异步FIFO、异步BRAM；脉冲信号增加电平转换时序规避采样丢失。
### 5 时钟多路复用TDM修复方案
构建FSM切换多路时钟BUFGMUX，插入空闲状态保证时钟切换稳定，同一硬件模块可被多时钟域分时调用，避免重复实例化增加资源功耗。

## 实验分析
1. 实验环境：AMD Alveo U280、Vitis2023.2，基于AutoSA/PolyBench构建P1~P3MC多时钟混合基准，对比原生Vitis基线、随机/BFS/DFS门控策略。
2. 时钟门控效果：单独门控动态功耗最高降62.35%，分层贪心策略远优于随机分配；LUT/FF硬件增量极低。
3. 多时钟域收益：差异化分配频率可单独降低动态功耗26.64%，BRAM资源仅增加2.31%。
4. 组合优化效果：门控+多时钟协同优化下动态功耗最大下降74.38%。
5. TDM验证：时钟多路复用方案不牺牲分时吞吐，仅小幅增加LUT开销，无需多份模块拷贝。

## 研究启发
1. FPGA时钟优化需在HLS高层统一完成域划分、资源分配、门控、CDC，后置RTL手动优化迭代成本过高。
2. BUFGCE门控资源数量受限，分层计算净功耗收益是高效分配核心，不可简单随机填充。
3 跨时钟域信号类型差异巨大，不能统一使用双触发器，需区分脉冲、存储、复位信号匹配专用同步电路。
4. ILP迭代约束可在海量时钟资源组合中快速得到全局低功耗解，兼顾硬件数量与分频数学约束。
5. 多时钟域与时钟门控属于互补优化，二者联合使用可实现功耗大幅衰减，具备工程落地价值。
