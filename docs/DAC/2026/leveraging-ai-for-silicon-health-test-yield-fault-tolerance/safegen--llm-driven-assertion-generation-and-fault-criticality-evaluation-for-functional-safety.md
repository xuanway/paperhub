Safegen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety
Authors：
[Xuanyi Tan](https://63dac.conference-program.com/?post_type=page&p=15&uid=76494182170114721261)，[Arjun Chaudhuri](https://63dac.conference-program.com/?post_type=page&p=15&uid=40588752157476891841)，[Rubin Parekhji](https://63dac.conference-program.com/?post_type=page&p=15&uid=48174017809229541771)，[Krishnendu Chakrabarty](https://63dac.conference-program.com/?post_type=page&p=15&uid=614843)

## 中文标题

SafeGen：面向功能安全的 LLM 驱动断言生成与故障关键性评估

## 英文摘要

With advances in autonomous driving and electric vehicle technologies, functional safety has become a key requirement in automotive chip design. Traditional simulation-based fault analysis tends to be overly conservative at the module level and fails to reflect true fault criticality. This paper presents SafeGen, an LLM-driven, formal-verification-assisted framework for functional-safety-oriented fault criticality assessment. SafeGen employs large language models (LLMs) with a document-level Hyper Knowledge Graph (HyperKG) that incorporates Failure Modes, Effects, and Diagnostic Analysis (FMEDA) guidelines to extract verifiable specifications from design and safety documents and to evaluate their importance for overall system safety. The HyperKG is then extended with register-transfer level (RTL) information to guide the generation of Functional Safety Assertions (FSAs) that are semantically grounded and design-aware, each linked to its corresponding specifications for traceable reasoning. A gate-to-RTL fault-mapping mechanism supporting both stuck-at and bridging faults, combined with formal property verification (FPV), enables semantic-level fault criticality grading based on specification-linked assertion violations. A digital–physical co-simulation platform for a field-oriented control (FOC) system validates SafeGen, demonstrating superior assertion quality compared to other LLM-based assertion generation frameworks. It further provides semantic interpretability in fault criticality assessment when compared to traditional simulation-based approaches.

## 中文摘要

随着自动驾驶与电动汽车技术的发展，功能安全已成为汽车芯片设计的一项关键要求。传统的基于仿真的故障分析在模块级往往过于保守，无法反映真实的故障关键性。本文提出 SafeGen，一个 LLM 驱动、形式验证辅助的、面向功能安全的故障关键性评估框架。SafeGen 采用大语言模型（LLM）并结合文档级超知识图谱（HyperKG），该图谱融入失效模式、影响与诊断分析（FMEDA）指南，用于从设计与安全文档中提取可验证规范，并评估其对整体系统安全的重要性。随后，HyperKG 被扩展以引入寄存器传输级（RTL）信息，指导生成语义有据、设计感知的功能安全断言（FSA），每条断言均链接到相应规范以支持可追溯推理。一种同时支持固定故障与桥接故障的门级到 RTL 故障映射机制，结合形式属性验证（FPV），可基于与规范关联的断言违例实现语义级故障关键性分级。针对磁场定向控制（FOC）系统的数字–物理协同仿真平台对 SafeGen 进行了验证，结果表明其断言质量优于其他基于 LLM 的断言生成框架；与传统基于仿真的方法相比，它还在故障关键性评估中提供了语义可解释性。
