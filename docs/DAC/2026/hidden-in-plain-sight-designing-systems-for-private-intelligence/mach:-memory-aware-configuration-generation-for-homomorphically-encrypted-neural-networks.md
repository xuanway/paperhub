MACH: Memory-Aware Configuration Generation for Homomorphically Encrypted Neural Networks
Authors：
[Honghui You](https://63dac.conference-program.com/?post_type=page&p=15&uid=9508598529533698686)，[Linjie Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=47885934638388795281)，[Yuhang Fan](https://63dac.conference-program.com/?post_type=page&p=15&uid=91381219430377791031)，[Wenzhe Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=051485579754740359)，[Tianxiang Sui](https://63dac.conference-program.com/?post_type=page&p=15&uid=14351812965477125551)，[Zhuoran Ji](https://63dac.conference-program.com/?post_type=page&p=15&uid=75996436509697727151)，[Lei Ju](https://63dac.conference-program.com/?post_type=page&p=15&uid=634143)

## 中文标题

MACH：面向同态加密神经网络的存储感知配置生成

## 英文摘要

Fully homomorphic encryption (FHE) enables direct computation on encrypted data that ensures robust privacy protection for machine learning systems. However, the substantial computational overhead of FHE necessitates efficient acceleration techniques for practical deployments. In GPU-accelerated homomorphically encrypted neural network (HENN) inference, we observe that the primary performance bottleneck shifts from computation to memory transfer due to huge memory footprints w.r.t. the limited device memory. To address this, we propose a memory-aware design framework to fully utilize GPU memory by adaptively trading computation for reduced memory footprint. Our framework introduces a static model to estimate memory footprint and latency for HENN inference. We propose an automatic design space exploration framework to generate optimal cryptographic, bootstrapping, and encoding configurations, thereby effectively minimizing execution latency with the given GPU memory capacity. Experiments with homomorphically encrypted ResNet-20 and ResNet-18 across various GPU devices show up to 4.97× speedup with a 91.88% reduction in memory footprint. It also demonstrates the first deployment of full-fledged homomorphically encrypted ResNet-20/18 at 128-bit security level on an RTX 4060 Ti GPU with 16 GB of device memory.

## 中文摘要

全同态加密（FHE）支持直接在加密数据上计算，为机器学习系统提供强健的隐私保护。然而 FHE 巨大的计算开销要求采用高效加速技术才能实际部署。在 GPU 加速的同态加密神经网络（HENN）推理中，我们观察到：由于内存占用巨大而设备内存有限，主要性能瓶颈已由计算转移至数据传输。为此，我们提出一种存储感知设计框架，通过自适应地以计算换取更小的内存占用来充分利用 GPU 内存。该框架引入静态模型以估计 HENN 推理的内存占用与延迟。我们提出自动设计空间探索框架，生成最优的密码学、自举与编码配置，从而在给定 GPU 内存容量下有效最小化执行延迟。在多种 GPU 设备上对同态加密 ResNet-20 与 ResNet-18 的实验显示，最高可达 4.97 倍加速，内存占用降低 91.88%。该工作还首次在配备 16 GB 显存的 RTX 4060 Ti GPU 上，以 128 位安全级别部署了完整的同态加密 ResNet-20/18。

## 英文关键词

Homomorphically encrypted neural network, memory management, design space exploration

## 中文关键词

同态加密神经网络、存储管理、设计空间探索
