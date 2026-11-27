Uvmarvel: an Automated LLM-Aided UVM Machine for Subsystem-Level RTL Verification
Authors：
[Junhao Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=6651823161996680511)，[Dingrong Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=4674631740535475858)，[Hanyuan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1422117424124782762)，[Yuchen Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4116076772303443402)，[Jie Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=38479733992353397501)，[Ke Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=42205136991210329061)，[Xinwei Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7117674552267504328)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)

## 中文标题

UVMarvel：面向子系统级 RTL 验证的自动化 LLM 辅助 UVM 机器

## 英文摘要

Verification presents a major bottleneck in Integrated Circuit (IC) development, consuming nearly 70% of total effort. While the Universal Verification Methodology (UVM) improves reuse through structured verification environments, constructing subsystem-level UVM testbenches and generating high-quality stimuli still require extensive manual coding, repeated EDA tool runs, and deep protocol and micro-architectural expertise. We present UVMarvel, an automated verification framework that leverages Large Language Models (LLMs) to build UVM testbenches for subsystem-level RTL. UVMarvel introduces an Intermediate Representation (IR) and a Bus Protocol Library to translate heterogeneous specifications into protocol-correct subsystem-level UVM testbenches, and employs a Signal Tracker and a Verilog Patching Library to guide LLM-based stimuli refinement. UVMarvel is the first framework capable of automatically constructing subsystem-level UVM testbenches across mainstream bus protocols, and it achieves an average code coverage of 95.65%, while reducing verification time from several human working days to a 4.5-hour automated execution.

## 中文摘要

验证是集成电路（IC）开发中的主要瓶颈，消耗了近 70%的总工作量。通用验证方法学（UVM）虽通过结构化的验证环境提升了复用性，但构建子系统级 UVM 测试平台并生成高质量激励仍需大量人工编码、反复运行 EDA 工具，以及深入的协议与微架构专业知识。我们提出 UVMarvel，一种利用大语言模型（LLM）为子系统级 RTL 构建 UVM 测试平台的自动化验证框架。UVMarvel 引入中间表示（IR）与总线协议库，将异构规格转换为协议正确的子系统级 UVM 测试平台，并采用信号追踪器（Signal Tracker）和 Verilog 补丁库来引导基于 LLM 的激励精化。UVMarvel 是首个能够跨主流总线协议自动构建子系统级 UVM 测试平台的框架，其平均代码覆盖率达到 95.65%，并将验证时间从数个人工工作日缩短为 4.5 小时的自动化执行。
