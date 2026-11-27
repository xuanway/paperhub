Breaking the Tuning Barrier: Zero-Hyperparameters Yield Multi-Corner Analysis Via Learned Priors
Authors：
[Wei Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=693843)，[Kaiqi Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2624973852976826836)，[Jiazhan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9202354047119215982)，[Hong Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1155970488846194195)，[Shan Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=0559831925586243736)

## 中文标题

突破调参壁垒：借助学习先验实现零超参数多工艺角分析

## 英文摘要

Yield Multi-Corner Analysis validates circuits across 25+ Process-Voltage-Temperature corners, resulting in a combinatorial simulation cost of 𝑂(𝐾×𝑁) where 𝐾denotes corners and 𝑁exceeds 104 samples per corner. Existing methods face a fundamental trade-off: simple models achieve automation but fail on nonlinear circuits, while advanced AI models capture complex behaviors but require hours of hyperparameter tuning per design iteration, forming the Tuning Barrier. We break this barrier by replacing engineered priors (i.e., model specifications) with learned priors from a foundation model pre-trained on millions of regression tasks. This model performs in-context learning, instantly adapting to each circuit without tuning or retraining. Its attention mechanism automatically transfers knowledge across corners by identifying shared circuit physics between operating conditions. Combined with an automated feature selector (1152D to 48D), our method matches state-of-the-art accuracy (mean MREs as low as 0.11%) with zero tuning, reducing total validation cost by over 10×.

## 中文摘要

良率多工艺角分析需在 25 个以上工艺-电压-温度（PVT）工艺角下验证电路，导致组合式的仿真开销为 𝑂(𝐾×𝑁)，其中 𝐾 表示工艺角数量，𝑁 为每个工艺角的样本数且超过 10⁴。现有方法面临根本性权衡：简单模型可实现自动化，但在非线性电路上失效；先进 AI 模型能捕捉复杂行为，但每次设计迭代都需要数小时的超参数调优，形成“调参壁垒”。我们通过用来自在数百万回归任务上预训练的基础模型的学习先验替代人工设计的先验（即模型规格），打破了这一壁垒。该模型执行上下文学习，无需调优或重训练即可即时适配每个电路。其注意力机制通过识别不同工作条件之间共享的电路物理特性，自动在工艺角之间迁移知识。结合自动特征选择器（从 1152 维降至 48 维），我们的方法在零调优下达到最先进精度（平均 MRE 低至 0.11%），并将总验证成本降低 10 倍以上。
