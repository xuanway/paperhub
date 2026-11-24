# Fine-Grained Loss Recovery via Packet-Level Content-Awareness for Ultra-low-latency Video Communications

**中文标题**：面向超低延迟视频通信的基于包级内容感知的细粒度丢包恢复

**所属 Session**：[Session 29: Networking II](index.md) · [ATC 2026](../index.md)

**作者**：Wei Li (Hong Kong University of Science and Technology), Zhewen Yang (Northeastern University), Hua Meng (Hong Kong University of Science and Technology), Zili Meng (Hong Kong University of Science and Technology)

## 英文摘要
Ultra-low-latency video applications, such as cloud gaming and VR, increasingly deliver high-bitrate frames within tens of milliseconds. As each frame may contain hundreds of packets, uniformly retransmitting every lost packet can unnecessarily block an entire frame, even when the missing packet has little rendered-quality impact. This paper presents LetItGo, a receiver-side content-aware loss-recovery mechanism based on the observation that lost packets within the same frame can have very different impacts on frame quality. LetItGo uses packet position and pre-decoding to decide whether a lost packet is worth waiting for. It retransmits high-impact losses and lets the existing decoder conceal less critical ones, enabling fine-grained recovery without changing the sender, encoder, playback-decoder interface, or transport protocol. We implement LetItGo in WebRTC for H.264 and extend it to H.265. Experiments with high-resolution videos and real cloud-gaming traces show that LetItGo reduces transmission time by 9.41% on average over a strong loss-recovery baseline while keeping rendered quality within a 0.44 dB-SSIM gap. Results across H.264 and H.265 at both 30 and 60 fps show that the benefit is not tied to a single codec.

## 中文摘要
云游戏与 VR 等超低延迟视频应用越来越多地在数十毫秒内传输高码率帧。由于每帧可能包含数百个包，对每个丢失的包一律重传可能不必要地阻塞整帧，即使缺失的包对渲染质量的影响甚微。本文提出 LetItGo，一种接收端的内容感知丢包恢复机制，其依据的观察是同一帧内丢失的包对帧质量的影响可能差异很大。LetItGo 利用包位置与预解码来判断某个丢失的包是否值得等待。它对高影响的丢包进行重传，并让现有解码器掩盖不那么关键的丢包，从而在不改变发送端、编码器、播放-解码器接口或传输协议的情况下实现细粒度恢复。我们在 WebRTC 中针对 H.264 实现了 LetItGo，并将其扩展到 H.265。使用高分辨率视频与真实云游戏轨迹的实验表明，LetItGo 相比一个强丢包恢复基线平均减少 9.41% 的传输时间，同时将渲染质量保持在 0.44 dB-SSIM 的差距之内。在 30 与 60 fps 下跨 H.264 与 H.265 的结果表明，该收益并不局限于单一编解码器。

## 英文关键词
Real-time video, Loss recovery, Packet retransmission, WebRTC

## 中文关键词
实时视频，丢包恢复，包重传，WebRTC

[返回 Session 29](index.md) · [返回 ATC 2026](../index.md)
