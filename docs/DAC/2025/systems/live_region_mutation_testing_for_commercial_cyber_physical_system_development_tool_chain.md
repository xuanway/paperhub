---
title: "Live Region Mutation Testing for Commercial Cyber-Physical System Development Tool Chain"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Live Region Mutation Testing for Commercial Cyber-Physical System Development Tool Chain

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS1: Autonomous Systems (Automotive, Robotics, Drones)</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133188">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133188</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>信息物理系统，Simulink，模输入等价性，差分测试，编译器测试 </p>
</div>

---

## 研究概要
本文提出面向Simulink编译器的LION活区域变异差分测试框架，采用store-revert块对保证数据流等价，结合MCMC采样生成多样化模块序列。通过同源模型多仿真模式输出对比捕获编译缺陷。实验在R2018a、R2021b版本共检出11个缺陷，长期测试稳定版发现16个有效bug，其中12个全新漏洞，检出能力优于SLforge、SLEMI、COMBAT。

## 背景和动机
1. Simulink是工控、车载CPS主流建模工具，编译器缺陷会导致代码生成异常，引发安全关键系统故障，但现有测试方案漏洞检出率偏低。
2. 现有变异测试仅改造僵尸无效区域，变异不影响数据流，编译器不会执行对应逻辑，难以触发深层编译缺陷。
3. 传统变异仅修改/删除原有模块，无法生成全新模块序列，对多类型编译器优化逻辑覆盖不足，变异多样性差。
4. Simulink无完备形式化规范，自带数据类型自动推导机制，简单修改易破坏输入等价(EMI)特性，导致差分测试失效。
5. 通用编译器活变异方案面向C/Java，不匹配Simulink框图、多采样时序等独有特性，无法直接移植。

## 相关工作
1. 随机生成类SLforge：全自动生成Simulink模型，仅覆盖少量模块类型，漏洞挖掘效率低，200CPU小时仅检出1个bug。
2. EMI变异SLEMI/COMBAT：基于输入等价改造模型，但仅针对僵尸区域，模块生成手段单一，新版本缺陷检出能力大幅衰减。
3. 通用语言活区域变异(LLVM/JVM)：面向文本程序，无框图数据流、采样时序适配逻辑，不能用于Simulink工具链。
4. CPS模型仿真优化类研究：聚焦仿真加速、测试用例生成，未针对Simulink编译器漏洞挖掘。
5. 传统差分测试(Csmith等)：仅适用于文本编译器，缺乏框图模型等价维持机制。

## 本文解决方案
### 1 等价数据流生成模块
通过Simulink信号覆盖工具剖分模型，筛选活区域插入store-revert自定义块对；存储块记录流经数据，恢复块还原数值，搭配类型转换块抵消自动推导干扰，严格维持EMI等价，在活区域构建合法变异空间。
### 2 MCMC驱动模型变异模块
基于海量有效模型库统计模块出现密度、转移概率，构建马尔可夫链；按接受概率采样生成多段全新模块序列插入块对之间，大幅提升模块多样性，自动适配数据类型兼容约束。
### 3 EMI差分测试模块
同源种子模型与变异模型同步运行Normal、Accelerator两种仿真模式，逐采样点比对输出；任意时刻数值不一致即判定编译器存在缺陷，自动最小复现模型并生成官方提交工单。
### 4 完整LION流水线
模型剖分→活区域插入等价块对→MCMC生成模块序列→类型校正→编译过滤→多模式差分比对→漏洞归约与上报，全流程自动化。

## 实验分析
1. 实验配置：测试Simulink R2018a、R2021b，基线SLforge/SLEMI/COMBAT，统一200CPU小时评测，种子含工业真实模型与SLforge生成模型。
2. 漏洞检出对比：基线合计最多检出6个bug，LION共发现11个；稳定版R2021b检出8个，优势显著。
3. 组件消融：关闭store-revert等价构造仅检出2个bug；替换MCMC为随机采样仅检出5个，两大核心组件缺一不可。
4. 长期实测：连续两月运行于商用稳定R2021b，上报16个官方确认漏洞，12个全新未公开缺陷，覆盖编译提示、时序、数值多类故障。
5. 工程落地：开源Matlab实现，自动生成最小复现模型，适配主流Simulink版本，变异成功率稳定约0.45。

## 研究启发
1. Simulink编译器测试必须优先改造活数据流区域，僵尸区域变异无法触发编译器深层优化逻辑，漏洞挖掘效率极低。
2. 块对隔离+类型校正可在复杂框图、自动类型推导机制下稳定维持输入等价，是差分测试可行基础。
3. 基于模型统计的MCMC采样相比随机模块生成，能显著提升变异多样性，覆盖更多编译器分支。
4. 商用成熟工具仍存在大量未被发现编译缺陷，长周期自动化变异测试具备工程实用价值。
5. 面向无规范框图式建模工具的测试，不能照搬文本程序活变异思路，需针对数据流、采样时序做定制等价改造。