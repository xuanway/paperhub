PREBA: A Hardware/software Co-Design for Multi-Instance GPU Based AI Inference Servers
Authors：
[jiin Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=4903577509198455688)，[Gwangoo Yeo](https://63dac.conference-program.com/?post_type=page&p=15&uid=4151811921024289885)，[Yujeong Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=90357862798610116711)，[Minsoo Rhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=642143)

## 中文标题

PREBA：面向基于多实例 GPU 的 AI 推理服务器的软硬件协同设计

## 英文摘要

NVIDIA’s Multi-Instance GPU (MIG) technology, which enables reconfiguration of large GPUs into smaller, independent slices, is a promising feature for high-performance AI inference servers. Our characterization reveals that the data preprocessing stage of AI inference causes a significant performance bottleneck in these MIG-based inference systems. We present PREBA, a hardware/software co-design targeting MIG inference servers. PREBA offloads data preprocessing to a latency-optimized, FPGA-based accelerator. Simultaneously, PREBA’s analytical model-based dynamic batching system maximizes small vGPU utilization by creating optimal, input-aware batches. PREBA provides 3.7× improvement in throughput, 3.5× energy-efficiency, and 3.0× cost-efficiency over a baseline that uses CPU-based preprocessing.

## 中文摘要

NVIDIA 的多实例 GPU（MIG）技术可将大型 GPU 重构为多个更小且相互独立的切片，是高性能 AI 推理服务器中一项颇具前景的特性。我们的表征分析表明，AI 推理的数据预处理阶段在这类基于 MIG 的推理系统中造成了显著的性能瓶颈。本文提出 PREBA，一种面向 MIG 推理服务器的软硬件协同设计。PREBA 将数据预处理卸载至经过延迟优化的、基于 FPGA 的加速器；同时，PREBA 基于解析模型的动态批处理系统通过构造最优的输入感知批次，最大化小型 vGPU 的利用率。相较采用 CPU 预处理的基线，PREBA 在吞吐率上提升 3.7×，能效提升 3.5×，成本效率提升 3.0×。
