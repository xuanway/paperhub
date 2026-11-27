---
title: "AUM: Unleashing the Efficiency Potential of Shared Processors with Accelerator Units for LLM Serving"
description: "HPCA 2026 · Domain Specific Accelerators"
tags:
  - "HPCA2026"
  - "Domain Specific Accelerators"
---

# AUM: Unleashing the Efficiency Potential of Shared Processors with Accelerator Units for LLM Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Domain Specific Accelerators。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Domain Specific Accelerators</p>
</div>

**论文链接**：
**作者**：Xinkai Wang Shanghai Jiao Tong University , Chao Li Shanghai Jiao Tong University , Yiming Zhuansun Shanghai Jiao Tong University , Jinyang Guo Shanghai Jiao Tong University , Xiaofeng Hou Shanghai Jiao Tong University , Jing Wang Shanghai Jiao Tong University , Luping Wang Alibaba Group , Weigao Chen Alibaba Group , Cheng Huang Alibaba Group , Guodong Yang Alibaba Group , Liping Zhang Alibaba Group , Minyi Guo Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

AUM：释放带加速器单元的共享处理器在 LLM 服务中的效率潜力

## 英文摘要

Generative AI, especially LLM, is driving a fundamental shift in software paradigms, prompting cloud providers to build more efficient serving infrastructures. To meet the computational demands of emerging software, modern CPU processors are integrating Accelerator Units (AU) in the pipeline to accelerate key operations, such as Intel AMX for matrix multiplication. Current practices that dedicate AU-enabled CPU exclusively to LLM serving lead to significant resource waste and inferior efficiency. To this end, sharing AU-enabled CPU with general workloads is necessary to harvest redundant resources and improve platform performance-per-watt. However, perfectly sharing AU can be challenging since they introduce three-dimensional variations: variable usage patterns, compulsory frequency interferences, and dissimilar resource bounds. Existing resource managers are oblivious to complex Accelerator Unit Variations (AUV), resulting in performance and efficiency degradations of up to 50% in shared environments. Therefore, this paper introduces AUM, a novel AU-aware resource manager designed to handle AUV and maximize the efficiency of shared processors. AUM has two cooperative components with three stages for three-dimensional AUV. The background profiler characterizes the usage, frequency, and resource information into a discrete model, guiding the runtime controller to analyze usage-aware requirements, select frequency-aware divisions, and make bound-aware resource decisions. Through extensive evaluations on production AU-enabled CPUs, we show that AUM improves CPU efficiency by 4.7-8.8% while maintaining high-performance AU applications by reducing SLO violations by 7-11% compared with state-of-the-art resource managers.

## 中文摘要

生成式 AI，尤其是 LLM，正推动软件范式发生根本转变，促使云厂商构建更高效的服务基础设施。为满足新兴软件的计算需求，现代 CPU 在流水线中集成加速器单元（AU）以加速关键操作，例如用于矩阵乘的 Intel AMX。当前将启用 AU 的 CPU 独占用于 LLM 服务的做法造成显著资源浪费与效率低下。因此，让启用 AU 的 CPU 与通用负载共享，以利用冗余资源并提升平台每瓦性能是必要的。然而完美共享 AU 颇具挑战，因为它们带来三个维度的差异：使用模式多变、频率干扰具有强制性以及资源边界不同。现有资源管理器对复杂的加速器单元差异（AUV）无感知，在共享环境中导致高达 50% 的性能与效率下降。为此本文提出 AUM，一种新颖的 AU 感知资源管理器，用于处理 AUV 并最大化共享处理器的效率。其后台剖析器将使用、频率与资源信息刻画为离散模型，引导运行时控制器分析使用感知的需求、选择频率感知的划分并做出边界感知的资源决策。在生产环境启用 AU 的 CPU 上的评估表明，与最先进的资源管理器相比，AUM 在将 SLO 违规减少 7–11% 的同时提升 CPU 效率 4.7–8.8%。
