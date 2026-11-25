Svacoder: Training Specialized LLMs for Hardware Assertion Generation via RTL-Grounded Bidirectional Data Synthesis
Authors：
[Yutong Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=09922789709518223611)，[Chenrui Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=14039596334962990911)，[Pengwei Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=58003768219925222871)，[Di Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=93145196318987296561)，[Rui Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6161280692627664157)，[Xishan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3691707932442798094)，[Zidong Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=85723840822451748731)，[Qi Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=616343)，[Xing Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=544143)

## 中文标题

SVACoder：通过以 RTL 为锚的双向数据合成训练面向硬件断言生成的专用 LLM

## 英文摘要

SystemVerilog Assertions (SVAs) are crucial for hardware verification. Recent studies leverage general-purpose LLMs to translate natural language properties to SVAs (NL2SVA), but they perform poorly due to limited data. We propose a data synthesis framework to tackle two challenges: the scarcity of high-quality real-world SVA corpora and the lack of reliable methods to determine NL-SVA semantic equivalence. For the former, large-scale open-source RTLs are used to guide LLMs to generate real-world SVAs; for the latter, bidirectional translation serves as a data selection method. With the synthesized data, we train SVACoder, a series of SVA generation models. Notably, SVACoder-14B achieves 75.8% on NL2SVA-Human and 84.0% on NL2SVA-Machine in Func.@1, matching or exceeding advanced LLMs like GPT-5 and DeepSeek-R1.

## 中文摘要

SystemVerilog 断言（SVA）对硬件验证至关重要。近期研究利用通用 LLM 将自然语言性质转换为 SVA（NL2SVA），但因数据有限而表现不佳。我们提出一个数据合成框架以应对两项挑战：高质量真实世界 SVA 语料的稀缺，以及判定 NL-SVA 语义等价性缺乏可靠方法。针对前者，利用大规模开源 RTL 引导 LLM 生成真实世界 SVA；针对后者，以双向翻译作为数据筛选方法。借助合成数据，我们训练了 SVACoder 系列 SVA 生成模型。值得注意的是，SVACoder-14B 在 NL2SVA-Human 上取得 75.8%、在 NL2SVA-Machine 上取得 84.0% 的 Func.@1，与 GPT-5、DeepSeek-R1 等先进 LLM 持平或更优。
