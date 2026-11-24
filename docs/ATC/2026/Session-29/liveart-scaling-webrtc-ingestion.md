# LiveART: Scaling WebRTC Ingestion

**中文标题**：LiveART：扩展 WebRTC 接入能力

**所属 Session**：[Session 29: Networking II](index.md) · [ATC 2026](../index.md)

**作者**：Jing Liu (ByteDance), Jianlin Xu (ByteDance), Bo Wang (ByteDance), Sandesh Dhawaskar Sathyanarayana (ByteDance), Wei Cao (ByteDance), Liang Yin (ByteDance), Feng Qian (ByteDance), Shu Shi (ByteDance)

## 英文摘要
This paper introduces LiveART, a WebRTC-based transport ingest system designed for the first-mile ingestion of large-scale live streaming services. LiveART addresses the QoE (Quality of Experience) gaps that RTMP (Real-Time Messaging Protocol) struggles to meet amid growing demands for low-latency live streaming. We share our experience of integrating WebRTC into large-scale live streaming systems, where cost, QoE, and computational load are critical. Our experimental studies reveal that direct integration of WebRTC harms user engagement due to mismatched QoS settings and bitrate oscillations, and incurs operational bandwidth overhead from an elevated bitrate. To overcome these hurdles, LiveART adapts standard WebRTC to large-scale ingestion transport through a series of pragmatic, non-intrusive designs across multi-level QoS enhancements, transport-level stability, and media-layer perception-guided bitrate control. Production A/B tests involving 480K streamers and over 4.8 billion views prove that LiveART significantly outperforms the RTMP protocol. Compared to RTMP, LiveART significantly improves QoE, reducing rebuffering time and frequency by 10.1% and 12.42%, audio stall time and frequency by 17.84% and 18.45%, video stall time and frequency by 5.94% and 6.44%, and end-to-end latency by 2.55%, while increasing bitrate by 1.49%. Additionally, LiveART reduces bandwidth costs by 1.46% during peak hours, while maintaining user engagement. Finally, ablation studies and a subjective user study (446 participants, 13,380 ratings) comprehensively validate the efficacy of LiveART’s design.

## 中文摘要
本文介绍 LiveART，一个基于 WebRTC 的传输接入系统，面向大规模直播服务的首英里（first-mile）接入。LiveART 弥补了在低延迟直播需求日益增长的情况下 RTMP（实时消息传输协议）难以满足的 QoE（体验质量）差距。我们分享了将 WebRTC 集成到大规模直播系统中的经验，其中成本、QoE 与计算负载至关重要。我们的实验研究表明，直接集成 WebRTC 会因 QoS 设置不匹配与码率振荡而损害用户参与度，并因码率升高带来运维层面的带宽开销。为克服这些障碍，LiveART 通过一系列务实且非侵入式的设计，在多级 QoS 增强、传输层稳定性以及媒体层感知引导的码率控制三个方面，将标准 WebRTC 适配为大规模接入传输。涉及 48 万主播和超过 48 亿次观看的生产环境 A/B 测试证明，LiveART 显著优于 RTMP 协议。与 RTMP 相比，LiveART 显著提升 QoE，将卡顿（rebuffering）时间与频次分别降低 10.1% 和 12.42%，将音频停顿时间与频次分别降低 17.84% 和 18.45%，将视频停顿时间与频次分别降低 5.94% 和 6.44%，并将端到端延迟降低 2.55%，同时将码率提升 1.49%。此外，LiveART 在高峰时段将带宽成本降低 1.46%，同时维持用户参与度。最后，消融研究与一项主观用户研究（446 名参与者、13,380 条评分）全面验证了 LiveART 设计的有效性。

## 英文关键词
WebRTC, Live Streaming, Ingest Transport Protocols, Congestion Control, Bitrate Adaptation, QoE

## 中文关键词
WebRTC，直播，接入传输协议，拥塞控制，码率自适应，QoE

[返回 Session 29](index.md) · [返回 ATC 2026](../index.md)
