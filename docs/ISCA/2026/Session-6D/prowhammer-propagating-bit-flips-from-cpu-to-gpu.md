---
title: "PRowhammer: Propagating Bit-flips from CPU to GPU"
description: "ISCA 2026 · Session 6D · PRowhammer: Propagating Bit-flips from CPU to GPU"
tags:
  - "ISCA2026"
  - "Session 6D"
  - "Rowhammer and Security"
---

# PRowhammer: Propagating Bit-flips from CPU to GPU

**中文标题：** PRowhammer: 将位翻转从 CPU 传播至 GPU

**所属 Session：** [Session 6D](index.md) · [ISCA 2026](../index.md)

**作者：** Mrityunjay Shukla, Shubham Roy, Sayandeep Saha, Biswabandan Panda

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The Rowhammer attack is an exploit that induces bit-flips in DRAMs. In the last decade, Rowhammer has been demonstrated on DDRs and LPDDRs used by CPUs, and recently it has been demonstrated on GDDRs used by GPUs. In a heterogeneous system with CPUs and GPUs, GPUs are dependent on the hDRAM (host’s DRAM, i.e., CPU’s DRAM) as all the data and the code executed on the GPU are first loaded into the hDRAM. We exploit the dependency of GPUs on hDRAM to develop a novel attack called Propagated Rowhammer (PRowhammer), which utilizes CPU-based Rowhammer bit-flips in hDRAM to corrupt GPU code before execution, thereby propagating the bit-flips to the GPU. We exploit two key observations that are, OS page deduplication of GPU shared libraries in hDRAM and inducing bit-flips transform GPU instructions into semantically altered yet valid instructions. Despite challenges such as the massive size of GPU shared libraries (hundreds of megabytes), the closed-source nature of the code, and the use of a proprietary compression algorithm for the SASS (GPU assembly) code, we develop automated techniques to identify exploitable bit-flip locations in hDRAM. We demonstrate PRowhammer on hDRAMs, such as DDRs (DDR3 and DDR4), with NVIDIA’s discrete GPUs that utilize the CUDA software stack. We demonstrate the effectiveness of PRowhammer against state-of-the-art machine learning (ML) models in realistic black-box settings, where the adversary operates on a CPU and lacks access to the ML model’s weights and architecture. With PRowhammer, a single bit-flip in the well-known shared library cuBLASLt degrades image classification accuracy across 16 test cases (ResNet-18, ResNet-34, ResNet-50 and VGG-16 on MNIST, FMNIST, CIFAR-10, and ImageNet) to random guessing, and in the worst-case scenario, it drops to 0%. We also demonstrate the effectiveness of PRowhammer on Large Language Models (LLMs) such as Llama-2, Mistral, and Falcon, where a single bit-flip in the GGML library reduces the generation quality, resulting in a BERTScore of 25%, which produces gibberish output. Overall, PRowhammer exposes an entirely new class of GPU vulnerabilities stemming from CPU-GPU architectural coupling, demanding holistic security approaches for heterogeneous computing systems.

## 中文摘要

Rowhammer 攻击是一种在 DRAM 中诱发位翻转的漏洞利用。过去十年中，Rowhammer 已在 CPU 使用的 DDR 和 LPDDR 上得到演示，最近又在 GPU 使用的 GDDR 上得到演示。在包含 CPU 与 GPU 的异构系统中，GPU 依赖于 hDRAM（主机 DRAM，即 CPU 的 DRAM），因为 GPU 上执行的所有数据和代码都首先加载到 hDRAM 中。我们利用 GPU 对 hDRAM 的依赖性，开发了一种名为传播式 Rowhammer（PRowhammer）的新型攻击，它利用 hDRAM 中基于 CPU 的 Rowhammer 位翻转在执行前破坏 GPU 代码，从而将位翻转传播到 GPU。我们利用了两个关键观察：hDRAM 中 GPU 共享库的 OS 页去重，以及诱发的位翻转会将 GPU 指令转换为语义改变但仍然有效的指令。尽管存在 GPU 共享库规模巨大（数百兆字节）、代码闭源以及对 SASS（GPU 汇编）代码使用专有压缩算法等挑战，我们开发了自动化技术来识别 hDRAM 中可利用的位翻转位置。我们在 DDR（DDR3 和 DDR4）等 hDRAM 上，针对使用 CUDA 软件栈的 NVIDIA 独立 GPU 演示了 PRowhammer。我们在真实的黑盒设置中展示了 PRowhammer 对最先进机器学习（ML）模型的有效性，其中攻击者在 CPU 上运行且无法访问 ML 模型的权重和架构。借助 PRowhammer，知名共享库 cuBLASLt 中的单个位翻转即可使 16 个测试用例（ResNet-18、ResNet-34、ResNet-50 和 VGG-16 在 MNIST、FMNIST、CIFAR-10 和 ImageNet 上）的图像分类精度降至随机猜测水平，最坏情况下降至 0%。我们还展示了 PRowhammer 对 Llama-2、Mistral 和 Falcon 等大语言模型（LLM）的有效性，其中 GGML 库中的单个位翻转会降低生成质量，导致 BERTScore 为 25%，产生乱码输出。总体而言，PRowhammer 揭示了一类源自 CPU-GPU 架构耦合的全新 GPU 漏洞，要求对异构计算系统采取整体性安全方法。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6D](index.md) · [返回 ISCA 2026](../index.md)
