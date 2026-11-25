Ternainfer: Pushing the Compression Boundary of Ternary LLMs Towards 1.58-Bit GPU Inference
Authors：
[Jie Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7163610914303907378)，[Edwin Hsing-Mean Sha](https://63dac.conference-program.com/?post_type=page&p=15&uid=729143)，[Longshan Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=3572394371196028397)，[Yuhong Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=89245068032895592501)，[Yunfan Chi](https://63dac.conference-program.com/?post_type=page&p=15&uid=2004434545244542807)，[Qingfeng Zhuge](https://63dac.conference-program.com/?post_type=page&p=15&uid=629143)

## 中文标题

TernaInfer：将三值 LLM 的压缩边界推向 1.58 比特 GPU 推理

## 英文摘要

Recent advances in Microsoft’s ternary BitNet, restricting weights to {−1, 0, +1}, have highlighted the potential of low-bit large language models (LLMs). Ideally, each ternary weight requires only log2(3) ≈1.58 bits. However, existing inference systems still use redundant bit representations for computational efficiency. To push the compression boundary and maintain efficiency, we propose TernaInfer, a GPU inference framework for ternary LLMs that integrates lossless compression with ternary-optimized sparse matrix multiplication. To our knowledge, TernaInfer is the first work to realize 1.58 bits per weight on the ternary BitNet while providing 1.53× throughput improvement over half-precision GPU inference. The code is available at: https://github.com/Gu-J/TernaInfer.

## 中文摘要

微软三值 BitNet 的近期进展将权重限制为 {−1, 0, +1}，凸显了低位宽大语言模型（LLM）的潜力。理想情况下，每个三值权重仅需 log2(3) ≈ 1.58 比特。然而，现有推理系统为换取计算效率仍采用冗余的位表示。为突破压缩边界并保持效率，我们提出 TernaInfer，这是一个面向三值 LLM 的 GPU 推理框架，将无损压缩与三值优化的稀疏矩阵乘法相结合。据我们所知，TernaInfer 是首个在三值 BitNet 上实现每权重 1.58 比特、同时相比半精度 GPU 推理取得 1.53× 吞吐提升的工作。代码见：https://github.com/Gu-J/TernaInfer。

## 英文关键词

Ternary LLM, Data Compression, GPU Acceleration

## 中文关键词

三值 LLM、数据压缩、GPU 加速
