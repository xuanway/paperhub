Debug Like a Human: Scaling LLM-Based Fault Localization to Processor Design via Block-Level Instruction-Oriented Slicing
Authors：
[Zizhen Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4530098830436978507)，[Xiaoguang Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=18374970855837132351)，[Deheng Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=79237435936129110281)，[Jiayu He](https://63dac.conference-program.com/?post_type=page&p=15&uid=22665827191751858831)，[Yihao Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=0810461669089994487)，[Guangda Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2077791635604255889)，[Yan Lei](https://63dac.conference-program.com/?post_type=page&p=15&uid=28310738578169441471)，[Jianjun Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=56270908089341287371)，[Jiang Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=59132999196972148771)

## 中文标题

像人类一样调试：通过块级指令导向切片将基于 LLM 的故障定位扩展至处理器设计

## 英文摘要

Fault localization in modern processor design code is a critical yet time-consuming step during processor verification. While recent advances in LLM-based techniques for module-level hardware design have shown promising results, automatically localizing bugs in large-scale, project-level processor designs remains challenging. In this paper, we present BluesFL, a novel block-level LLM-based fault localization framework for processor designs. Inspired by the way engineers debug processors, we first propose a dataflow-based code blockization approach to guide LLMs to focus on critical local code context. We further propose a Block-level Instruction-Oriented Slicing (Blues) algorithm that enables LLMs to mimic human reasoning by analyzing instruction execution paths and processor states. We evaluate BluesFL on a real-world RISC-V processor core comprising 19K lines of SystemVerilog code. Experimental results demonstrate that BluesFL correctly localizes 24 bugs at Top-1, achieving 242.9% improvement over the existing state-of-the-art (7 bugs). Cost analysis shows that BluesFL requires an average of only $0.257 to localize a single bug.

## 中文摘要

现代处理器设计代码中的故障定位是处理器验证过程中关键却耗时的环节。尽管近期基于 LLM 的模块级硬件设计技术已展现出良好前景，但在大规模、项目级处理器设计中自动定位缺陷仍充满挑战。本文提出 BluesFL，一个面向处理器设计的新型块级 LLM 故障定位框架。受工程师调试处理器方式的启发，我们首先提出基于数据流的代码分块方法，引导 LLM 关注关键的局部代码上下文。我们进一步提出块级指令导向切片（Blues）算法，使 LLM 能够通过分析指令执行路径和处理器状态来模拟人类的推理过程。我们在一个包含 1.9 万行 SystemVerilog 代码的真实 RISC-V 处理器核上评估 BluesFL。实验结果表明，BluesFL 在 Top-1 上正确本地化了 24 个缺陷，相较现有最优方法（7 个缺陷）提升 242.9%。成本分析显示，BluesFL 定位单个缺陷平均仅需 0.257 美元。

## 英文关键词

Fault Localization, Processor Verification, Large Language Model

## 中文关键词

故障定位、处理器验证、大语言模型
