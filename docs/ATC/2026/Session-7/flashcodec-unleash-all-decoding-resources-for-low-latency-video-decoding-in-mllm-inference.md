# FlashCodec: Unleash All Decoding Resources for Low-Latency Video Decoding in MLLM Inference

**中文标题**：FlashCodec：释放全部解码资源以实现 MLLM 推理中的低延迟视频解码

**所属 Session**：[Session 7: Long-context and Multimodal LLMs](index.md) · [ATC 2026](../index.md)

**作者**：Lingxiao Zhao (Wuhan University), Haoran Zhou (Wuhan University), Yuezhi Che (Wuhan University), Rongyu Luo (Wuhan University), Dazhao Cheng (WuHan University)

## 英文摘要
Multimodal Large Language Models (MLLMs) increasingly support video understanding workloads, where video decoding constitutes a substantial portion of end-to-end inference latency, as raw video streams must be decoded into pixel frames before model processing. However, existing frameworks fail to effectively leverage abundant decoding resources (e.g., CPUs and NVDECs) to minimize per-video decoding latency while maintaining high throughput. As a result, video decoding becomes a dominant contributor to the Time-To-First-Token (TTFT). This inefficiency arises from inter-frame dependency constraints in video decoding, device-level heterogeneity between CPU and GPU, and intrinsic limitations of decoding resources themselves, along with GPU resource contention with co-located MLLM inference, collectively limiting effective resource utilization. In this paper, we present FlashCodec, a video decoding framework designed to effectively utilize heterogeneous decoding resources for low-latency, high-throughput video decoding. FlashCodec introduces: (1) a dependency-isolated GOP-level scheduling scheme that enables parallelism without redundant decoding; (2) a runtime adaptive scheduler that dynamically assigns GOPs to heterogeneous decoders without pre-allocation, guided by device characteristics to maximize utilization; and (3) an SM-light decoding pipeline that minimizes reliance on GPU SMs, reducing interference under co-located inference. Together, these techniques enable efficient and low-latency video decoding for latency-critical online MLLM inference. Experiments across a wide range of codecs and GPU servers show that FlashCodec achieves 6.8–25.7× decoding speedup over out-of-the-box implementations with over 90% peak efficiency, surpasses static chunking parallelization strategies 2.7-7.0× in latency and 2.6-9.8× in throughput, incurs minimal overhead when colocated with MLLM services, and enables up to 7.1× stricter TTFT SLOs in end-to-end inference.

## 中文摘要
多模态大语言模型（MLLM）日益支持视频理解工作负载，其中视频解码占端到端推理延迟的相当大一部分，因为原始视频流必须先解码为像素帧才能进行模型处理。然而，现有框架未能有效利用丰富的解码资源（如 CPU 和 NVDEC）来在保持高吞吐的同时最小化单视频解码延迟。因此，视频解码成为首 token 时延（TTFT）的主要贡献者。这种低效源于视频解码中的帧间依赖约束、CPU 与 GPU 之间的设备级异构性以及解码资源自身的固有局限，加之与同机部署的 MLLM 推理之间的 GPU 资源争用，共同限制了资源的有效利用。本文提出 FlashCodec，一个旨在有效利用异构解码资源以实现低延迟、高吞吐视频解码的视频解码框架。FlashCodec 引入：(1) 一种依赖隔离的 GOP 级调度方案，可在无冗余解码的前提下实现并行；(2) 一个运行时自适应调度器，无需预分配即可将 GOP 动态分配给异构解码器，并以设备特性为引导以最大化利用率；(3) 一条轻量占用 SM 的解码流水线，最小化对 GPU SM 的依赖，降低同机部署推理时的干扰。这些技术共同为延迟敏感的在线 MLLM 推理实现了高效、低延迟的视频解码。在多种编解码器和多种 GPU 服务器上的实验表明，FlashCodec 相较开箱即用实现取得 6.8–25.7× 的解码加速，峰值效率超过 90%，在延迟上超过静态分块并行策略 2.7–7.0×，在吞吐上超过 2.6–9.8×，与 MLLM 服务同机部署时开销极小，并使端到端推理中的 TTFT SLO 最多收紧 7.1×。

## 英文关键词
Video Decoding, MLLM Inference, Hardware Decoding Resources

## 中文关键词
视频解码，MLLM 推理，硬件解码资源

[返回 Session 7](index.md) · [返回 ATC 2026](../index.md)
