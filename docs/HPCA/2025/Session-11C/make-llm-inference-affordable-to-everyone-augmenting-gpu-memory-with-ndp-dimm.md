---
title: "Make LLM Inference Affordable to Everyone: Augmenting GPU Memory with NDP-DIMM"
description: "HPCA 2025 · Viva Las Learning Models (with PIM)"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models (with PIM)"
---

# Make LLM Inference Affordable to Everyone: Augmenting GPU Memory with NDP-DIMM

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models (with PIM)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models (with PIM)</p>
</div>

**论文链接**：
**作者**：Lian Liu (1. University of Chinese Academy of Sciences. 2. CICS, Institute of Computing Technology, CAS), Shixin Zhao (1. University of Chinese Academy of Sciences. 2. CICS, Institute of Computing Technology, CAS), Bing Li (Institute of Microelectronics, Chinese Academy of Sciences), Haimeng Ren (shanghaiTech University), Zhaohui Xu (shanghaiTech University), Mengdi Wang (Institute of Computing Technology), Xiaowei Li (Institute of Computing Technology, CAS, China), Yinha Han (ICT, Chinese Academy of Sciences), Ying Wang (Institute of Computing Technology, Chinese Academy of Sciences)
**会议**：HPCA 2025

---

## 中文标题

让人人都能负担 LLM 推理：用 NDP-DIMM 扩展 GPU 内存

## 英文摘要

The billion-scale Large Language Models (LLMs) necessitate deployment on expensive server-grade GPUs with large-storage HBMs and abundant computation capability. As LLM-assisted services become popular, achieving cost-effective LLM inference on budget-friendly hardware becomes the current trend. This has sparked extensive research into relocating LLM parameters from expensive GPUs to external host memory. However, the restricted bandwidth between the host and GPU memory limits the inference performance of existing solutions. This work introduces Hermes, a budget-friendly system that leverages the near-data processing units (NDP) within commodity DRAM DIMMs to enhance the performance of a single consumer-grade GPU, achieving efficient LLM inference. We recognize that the inherent activation sparsity in LLMs naturally divides weight parameters into two categories, termed “hot” and “cold” neurons, respectively. Hot neurons, which consist of only approximately 20% of all weight parameters, account for 80% of the total computational load. In contrast, cold neurons make up the other 80% of parameters but are responsible for just 20% of the computational workload. Leveraging this observation, we propose a heterogeneous computing strategy: mapping hot neurons to a single computation-efficient GPU without large-capacity HBMs, while offloading cold neurons to NDP-DIMMs, which offer large memory size but limited computation capabilities. In addition, the dynamic nature of activation sparsity necessitates a real-time partition of hot and cold neurons and adaptive remapping of cold neurons across multiple NDP-DIMM modules. To tackle these issues, we introduce a lightweight predictor that ensures optimal real-time neuron partition and adjustment between GPU and NDP-DIMMs. Furthermore, we utilize a window-based online scheduling mechanism to maintain load balance among multiple NDP-DIMM modules. In summary, Hermes facilitates the deployment of LLaMA2-70B on consumer-grade hardware at a rate of 13.75 tokens/s and realizes an average 75.24× speedup over the state-of-the-art offloading-based inference system on popular LLMs.

## 中文摘要

十亿参数规模的大语言模型（LLM）必须在配备大容量 HBM 与充足算力的昂贵服务器级 GPU 上部署。随着 LLM 辅助服务普及，在预算友好硬件上实现高性价比的 LLM 推理成为当前趋势。这催生了将 LLM 参数从 GPU 迁移到外部主机内存的大量研究。然而主机与 GPU 内存之间受限的带宽制约了现有方案的推理性能。本工作提出 Hermes，一个高性价比系统，它利用商用 DRAM DIMM 内的近数据处理单元（NDP）提升单块消费级 GPU 的性能，实现高效的 LLM 推理。我们注意到，LLM 固有的激活稀疏性自然地将权重参数分为两类，分别称为“热”与“冷”神经元。热神经元仅占全部权重参数的约 20%，却承担 80% 的总计算量。相反，冷神经元占其余 80% 的参数，却只负责 20% 的计算负载。据此我们提出异构计算策略：将热神经元映射到单块计算高效但不具备大容量 HBM 的 GPU，而将冷神经元卸载到 NDP-DIMM，后者提供大内存容量但计算能力有限。此外，激活稀疏性的动态变化要求实时划分热、冷神经元，并在多个 NDP-DIMM 模块间自适应重映射冷神经元。为此我们引入轻量级预测器，确保在 GPU 与 NDP-DIMM 之间进行最优的实时神经元划分与调整。我们还采用基于窗口的在线调度机制，在多个 NDP-DIMM 模块间维持负载均衡。总之，Hermes 使 LLaMA2-70B 能以 13.75 tokens/s 部署在消费级硬件上，并在主流 LLM 上相比最先进的卸载式推理系统实现平均 75.24× 的加速比。
