---
title: "FastPath: A Hybrid Approach for Efficient Hardware Security Verification"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "hardware-verification"
  - "information-leakage"
  - "formal-verification"
  - "microarchitecture"
  - "risc-v"
---

# FastPath: A Hybrid Approach for Efficient Hardware Security Verification

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://kastner.ucsd.edu/wp-content/uploads/2025/06/admin/dac25-fastpath.pdf">https://kastner.ucsd.edu/wp-content/uploads/2025/06/admin/dac25-fastpath.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 硬件安全，信息流跟踪，仿真，形式化验证，数据不感知计算 </p>
</div>


---

## 研究概要
本文提出FastPath混合硬件安全验证框架，融合超流图静态分析、信息流仿真IFT、UPEC完备形式化验证三模块，自动化验证硬件数据无泄漏特性。以仿真结果划分证明空间，大幅减少人工迭代开销。在AES、RISC-V cv32e40s、BOOM等设计测试，人工工作量降低36%~100%，并发现cv32e40s未公开操作数侧信道漏洞。

## 背景和动机
1. 时序、推测类微架构侧信道攻击频发，恒定时间编程假设常被处理器硬件优化打破，仅软件防护不可靠，需硬件层完备验证。
2. 现有纯形式化UPEC验证虽具备完备安全证明能力，但迭代过程需人工排查海量信号反例，大型CPU验证人力成本极高。
3. 纯仿真IFT验证执行高效，但测试激励覆盖有限，易遗漏角落泄露路径，无法给出安全完备性保证。
4. 缺少三者协同自动化流程，静态分析、仿真、形式化工具割裂，无法自动传递中间结果优化证明流程。
5. 主流RISC安全处理器仍存在未被挖掘的硬件操作数泄露缺陷，缺乏高效验证手段提前定位漏洞。

## 相关工作
1. 纯形式化UPEC-DIT：通过双实例2安全模型验证数据无关时序，完备可靠，但需人工逐次过滤泄露信号，大型核工作量巨大。
2. 硬件信息流仿真IFT：快速标记信号污点，快速定位明显泄露，但依赖测试用例，角落场景易漏报，无完备安全结论。
3. HyperFlow图静态分析：RTL静态抽取信息流路径，无测试开销，但存在大量假阳性，无法判定路径是否可达。
4. Clepsydra等单工具验证方案：仅独立使用仿真或形式化，未构建三者自动化联动流水线。
5. 专用硬件侧信道检测工具：仅针对单一模块，不支持全处理器流水线端到端无泄漏证明。

## 本文解决方案
### 1 三段式自动化验证流水线
流程分为HFG静态分析、IFT污点仿真、UPEC形式化校验，模块间自动传递中间数据，无需人工导出导入结果。
### 2 HyperFlow图前置快速筛除
从RTL构建信息流超流图，查询敏感输入到控制输出路径，无通路直接终止验证，密码加速器可100%省去仿真与形式步骤。
### 3 IFT仿真提取未污染状态集
对设计插污点逻辑仿真，记录全程未被机密数据污染的寄存器集合Z'，作为形式化的语义划分依据，过滤大量无关信号。
### 4 基于Z'优化UPEC归纳证明
将仿真得到的干净状态作为形式化假设条件，直接跳至归纳固定点校验，省去人工逐条排查传播信号，大幅减少反例处理量。
### 5 反例分层处理机制
区分真实硬件漏洞、软件约束可规避场景、虚假不可达路径，分别执行RTL修复、新增软件限制、添加不变量细化证明。

## 实验分析
1. 测试对象：SHA512/AES密码核、除法单元、cv32e40s、BOOM乱序RISC-V处理器，采用Radix仿真+OneSpin形式工具。
2. 人力开销：相较纯UPEC，各设计人工检查量下降36%~100%；SHA/AES无需人工干预，BOOM大型核减少87%人工工作量。
3. 漏洞挖掘：在cv32e40s处理器ID-EX流水线发现全新内部操作数泄露漏洞，并提供修复方案。
4. 执行效率：IFT仿真仅1~2分钟，形式单轮校验10秒内，综合验证耗时极低。
5. 判定结果：密码加速器天然满足数据无泄露；除法、通用CPU仅在特定软件约束下安全，ZipCPU除法完全不满足无泄漏。

## 研究启发
1. 静态分析、仿真、形式化三者具备强互补性，串联自动化流水线可兼顾效率与完备安全证明。
2. IFT仿真的污点状态可作为形式化证明先验知识，从根源减少人工迭代，解决纯形式化人力瓶颈。
3. 即使标称安全的RISC处理器，流水线缓存、未屏蔽数据接口仍存在隐蔽操作数侧信道，必须全流水线验证。
4. 硬件安全验证不能只输出有无漏洞，还应输出配套软件约束，软硬件协同才能实现数据无泄漏运行。
5. 小型密码核可通过静态分析直接完成证明，复杂乱序CPU必须结合仿真+形式化才能覆盖全部角落泄露路径。
