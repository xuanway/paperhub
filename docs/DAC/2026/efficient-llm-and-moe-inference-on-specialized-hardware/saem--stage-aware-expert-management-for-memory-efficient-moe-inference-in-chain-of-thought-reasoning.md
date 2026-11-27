SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning
Authors：
[Yujie Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=70226537940019910531)，[Bin Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=40138255384532296961)，[Tulika Mitra](https://63dac.conference-program.com/?post_type=page&p=15&uid=187343)

## 中文标题

SAEM：面向思维链推理中内存高效 MoE 推理的阶段感知专家管理

## 英文摘要

Chain-of-thought (CoT) prompting improves LLM reasoning by decomposing complex problems into intermediate steps, but its sequential nature increases decoding latency and memory usage. Mixture-of-Experts (MoE) models scale capacity through sparse expert activation, yet their full expert weights often exceed GPU memory and require costly GPU–CPU transfers. Existing runtimes treat all tokens uniformly, overlooking a key structural property of CoT traces: consecutive reasoning stages exhibit coherent and predictable expert activation patterns. Ignoring this stage-level regularity leads to inefficient caching and unnecessary data movement. We propose SAEM, a stage-aware MoE inference runtime that detects reasoning stage boundaries and exploits stage-level activation coherence to guide expert placement. SAEM combines stage-aware caching, expert-aligned token repacking, and in-situ CPU execution to reduce data transfer and kernel fragmentation. On mathematical reasoning workloads, SAEM achieves an average 1.54× throughput improvement over state-of-the-art caching and offloading baselines under constrained GPU memory, demonstrating the effectiveness of stage-aware, locality-driven MoE inference for CoT reasoning.

## 中文摘要

思维链（CoT）提示通过将复杂问题分解为中间步骤来提升 LLM 的推理能力，但其串行特性会增加解码延迟与内存占用。混合专家（MoE）模型通过稀疏的专家激活来扩展模型容量，然而其完整的专家权重往往超出 GPU 内存容量，需要付出高昂的 GPU–CPU 传输代价。现有运行时对所有 token 一视同仁，忽略了 CoT 轨迹的一个关键结构特性：相邻的推理阶段呈现出连贯且可预测的专家激活模式。忽视这种阶段级规律会导致缓存效率低下与不必要的数据搬运。我们提出 SAEM，一种阶段感知的 MoE 推理运行时，它能够检测推理阶段的边界，并利用阶段级激活连贯性来指导专家放置。SAEM 结合了阶段感知缓存、专家对齐的 token 重打包以及原位 CPU 执行，以减少数据传输与内核碎片化。在数学推理负载上，SAEM 在受限的 GPU 内存条件下相比最先进的缓存与卸载基线平均取得 1.54 倍的吞吐提升，证明了阶段感知、局部性驱动的 MoE 推理对 CoT 推理的有效性。
