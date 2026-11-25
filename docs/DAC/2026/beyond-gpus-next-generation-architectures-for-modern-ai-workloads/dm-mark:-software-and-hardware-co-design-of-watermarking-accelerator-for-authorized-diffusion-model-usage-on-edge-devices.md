DM-MARK: Software and Hardware Co-Design of Watermarking Accelerator for Authorized Diffusion Model Usage on Edge Devices
Authors：
[Shiyu Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=15705776153369400251)，[Jie Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=971543)

## 中文标题

DM-MARK：面向边缘设备上扩散模型授权使用的软硬件协同设计水印加速器

## 英文摘要

With the rapid growths of generative models like diffusion models (DMs), distinguishing authentic images from forfeited ones has become increasingly challenging, raising privacy, security, and ethical concerns. Watermarking offers an effective solution for authentication and traceability of generated images. Unlike traditional methods, emerging watermarking techniques for DMs enable marking AI-generated content with resilience to commonly used watermark weakening or erasing techniques. However, these methods demand high computational resource and latency, posing challenges for practical use, especially on edge devices. This work presents DM-MARK, a software-hardware co-optimized diffusion framework supporting efficient watermark generation and reverse detection. DM-MARK is implemented in 12nm FinFET technology, achieving robust watermarking with improved quality and reduced overhead. Evaluations show 11.33% higher detection accuracy, 18× latency speedup over GPU, 3.1× on-chip memory savings, an average of 4.56× EMA reduction. It also achieves 212.5× speedup over the baseline ASIC design with negligible accuracy loss. The proposed DM-MARK scheme offers a scalable and practical solution for protecting AI-generated content in real-time on edge devices.

## 中文摘要

随着扩散模型（DM）等生成模型的快速增长，区分真实图像与被篡改图像变得日益困难，引发了隐私、安全与伦理方面的担忧。水印为生成图像的认证与溯源提供了有效手段。与传统方法不同，面向 DM 的新兴水印技术能够对 AI 生成内容进行标记，并对常用的水印削弱或擦除技术具有鲁棒性。然而，这些方法需要大量计算资源和时延，给实际应用带来挑战，在边缘设备上尤为如此。本工作提出 DM-MARK，一个软硬件协同优化的扩散框架，支持高效的水印生成与反向检测。DM-MARK 采用 12nm FinFET 工艺实现，在提升质量、降低开销的同时实现鲁棒水印。评估显示，其检测精度提升 11.33%，相较 GPU 的时延加速 18 倍，片上存储节省 3.1 倍，EMA 平均降低 4.56 倍。它相较基线 ASIC 设计还实现 212.5 倍加速，且精度损失可忽略。所提出的 DM-MARK 方案为在边缘设备上实时保护 AI 生成内容提供了可扩展且实用的解决方案。
