Actionflow: A Pipelined Action Acceleration for Vision Language Models on Edge
Authors：
[Yuntao Dai](https://63dac.conference-program.com/?post_type=page&p=15&uid=6429659035042306027)，[Hang Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=62917990745741357271)，[teng wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=652843)，[Qianyu Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=452843)，[Yifei Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=00544405713481265281)，[zhiyong qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0699576879261099567)，[Lei Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=852843)，[Wenqi Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=425843)，[Xuehai Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=513843)

## 中文标题

ActionFlow：面向边缘视觉语言模型的动作流水化加速

## 英文摘要

Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hindered by high inference latency. While smooth robotic interaction requires control frequencies of 20–30 Hz, current VLA models typically operate at only 3–5 Hz on edge devices due to the memory-bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge platforms. At the core of ActionFlow is a Cross-Request Pipelining strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross-Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55× improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dynamic manipulation on edge hardware. Our work is available at https://github.com/Frankd35/Action-Flow.

## 中文摘要

视觉—语言—动作（VLA）模型已成为机器人感知与控制的统一范式，可实现涌现式泛化与长时程任务执行。然而，其在高动态真实环境中的部署受到高推理延迟的严重制约。流畅的机器人交互需要 20–30 Hz 的控制频率，而当前 VLA 模型在边缘设备上通常仅以 3–5 Hz 运行，原因在于自回归解码受内存带宽限制。现有优化往往需要大量重训练或损害模型精度。为弥合这一差距，我们提出 ActionFlow，一种面向资源受限边缘平台的系统级推理框架。ActionFlow 的核心是跨请求流水（Cross-Request Pipelining）策略，这一新型调度器将 VLA 推理重构为微请求构成的宏流水线。该策略跨连续时间步智能地将受内存限制的 Decode 阶段与受计算限制的 Prefill 阶段合并批处理，从而最大化硬件利用率。此外，为支撑该调度，我们提出跨请求状态打包前向算子与统一 KV 环形缓冲区，将碎片化的内存操作融合为高效的稠密计算。实验结果表明，ActionFlow 在无需重训练的情况下使 OpenVLA-7B 模型的 FPS 提升 2.55×，从而在边缘硬件上实现实时动态操作。我们的工作见 https://github.com/Frankd35/Action-Flow。

## 英文关键词

VLA, Acceleration, Embodied Robot

## 中文关键词

VLA、加速、具身机器人
