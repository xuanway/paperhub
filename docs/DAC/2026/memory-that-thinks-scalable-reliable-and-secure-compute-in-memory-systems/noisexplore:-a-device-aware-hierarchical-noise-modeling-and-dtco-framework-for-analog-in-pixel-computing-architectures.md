Noisexplore: A Device-Aware Hierarchical Noise Modeling and DTCO Framework for Analog In-Pixel Computing Architectures
Authors：
[Jinghan Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=42380378371807697861)，[Zheng Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=8834590512747379409)，[Yi Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5235345834510493071)，[Nan Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=52695449874143816241)，[Shuhan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=86207834301799489501)，[Ligong Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=07122271305884295031)，[Xiaoyan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6439889453480536974)

## 中文标题

NoiseXplore：面向模拟像素内计算架构的器件感知分层噪声建模与 DTCO 框架

## 英文摘要

In-Pixel computing (IPC) enables energy-efficient edge AI by performing analog computation within image sensor arrays, but faces severe noise-induced accuracy degradation. Existing design flows lack comprehensive device-aware noise modeling and cross-layer optimization tools. We introduce NoiseXplore, the first end-to-end design-technology co-optimization (DTCO) framework that connects device physics, circuit and array modeling, and application-level accuracy. The framework includes: (1) physics-grounded noise models capturing both spatial variations (device mismatch) and temporal fluctuations (thermal noise, shot noise, and trap-induced random telegraph noise); (2) device-aware signal-to-noise ratio (SNR) estimation coupled with accurate neural network co-simulation to quantify algorithm sensitivity to analog non-idealities; and (3) circuit-level performance modeling (area, speed, power) for IPC arrays, seamlessly integrated into the widely-adopted NeuroSim framework. and (4) automated Bayesian DTCO that efficiently explores the multidimensional design space (device area, integration time, cell bit-width) to identify optimal operating points tailored to specific applications. We demonstrate NoiseXplore using a novel 1T FDSOI-based IPC as a challenging case study due to its extreme noise sensitivity from direct photocurrent readout. DTCO Optimized configurations achieve 50 fps throughput while maintaining 86.8% CIFAR-10 classification accuracy on a three-class subset (airplane/car/ship). NoiseXplore establishes a comprehensive methodology for noise-aware codesign of emerging IPC architectures, enabling practical deployment of analog IPC for edge AI applications.

## 中文摘要

像素内计算（IPC）通过在图像传感器阵列内部完成模拟计算，为边缘 AI 提供了高能效途径，但面临严重的噪声致精度退化问题。现有设计流程缺乏全面的器件感知噪声建模与跨层优化工具。我们提出 NoiseXplore，这是首个贯通器件物理、电路与阵列建模以及应用级精度的端到端设计—工艺协同优化（DTCO）框架。该框架包括：(1) 基于物理的噪声模型，同时刻画空间变化（器件失配）与时间涨落（热噪声、散粒噪声以及陷阱诱导的随机电报噪声）；(2) 器件感知的信噪比（SNR）估计，并结合精确的神经网络协同仿真以量化算法对模拟非理想因素的敏感度；(3) 面向 IPC 阵列的电路级性能建模（面积、速度、功耗），并实现与广泛采用的 NeuroSim 框架的无缝集成；(4) 自动化贝叶斯 DTCO，高效探索多维设计空间（器件面积、积分时间、单元位宽），以确定针对特定应用定制的最优工作点。我们以一种新型 1T FDSOI 基 IPC 作为富有挑战性的案例来展示 NoiseXplore，该结构由于直接读取光电流而对噪声极为敏感。经 DTCO 优化的配置在保持 86.8% CIFAR-10 三分类子集（飞机/汽车/船）精度的同时实现 50 fps 的吞吐率。NoiseXplore 为新兴 IPC 架构的噪声感知协同设计建立了系统化方法，使模拟 IPC 在边缘 AI 应用中得以实际部署。

## 英文关键词

In-pixel computing, noise, neural networks, DTCO

## 中文关键词

像素内计算、噪声、神经网络、DTCO
