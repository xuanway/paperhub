---
title: "TESSA: A Thermal-Centric, Sensor-Free Framework with Spatially Aware Elastic Execution for 3D-Stacked-DRAM-Based LLM Accelerators"
description: "MICRO 2026 · Session 4C · TESSA：面向三维堆叠 DRAM LLM 加速器、具备空间感知弹性执行的无传感器热管理框架"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "DRAM"
  - "Thermal Management"
---

# TESSA: A Thermal-Centric, Sensor-Free Framework with Spatially Aware Elastic Execution for 3D-Stacked-DRAM-Based LLM Accelerators

**中文标题：** TESSA：面向三维堆叠 DRAM LLM 加速器、具备空间感知弹性执行的无传感器热管理框架

**所属 Session：** [Session 4C](index.md) · [MICRO 2026](../index.md)

**作者：** Huanyu Wang, Yang Wang, Yutong Su, Jiaxin Yang, Junan Lu, Huiming Han, Yang Hu, Shouyi Yin

**来源：** MICRO 2026，pp. 1544–1558；[DOI](https://doi.org/10.1109/MICRO67795.2026.00113)

## 英文摘要

Three-dimensional (3D)-stacked DRAM is a promising substrate for large language model (LLM) acceleration, with implementations based on either HBM-like stacks with nearby logic or hybrid-bonded logic–memory fabrics. The same integration concentrates heat: concurrent compute and memory activity raises thermal stress and pushes designs toward coarse worst-case throttling that leaves spatial headroom unused. Fine-grained thermal management is limited by observability, since dense sensors in stacked DRAM add area and telemetry overhead. This paper presents TESSA, a sensor-free framework for thermal management of 3D-stacked-DRAM LLM accelerators. TESSA uses controlled local refresh pauses to convert temperature-dependent DRAM retention errors into temperature estimates. It uses the LLM's own KV-cache records as recoverable thermal probe carriers, avoiding a separate probe store and redundant readback traffic. TESSA then uses thermal-aware elastic execution to desynchronize high-power phases and rebalance ready work across regions at exact merge boundaries. Across HBM-like and hybrid-bonded architectures, TESSA's closed-loop thermal control reduces average prefill/decode latency by 51%-39% over peak-constrained global control and incurs 0.73%-0.91% capacity/bandwidth overhead.

## 中文摘要

三维 (3D) 堆叠 DRAM 是大语言模型 (LLM) 加速的有前景的基底，其实现基于具有附近逻辑的类 HBM 堆栈或混合键合逻辑内存结构。同样的集成会集中热量：并发计算和内存活动会增加热应力，并将设计推向粗略的最坏情况节流，从而导致空间净空未被利用。细粒度热管理受到可观察性的限制，因为堆叠式 DRAM 中的密集传感器增加了面积和遥测开销。本文介绍了 TESSA，一种用于 3D 堆叠 DRAM LLM 加速器热管理的无传感器框架。 TESSA 使用受控的本地刷新暂停将与温度相关的 DRAM 保留误差转换为温度估计值。它使用LLM自己的KV缓存记录作为可恢复的热探针载体，避免了单独的探针存储和冗余的读回流量。然后，TESSA 使用热感知弹性执行来取消同步高功率阶段，并在精确的合并边界处重新平衡跨区域的就绪工作。在类似 HBM 和混合键合架构中，TESSA 的闭环热控制比峰值受限全局控制将平均预填充/解码时延减少了 51%-39%，并产生了 0.73%-0.91% 的容量/带宽开销。

## 中文关键词

大语言模型；近存处理；三维堆叠 DRAM；热管理；无传感器控制

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4C](index.md) · [MICRO 2026 主页](../index.md)
