---
title: "Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot"
description: "FAST 2025 · Machine Learning and Storage · 以 KVCache 为中心的分离式架构，池化存储替代重复预填充，容量提升 59%~498%"
tags:
  - "FAST2025"
  - "Machine Learning and Storage"
  - "KVCache"
  - "disaggregated architecture"
  - "最佳论文"
---

# Mooncake: Trading More Storage for Less Computation — A KVCache-centric Architecture for Serving LLM Chatbot

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Kimi 的 serving 平台把 GPU 集群中闲置的 CPU、DRAM、SSD 与 NIC 池化成全局 KVCache，由调度器在严格 TTFT、TBT SLO 下最大化有效吞吐。真实 trace 回放中有效请求容量比 vLLM 等基线高 59%~498%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Machine Learning and Storage · 最佳论文</p>
</div>

**中文标题**：Mooncake：以更多存储换取更少计算——面向 LLM 聊天机器人服务的 KVCache 中心架构

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/qin](https://www.usenix.org/conference/fast25/presentation/qin)

**论文 PDF**：[fast25-qin.pdf](https://www.usenix.org/system/files/fast25-qin.pdf)

**作者**：Ruoyu Qin（Moonshot AI and Tsinghua University）；Zheming Li、Weiran He、Jialei Cui（Moonshot AI）；Feng Ren、Mingxing Zhang、Yongwei Wu、Weimin Zheng（Tsinghua University）；Xinran Xu（Moonshot AI）

**会议**：FAST 2025 · Santa Clara, CA · 第 155–170 页 · **最佳论文**

**Session**：Machine Learning and Storage · 2025-02-25 15:50–17:30 · Chair：Kan Wu（Google）

**所属 Session**：[Machine Learning and Storage](index.md) · [FAST 2025](../index.md)

**关键词**：KVCache, disaggregated architecture, prefix caching, LLM serving, SLO, RDMA

---

## 英文摘要

Mooncake is the serving platform for Kimi, an LLM chatbot service developed by Moonshot AI. This platform features a KVCache-centric disaggregated architecture that not only separates prefill and decoding clusters but also efficiently utilizes the underexploited CPU, DRAM, SSD and NIC resources of the GPU cluster to establish a disaggregated KVCache. At the core of Mooncake is its KVCache-centric global cache and a scheduler designed to maximize throughput while adhering to stringent latency-related Service Level Objectives (SLOs).

Our experiments demonstrate that Mooncake excels in scenarios involving long-context inputs. In tests using real traces, Mooncake increases the effective request capacity by 59%~498% when compared to baseline methods, all while complying with SLOs. Currently, Mooncake is operational across thousands of nodes, processing over 100 billion tokens daily. In practical deployments, Mooncake's innovative architecture enables Kimi to handle 115% and 107% more requests on NVIDIA A800 and H800 clusters, respectively, compared to previous systems.

## 中文摘要

Mooncake 是 Moonshot AI 为 LLM 聊天服务 Kimi 打造的 serving 平台。其核心是 KVCache 为中心的分离式架构：不仅把 prefill 与 decoding 集群分开，还把 GPU 集群中未被充分利用的 CPU、DRAM、SSD 与 NIC 资源组织成分离式 KVCache 池。其核心是以 KVCache 为中心的全局缓存，以及一个旨在遵守严格延迟 SLO 的同时最大化吞吐的调度器。

实验表明，Mooncake 在长上下文输入场景中表现出色；在真实 trace 测试中，它满足 SLO 的同时把有效请求容量相对基线提升 59%~498%；它已在数千个节点上运行，每天处理超过 1000 亿个 token，并使 Kimi 在 A800 与 H800 集群上分别比此前系统多承接 115% 与 107% 的请求。

## 一句话总结

> KVCache 不必留在本地：把集群闲置的 CPU、DRAM、SSD 与 NIC 池化成全局缓存，用更多存储换掉重复的预填充计算。

## 研究背景与问题

- **负载与目标高度分化**：LLM 服务在输入输出长度、到达分布与 SLO 类型上差异很大，MaaS 商要在满足首 token 延迟（TTFT）与 token 间延迟（TBT）两类约束的前提下最大化有效吞吐（goodput）。
- **前缀复用被容量卡住**：相同输入前缀在不同会话与查询间反复出现，其 KVCache 可无损复用，但已有方案把缓存限制在本地 HBM 与 DRAM，而本地 DRAM 容量只能支撑理论上限 50% 的缓存命中率。
- **两阶段特性不同**：prefill 计算密集、decoding 受显存容量与 TBT 约束，已有工作尝试分离两者，但带宽开销与 chunked prefill 的取舍仍有争议，缺少把 KVCache 本身也池化的完整设计。

## 核心贡献

- **KVCache 为中心的分离式架构**：把 prefill 池、decoding 池与经由 RDMA 互联的分布式 KVCache 池（Mooncake Store）分开部署，用 GPU 集群中未被充分利用的 CPU、DRAM、SSD 与 NIC 资源构建近 GPU 的全局前缀缓存。
- **全局调度器 Conductor**：为每个请求选出一对 prefill 与 decoding 实例，并按 KVCache 复用情况执行换入、复制等调度操作，形成 cache-aware 的 prefill 调度与负载均衡的 decoding 调度。
- **分级优化目标**：prefill 阶段以最大化缓存复用为目标，受 TTFT SLO、MFU 下界与 DRAM 容量约束；decoding 阶段以最大化吞吐为目标，受 TBT SLO 与 VRAM 容量约束。
- **chunked pipeline parallelism（CPP）**：把单个长上下文请求的处理切分到多个节点，降低长输入的 TTFT，相比传统 sequence parallelism 减少网络开销并降低对频繁弹性扩缩容的依赖。

## 方法与技术要点

- **请求调度三步走**：Conductor 先把尽可能多的可复用 KVCache 传到选定的 prefill 实例；prefill 按 chunk 与层推进，并持续把产生的 KVCache 流式送给对应的 decoding 实例；decoding 实例加载 KVCache 后把请求加入 continuous batching 生成输出。
- **缓存池化**：Mooncake Store 由 CPU、DRAM、SSD 与 RDMA 资源构成 PB 级缓存池，RDMA 网络带宽最高 8×400 Gbps，使前缀缓存不再受单机 DRAM 容量限制。
- **热点迁移**：用启发式的自动化热点迁移复制热 KVCache 块以避开取数拥塞，无需精确预测未来使用；冷块则换出以减少预留成本。
- **传输引擎**：高优化的 RDMA KVCache 传输引擎使 P/D 分离下的通信开销可控，因此在严格 SLO 场景下 P/D 分离比 chunked prefill 更合适。
- **P/D 比例取舍**：在线流量的统计特性通常稳定，因此固定 prefill 与 decoding 的节点比例并持续监控两侧负载，仅在明显波动时切换节点角色；实测该比例接近 1:1 时有效请求容量最高。

## 评估与主要结果

- **有效请求容量**：在真实对话负载回放、不同 TBT SLO 阈值下，Mooncake 的有效请求容量比基线提升 59%~498%（Mooncake 与 vLLM、vLLM Prefix Caching、vLLM Chunked Prefill 三个基线各用 16 个 8×A800 节点）。
- **全局缓存的价值**：与本地缓存设计相比，Mooncake Store 的缓存命中率最高为 2.36 倍，使 prefill 计算时间最多节省 48%；作为对照，本地 DRAM 只能支撑 50% 的理论命中率。
- **传输引擎**：支持高速 RDMA 传输的引擎比现有方案分别快约 2.4 倍与 4.6 倍。
- **生产部署**：Mooncake 已在数千个节点上运行，每日处理超过 1000 亿（100 billion）个 token；相比此前的系统，Kimi 在 NVIDIA A800 与 H800 集群上分别多承接 115% 与 107% 的请求。

[返回 Machine Learning and Storage](index.md) · [返回 FAST 2025](../index.md)
