Highly-Parallel Atom-Detection Accelerator for Tweezer-Based Neutral Atom Quantum Computers
Authors：
[Jonas Winklmann](https://63dac.conference-program.com/?post_type=page&p=15&uid=6299174815506318331)，[Yian Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=41133757151360509311)，[Xiaorang Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=8429657569029138024)，[Korbinian Staudacher](https://63dac.conference-program.com/?post_type=page&p=15&uid=3292770038968598354)，[Martin Schulz](https://63dac.conference-program.com/?post_type=page&p=15&uid=1783746425991348106)

## 中文标题

面向基于光镊的中性原子量子计算机的高并行原子检测加速器

## 英文摘要

Neutral atom quantum computers (NAQCs) are among the most promising computational platforms for quantum computing. Controlling and measuring individual atoms and their states, which often requires multiple imaging and image-analysis procedures, is typically the most time-consuming task during computation and contributes significantly to overall cycle times. To resolve this challenge, we propose a highly-parallel atom-detection accelerator for tweezer-based NAQCs. Our design builds on an existing state-reconstruction method and combines an algorithm-level optimization with a Field Programmable Gate Array (FPGA) implementation to maximize parallelism and reduce the run time of the image-analysis process. We identify and overcome several challenges for an FPGA implementation, such as introducing a prefetching mechanism to improve scalability and customizing bus transfers to support large bandwidths. Tested on a Xilinx UltraScale+ FPGA, our design can analyze a 256×256-pixel fluorescence image in just 115 𝜇𝑠, achieving 34.9× and 6.3× speedups over the original and optimized CPU baseline, respectively. Moreover, our accelerator can maintain consistent resource utilization across various atom array sizes, contributing to the ongoing efforts toward scalable and fully integrated FPGA-based control systems for NAQCs.

## 中文摘要

中性原子量子计算机（NAQC）是量子计算最具前景的计算平台之一。对单个原子及其状态的控制与测量通常需要多次成像与图像分析流程，这往往是计算过程中最耗时的任务，并显著影响整体周期时间。为应对这一挑战，我们提出一种面向基于光镊的 NAQC 的高并行原子检测加速器。我们的设计建立在已有的状态重建方法之上，将算法级优化与现场可编程门阵列（FPGA）实现相结合，以最大化并行度并缩短图像分析流程的运行时间。我们识别并克服了 FPGA 实现中的若干挑战，例如引入预取机制以提升可扩展性、定制总线传输以支持大带宽。在 Xilinx UltraScale+ FPGA 上测试时，我们的设计可在仅 115 μs 内分析一幅 256×256 像素的荧光图像，相较原始 CPU 基线与优化后的 CPU 基线分别实现 34.9 倍与 6.3 倍加速。此外，我们的加速器在不同原子阵列规模下能够保持一致的资源利用率，有助于推动面向 NAQC 的可扩展、全集成 FPGA 控制系统的持续发展。

## 英文关键词

Quantum Computing, Neutral Atoms, Atom Detection, Image Reconstruction, FPGA

## 中文关键词

量子计算、中性原子、原子检测、图像重建、FPGA
