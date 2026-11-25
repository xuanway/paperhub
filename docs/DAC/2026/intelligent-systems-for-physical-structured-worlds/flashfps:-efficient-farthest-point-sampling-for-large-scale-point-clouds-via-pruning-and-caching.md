Flashfps: Efficient Farthest Point Sampling for Large-Scale Point Clouds via Pruning and Caching
Authors：
[Yuzhe Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=75966342702164807181)，[Hancheng Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=56847798060361943901)，[Cong Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=824843)，[Junyao Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7844080596441581494)，[Qinsi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=073371386275148005)，[Yueqian Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=36515793019161956461)，[Changchun Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=2142464156335276396)，[Hai (Helen) Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=631143)，[Yiran Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=712143)

## 中文标题

FlashFPS：通过剪枝与缓存实现大规模点云的高效最远点采样

## 英文摘要

Point-based Neural Networks (PNNs) have become a key approach for point cloud processing. However, a core operation in these models, Farthest Point Sampling (FPS), often introduces significant inference latency, especially for large-scale processing. Despite existing CUDA-and hardware-level optimizations, FPS remains a major bottleneck due to exhaustive computations across multiple network layers in PNNs, which hinders scalability. Through systematic analysis, we identify three substantial redundancies in FPS, including unnecessary full-cloud computations, redundant late-stage iterations, and predictable inter-layer outputs that make later FPS computations avoidable. To address these, we propose FlashFPS, a hardware-agnostic, plug-and-play framework for FPS acceleration, composed of FPS-Prune and FPS-Cache. FPS-Prune introduces candidate pruning and iteration pruning to reduce redundant computations in FPS while preserving sampling quality, and FPS-Cache eliminates layer-wise redundancy via cache-and-reuse. Integrated into existing CUDA libraries and state-of-the-art PNN accelerators, FlashFPS achieves 5.16× speedup over the standard CUDA baseline on GPU and 2.69× on PNN accelerators, with negligible accuracy loss, enabling efficient and scalable PNN inference. Codes are released at https://github.com/Yuzhe-Fu/FlashFPS.

## 中文摘要

基于点的神经网络（PNN）已成为点云处理的关键途径。然而，此类模型中的一项核心操作——最远点采样（FPS）——往往带来显著的推理时延，在大规模处理场景中尤为突出。尽管已有 CUDA 层面与硬件层面的优化，由于在 PNN 中跨多个网络层进行穷举式计算，FPS 仍是主要瓶颈，制约了可扩展性。通过系统分析，我们识别出 FPS 中的三类显著冗余，包括不必要的全点云计算、后期迭代中的冗余，以及可预测的层间输出——后者使后续的 FPS 计算可以被规避。针对这些问题，我们提出 FlashFPS，一个硬件无关、即插即用的 FPS 加速框架，由 FPS-Prune 与 FPS-Cache 组成。FPS-Prune 引入候选剪枝与迭代剪枝，在保持采样质量的同时减少 FPS 中的冗余计算；FPS-Cache 则通过缓存与复用消除逐层冗余。将 FlashFPS 集成到现有 CUDA 库与最先进的 PNN 加速器中，可在 GPU 上相比标准 CUDA 基线取得 5.16× 加速，在 PNN 加速器上取得 2.69× 加速，且精度损失可忽略，从而实现了高效、可扩展的 PNN 推理。代码见 https://github.com/Yuzhe-Fu/FlashFPS 。
