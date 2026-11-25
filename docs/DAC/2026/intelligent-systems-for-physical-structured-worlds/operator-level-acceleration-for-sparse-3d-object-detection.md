Operator-Level Acceleration for Sparse 3D Object Detection
Authors：
[Hongjin Zhong](https://63dac.conference-program.com/?post_type=page&p=15&uid=2784873914082440793)，[Jingyu Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=8591376386612104938)，[Mingyue Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=4207571490745664305)，[Shuai Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=42340509402294579501)，[Yuanhai Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=43115204365826298971)，[Kai Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=586143)

## 中文标题

面向稀疏 3D 目标检测的算子级加速

## 英文摘要

3D object detection is critical for robotics and autonomous driving, yet inference latency remains a bottleneck for efficient deployment on resource-constrained platforms. Existing acceleration strategies for sparse 3D detectors fail to fully exploit the intrinsic sparsity of voxels. To address this challenge, we propose a systematic operator-level acceleration pattern that exploits structural properties of sparse voxels through three synergistic techniques: (1) cache-aware attention fusion that redesigns slot-based aggregation via tiled tensor decomposition, achieving 10.0–33.5× speedup on RTX 4090 GPU and 21.5–50.8× speedup on A100 GPU while enabling previously infeasible high-dimensional attention heads (𝑑=512−1024); (2) sparsity-driven convolution approximation that leverages attention-induced feature redundancy to replace 3D axial convolutions with lightweight 1D channel operations, delivering 1.4–2.1× acceleration with negligible accuracy loss (<4% mAP); and (3) structure-aware precision reduction employing profiling-guided mixed-precision assignment that selectively applies FP16 to high-cost operators with high tolerance to precision loss, while preserving FP32 for others, achieving 1.93–2.19× speedup. All optimizations preserve network architecture and require no retraining. Experimental results show that our method achieves a 2.1–2.5× end-to-end speedup over state-of-the-art baselines while maintaining accuracy within 4% mAP and 2.5% NDS, establishing a novel pattern for efficient sparse 3D perception.

## 中文摘要

3D 目标检测对机器人与自动驾驶至关重要，然而推理时延仍是其在资源受限平台上高效部署的瓶颈。现有面向稀疏 3D 检测器的加速策略未能充分利用体素固有的稀疏性。为应对这一挑战，我们提出一套系统化的算子级加速方案，借助三项协同技术挖掘稀疏体素的结构特性：(1) 缓存感知的注意力融合，通过分块张量分解重新设计基于 slot 的聚合，在 RTX 4090 GPU 上取得 10.0–33.5× 加速、在 A100 GPU 上取得 21.5–50.8× 加速，同时使此前无法实现的高维注意力头（d=512–1024）成为可能；(2) 稀疏驱动的卷积近似，利用注意力引起的特征冗余，以轻量级 1D 通道操作替代 3D 轴向卷积，在精度损失可忽略（<4% mAP）的情况下带来 1.4–2.1× 加速；(3) 结构感知的精度降低，采用由性能分析引导的混合精度分配，对高开销且对精度损失容忍度高的算子有选择地使用 FP16，其余算子保留 FP32，从而取得 1.93–2.19× 加速。所有优化均保持网络架构不变且无需重新训练。实验结果表明，我们的方法相比最先进基线取得 2.1–2.5× 的端到端加速，同时精度保持在 4% mAP 与 2.5% NDS 的偏差范围内，为高效稀疏 3D 感知建立了新范式。
