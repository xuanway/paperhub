---
title: "Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity"
description: "ASPLOS 2025 · Session 10C · Dilu：通过内省弹性实现 Serverless 深度学习服务的 GPU 按需资源供给"
tags:
  - "ASPLOS2025"
  - "Session 10C"
  - "Serverless Computing"
---

# Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity

**中文标题：** Dilu：通过内省弹性实现 Serverless 深度学习服务的 GPU 按需资源供给

**所属 Session：** [Session 10C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Cunchi Lv (ICT, CAS,UCAS), Xiao Shi (ICT, CAS,Nanjing Institute of InforSuperBahn), Zhengyu Lei (ICT, CAS,UCAS), Jinyue Huang (ICT, CAS, UCAS), Wenting Tan (ICT, CAS), Xiaohui Zheng (ICT, CAS), Xiaofang Zhao (ICT, CAS,IICT, Suzhou, CAS)

**单位：** ICT, CAS,UCAS；ICT, CAS,Nanjing Institute of InforSuperBahn；ICT, CAS, UCAS；ICT, CAS；ICT, CAS,IICT, Suzhou, CAS

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707251) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Serverless computing, with its ease of management, autoscaling, and cost-effectiveness, is widely adopted by deep learning (DL) applications. DL workloads, especially with large language models, require substantial GPU resources to ensure QoS. However, it is prone to produce GPU fragments (e.g., 15%-94%) in serverless DL systems due to the dynamicity of workloads and coarse-grained static GPU allocation mechanisms, gradually eroding the profits offered by serverless elasticity. Different from classical serverless systems that only scale horizontally, we present introspective elasticity (IE), a fine-grained and adaptive two-dimensional co-scaling mechanism to support GPU resourcing-on-demand for serverless DL tasks. Based on this insight, we build Dilu, a cross-layer and GPU-based serverless DL system with IE support. First, Dilu provides multi-factor profiling for DL tasks with efficient pruning search methods. Second, Dilu adheres to the resourcing-complementary principles in scheduling to improve GPU utilization with QoS guarantees. Third, Dilu adopts an adaptive 2D co-scaling method to enhance the elasticity of GPU provisioning in real time. Evaluations show that it can dynamically adjust the resourcing of various DL functions with low GPU fragmentation (10%-46% GPU defragmentation), high throughput (up to 1.8× inference and 1.1× training throughput increment) and QoS guarantees (11%-71% violation rate reduction), compared to the SOTA baselines. mons Attribution-NonCommercial-ShareAlike International 4.0 License.

## 中文摘要

Serverless 计算凭借其易管理性、自动伸缩与成本效益，已被深度学习（DL）应用广泛采用。DL 工作负载，尤其是涉及大语言模型的负载，需要大量 GPU 资源来保证服务质量（QoS）。然而，由于工作负载的动态性以及粗粒度的静态 GPU 分配机制，Serverless DL 系统中容易产生 GPU 碎片（例如 15%-94%），从而逐渐侵蚀 Serverless 弹性所带来的收益。与仅做水平伸缩的经典 Serverless 系统不同，我们提出内省弹性（introspective elasticity，IE）——一种细粒度、自适应的二维协同伸缩机制，用以支持 Serverless DL 任务的 GPU 按需资源供给。基于这一洞见，我们构建了 Dilu，一个支持 IE 的跨层、基于 GPU 的 Serverless DL 系统。首先，Dilu 借助高效的剪枝搜索方法为 DL 任务提供多因素剖析。其次，Dilu 在调度中遵循资源互补原则，在保证 QoS 的前提下提升 GPU 利用率。第三，Dilu 采用自适应的二维协同伸缩方法，实时增强 GPU 供给的弹性。评估表明，与 SOTA 基线相比，它能够以较低的 GPU 碎片（10%-46% 的 GPU 碎片消减）、高吞吐（推理吞吐最高提升 1.8 倍、训练吞吐提升 1.1 倍）以及 QoS 保障（违约率降低 11%-71%）动态调整各类 DL 函数的资源供给。mons Attribution-NonCommercial-ShareAlike International 4.0 License.

## 英文关键词

Serverless Deep Learning, GPU Resourcing-onDemand, Introspective Elasticity, Co-scaling

## 中文关键词

Serverless 深度学习；GPU 按需资源供给；内省弹性；协同伸缩

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707251)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10C](index.md) · [返回 ASPLOS 2025](../index.md)
