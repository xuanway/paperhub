CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution
Authors：
[Mu-Young Son](https://63dac.conference-program.com/?post_type=page&p=15&uid=46166305451895887471)，[Yi Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7035928511391335204)，[Seungjae Yoo](https://63dac.conference-program.com/?post_type=page&p=15&uid=0097923392802192532)，[Soongyu Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=87620130377898780471)，[Joo-Young Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=013143)

## 中文标题

CoX-MoE：面向高吞吐 MoE 推理的合并式专家执行与 AMX 使能 CPU-GPU 协同执行

## 英文摘要

The Mixture-of-Experts (MoE) architecture improves computational efficiency via sparse expert activation, but throughput-oriented inference faces substantial GPU memory pressure due to a significant parameter size and intermediate data. Prior works attempt to mitigate this using expert offloading with micro-batching or by offloading computation to the CPU. However, the fragmented workload resulting from micro-batching degrades operational intensity, causing expert execution to become memory-bound. Meanwhile, CPU offloading is constrained by slow PCIe transfers and its limited applicability to attention computation in the decode stage. Consequently, these inefficiencies prevent effective system utilization, severely restricting the end-to-end throughput of MoE inference. To address these challenges, this paper proposes CoX-MoE, an Advanced Matrix Extensions (AMX)–enabled CPU–GPU collaborative system that comprehensively optimizes MoE inference by combining coalesced expert execution with strategic workload orchestration for higher throughput. CoX-MoE introduces (i) a coalescing-aware orchestration policy to jointly optimize resource allocation by adopting ordinary batch, instead of micro-batch, for expert computation and selective attention offloading, and (ii) a static expert-aware stratification scheme that pre-assigns frequently activated experts to the GPU, mitigating PCIe transfer overhead and balancing workload for the CPU and GPU during inference. Compared to state-of-the-art frameworks, CoX-MoE delivers significant gains, achieving up to 7.1× and 2.4× higher throughput than FlexGen and MoE-Lightning, respectively.

## 中文摘要

混合专家（MoE）架构通过稀疏的专家激活提升了计算效率，但面向吞吐的推理仍因庞大的参数规模和中间数据而承受巨大的 GPU 显存压力。已有工作试图通过微批处理下的专家卸载，或将计算卸载到 CPU 来缓解该问题。然而，微批处理造成的碎片化负载降低了运算强度，使专家执行变为访存受限；同时，CPU 卸载受制于缓慢的 PCIe 传输，且难以适用于解码阶段的注意力计算。因此，这些低效问题阻碍了系统的有效利用，严重限制了 MoE 推理的端到端吞吐。为应对上述挑战，本文提出 CoX-MoE，一种由高级矩阵扩展（AMX）使能的 CPU-GPU 协同系统，通过将合并式专家执行与策略性工作负载编排相结合来全面优化 MoE 推理，从而实现更高吞吐。CoX-MoE 引入：（i）合并感知的编排策略，采用常规批而非微批执行专家计算并有选择地卸载注意力，以联合优化资源分配；（ii）静态的专家感知分层方案，将高频激活的专家预先分配给 GPU，从而降低 PCIe 传输开销，并在推理期间平衡 CPU 与 GPU 的负载。与最先进框架相比，CoX-MoE 取得显著收益，吞吐分别较 FlexGen 和 MoE-Lightning 高出至多 7.1 倍和 2.4 倍。

## 英文关键词

MoE Inference, Offloading, Coalescing Micro-Batch, GPU-CPU Cooperative Computing, AMX

## 中文关键词

MoE 推理、卸载、微批合并、GPU-CPU 协同计算、AMX
