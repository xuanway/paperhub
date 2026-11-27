LLM4SDC: Leveraging Multi-Agent System for Automated SDC Generation and Benchmarking
Authors：
[Peiyi Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=3140913406375347738)，[Yuntao Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3670065592072189317)，[Haiyang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=31508100863972503931)，[Fangzhou Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=70986091953490229061)，[Xufeng Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=30331677937965060601)，[Yuyang Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=8432721704885972621)

## 中文标题

LLM4SDC：利用多智能体系统实现 SDC 自动生成与基准评测

## 英文摘要

Logic synthesis quality depends critically on accurate Synopsys design constraints (SDCs), yet manual generation is labor-intensive and error-prone. We construct SDCBench, the first SDC generation benchmark with aligned specification-design-testbench triples, and LLM4SDC, the first end-to-end automated framework for SDC generation. LLM4SDC hierarchically decomposes the task into specialized agents to extract timing-relevant information, conduct domain-specific retrieval-augmented generation, and synthesize static constraints from expert-curated templates, as well as discover dynamic timing exceptions by verification-guided pipelines. Evaluated on SDCBench, LLM4SDC achieves near-perfect syntax correctness, superior semantic fidelity, and high false path accuracy, significantly outperforming state-of-the-art baselines while improving physical design metrics.

## 中文摘要

逻辑综合质量严重依赖于准确的 Synopsys 设计约束（SDC），而人工生成既费力又易错。我们构建了 SDCBench，这是首个具有对齐的规范—设计—测试平台三元组的 SDC 生成基准，同时也构建了 LLM4SDC，这是首个端到端的 SDC 自动生成框架。LLM4SDC 将任务层次化地分解给各个专门智能体，以提取时序相关信息、执行领域专用的检索增强生成、从专家整理的模板中综合静态约束，并通过验证引导的流水线发掘动态时序例外。在 SDCBench 上评估，LLM4SDC 达到近乎完美的语法正确性、优异的语义保真度和较高的伪路径准确率，显著优于现有最优基线，同时改善了物理设计指标。
