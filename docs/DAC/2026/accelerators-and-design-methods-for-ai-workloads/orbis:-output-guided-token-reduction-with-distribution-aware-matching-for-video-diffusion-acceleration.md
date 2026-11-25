ORBIS: Output-Guided Token Reduction with Distribution-Aware Matching for Video Diffusion Acceleration
Authors：
[Hangyeol Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=74453028765797217431)，[Joo-Young Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=013143)

## 中文标题

ORBIS：面向视频扩散加速的输出引导 Token 缩减与分布感知匹配

## 英文摘要

Diffusion Transformer (DiT) has emerged as a powerful model architecture for generating high-quality images and videos. In the case of video DiT, 3D Spatio-Temporal Attention increases token length in proportion to the number of frames, sharply increasing computational cost. Token reduction methods mitigate this cost by exploiting spatial redundancy, but existing approaches rely on inaccurate similarity estimates and lightweight matching algorithms, resulting in poor matching quality and only marginal acceleration. To overcome these limitations, we propose ORBIS, an SW–HW co-designed accelerator for video DiT. ORBIS leverages the output activation from the previous timestep to obtain more accurate inter-token similarity, substantially improving matching quality and enabling a higher token reduction ratio. We further introduce a Distribution-Aware Token Matching (DATM) algorithm that captures global token distribution and explicitly minimizes token-pair loss for additional gains. To fully hide DATM latency, we design specialized, deeply pipelined hardware and minimize its hardware cost through quantization, occupying only 2.4% of total area with negligible accuracy loss. Extensive experiments show that ORBIS achieves about 2× higher token reduction ratio than the state-of-the-art approach, AsymRnR, while delivering up to 4.5× speedup and 79.3% energy reduction compared to an NVIDIA A100 GPU.

## 中文摘要

扩散 Transformer（DiT）已成为生成高质量图像和视频的强大模型架构。在视频 DiT 中，三维时空注意力使 Token 长度随帧数成比例增长，从而急剧增加计算开销。Token 缩减方法通过利用空间冗余来缓解这一开销，但现有方法依赖不准确的相似性估计和轻量级匹配算法，导致匹配质量差、加速效果有限。为克服这些局限，我们提出了 ORBIS，一种面向视频 DiT 的软硬件协同设计加速器。ORBIS 利用上一时间步的输出激活获得更准确的 Token 间相似性，显著提升匹配质量，并支持更高的 Token 缩减比例。我们进一步提出分布感知 Token 匹配（DATM）算法，该算法捕获全局 Token 分布并显式最小化 Token 对损失，以获得额外收益。为完全隐藏 DATM 的延迟，我们设计了专用的深度流水线硬件，并通过量化将其硬件开销降至最低，仅占总面积的 2.4%，且精度损失可忽略。大量实验表明，ORBIS 的 Token 缩减比例约为当前最优方法 AsymRnR 的 2 倍，同时相比 NVIDIA A100 GPU 实现高达 4.5 倍的加速和 79.3% 的能耗降低。

## 英文关键词

Diffusion Model, Token Reduction Approach, SW-HW Co-Design

## 中文关键词

扩散模型、Token 缩减方法、软硬件协同设计
