DRIFT: Harnessing Inherent Fault Tolerance for Efficient and Reliable Diffusion Model Inference
Authors：
[jinqi wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=4192815150900154491)，[Tong Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=21842765951470382951)，[Runsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=214343)，[Meng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=414843)

## 中文标题

DRIFT：利用固有容错能力实现高效可靠的扩散模型推理

## 英文摘要

Diffusion model deployment has been suffering from high energy consumption and inference latency despite its superior performance in visual generation tasks. Dynamic voltage and frequency scaling (DVFS) offers a promising solution to exploit the potential of the underlying accelerators. However, existing approaches often lead to either limited efficiency gains or degraded output quality because they overlook the inherent fault tolerance of the diffusion model. Therefore, in this paper, we propose DRIFT, a novel algorithm-architecture co-optimization framework that harnesses the fault tolerance for efficient and reliable diffusion model inference. We first perform a comprehensive resilience analysis on representative diffusion models. Building on these observations, we introduce a fine-grained, resilience-aware DVFS strategy that selectively protects error-sensitive network blocks and timesteps, and a rollback algorithm-based fault tolerance (ABFT) mechanism that adaptively corrects only critical errors by reverting to previous timesteps. We further optimize offloading intervals and reorganize data layouts to reduce memory overhead. Experiments across diverse models and datasets show that DRIFT can achieve on average 36% energy savings through voltage underscaling or 1.7× speedup via overclocking while maintaining generation quality.

## 中文摘要

尽管扩散模型在视觉生成任务中表现优异，但其部署始终受制于高能耗与推理延迟。动态电压频率调节（DVFS）为挖掘底层加速器的潜力提供了有前景的方案。然而，现有方法往往因忽视扩散模型固有的容错能力，而只能获得有限的效率收益或导致输出质量下降。因此，本文提出 DRIFT，一种新颖的算法-架构协同优化框架，利用容错能力实现高效可靠的扩散模型推理。我们首先对代表性扩散模型进行全面的脆弱性分析。基于这些观察，我们提出细粒度、容错感知的 DVFS 策略，选择性地保护对错误敏感的网络块与时间步；并提出基于回滚的算法级容错（ABFT）机制，通过回退到先前时间步来仅自适应地纠正关键错误。我们进一步优化卸载间隔并重组数据布局以降低内存开销。跨多种模型与数据集的实验表明，DRIFT 在保持生成质量的同时，可通过欠压平均节省 36% 的能耗，或通过超频获得 1.7 倍的加速。
