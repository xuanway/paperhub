Reflectbench: An Agentic Framework for Generating System-Level Design Testbench via Consensus and Reflection
Authors：
[Junzhe Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=55645023100429111311)，[Chao Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=04993692006417441231)，[Puyuan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=68265520275356888401)，[Jinheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=93980373795816939751)，[Xiaowei Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=36461621502894497151)，[Zhuorui Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=6507880996687476722)，[Zhaoyan Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=010443)，[Mengying Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=3675855616153509776)，[Zheyu Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=579504109826784041)，[Zhenge Jia](https://63dac.conference-program.com/?post_type=page&p=15&uid=73074348703888030031)

## 中文标题

ReflectBench：一种基于共识与反思的系统级设计测试平台生成智能体框架

## 英文摘要

Hardware design verification is essential for ensuring the functional correctness of electronic designs. Recent advances have explored using Large Language Models (LLMs) to automate hardware testbench synthesis. However, existing approaches primarily target single hardware modules and often fail to generalize to complex, system-level designs. As design complexity increases, both the LLM-generated testbench and the reference design are more likely to exhibit correlated or compensating errors, often producing false-positive outcomes that obscure true functional violations. To tackle these challenges, we propose ReflectBench, an agentic framework for automated system-level hardware design verification with logic analysis, consensus-based validation, feedback self-reflection, and testbench self-correction. To further minimize manual effort in preparing data, we devise Self-Reflective Domain Knowledge Mining, an automated approach for constructing an effective retrieval database aligned with hardware semantics. We also develop ReflectVDB, a benchmark consisting of 53 system-level hardware designs for evaluating LLM-based verification frameworks. Experimental results show that our approach outperforms SOTA framework ConfiBench on both ReflectVDB and AutoBench datasets, achieving 7.6% and 4.5% improvement in terms of testbench generation success rate, and 3.8% and 1.2% improvement in terms of coverage rate. The framework and ReflectVDB benchmark are open-sourced at https://gitee.com/sdu-aes-lab/reflectbench.

## 中文摘要

硬件设计验证对于确保电子设计的功能正确性至关重要。近期研究已探索利用大语言模型（LLM）自动化硬件测试平台（testbench）的合成。然而，现有方法主要针对单一硬件模块，往往难以泛化到复杂的系统级设计。随着设计复杂度提升，LLM 生成的测试平台与参考设计都更可能出现相关错误或相互补偿的错误，常常产生掩盖真实功能违规的假阳性结果。为应对这些挑战，我们提出 ReflectBench，这是一个面向系统级硬件设计自动化验证的智能体框架，具备逻辑分析、基于共识的验证、反馈自我反思以及测试平台自我修正能力。为进一步减少数据准备中的人工投入，我们设计了自反思领域知识挖掘方法，这是一种与硬件语义对齐、用于构建高效检索数据库的自动化途径。我们还开发了 ReflectVDB，这是一个包含 53 个系统级硬件设计、用于评估基于 LLM 的验证框架的基准。实验结果表明，我们的方法在 ReflectVDB 与 AutoBench 数据集上均优于 SOTA 框架 ConfiBench，在测试平台生成成功率上分别提升 7.6% 与 4.5%，在覆盖率上分别提升 3.8% 与 1.2%。该框架与 ReflectVDB 基准已开源于 https://gitee.com/sdu-aes-lab/reflectbench。

## 英文关键词

Verification, LLM, Reflection, TestBench, Hardware Design

## 中文关键词

验证、LLM、反思、测试平台、硬件设计
