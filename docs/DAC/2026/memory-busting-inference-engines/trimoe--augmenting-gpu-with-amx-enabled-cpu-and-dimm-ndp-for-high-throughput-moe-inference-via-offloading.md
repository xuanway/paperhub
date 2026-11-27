Trimoe: Augmenting GPU with AMX-Enabled CPU and DIMM-NDP for High-Throughput MoE Inference via Offloading
Authors：
[Yudong Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=3303936576453226807)，[Yintao He](https://63dac.conference-program.com/?post_type=page&p=15&uid=707143)，[Tianhua Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=96180176271705432401)，[Lian Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4057664314367821596)，[Shixin Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=63233797065013325331)，[Zhirong Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=9273655828382873732)，[Mengdi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=636343)，[Cangyuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=80239264246888364941)，[yinhe han](https://63dac.conference-program.com/?post_type=page&p=15&uid=856243)，[Ying Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=412243)

## 中文标题

TriMoE：借助支持 AMX 的 CPU 与 DIMM-NDP 增强 GPU，通过卸载实现高吞吐 MoE 推理

## 英文摘要

To deploy large Mixture-of-Experts (MoE) models cost-effectively, offloading-based single-GPU heterogeneous inference is crucial. While GPU–CPU architectures that offload cold experts are constrained by host memory bandwidth, emerging GPU-NDP architectures utilize DIMM-NDP to offload non-hot experts. However, non-hot experts are not a homogeneous memory-bound group: a significant subset of warm experts exists is severely penalized by high GPU I/O latency yet can saturate NDP compute throughput, exposing a critical compute gap. We present TriMoE, a novel GPU–CPU–NDP architecture that fills this gap by synergistically leveraging AMX-enabled CPU to precisely map hot, warm, and cold experts onto their optimal compute units. We further introduce a bottleneck-aware expert scheduling policy and a prediction-driven dynamic relayout/rebalancing scheme. Experiments demonstrate that TriMoE achieves up to 2.83× speedup over state-of-the-art solutions.

## 中文摘要

为以低成本部署大型混合专家（MoE）模型，基于卸载的单 GPU 异构推理至关重要。将冷门专家卸载至 CPU 的 GPU-CPU 架构受制于主机存储带宽，而新兴的 GPU-NDP 架构则利用 DIMM-NDP 卸载非热门专家。然而，非热门专家并非同质的受存储带宽约束的群体：其中还存在着相当一部分温门（warm）专家，它们因较高的 GPU I/O 延迟而遭受严重损失，却又能充分占满 NDP 的计算吞吐，从而暴露出关键的计算缺口。我们提出 TriMoE，一种新颖的 GPU-CPU-NDP 架构，通过协同利用支持 AMX 的 CPU，将热门、温门与冷门专家精确映射至各自最优的计算单元，从而填补这一缺口。我们进一步引入瓶颈感知的专家调度策略，以及预测驱动的动态重布局/再平衡机制。实验表明，TriMoE 相较当前最优方案可实现最高 2.83 倍的加速。
