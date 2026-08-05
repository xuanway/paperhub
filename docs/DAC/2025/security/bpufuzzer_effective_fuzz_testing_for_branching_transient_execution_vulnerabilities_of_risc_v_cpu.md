---
title: "BPUFuzzer: Effective Fuzz Testing for Branching Transient Execution Vulnerabilities of RISC-V CPU"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "risc-v"
  - "transient-execution"
  - "spectre"
  - "fuzz-testing"
  - "cpu-verification"
  - "hardware-security"
---

# BPUFuzzer: Effective Fuzz Testing for Branching Transient Execution Vulnerabilities of RISC-V CPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133085">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133085</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>瞬态执行漏洞，模糊测试，分支预测单元 </p>
</div>

---


## 研究概要
本文提出面向RISC-V处理器预硅RTL模糊测试工具BPUFuzzer，基于CFG生成含循环的完整控制流测试用例，设计BPU、RoB微架构感知的适应度与覆盖度指标引导种子筛选。在Boom v3上测试，相较SpecDoctor覆盖提升16.7%，并发现新型Spectre-Loop推测执行漏洞。

## 背景和动机
1. 现代CPU分支预测单元BPU易引发Spectre类推测执行漏洞，现有模糊工具无法完整覆盖循环控制流，漏洞挖掘能力受限。
2. SpecDoctor等主流工具生成测试用例时禁用循环结构，缺失循环预测相关漏洞的测试场景，且无微架构专属反馈机制。
3. 现有RTL模糊工具仅关注寄存器、控制信号，忽略BTB、LOOP、RoB等分支预测硬件状态，难以定位BPU侧隐蔽泄露。
4. 分支指令组合空间庞大，海量测试用例中筛选高风险样本缺乏量化评估标准，测试效率低下。
5. 缺少面向RISC-V乱序处理器、适配完整循环结构的预硅漏洞检测方案，芯片流片前隐患难以提前暴露。

## 相关工作
1. 后硅模糊Medusa、SpecFuzz：依赖现成CPU，无法在RTL设计阶段提前挖掘潜在漏洞。
2. 预硅工具Introspectre：仅针对Meltdown类漏洞，测试样本固定，控制流覆盖不足。
3. DifuzzRTL/SIGFuzz：以多路选择器控制信号为覆盖标准，不匹配推测执行硬件特征。
4. SpecDoctor：基于CFG生成用例，但强制屏蔽循环，无BPU硬件状态反馈，无法发现LOOP相关漏洞。
5. WhisperFuzz：侧重时序行为，未设计BTB、TAGE、LOOP预测器专用覆盖与适应度评价函数。

## 本文解决方案
### 1 支持全循环的CFG测试用例生成与校验
对基本块内指令、跳转目标双向变异；设计无限循环检测修正算法，区分无条件死循环、固定条件循环两类无效用例，自动调整分支源寄存器保证循环可退出。
### 2 BPU/RoB微架构硬件插桩
采集BTB、uBT、TAGE、LOOP预测器读写、预测错误、重排序缓冲区完整硬件状态日志，作为漏洞判定原始数据。
### 3 漏洞导向适应度函数
以分支预测错误次数加权BTB命中次数构建适应度值，优先选取易触发推测乱序执行的测试样本作为变异种子。
### 4 分支预测专属覆盖度计算
哈希BT集合、元数据状态生成覆盖特征，优先新增硬件状态的用例，小概率保留低覆盖样本避免局部最优。
### 5 锦标赛式种子筛选流程
先过滤新增覆盖用例，剩余样本随机保留5%；候选集按适应度锦标赛择优，迭代生成高风险测试序列。

## 实验分析
1. 实验平台：Chipyard仿真Boom v3 RV64G乱序处理器，基线工具SpecDoctor，统一6基本块约束。
2. 控制流多样性：SpecDoctor仅生成120种无环CFG，BPUFuzzer可生成海量含循环异构控制流图。
3. 覆盖指标：同等测试量下硬件状态覆盖提升16.7%；带反馈机制漏洞样本检出效率提升14.5%。
4. 漏洞挖掘：检出uBTB、LOOP等SpecDoctor无法发现的Spectre变种，全新Spectre-Loop可1024bit密钥泄露，误码率低于0.01%。
5. 漏洞原理验证：Spectre-Loop利用LOOP预测器提前退出，越界瞬态访存，配合刷新重载完成密钥提取。

## 研究启发
1. 循环分支预测是易被忽视的硬件漏洞面，模糊测试必须完整支持循环控制流才能全覆盖推测执行风险。
2. 通用控制信号覆盖标准不适用于侧信道/推测漏洞，需针对BPU、RoB等微组件定制覆盖指标。
3. 融合硬件运行状态的适应度函数可高效筛选高风险测试用例，大幅降低无效仿真开销。
4. 预硅RTL模糊是芯片流片前排查Spectre类漏洞低成本手段，无需依赖实体CPU硬件。
5. 分支预测子模块（LOOP/uBT/TAGE）均存在独立泄露通路，安全验证需分模块专项测试。

## 相关资源

- **RISC-V Boom**：[https://github.com/riscv-boom/riscv-boom](https://github.com/riscv-boom/riscv-boom)
- **Chipyard 框架**：[https://github.com/ucb-bar/chipyard](https://github.com/ucb-bar/chipyard)
- **Verilator**：[https://www.veripool.org/verilator/](https://www.veripool.org/verilator/)
- **Spectre 代表性文献**：
  - Kocher et al., "Spectre Attacks: Exploiting Speculative Execution" (IEEE S&P 2019)
  - Canella et al., "A Systematic Evaluation of Transient Execution Attacks and Defenses" (USENIX Security 2019)
- **CPU Fuzz 测试相关**：
  - "Transynther: Automatic Discovery of Transient Execution Vulnerabilities" (ISCA 2021)
  - "SpecFuzz: A Framework for Coverage-Guided Fuzzing of Speculative Execution Vulnerabilities" (USENIX Security 2022)
- **RISC-V 安全扩展**：[RISC-V Security Standing Committee](https://lists.riscv.org/g/security)
