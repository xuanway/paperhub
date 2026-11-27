DRCGen: A Controllable DRC Violation Case Generator with Cross-PDK Transferability for Rule-Deck and Tool Validation
Authors：
[Shunjie Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1492130949708013826)，[Yuxuan Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1628004437784333017)，[Haodong Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67762242078220399721)，[Youran Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9622103312490018689)，[Jianli Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=539243)，[Jun Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=639243)，[Kun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=565843)

## 中文标题

DRCGen：面向规则套件与工具验证的、具备跨 PDK 可迁移性的可控 DRC 违例样本生成器

## 英文摘要

VLSI layout pattern generation plays a crucial role in design for manufacturability (DFM). Patterns that incorporate specific design rule checking (DRC) violations are valuable for applications such as foundry design-rule deck development, EDA tool validation, and generating training data for AI-based DRC research. However, existing research primarily focuses on producing DRC-clean layouts by enforcing rule compliance through constraints or filtering, while ignoring the generation of controllable violations. To address this gap, we propose DRCGen, a controllable framework for generating DRC violation patterns with transferability across different process design kits (PDKs). DRCGen is based on a diffusion model with conditional control, generating structured control hints to encode spatial and semantic violation information for fine-tuning the model. The model can generate violation patterns of user-specified types within a target region based on a natural-language prompt, while maintaining DRC-compliance outside the region. Additionally, we incorporate few-shot learning to facilitate rapid transfer across different PDKs. Experimental results show that, compared to state-of-the-art methods, our approach achieves a 2.27× increase in topological diversity and a 1.02× increase in geometric diversity. Compared to Calibre LSG, we achieve 3.31× and 1.15× improvements in topological and geometric diversity, respectively.

## 中文摘要

VLSI 版图图案生成在设计可制造性（DFM）中起着至关重要的作用。包含特定设计规则检查（DRC）违例的图案，对于代工厂设计规则套件开发、EDA 工具验证以及为基于 AI 的 DRC 研究生成训练数据等应用具有重要价值。然而，现有研究主要通过约束或过滤强制符合规则，从而生成 DRC 洁净的版图，而忽略了可控违例的生成。为填补这一空白，我们提出 DRCGen，一个可跨不同工艺设计套件（PDK）迁移的可控 DRC 违例图案生成框架。DRCGen 基于具有条件控制的扩散模型，生成结构化的控制提示以编码空间与语义违例信息，用于微调模型。该模型能够依据自然语言提示在目标区域内生成用户指定类型的违例图案，同时保持区域之外的 DRC 合规性。此外，我们引入少样本学习以促进跨不同 PDK 的快速迁移。实验结果表明，与最先进方法相比，我们的方法在拓扑多样性上提升 2.27 倍、在几何多样性上提升 1.02 倍。与 Calibre LSG 相比，我们在拓扑多样性和几何多样性上分别提升 3.31 倍和 1.15 倍。
