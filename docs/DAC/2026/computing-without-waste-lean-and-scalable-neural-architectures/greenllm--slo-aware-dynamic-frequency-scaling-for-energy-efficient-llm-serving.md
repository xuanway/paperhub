Greenllm: SLO-Aware Dynamic Frequency Scaling for Energy-Efficient LLM Serving
Authors：
[Qunyou Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4269025682461797595)，[Darong Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3326390563316747454)，[Marina Zapater](https://63dac.conference-program.com/?post_type=page&p=15&uid=153143)，[David Atienza](https://63dac.conference-program.com/?post_type=page&p=15&uid=142143)

## 中文标题

GreenLLM：面向高能效 LLM 服务的 SLO 感知动态频率调节

## 英文摘要

Today’s Large Language Models (LLMs) inference costs are dominated by GPU energy consumption. LLM inference consists of two stages: prefill and decode, each exhibiting different characteristics. However, current GPU power governors disregard these differences and are not aware of runtime performance, leading to suboptimal DVFS configurations, head-of-line blocking, and excessive energy consumption. We introduce GreenLLM, a service-level objectives (SLO)- aware serving framework that minimizes GPU energy by explicitly separating prefill and decode control with a runtime optimization algorithm for end-to-end energy reduction without sacrificing performance. For prefill, GreenLLM solves a queueing-aware optimization to select the energy-minimal frequency for the target GPU. During decode, a dual-loop controller tracks throughput (tokens-per-second) and adjusts frequency with hysteresis during runtime, using fine grained steps to maintain tail TBT within target bounds. Across Alibaba and Azure trace replays, GreenLLM achieves up to 34% reduction in total energy consumption compared to the default DVFS baseline, with no loss of throughput and only less than 3.5% increase in SLO violations.

## 中文摘要

如今，大语言模型（LLM）的推理成本主要由 GPU 能耗主导。LLM 推理包含预填充（prefill）与解码（decode）两个阶段，二者特性各不相同。然而，当前的 GPU 功耗管理策略忽视了这些差异，也未感知运行时性能，导致 DVFS 配置次优、队头阻塞以及过高的能耗。我们提出 GreenLLM，一个服务等级目标（SLO）感知的服务框架，通过显式分离预填充与解码的控制，并配合运行时优化算法，在不牺牲性能的前提下最小化 GPU 能耗，实现端到端能耗降低。对于预填充阶段，GreenLLM 求解一个队列感知的优化问题，为目标 GPU 选择能耗最低的频率。在解码阶段，双环控制器跟踪吞吐量（每秒 token 数），并在运行时以滞后方式调节频率，采用细粒度步长使尾部 TBT 保持在目标范围内。在 Alibaba 与 Azure 的 trace 回放中，GreenLLM 相较默认 DVFS 基线最高降低 34% 的总能耗，吞吐量无损，SLO 违例仅增加不到 3.5%。
