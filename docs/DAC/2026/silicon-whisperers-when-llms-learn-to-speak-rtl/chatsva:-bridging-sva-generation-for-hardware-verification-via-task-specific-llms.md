ChatSVA: Bridging SVA Generation for Hardware Verification via Task-Specific LLMs
Authors：
[Lik Tung Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1657146794061621684)，[Jie Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=38479733992353397501)，[shaokai ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=2369779353241294141)，[mengli zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=28463306731419860571)，[Jia Xiong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1380754946707582248)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)，[Hugo Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6667584974133539683)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)，[Jun Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=52664182327005683081)

## 中文标题

ChatSVA：借助任务专用 LLM 打通硬件验证中的 SVA 生成

## 英文摘要

Functional verification consumes over 50% of the IC development lifecycle, where SystemVerilog Assertions (SVAs) are indispensable for formal property verification and enhanced simulation-based debugging. However, manual SVA authoring is labor-intensive and error-prone. While Large Language Models (LLMs) show promise, their direct deployment is hindered by low functional accuracy and a severe scarcity of domain-specific data. To address these challenges, we introduce ChatSVA, an end-to-end SVA generation system built upon a multi-agent framework. At its core, the AgentBridge platform enables this multi-agent approach by systematically generating high-purity datasets, overcoming the data scarcity inherent to few-shot scenarios. Evaluated on 24 RTL designs, ChatSVA achieves 98.66% syntax and 96.12% functional pass rates, generating 139.5 SVAs per design with 82.50% function coverage. This represents a 33.3 percentage point improvement in functional correctness and an over 11× enhancement in function coverage compared to the previous state-of-the-art (SOTA). ChatSVA not only sets a new SOTA in automated SVA generation but also establishes a robust framework for solving long-chain reasoning problems in few-shot, domain-specific scenarios. A publicly accessible ChatSVA web service is available at https://www.nctieda.com/CHATDV.html.

## 中文摘要

功能验证占据 IC 开发周期 50% 以上的时间，其中 SystemVerilog 断言（SVA）对形式性质验证和增强的仿真调试不可或缺。然而，人工编写 SVA 既耗费人力又容易出错。尽管大语言模型（LLM）展现出潜力，但其直接部署受限于功能正确率低以及领域专用数据的严重匮乏。为应对这些挑战，我们提出 ChatSVA，一个构建于多智能体框架之上的端到端 SVA 生成系统。其核心 AgentBridge 平台通过系统化地生成高纯度数据集来支撑这种多智能体方法，克服了少样本场景固有的数据稀缺问题。在 24 个 RTL 设计上评估，ChatSVA 达到 98.66% 的语法通过率和 96.12% 的功能通过率，每个设计生成 139.5 条 SVA，功能覆盖率达到 82.50%。相较于此前的最先进水平（SOTA），其功能正确性提升 33.3 个百分点，功能覆盖提升超过 11×。ChatSVA 不仅在自动化 SVA 生成上刷新了 SOTA，还为解决少样本、领域专用场景中的长链推理问题建立了稳健框架。ChatSVA 的公开 Web 服务地址为 https://www.nctieda.com/CHATDV.html。

## 英文关键词

SVA, LLM, LLM-aided Design, Formal Verification

## 中文关键词

SVA、LLM、LLM 辅助设计、形式验证
