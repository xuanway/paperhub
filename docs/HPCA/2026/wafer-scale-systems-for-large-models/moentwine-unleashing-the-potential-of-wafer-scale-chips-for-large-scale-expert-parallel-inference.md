---
title: "MoEntwine: Unleashing the Potential of Wafer-scale Chips for Large-scale Expert Parallel Inference"
description: "HPCA 2026 · Wafer-Scale Systems for Large Models"
tags:
  - "HPCA2026"
  - "Wafer-Scale Systems for Large Models"
---

# MoEntwine: Unleashing the Potential of Wafer-scale Chips for Large-scale Expert Parallel Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Wafer-Scale Systems for Large Models。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Wafer-Scale Systems for Large Models</p>
</div>

**论文链接**：
**作者**：Xinru Tang Tsinghua University , Jingxiang Hou Tsinghua University , Dingcheng Jiang Tsinghua University , Taiquan Wei Tsinghua University , Jiaxin Liu Tsinghua University , Jinyi Deng Tsinghua University , Huizheng Wang Tsinghua University , Qize Yang Tsinghua University , Haoran Shang Tsinghua University , Chao Li Shanghai Jiao Tong University , Yang Hu Tsinghua University , Shouyi Yin Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

MoEntwine：释放晶圆级芯片在大规模专家并行推理中的潜力

## 英文摘要

As large language models (LLMs) continue to scale up, mixture-of-experts (MoE) has become a common technology in SOTA models. MoE models rely on expert parallelism (EP) to alleviate memory bottleneck, which introduces all-to-all communication to dispatch and combine tokens across devices. However, in widely-adopted GPU clusters, high-overhead cross-node communication makes all-to-all expensive, hindering the adoption of EP. Recently, wafer-scale chips (WSCs) have emerged as a platform integrating numerous devices on a wafer-sized interposer. WSCs provide a unified high-performance network connecting all devices, presenting a promising potential for hosting MoE models. Yet, their network is restricted to a mesh topology, causing imbalanced communication pressure and performance loss. Moreover, the lack of on-wafer disk leads to high-overhead expert migration on the critical path. To fully unleash this potential, we first propose Entwined Ring Mapping (ER-Mapping), which co-designs the mapping of attention and MoE layers to balance communication pressure and achieve better performance. We find that under ER-Mapping, the distribution of cold and hot links in the attention and MoE layers is complementary. Therefore, to hide the migration overhead, we propose the Non-invasive Balancer (NI-Balancer), which splits a complete expert migration into multiple steps and alternately utilizes the cold links of both layers. Evaluation shows ER-Mapping achieves communication reduction up to 62%. NI-Balancer further delivers 54% and 22% improvements in MoE computation and communication, respectively. Compared with the SOTA NVL72 supernode, the WSC platform delivers an average 39% higher per-device MoE performance owing to its scalability to larger EP.

## 中文摘要

随着大语言模型（LLM）持续扩张，混合专家（MoE）已成为最先进模型中的常见技术。MoE 模型依靠专家并行（EP）缓解内存瓶颈，但这会引入全对全通信以在设备间分发与合并词元；在广泛采用的 GPU 集群中，高开销的跨节点通信使全对全通信代价高昂，阻碍了 EP 的应用。近来，晶圆级芯片（WSC）作为在晶圆尺寸中介层上集成大量器件的平台出现，其统一网络连接所有器件，为承载 MoE 模型带来可观潜力；但其网络受限于网格拓扑，造成通信压力不均衡与性能损失，且片上缺乏磁盘使关键路径上的专家迁移开销高昂。为充分释放潜力，我们首先提出交织环映射（ER-Mapping），协同设计注意力层与 MoE 层的映射以平衡通信压力，并获得更好性能；我们发现 ER-Mapping 下两层冷、热链路的分布互补。因此，为隐藏迁移开销，我们提出非侵入式均衡器（NI-Balancer），将一次完整的专家迁移拆分为多步并交替利用两层的冷链路。评估显示 ER-Mapping 使通信量最多降低 62%，NI-Balancer 进一步使 MoE 计算与通信分别改善 54% 与 22%。与最先进的 NVL72 超级节点相比，WSC 平台因可扩展到更大 EP，单设备 MoE 性能平均高出 39%。
