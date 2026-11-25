Hardware-Aware Neural Architecture Search for Real-Time BEV-Based 3D Object Detection
Authors：
[Jisup Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=4963233050267324627)，[Soonhoi Ha](https://63dac.conference-program.com/?post_type=page&p=15&uid=574343)，[Jeongwon Her](https://63dac.conference-program.com/?post_type=page&p=15&uid=8589459184401361772)

## 中文标题

面向实时 BEV 3D 目标检测的硬件感知神经架构搜索

## 英文摘要

Bird’s-eye-view (BEV) fusion of multi-modal sensor data is a leading approach for high-performance 3D object detection. However, state-of-the-art models rarely exceed 10 FPS even on powerful GPUs, limiting their use in real-time applications. In this paper, we present a neural architecture search (NAS) framework that identifies models achieving both high accuracy and real-time inference. The search space is explicitly designed with hardware constraints to balance accuracy and computational efficiency on resource-limited platforms. To better align LiDAR and camera features in the BEV conversion module, we introduce a lightweight depth estimation network and a LiDAR–camera cross-attention mechanism that enhances detection accuracy with minimal overhead. On the challenging nuScenes benchmark, our model achieves 70.1% mAP, which represents a 2.3% point improvement over the baseline model, while running at 35.6 FPS on the NVIDIA Jetson AGX Orin, demonstrating its suitability for real-time autonomous driving.

## 中文摘要

多模态传感器数据的鸟瞰图（BEV）融合是实现高性能 3D 目标检测的领先方法。然而，最先进的模型即使在强大的 GPU 上也很难超过 10 FPS，限制了其在实时应用中的使用。本文提出一个神经架构搜索（NAS）框架，用于识别同时实现高精度与实时推理的模型。搜索空间在设计时显式考虑硬件约束，以在资源受限平台上平衡精度与计算效率。为在 BEV 转换模块中更好地对齐 LiDAR 与相机特征，我们引入轻量级深度估计网络以及 LiDAR-相机交叉注意力机制，以极小开销提升检测精度。在具有挑战性的 nuScenes 基准上，我们的模型达到 70.1% mAP，相比基线模型提升 2.3 个百分点，同时在 NVIDIA Jetson AGX Orin 上以 35.6 FPS 运行，展示了其用于实时自动驾驶的适用性。
