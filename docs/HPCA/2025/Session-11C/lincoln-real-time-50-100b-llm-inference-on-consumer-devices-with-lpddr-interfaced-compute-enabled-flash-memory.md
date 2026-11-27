---
title: "Lincoln: Real-Time 50~100B LLM Inference on Consumer Devices with LPDDR-Interfaced, Compute-Enabled Flash Memory"
description: "HPCA 2025 · Viva Las Learning Models (with PIM)"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models (with PIM)"
---

# Lincoln: Real-Time 50~100B LLM Inference on Consumer Devices with LPDDR-Interfaced, Compute-Enabled Flash Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models (with PIM)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models (with PIM)</p>
</div>

**论文链接**：
**作者**：Weiyi Sun (Tsinghua University), Mingyu Gao (Tsinghua University), Zhaoshi Li (MetaX Technology), Aoyang Zhang (Tsinghua University), Iris Ying Chou (Tsinghua University), Jianfeng Zhu (Tsinghua University), Shaojun Wei (Tsinghua University), Leibo Liu (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

Lincoln：基于 LPDDR 接口计算增强闪存的消费级设备 50~100B LLM 实时推理

## 英文摘要

With the widespread use of large language models (LLMs), and with the privacy and cost concerns on cloud-based services, vendors are now pushing LLM inference to consumer devices. However, current attempts only enable real-time inference of low-quality small-sized LLMs. Large-sized LLMs have to load most of their weights from Flash storage for every execution iteration, which dominates the execution time of both the prefill and the generation phase. This performance bottleneck is attributed to both the low internal Flash memory bandwidth and the low transmission bandwidth between Flash and the Neural Processing Unit (NPU). To tackle these two challenges, we present Lincoln, a device-architecture co-design solution with LPDDR-interfaced, Compute-Enabled Flash Memory. On the device level, we boost the Flash internal bandwidth by improving upon existing array shrinking methods, to enable lower read latency and more parallel Flash planes within each Flash die. We specifically leverage 3D hybrid bonding, which is already adopted in consumer Flash products, to maintain high area efficiency and low density loss. On the architecture level, to leverage such increased internal bandwidth for resolving the transmission bottleneck, we propose two solutions for the two distinct phases of LLMs. For the compute-intensive prefill phase, we let Flash devices use the existing high-speed LPDDR interface (originally for DRAM), which offers much higher transmission bandwidth to the NPU than the conventional Flash interface, while maintaining good cost and area efficiency. For the memory-intensive generation phase, we rely on hybrid-bonding-based near-Flash computing to fully utilize the internal Flash bandwidth, and further equip with speculative decoding to eventually reach the real-time latency goal. Our evaluation shows that Lincoln enables real-time inference, with up to 13.23× and 254.1× speedups for LLM prefill and generation phases over conventional SSD-based systems.

## 中文摘要

随着大语言模型（LLM）的广泛使用，加上云端服务的隐私与成本顾虑，厂商正将 LLM 推理推向消费级设备。然而现有尝试仅能实现低质量小型 LLM 的实时推理。大尺寸 LLM 在每次执行迭代中都必须从闪存加载大部分权重，这主导了预填充阶段与生成阶段的执行时间。该瓶颈既源于闪存内部带宽低，也源于闪存与神经网络处理器（NPU）之间的传输带宽低。为应对这两项挑战，我们提出 Lincoln，一种 LPDDR 接口计算增强闪存的器件与架构协同设计方案。在器件层面，我们改进现有阵列缩小方法以提升闪存内部带宽，使每个闪存晶粒内实现更低读时延与更多可并行闪存平面。我们特别利用已在消费级闪存产品中采用的 3D 混合键合，保持高面积效率与低密度损失。在架构层面，为用提升后的内部带宽化解传输瓶颈，我们针对 LLM 两个不同阶段提出两种方案。对计算密集的预填充阶段，我们让闪存器件使用现有的高速 LPDDR 接口（原用于 DRAM），可为 NPU 提供远高于传统闪存接口的传输带宽，并保持良好成本与面积效率。对访存密集的生成阶段，我们依靠基于混合键合的近闪存计算充分利用闪存内部带宽，并配合推测解码，最终达到实时时延目标。评估表明，Lincoln 可实现实时推理，相比传统基于 SSD 的系统，LLM 预填充与生成阶段分别获得最高 13.23× 和 254.1× 的加速比。
