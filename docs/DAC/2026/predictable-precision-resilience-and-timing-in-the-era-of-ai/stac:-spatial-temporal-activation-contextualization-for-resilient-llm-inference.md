STAC: Spatial-Temporal Activation Contextualization for Resilient LLM Inference
Authors：
[Rengang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=16383868793392611511)，[Leyan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=73967472539745366021)，[Zizhen Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2120435217578556355)，[Bin Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=62143079060338402021)，[Naixing Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1859008848176783391)，[Cheng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3927152179176732101)，[Jing Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=516343)，[Huawei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=535143)

## 中文标题

STAC：面向韧性 LLM 推理的时空激活上下文化

## 英文摘要

Large Language Models (LLMs) are increasingly deployed in safety-critical settings, making reliable inference under soft errors a key systems challenge. We find that existing low-cost defenses fail because LLM activations are not statistically stable: Prefill produces large structured outliers essential for semantics, while Decode activations drift over time in the autoregressive process. This Outlier Dichotomy renders static thresholds harmful to fault-free accuracy and ineffective for fault resilience. We propose STAC, a lightweight spatial–temporal activation contextualization mechanism that adapts its protective bounds to the intrinsic activation regularities of LLMs, accurately tracking structured spatial outliers in Prefill and the drift-prone temporal dynamics of Decode. By preserving legitimate activations and sup-pressing fault-induced outliers, STAC delivers robust protection with minimal overhead. Across diverse models and workloads, STAC consistently outperforms prior low-cost defenses: it preserves fault-free accuracy and raises the maximum tolerable fault rate to 10−6, achieving a 10× improvement over the state of the art with 3.85% average latency.

## 中文摘要

大语言模型（LLM）越来越多地部署于安全关键场景，使软错误下的可靠推理成为关键的系统挑战。我们发现，现有低成本防护之所以失效，是因为 LLM 的激活值在统计上并不稳定：Prefill 阶段会产生对语义至关重要的大幅结构化离群值，而 Decode 阶段的激活值则在自回归过程中随时间漂移。这种“离群值二分性”使静态阈值既损害无故障精度，又无法有效保障故障韧性。我们提出 STAC，一种轻量级的时空激活上下文化机制，使其保护边界自适应于 LLM 固有的激活规律，在 Prefill 阶段准确跟踪结构化空间离群值，在 Decode 阶段准确跟踪易漂移的时间动态。通过保留合法激活并抑制故障诱导的离群值，STAC 以极小开销提供稳健保护。在多种模型与工作负载上，STAC 一致优于先前的低成本防护：它保持无故障精度，并将最大可容忍故障率提升至 10^-6，相较最先进工作实现 10× 提升，平均延迟开销仅为 3.85%。

## 英文关键词

LLM Inference, Fault Tolerance

## 中文关键词

LLM 推理、容错
