# TensorBridge: Bridging Microscaled FP4 Weights to FP8 Tensor Cores for LLM Serving

**中文标题**：TensorBridge：为 LLM 服务将微缩放 FP4 权重桥接至 FP8 Tensor Core

**所属 Session**：[Session 26: LLM Inference III](index.md) · [ATC 2026](../index.md)

**作者**：Jiaxiang Zou (The Hong Kong University of Science and Technology (Guangzhou)), Yonghao Chen (The Hong Kong University of Science and Technology (Guangzhou)), Rui Meng (The Hong Kong University of Science and Technology (Guangzhou)), Ruilong WU (The Hong Kong University of Science and Technology (Guangzhou)), Xinyu Chen (The Hong Kong University of Science and Technology (Guangzhou))

## 英文摘要
Low-bit LLM serving increasingly targets W4A8 execution, where 4-bit weights reduce memory traffic while 8-bit activations retain a high-throughput Tensor Core path. NVFP4 is an attractive checkpoint format for this regime because its E2M1 payloads and group-16 E4M3 scales preserve accuracy better than coarse integer W4 formats. However, deployed GPUs without native NVFP4 Tensor Core support cannot execute these checkpoints as stored. Keeping these checkpoints on such GPUs falls back to A16 execution and misses the FP8 Tensor Core path. Converting them offline to FP8 or integer W4A8 recovers that path, but either doubles weight traffic or gives up NVFP4’s accuracy advantage. This paper presents TensorBridge, a software-defined NVFP4A8 execution path for native NVFP4 checkpoints on Hopper GPUs. TensorBridge treats NVFP4-to-FP8 translation as register-level WGMMA operand construction rather than checkpoint conversion or expanded-weight materialization. Because Hopper’s CUDA cores lack FP8 multipliers, it exploits floating-point multiplication approximation (FPMA) to turn E2M1-by-E4M3 scaling into CUDA-core integer shift-and-add operations. These CUDA-core operations construct FP8-compatible operands directly in registers, so Tensor Cores stay dedicated to FP8 WGMMA. TensorBridge reaches 71.98% average zero-shot accuracy, only 0.28 points below BF16 and 0.59 points above W4A8. It outperforms vLLM CUTLASS W4A8 by 1.15× and NVFP4A16 Marlin by 2.62× geometric mean. TensorBridge is open-sourced at https://github.com/CLab-HKUST-GZ/atc26-tensorbridge.

## 中文摘要
低位 LLM 服务日益以 W4A8 执行为目标，其中 4 位权重减少内存流量，而 8 位激活保留高吞吐的 Tensor Core 路径。NVFP4 是这一场景下颇具吸引力的检查点格式，因为其 E2M1 载荷和组 16 的 E4M3 缩放相比粗粒度整数 W4 格式能更好地保持精度。然而，不支持原生 NVFP4 Tensor Core 的已部署 GPU 无法按存储原样执行这些检查点。在此类 GPU 上保留这些检查点会退回到 A16 执行，从而错失 FP8 Tensor Core 路径。离线将其转换为 FP8 或整数 W4A8 可恢复该路径，但要么使权重流量翻倍，要么放弃 NVFP4 的精度优势。本文提出 TensorBridge，一种在 Hopper GPU 上针对原生 NVFP4 检查点的软件定义 NVFP4A8 执行路径。TensorBridge 将 NVFP4 到 FP8 的转换视为寄存器级的 WGMMA 操作数构造，而非检查点转换或展开权重的物化。由于 Hopper 的 CUDA core 缺少 FP8 乘法器，它利用浮点乘法近似（FPMA）将 E2M1 乘以 E4M3 的缩放转换为 CUDA core 的整数移位相加操作。这些 CUDA core 操作直接在寄存器中构造 FP8 兼容的操作数，从而使 Tensor Core 始终专用于 FP8 WGMMA。TensorBridge 达到 71.98% 的平均零样本精度，仅比 BF16 低 0.28 个百分点，比 W4A8 高 0.59 个百分点。它相比 vLLM CUTLASS W4A8 高出 1.15×，相比 NVFP4A16 Marlin 的几何平均高出 2.62×。TensorBridge 已在 https://github.com/CLab-HKUST-GZ/atc26-tensorbridge 开源。

## 英文关键词
Large Language Model, Quantization, NVFP4, FP8, GEMM, GPU Kernel

## 中文关键词
大语言模型，量化，NVFP4，FP8，GEMM，GPU Kernel

## 代码与研究制品

- [code](https://github.com/CLab-HKUST-GZ/atc26-tensorbridge)

[返回 Session 26](index.md) · [返回 ATC 2026](../index.md)
