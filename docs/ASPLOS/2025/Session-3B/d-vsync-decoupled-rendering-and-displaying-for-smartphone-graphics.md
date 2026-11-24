---
title: "D-VSync: Decoupled Rendering and Displaying for Smartphone Graphics"
description: "ASPLOS 2025 · Session 3B · D-VSync：面向智能手机图形的渲染与显示解耦"
tags:
  - "ASPLOS2025"
  - "Session 3B"
  - "Graphics"
---

# D-VSync: Decoupled Rendering and Displaying for Smartphone Graphics

**中文标题：** D-VSync：面向智能手机图形的渲染与显示解耦

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yuanpei Wu (IPADS, Shanghai Jiao Tong University,Engineering Research Center for Domain-specific Operating Systems, Ministry of Education), Dong Du (IPADS, Shanghai Jiao Tong University,Engineering Research Center for Domain-specific Operating Systems, Ministry of Education), Chao Xu (Fields Lab, Huawei Central Software Institute), Yubin Xia (IPADS, Shanghai Jiao Tong University,Engineering Research Center for Domain-specific Operating Systems, Ministry of Education), Ming Fu (Fields Lab, Huawei Central Software Institute), Binyu Zang (IPADS, Shanghai Jiao Tong University,Engineering Research Center for Domain-specific Operating Systems, Ministry of Education), Haibo Chen (IPADS, Shanghai Jiao Tong University,Key Laboratory of System Software (Chinese Academy of Science))

**单位：** IPADS, Shanghai Jiao Tong University,Engineering Research Center for Domain-specific Operating Systems, Ministry of Education；Fields Lab, Huawei Central Software Institute；Chinese Academy of Science

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707235) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Rendering service, which typically orchestrates screen display and UI through Vertical Synchronization (VSync), is an indispensable system service for user experiences of smartphone OSes (e.g., Android, OpenHarmony, and iOS). The recent trend of large high-frame-rate screens, stunning visual effects, and physics-based animations has placed unprecedented pressure on the VSync-based rendering architecture, leading to higher frame drops and longer rendering latency. This paper proposes Decoupled Vertical Synchronization (D-VSync), which decouples execution and displaying in the rendering service. D-VSync allows frames to be rendered a number of VSync periods before being physically displayed on the screen. The key insight behind D-VSync to resolve the limitation of VSync is that, the decoupling enables sporadic long frames to utilize the computational power saved by common short frames, therefore providing a larger time window to tolerate workload fluctuations. Evaluation results of 75 common OS use cases and apps on OpenHarmony (Mate 40 Pro, Mate 60 Pro), 25 popular apps on Android (Google Pixel 5), and simulations of 15 mobile games show that compared to VSync, D-VSync on average reduces frame drops by 72.7%, user-perceptible stutters by 72.3%, and rendering latency by 31.1%, with only 0.13%–0.37% more power consumption. D-VSync has been integrated into HarmonyOS NEXT.

## 中文摘要

渲染服务通常通过垂直同步（VSync）编排屏幕显示与 UI，是智能手机操作系统（如 Android、OpenHarmony 和 iOS）用户体验中不可或缺的系统服务。近期大尺寸高刷新率屏幕、惊艳的视觉效果以及基于物理的动画等趋势，给基于 VSync 的渲染架构带来了前所未有的压力，导致更高的丢帧率和更长的渲染延迟。本文提出解耦垂直同步（Decoupled Vertical Synchronization，D-VSync），将渲染服务中的执行与显示解耦。D-VSync 允许帧在被实际显示到屏幕之前的若干个 VSync 周期内完成渲染。D-VSync 解决 VSync 局限性的关键洞见在于：这种解耦使偶发的长帧能够利用常见短帧所节省的算力，从而提供更大的时间窗口来容忍工作负载波动。在 OpenHarmony（Mate 40 Pro、Mate 60 Pro）上对 75 个常见操作系统用例与应用、在 Android（Google Pixel 5）上对 25 个流行应用以及对 15 款手机游戏的仿真进行评估，结果表明，与 VSync 相比，D-VSync 平均将丢帧减少 72.7%、将用户可感知的卡顿减少 72.3%、将渲染延迟降低 31.1%，而功耗仅增加 0.13%–0.37%。D-VSync 已集成到 HarmonyOS NEXT 中。

## 英文关键词

Operating system, graphics system, rendering service, vertical synchronization

## 中文关键词

操作系统；图形系统；渲染服务；垂直同步

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707235)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2025](../index.md)
