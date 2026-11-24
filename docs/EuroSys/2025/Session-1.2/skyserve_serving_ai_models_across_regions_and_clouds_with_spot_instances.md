---
title: "SkyServe: Serving AI Models across Regions and Clouds with Spot Instances"
description: "EuroSys 2025 · LLM Serving · Ziming Mao (UC Berkeley), Tian Xia (UC Berkeley), Zhanghao Wu (UC Berkeley), Wei"
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# SkyServe: Serving AI Models across Regions and Clouds with Spot Instances

**中文标题：** 利用竞价实例跨区域和云服务提供 AI 模型服务

**所属 Session：** [Session 1.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Ziming Mao (UC Berkeley), Tian Xia (UC Berkeley), Zhanghao Wu (UC Berkeley), Wei-Lin Chiang (UC Berkeley), Tyler Griggs (UC Berkeley), Romil Bhardwaj (UC Berkeley), Zongheng Yang (UC Berkeley), Scott Shenker (ICSI AND UC Berkeley), Ion Stoica (UC Berkeley)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717459)

## 英文摘要

Recent years have witnessed an explosive growth of AI models. The high cost of hosting AI services on GPUs and their demanding service requirements, make it timely and challenging to lower service costs and guarantee service quality. While spot instances have long been offered with a large discount, spot preemptions have discouraged users from using them to host model replicas when serving AI models.

To address this, we propose a simple yet efficient policy, SpotHedge, that leverages spot replicas across different failure domains (e.g., regions and clouds) to ensure availability, lower costs, and high service quality. SpotHedge intelligently spreads spot replicas across different regions and clouds to improve availability and reduce correlated preemptions, overprovisions cheap spot replicas than required as a safeguard against possible preemptions, and dynamically falls back to on-demand replicas when spot replicas become unavailable. We built SkyServe, a system leveraging SpotHedge to efficiently serve AI models over a mixture of spot and on-demand replicas across regions and clouds. We compared SkyServe with both research and production systems on real AI workloads: SkyServe reduces cost by 43% on average while achieving high resource availability compared to using on-demand replicas. Additionally, SkyServe improves P50, P90, and P99 latency by 2.3×, 2.1×, 2.1× on average compared to other research and production systems.

## 中文摘要

近年来，AI 模型呈爆炸式增长。在 GPU 上托管 AI 服务的高昂成本及其苛刻的服务需求，使得降低服务成本并保障服务质量既及时又充满挑战。尽管竞价实例长期以来以大幅折扣提供，但竞价实例的抢占问题一直使人们不愿用它们托管模型副本来提供 AI 模型服务。

为此，我们提出了一种简单而高效的策略 SpotHedge，它利用跨不同故障域（例如区域和云）的竞价副本，以确保可用性、降低成本并保持高服务质量。SpotHedge 智能地将竞价副本分散到不同区域和云中，以提高可用性并减少相关抢占；它超量配置比所需更多的廉价竞价副本，作为应对可能抢占的保障；并在竞价副本不可用时动态回退到按需实例。我们构建了 SkyServe，一个利用 SpotHedge 在跨区域和云的竞价与按需实例混合环境中高效服务 AI 模型的系统。我们在真实 AI 工作负载上将 SkyServe 与研究系统和生产系统进行了比较：与使用按需实例相比，SkyServe 平均降低成本 43%，同时实现高资源可用性。此外，与其他研究系统和生产系统相比，SkyServe 平均将 P50、P90 和 P99 延迟改善 2.3 倍、2.1 倍和 2.1 倍。

**英文关键词：** Spot Instance, AI Serving, Multi-cloud, Cloud Computing

**中文关键词：** 竞价实例、AI 服务、多云、云计算

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
