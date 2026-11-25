Specmoe: A Fast and Efficient Mixture-of-Experts Inference via Self-Assisted Speculative Decoding
Authors：
[Jehyeon Bang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8783682422973193613)，[Eunyeong Cho](https://63dac.conference-program.com/?post_type=page&p=15&uid=4827248726870414334)，[Ranggi Hwang](https://63dac.conference-program.com/?post_type=page&p=15&uid=09910720659952338761)，[Jinha Chung](https://63dac.conference-program.com/?post_type=page&p=15&uid=9921384446730822966)，[Minsoo Rhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=642143)

## 中文标题

SpecMoE：一种基于自辅助投机解码的快速高效混合专家推理方法

## 英文摘要

The Mixture-of-Experts (MoE) architecture has emerged as a promising approach to mitigate the rising computational costs of large language models (LLMs) by selectively activating parameters. However, its high memory requirements and sub-optimal parameter efficiency pose significant challenges for efficient deployment. Although CPU-offloaded MoE inference systems have been proposed in the literature, they offer limited efficiency, particularly for large batch sizes. In this work, we propose SpecMoE, a memory-efficient MoE inference system based on our self-assisted speculative decoding algorithm. SpecMoE demonstrates the effectiveness of applying speculative decoding to MoE inference without requiring additional model training or fine-tuning. Our system improves inference throughput by up to 4.30×, while significantly reducing bandwidth requirements of both memory and interconnect on memory-constrained systems.

## 中文摘要

混合专家（MoE）架构通过选择性激活参数，已成为缓解大语言模型（LLM）计算成本不断上升的一种有前景的方法。然而，其高内存需求与次优的参数效率给高效部署带来了重大挑战。尽管已有研究提出了 CPU 卸载的 MoE 推理系统，但其效率有限，在大批量尺寸下尤为明显。本文提出 SpecMoE，一个基于我们自辅助投机解码算法的内存高效 MoE 推理系统。SpecMoE 证明了无需额外模型训练或微调即可将投机解码应用于 MoE 推理的有效性。我们的系统将推理吞吐量最高提升 4.30 倍，同时在内存受限系统中显著降低内存与互连的带宽需求。
