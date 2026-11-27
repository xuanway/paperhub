Relay-GS: Reusing Temporal Sort Information for 4D Gaussian Splatting Acceleration
Authors：
[Yeonggeon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=07235736733543747421)，[Seongmin Ki](https://63dac.conference-program.com/?post_type=page&p=15&uid=63863936810015365211)，[Sangkyu Jeon](https://63dac.conference-program.com/?post_type=page&p=15&uid=18298707481132834941)，[Sungju Ryu](https://63dac.conference-program.com/?post_type=page&p=15&uid=46756987224121538951)

## 中文标题

Relay-GS：复用时间排序信息加速 4D 高斯泼溅

## 英文摘要

This paper presents Relay-GS, an algorithm-hardware co-design that accelerates 4D Gaussian splatting (4DGS) rendering. Conventional methods process each frame independently and repeatedly execute the heavy sorting stage. This results in performance bottlenecks during real-time rendering. To mitigate this inefficiency, our approach introduces optimizations at both algorithmic and architectural levels. At the algorithmic level, we propose selective Gaussian sorting (SGS), which reuses the sorted results of previous frames, and periodic correction to maintain rendering quality. At the architectural level, we design a fine-grained pipeline to hide sorting latency and a parallel rasterization unit that reduces operations through parameter sharing. Our experimental results show that the proposed accelerator achieves a speedup of 1.55× to 1.64× and up to 16.5% in energy savings over a baseline design, while maintaining a rendering quality with negligible degradation compared to that of full sorting.

## 中文摘要

本文提出了 Relay-GS，一种加速 4D 高斯泼溅（4DGS）渲染的算法-硬件协同设计。传统方法独立处理每一帧，并重复执行繁重的排序阶段，导致实时渲染中的性能瓶颈。为缓解这一低效问题，我们在算法和架构两个层面引入优化。在算法层面，我们提出选择性高斯排序（SGS），复用前若干帧的排序结果，并通过周期性校正保持渲染质量。在架构层面，我们设计细粒度流水线以隐藏排序延迟，并设计通过参数共享减少运算的并行光栅化单元。实验结果表明，与基线设计相比，所提出的加速器实现了 1.55 倍至 1.64 倍的加速以及最高 16.5% 的能耗节省，同时与完整排序相比保持渲染质量无明显下降。

## 英文关键词

4D Gaussian Splatting, software-hardware co-design, hardware accelerator, real-time rendering, temporal coherence

## 中文关键词

4D 高斯泼溅、软硬件协同设计、硬件加速器、实时渲染、时间一致性
