Think Before You Prune: Self-Reflective Structured Pruning for Reasoning Language Models
Authors：
[Ziyan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=75798595546175056731)，[Enmao Diao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0770981653736691933)，[Qi Le](https://63dac.conference-program.com/?post_type=page&p=15&uid=3400238107050680919)，[Pu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1167221529869113453)，[Guanchu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5040742883476248679)，[Minwoo Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=52949847378991434521)，[Shu-ping Yeh](https://63dac.conference-program.com/?post_type=page&p=15&uid=2801840864582908087)，[Li Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=826843)

## 中文标题

先思考后剪枝：面向推理语言模型的自反思结构化剪枝

## 英文摘要

Reasoning LLMs (RLMs) such as OpenAI o1, DeepSeek-R1, and Qwen3 deliver strong multi-step reasoning through chain-of-thought generation, but their large model sizes and lengthy decode-time outputs make them costly to deploy and unsuitable for resource-constrained settings. To reduce computing and memory cost, pruning offers a promising solution by removing unimportant parameters. However, despite their success on standard LLMs, existing pruning methods severely damage RLMs, as even moderate sparsity (e.g., 20%) can collapse accuracy and completely disrupt the model’s reasoning coherence. We begin by analyzing why existing pruning pipelines fail on reasoning LLMs and find that their brittleness largely stems from a mismatch between the calibration data, the pruning objective, and the model’s decode-time reasoning behavior. Our study further shows that the most reliable calibration signal comes not from human-written labels but from the model’s own self-generated reasoning traces, which more accurately reflect its inference distribution. Guided by these insights, we introduce RESP, a self-reflective structured pruning framework that aligns pruning decisions with the model’s reasoning dynamics through self-generated calibration, decode-only gradient-based importance estimation, and progressive regeneration that maintains calibration fidelity as sparsity increases. Experiments on Qwen3-8B demonstrate that RESP markedly outperforms existing structured pruning methods on both GSM8K and MathQA, preserving near-dense accuracy at 20–30% sparsity and substantially mitigating performance collapse at higher sparsity levels. At 40% sparsity, RESP attains 81.3% accuracy on GSM8K and 59.6% on MathQA, surpassing the strongest baselines by 66.87% and 47%, respectively.

## 中文摘要

诸如 OpenAI o1、DeepSeek-R1 和 Qwen3 等推理 LLM（RLM），通过思维链生成实现强大的多步推理，但其庞大的模型规模和冗长的解码输出使其部署成本高昂，不适合资源受限环境。为降低计算与内存开销，剪枝通过移除不重要参数提供了有前景的解决方案。然而，尽管这些方法在标准 LLM 上取得成功，现有剪枝方法却严重损害 RLM，甚至中等稀疏度（例如 20%）就会使精度崩溃并完全破坏模型的推理连贯性。我们首先分析现有剪枝流程为何在推理 LLM 上失败，发现其脆弱性主要源于校准数据、剪枝目标与模型解码时推理行为之间的不匹配。我们的研究进一步表明，最可靠的校准信号并非来自人工编写的标签，而是来自模型自身生成的推理轨迹，后者更准确地反映了其推理分布。在这些洞见指导下，我们提出 RESP，一个自反思结构化剪枝框架，通过自生成校准、仅解码期基于梯度的重要性估计，以及随稀疏度提高而保持校准保真度的渐进式再生成，使剪枝决策与模型的推理动态对齐。在 Qwen3-8B 上的实验表明，RESP 在 GSM8K 和 MathQA 上均显著优于现有结构化剪枝方法，在 20–30% 稀疏度下保持接近稠密模型的精度，并在更高稀疏度下大幅缓解性能崩溃。在 40% 稀疏度下，RESP 在 GSM8K 上达到 81.3% 精度，在 MathQA 上达到 59.6%，分别超越最强基线 66.87% 和 47%。

## 英文关键词

Pruning, Large language Models, Reasoning LLMs

## 中文关键词

剪枝、大语言模型、推理 LLM
