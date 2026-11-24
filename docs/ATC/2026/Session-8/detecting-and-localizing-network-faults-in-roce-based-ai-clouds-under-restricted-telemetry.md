# Detecting and Localizing Network Faults in RoCE-Based AI Clouds under Restricted Telemetry

**中文标题**：受限遥测条件下基于 RoCE 的 AI 云中网络故障的检测与定位

**所属 Session**：[Session 8: Data Center Networking](index.md) · [ATC 2026](../index.md)

**作者**：Sinuo Cao (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Weiqi Zhu (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Jie Gui (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Jintao He (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Qun Huang (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Hao Liang (Huawei Technologies Co. Ltd), Yang Wang (Huawei Technologies Co. Ltd), Bolong Cui (Huawei Technologies Co. Ltd), Tingfeng Jiang (Huawei Technologies Co. Ltd), Weiling Gu (Huawei Technologies Co. Ltd), Tao Peng (Huawei Technologies Co. Ltd), Xudong Liu (Huawei Technologies Co. Ltd), Ronghua Sun (Huawei Technologies Co. Ltd), Zhi Zhang (Huawei Technologies Co. Ltd), Xiangyang Wu (Huawei Technologies Co. Ltd), Wei Song (Huawei Technologies Co. Ltd)

## 英文摘要
This paper addresses network fault detection and localization in Huawei’s large-scale RoCE-based AI public cloud infrastructures. Diagnosing network faults is difficult in this scenario. Public-cloud privacy and commodity-switch hardware restrict the available diagnostic signals to network-side, standard-switch telemetry. Moreover, RoCE semantics and the throughput-sensitive training workloads we host make TCP-targeted and latency-based techniques a poor fit. To address these challenges, we present FACT, a production system that exploits protocol-native signals already present in the network using only commodity-switch capabilities. These signals include NAK packets for packet loss, packet conservation counters, and per-flow throughput computed from mirrored packet headers. FACT organizes these signals into a two-tier architecture that separates objective fault detection from evidence-based root-cause analysis. We have deployed FACT in multiple production infrastructures, and the longest deployment has lasted 18 months. Across all deployed infrastructures in 2025, FACT detected thousands of network faults and localized 99.95% of network faults within 10 minutes.

## 中文摘要
本文研究华为大规模基于 RoCE 的 AI 公有云基础设施中的网络故障检测与定位问题。在该场景下诊断网络故障十分困难。公有云隐私与商用交换机硬件的限制，将可用的诊断信号限定为网络侧的标准交换机遥测。此外，RoCE 语义以及我们所承载的吞吐敏感型训练负载，使面向 TCP 的技术与基于延迟的技术都不适用。为应对这些挑战，我们提出 FACT，一个仅利用商用交换机能力、挖掘网络中已有协议原生信号的生产系统。这些信号包括用于丢包的 NAK 报文、报文守恒计数器，以及由镜像报文头计算得到的每流吞吐。FACT 将这些信号组织为两层架构，将客观的故障检测与基于证据的根因分析分离。我们已在多个生产基础设施中部署 FACT，最长的一次部署已持续 18 个月。在 2025 年所有已部署的基础设施中，FACT 检测到数千个网络故障，并在 10 分钟内定位了 99.95% 的网络故障。

## 英文关键词
Network Fault Localization, Network Monitoring, RDMA, RoCE, Data Center Networks, AI Infrastructure

## 中文关键词
网络故障定位，网络监控，RDMA，RoCE，数据中心网络，AI 基础设施

[返回 Session 8](index.md) · [返回 ATC 2026](../index.md)
