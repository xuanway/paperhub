---
title: "InterConFuzz: A Fuzzing-based Comprehensive NoC Verification Framework"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# InterConFuzz: A Fuzzing-based Comprehensive NoC Verification Framework

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133216">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133216</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 硬件安全，片上网络，安全验证，模糊测试 </p>
</div>


---

## 研究概要
本文提出基于UVM的混合模糊验证框架InterConFuzz，融合覆盖率制导模糊测试与符号执行，通过CFG检查点局部复位减少仿真开销。在OpenTitan TL-UL NoC中检出5类安全漏洞，较SeVNoC多发现3个；内存、算力开销分别降低24.4%、29.5%，覆盖率与主流NoC模糊工具NoCFuzzer持平。

## 背景和动机
1. 片上网络(NoC)是SoC互联核心，路由、事务漏洞易引发数据泄露、DoS攻击，传统人工测试覆盖不足、漏漏洞风险高。
2. 纯仿真验证迭代慢，形式化方法难以适配大规模RTL NoC，现有硬件模糊工具全局状态探索能力弱。
3. 现有NoC验证工具缺少符号执行引导机制，覆盖率停滞时无法自动生成新激励，大量重复仿真浪费算力。
4. 全电路硬复位耗时巨大，频繁重置拖慢验证速度，缺少局部检查点回滚机制。
5. 主流SeVNoC、NoCFuzzer漏洞检出能力有限，无法覆盖事务残留、地址篡改等边界安全场景。

## 相关工作
1. 软件模糊工具(AFL/libFuzzer)：面向程序二进制，无法适配硬件时序、总线事务特征。
2. RTL专用模糊器(NoCFuzzer)：仅随机生成激励，无符号约束引导，覆盖率提升缓慢。
3. SeVNoC：基于CFG静态分析，缺少动态模糊迭代，无法捕获运行时事务篡改漏洞。
4. 硬件符号执行：单路径求解开销大，未与UVM仿真流程融合，工业落地难度高。
5. 传统UVM约束随机：依赖人工编写约束，边界场景覆盖不足，人力成本高。

## 本文解决方案
### 1 UVM原生融合混合模糊架构
扩展标准UVM验证环境，新增指令语料库、依赖方程提取、SMT约束求解、覆盖率统计模块，完全兼容工业UVM验证流程。
### 2 CFG驱动检查点局部复位机制
PyVerilog提取RTL控制流图，将高分支寄存器标记为检查点；覆盖率停滞时仅回滚至就近检查点，替代全局复位，大幅削减仿真周期开销。
### 3 符号执行引导激励生成
覆盖率长时间无增长时，提取未覆盖路径约束送入Z3求解器，生成针对性总线事务激励，主动探索边界安全场景。
### 4 控制寄存器覆盖率度量方法
以控制寄存器组合状态作为覆盖率指标，精准量化NoC内部路径覆盖，解决传统波形覆盖粒度粗糙问题。
### 5 安全属性漏洞检测机制
预设数据残留、地址篡改、虚假事务等安全断言，仿真时实时监控属性违例，自动输出漏洞触发波形与激励序列。

## 实验分析
1. 测试基准：OpenTitan TL-UL NoC（漏洞检测）、OpenPiton NoC（覆盖率对比），仿真器采用Vivado。
2. 漏洞检出：共发现5类CWE安全缺陷，SeVNoC仅检出2种，遗漏事务残留、源/目的地址篡改漏洞。
3. 资源开销：相较SeVNoC，内存占用下降24.4%，计算资源减少29.5%。
4. 覆盖率对比：与NoCFuzzer最终覆盖率持平，收敛速度更快；Interval=3为算力与覆盖最优平衡点。
5. 稳定性：多轮测试覆盖率方差仅2.64%，激励随机性带来波动小，验证结果稳定可靠。

## 研究启发
1. 将符号执行与硬件模糊、工业UVM流程结合，可自动生成边界激励，大幅降低人工约束编写成本。
2. 基于CFG的局部检查点回滚是降低硬件模糊仿真开销的有效手段，避免全设计频繁复位。
3. 控制寄存器组合比传统行/信号覆盖更适合衡量NoC内部状态完备性。
4. 现有静态CFG分析工具无法覆盖运行时动态事务漏洞，必须搭配动态模糊迭代检测安全缺陷。
5. 面向总线安全验证，混合式模糊框架可在算力更低的前提下提升漏洞检出完备性，适配商用SoC验证流程。
