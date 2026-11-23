---
title: "SEAL: A Single-Event Architecture for In-Sensor Visual Localization"
description: "ISCA 2025 · Session 8C · SEAL：面向传感器内视觉定位的单事件架构"
tags:
  - "ISCA2025"
  - "Session 8C"
  - "Domain Specific Accelerators II"
---

# SEAL: A Single-Event Architecture for In-Sensor Visual Localization

**中文标题：** SEAL：面向传感器内视觉定位的单事件架构

**所属 Session：** [Session 8C](index.md) · [ISCA 2025](../index.md)

**作者：** Ryan Hou, Thomas Twomey, Vasileios Milionis, Evangelos Dikopoulos, Tianrui Ma, Yuhao Zhu, Georgios Tzimpragos

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731034) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Image sensors have low costs and broad applications, but the large data volume they generate can result in significant energy and la- tency overheads during data transfer, storage, and processing. This paper explores how shifting from traditional binary encoding to delay-based codes early on can address these inefficiencies, enabling keypoint detection and tracking within digital pixel sensors. The re- sult is SEAL, a Single-Event Architecture for In-Sensor Localization. SEAL optimizes the entire pipeline between the pixel array and the sensor-processor interface by introducing a temporal processor co-designed with analog-to-time converters, followed by a custom heavily quantized frontend processor. Its implementation is fully digital, relying on off-the-shelf CMOS cells and EDA tools, and adheres to race logic’s single-wire-per-variable and single-event- per-wire policies to maximize energy and area efficiency wherever possible. Our evaluation—combining analog and digital simulations, FPGA prototyping, and an end-to-end system analysis incorporat- ing a host processor for visual inertial odometry (VIO) backend tasks—demonstrates a 16–61×reduction in the latency of keypoint detection and tracking compared to software baselines running on the host processor, and a 7×reduction in energy consumption compared to a standard digital pixel sensor without processing capabilities. Meanwhile, SEAL preserves robust tracking accuracy: on the EuRoC dataset, the average root mean square absolute tra- jectory error decreases by 1.0 cm for HybVIO and increases by just 0.3 cm for VINS-Mono compared to their original implementations.

## 中文摘要

图像传感器成本低廉、应用广泛，但它产生的海量数据会在传输、存储与处理阶段带来巨大的能耗与延迟开销。本文研究将早期编码方式从传统二进制编码改为基于时延的编码，以此缓解上述低效问题，在数字像素传感器内部实现关键点检测与跟踪。基于该思路，本文提出SEAL：面向感内定位的单事件架构（Single-Event Architecture for In-Sensor Localization）。

SEAL协同设计时序处理器与模数-时间转换器，再搭配定制化的重度量化前端处理器，对像素阵列到传感器-处理器接口之间的整条流水线进行优化。该设计为全数字实现，采用商用标准CMOS单元与EDA工具；同时遵循竞争逻辑（race logic）的规则：每个变量仅用单根信号线、每根信号线只承载单事件，尽可能最大化能效与面积利用率。

本文评测融合了数模仿真、FPGA原型验证以及端到端系统分析，后端视觉惯性里程计（VIO）任务由主机处理器完成。实验结果表明：相比在主机上运行的软件基线，SEAL将关键点检测与跟踪的延迟降低16–61倍；对比无处理能力的标准数字像素传感器，能耗降低7倍。同时SEAL能够保持稳定的跟踪精度：在EuRoC数据集上，和原生实现相比，HybVIO的平均轨迹均方根绝对误差下降1.0 cm，VINS-Mono仅上升0.3 cm。

## 英文关键词

Image sensors, computer vision, AR/VR, robot sensing systems, in-sensor computing, race logic.

## 中文关键词

图像传感器, 计算机视觉, 增强现实/虚拟现实, 机器人感知系统, 感内计算, 竞争逻辑

## 代码与研究制品

- [代码仓库](https://github.com/Mad-PCLs/SEAL)
- [研究制品](https://doi.org/10.5281/zenodo.15314015)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731034)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8C](index.md) · [返回 ISCA 2025](../index.md)
