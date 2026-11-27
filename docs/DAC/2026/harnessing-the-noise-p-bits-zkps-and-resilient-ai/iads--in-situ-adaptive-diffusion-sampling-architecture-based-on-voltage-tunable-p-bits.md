iADS: In-Situ Adaptive Diffusion Sampling Architecture Based on Voltage-Tunable P-Bits
Authors：
[Chenhao Xia](https://63dac.conference-program.com/?post_type=page&p=15&uid=11966202281334648401)，[Haoxuan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=82838057655709351021)，[Weican Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=19647264217862366651)，[Hongjie Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=7655497578774455827)，[Guanwen Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=11207522113023810851)，[Yuxiang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1943053426314916095)，[Yunyi Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=99290589600619141951)，[Fei Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1787093800742696996)

## 中文标题

iADS：基于电压可调 p-bit 的原位自适应扩散采样架构

## 英文摘要

Diffusion models (DMs) have emerged as a revolutionary technology in AI generation. But the sequential iterations and noise generation would limit DM speed and energy efficiency. Probabilistic computing, which can map probabilistic modulation onto intrinsic hardware structures, is poised to overcome this bottleneck. This work proposed an optimized self-compensating p-bit unit and constructed an in-situ adaptive diffusion sampling (iADS) architecture. To the best of our knowledge, this is the first time to achieve in-situ Gaussian noise generation and scaling in hardware. An iADS circuit composed of 256 p-bit units was fabricated and successfully generated MNIST images in experiments. Furthermore, a hardware-calibrated 1,048,576 p-bit iADS architecture, has achieved training and image generation for CIFAR10 (FID=9.96) and CelebA-HQ, by combining hardware adaptive scaling and hybrid frequency-pixel loss mechanism. While maintaining generation quality comparable to software-only DMs, this approach achieves an approximately 8× reduction in energy consumption and a roughly 143× reduction in area relative to conventional PRNG architectures, underscoring its potential for highly efficient acceleration of DMs.

## 中文摘要

扩散模型（DM）已成为 AI 生成领域的一项革命性技术。但顺序迭代与噪声生成会限制 DM 的速度与能效。概率计算能够将概率调制映射到内在的硬件结构上，有望突破这一瓶颈。本工作提出一种优化的自补偿 p-bit 单元，并构建了原位自适应扩散采样（iADS）架构。据我们所知，这是首次在硬件中实现原位高斯噪声生成与缩放。我们制备了由 256 个 p-bit 单元组成的 iADS 电路，并在实验中成功生成 MNIST 图像。进一步地，我们结合硬件自适应缩放与混合频率-像素损失机制，构建了经硬件校准的 1,048,576 p-bit iADS 架构，实现了 CIFAR10（FID=9.96）与 CelebA-HQ 的训练与图像生成。在保持与纯软件 DM 相当的生成质量的同时，该方法相对传统 PRNG 架构将能耗降低约 8 倍、面积减少约 143 倍，凸显了其高效加速 DM 的潜力。

## 英文关键词

Diffusion model, Emerging architecture, Adaptive diffusion sampling, Probabilistic computing

## 中文关键词

扩散模型、新兴架构、自适应扩散采样、概率计算
