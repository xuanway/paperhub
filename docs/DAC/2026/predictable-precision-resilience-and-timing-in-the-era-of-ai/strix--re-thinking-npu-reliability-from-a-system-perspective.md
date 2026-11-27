Strix: Re-Thinking NPU Reliability from a System Perspective
Authors：
[Jiapeng Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=30384709835922261001)，[Jie Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=71305096419031320321)，[Hao Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=6994959995200007163)，[Ran Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=7384841273738841016)，[Dean You](https://63dac.conference-program.com/?post_type=page&p=15&uid=2160294947484353928)，[Hui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0793243510929650245)，[Yingquan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1649820901453085703)，[Tinglue Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0310428917140105595)，[Xudong Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=41132883761843351721)，[Jing Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=756143)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)

## 中文标题

Strix：从系统视角重新审视 NPU 可靠性

## 英文摘要

DNNs and LLMs increasingly rely on hardware accelerators, including in safety-critical domains, while technology scaling and growing model complexity make hardware faults more frequent. Existing system-level mechanisms typically treat the NPU as a monolithic unit, using coarse-grained replication that incurs prohibitive performance and hardware overheads, leaving a gap between reliability requirements and deployable solutions. To bridge this gap, we present Strix, a full-stack NPU reliability framework on an open-source SoC, spanning micro-architecture, ISA, and programming methods. Strix re-partitions the NPU along the system inference pipeline, identifies dominant failure modes, and attaches targeted safeguards, achieving sub-micro-second fault localisation, error detection, and correction with only 1.04× slowdown and minimal hardware overhead.

## 中文摘要

DNN 与 LLM 日益依赖硬件加速器，其中也包括安全关键领域；与此同时，工艺微缩与模型复杂度的增长使硬件故障更加频繁。现有的系统级机制通常将 NPU 视为单一整体，采用粗粒度复制，带来难以承受的性能与硬件开销，使可靠性需求与可部署方案之间出现鸿沟。为弥合这一鸿沟，我们提出 Strix——一个构建于开源 SoC 之上的全栈 NPU 可靠性框架，涵盖微架构、ISA 与编程方法。Strix 沿系统推理流水线对 NPU 进行重新划分，识别主导失效模式，并附加有针对性的防护措施，仅以 1.04× 的性能下降和极小的硬件开销，实现亚微秒级的故障定位、错误检测与纠正。
