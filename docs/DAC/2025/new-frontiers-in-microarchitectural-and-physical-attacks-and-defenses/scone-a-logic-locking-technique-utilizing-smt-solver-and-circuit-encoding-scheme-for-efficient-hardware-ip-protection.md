---
title: "SCONE: A Logic Locking Technique Utilizing SMT Solver and Circuit Encoding Scheme for Efficient Hardware IP Protection"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "logic-locking"
  - "smt-solver"
  - "hardware-ip-protection"
---

# SCONE: A Logic Locking Technique Utilizing SMT Solver and Circuit Encoding Scheme

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132623">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132623</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 逻辑锁定，编码方案，SMT求解器 </p>
</div>

---

## 研究概要
本文提出SCONE逻辑锁定方案，基于SMT求解器与安全电路编码改进SFLL-D2PIP。SMT直接提取D2PIP规避PI表NP难转换，扩展异或编码增大密钥空间，分硬件编码/设计期编码两种实现。在IBEX等电路验证，处理速度提升350倍，可抵御SAT、SPS等五类输入/结构攻击，PPA开销可控。

## 背景和动机
1. 全球代工IC供应链存在IP盗版、逆向、木马威胁，逻辑锁定是主流硬件IP防护手段。
2. 现有SFLL-D2PIP需生成完整质蕴含PI表提取保护输入，属于NP难问题，大规模电路极易超时，可扩展性极差。
3. 原始方案D2PIP样本稀少、可选范围窄，密钥长度短，易遭受暴力破解，灵活性与安全性不足。
4. SFLL-HD、SFLL-flex等传统锁定方案无法抵御SPI等结构攻击，仅D2PIP具备综合防御能力，但落地困难。
5. 缺少兼顾可扩展、高灵活、抗多类攻击一体化SFLL优化方案。

## 相关工作
1. 基础SFLL系列（SFLL-HD、SFLL-flex）：依靠固定PIP混淆，易被SPI结构攻击攻破，无D2距离约束。
2. SFLL-D2PIP：基于PI表筛选距离≥2的PIP，可抵御5类攻击，但PI提取指数级耗时，D2样本稀缺。
3. 硬件编码STATION：仅面向有限状态机，依赖状态转换表，通用性差，无法适配通用组合电路。
4. 各类逻辑攻击：SAT输入攻击、ATR/SPS/FALL/SPI四类结构攻击，可破解多数简易锁定电路。
5. 机器学习类锁定攻击（SAIL、OMLA）：针对密钥门插入型锁定，对SFLL类剥离架构无有效破解能力。

## 本文解决方案
### 1 SMT快速D2PIP提取模块
绕过PI表生成，通过Z3 SMT求解器布尔约束直接筛选最小项D2PIP；限定目标最小项所有汉明距离1邻域输出恒0，迭代遍历全输入空间，100%提取成功率。
### 2 多层异或安全编码机制
原始n位输入新增m位扩展输入，新增位由原始多输入异或生成；原始D2PIP映射为更长编码后PIP，指数扩大密钥空间，保持Dist2安全特性。
### 3 两种SCONE硬件实现
①硬件编码ES：设计阶段不改动原电路，集成可配置编码模块，原始输入空间不变，SAT抗性有限；②设计期编码：原生扩展输入位，密钥长度大幅提升，SAT迭代呈指数增长，安全性更强。
### 4 三层防护电路架构
由编码单元ES、剥离功能电路FSC、恢复单元组成；仅输入合法长密钥时输出原始功能，非法密钥输出随机错误值。
### 5 标准化保护流程
先SMT提取D2PIP，无充足样本则启用编码扩展；生成编码电路后与SFLL单元综合，输出锁定门级网表，兼容主流综合工具。

## 实验分析
1. 测试基准：ISCAS85、ITC99、MIPS、IBEX、GPS等多规模电路，对比原生D2PIP方案。
2. 可扩展性：原生方案多数电路72小时超时，SCONE处理IBEX仅748秒，速度提升350倍，提取成功率100%。
3. 安全性能：两种实现均抵御SAT、SPS、ATR、FALL、SPI五类攻击；设计期编码SAT迭代指数上涨，PIP≥17位攻击72小时超时。
4. PPA开销：无硬件编码实现面积/功耗开销低于10%，部分电路时序小幅提升；带ES实现开销更高但仍可控。
5. 灵活性：编码可自定义扩展位数，D2PIP可选数量、最大密钥长度远高于原有方案，暴力破解难度大幅上升。

## 研究启发
1. PI表遍历式D2PIP提取存在本质性能瓶颈，SMT布尔约束是大规模电路可扩展替代方案。
2. 输入层轻量异或编码无需修改核心逻辑，低成本提升密钥长度与暴力攻击抗性，不破坏Dist2安全约束。
3. 逻辑锁定需分设计流程提供两种实现路径，设计期原生编码安全上限更高，后加编码适配存量IP保护。
4. 评估硬件锁安全必须同时覆盖输入SAT与多类结构攻击，单一防御手段存在漏洞。
5. 硬件安全EDA流程中，SMT工具可大量替代NP难网表变换操作，兼顾效率与防护强度。