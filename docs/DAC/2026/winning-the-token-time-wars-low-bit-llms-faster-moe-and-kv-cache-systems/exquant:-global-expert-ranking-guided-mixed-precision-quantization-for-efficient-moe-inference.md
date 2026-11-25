Exquant: Global Expert Ranking–guided Mixed-Precision Quantization for Efficient MoE Inference
Authors：
[Chenyang Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=55869298845145161621)，[Fangxin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=318143)，[Junjie Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=26092282016617962951)，[Ning Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=97857849623460577211)，[Haibing Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=828243)

## 中文标题

ExQuant：全局专家排序引导的混合精度量化用于高效 MoE 推理

## 英文摘要

Mixture-of-Experts (MoE) large language models (LLMs) leverage dynamic routing and sparse activation to improve efficiency and scalability, achieving high performance with reduced computational cost. However, their complex architecture and large memory footprint pose significant challenges for deployment, particularly on resource-constrained hardware. Post-training quantization (PTQ) is a widely used technique to reduce model size and memory usage. Existing PTQ approaches for MoE models are predominantly layer-wise and task-agnostic, optimizing reconstruction error independently within each layer. As a result, they ignore cross-layer differences in expert importance and fail to leverage task-specific signals, causing pivotal experts to be over-compressed, rarely activated experts to be over-provisioned, and overall accuracy to degrade. To overcome these limitations, we propose ExQuant, a PTQ framework for MoE LLMs that enables global, expert-level mixed-precision quantization. ExQuant first constructs a Globally Comparable Expert Importance Metric by integrating expert routing frequency and post-ablation performance. Based on this metric, it assigns tiered bit-widths to experts and employs a precision-aware load balancing strategy to dynamically schedule computation across processing elements, fully exploiting slack between low-and high-precision workloads. Experiments demonstrate that ExQuant significantly reduces memory footprint, improves inference efficiency, and achieves 2.87 −5.93% accuracy improvement over existing MoE quantization methods.

## 中文摘要

混合专家（MoE）大语言模型（LLM）借助动态路由与稀疏激活提升效率与可扩展性，在降低计算开销的同时实现高性能。然而，其复杂的架构与庞大的内存占用给部署带来了重大挑战，在资源受限的硬件上尤为突出。训练后量化（PTQ）是一种广泛用于减小模型规模与内存占用的技术。现有的 MoE 模型 PTQ 方法大多采用逐层方式且与任务无关，在每一层内部独立优化重建误差。因此，它们忽略了专家重要性在层间的差异，也未能利用任务特定信号，导致关键专家被过度压缩、极少激活的专家反而获得过多资源，整体精度下降。为克服这些局限，我们提出 ExQuant，一个面向 MoE LLM 的 PTQ 框架，可实现全局的、专家级混合精度量化。ExQuant 首先通过融合专家路由频率与消融后性能，构建全局可比的专家重要性度量。基于该度量，它为专家分配分层位宽，并采用精度感知的负载均衡策略在处理单元之间动态调度计算，充分利用低精度与高精度负载之间的松弛。实验表明，ExQuant 显著降低了内存占用，提升了推理效率，并相较现有 MoE 量化方法取得 2.87%−5.93% 的精度提升。
