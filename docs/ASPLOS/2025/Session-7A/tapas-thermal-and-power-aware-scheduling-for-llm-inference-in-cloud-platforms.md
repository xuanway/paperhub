---
title: "TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms"
description: "ASPLOS 2025 · Session 7A · TAPAS：云平台中面向 LLM 推理的热感知与功耗感知调度"
tags:
  - "ASPLOS2025"
  - "Session 7A"
  - "Serving LLMs"
---

# TAPAS: Thermal- and Power-Aware Scheduling for LLM Inference in Cloud Platforms

**中文标题：** TAPAS：云平台中面向 LLM 推理的热感知与功耗感知调度

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jovan Stojkovic (University of Illinois at Urbana-Champaign), Chaojie Zhang (Microsoft Azure Research), Íñigo Goiri (Microsoft Azure Research), Esha Choukse (Microsoft Azure Research), Haoran Qiu (Microsoft Azure Research), Rodrigo Fonseca (Microsoft Azure Research), Josep Torrellas (University of Illinois at Urbana-Champaign), Ricardo Bianchini (Microsoft Azure)

**单位：** University of Illinois at Urbana-Champaign；Microsoft Azure Research；Microsoft Azure

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716025) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The rising demand for generative large language models (LLMs) poses challenges for thermal and power management in cloud datacenters. Traditional techniques are often inadequate for LLM inference due to the fine-grained, millisecond-scale execution phases, each with distinct performance, thermal, and power profiles. Additionally, LLM inference workloads are sensitive to various configuration parameters (e.g., model parallelism, size, and quantization) that involve trade-offs between performance, temperature, power, and output quality. Moreover, clouds often co-locate SaaS and IaaS workloads, each with different levels of visibility and flexibility. To address these challenges, we propose TAPAS, a thermaland power-aware framework designed for LLM inference clusters in the cloud. TAPAS enhances cooling and power oversubscription capabilities, reducing the total cost of ownership (TCO) while effectively handling emergencies (e.g., cooling and power failures). TAPAS leverages historical temperature and power data, along with the adaptability of SaaS workloads, to: (1) efficiently place new GPU workload VMs within cooling and power constraints, (2) route LLM inference requests across SaaS VMs, and (3) reconfigure SaaS VMs to manage load spikes and emergency situations. Our evaluation on a large GPU cluster demonstrates significant reductions in thermal and power throttling events, boosting system efficiency. Attribution International 4.0 License.

## 中文摘要

生成式大语言模型（LLM）需求的增长给云数据中心的热管理和功耗管理带来挑战。传统技术往往难以适用于 LLM 推理，因为其执行阶段细粒度、以毫秒为尺度，且每个阶段都具有不同的性能、热和功耗特征。此外，LLM 推理工作负载对各种配置参数（如模型并行、规模和量化）敏感，这些参数涉及性能、温度、功耗和输出质量之间的权衡。而且，云中通常混部 SaaS 与 IaaS 工作负载，二者的可见性和灵活性程度各不相同。为应对这些挑战，我们提出 TAPAS，一个为云中 LLM 推理集群设计的热感知与功耗感知框架。TAPAS 增强了冷却与功耗超售能力，在有效处理紧急情况（如冷却和供电故障）的同时降低总拥有成本（TCO）。TAPAS 利用历史温度与功耗数据以及 SaaS 工作负载的可适应性，来：(1) 在冷却和功耗约束内高效放置新的 GPU 工作负载虚拟机，(2) 在 SaaS 虚拟机之间路由 LLM 推理请求，(3) 重新配置 SaaS 虚拟机以应对负载尖峰和紧急情况。我们在大型 GPU 集群上的评估表明，热与功耗限流事件显著减少，系统效率得到提升。Attribution International 4.0 License.

## 英文关键词

Large language models, GPUs, thermal management, power management, cloud datacenters

## 中文关键词

大语言模型；GPU；热管理；功耗管理；云数据中心

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716025)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2025](../index.md)
