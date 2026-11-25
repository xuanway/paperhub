Excavating Consistency Across Editing Steps for Effective Multi-Step Image Editing
Authors：
[Chunyu Qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=7888426696204542069)，[Zhuoran Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=92792859262361042411)，[Cheng Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03164341137605558081)，[Zhihui Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=80645102325359974801)，[Jianglong Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=86357331869719719021)，[Jun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=690984560257183931)，[Xiaoyao Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=743443)，[Haibing Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=828243)

## 中文标题

挖掘跨编辑步骤的一致性以实现有效的多步图像编辑

## 英文摘要

Multi-step image editing with diffusion models typically requires repeatedly executing the inversion–denoising paradigm, which leads to severe challenges in both image quality and computational efficiency. Repeated inversion introduces errors that accumulate across editing steps, degrading image quality, while regeneration of unchanged background regions incurs substantial computational overhead. In this paper, we present ExCave, a training-free multi-step editing framework that improves both image quality and computational efficiency by excavating consistency across editing steps. ExCave introduces an inversion sharing mechanism that performs inversion once and reuses its consistent features across subsequent edits, thereby significantly reducing errors. To eliminate redundant computation, we propose the CacheDiff method that regenerates only the edited regions while reusing consistent features from unchanged background regions. Finally, we design GPU-oriented optimizations to translate theoretical gains into practical reductions in end-to-end latency. Extensive experiments demonstrate that ExCave achieves superior image quality and dramatically reduces inference latency, establishing a new paradigm for accurate and efficient multi-step editing. The source code is available at https://github.com/ACA-Lab/ExCave.

## 中文摘要

基于扩散模型的多步图像编辑通常需要反复执行“反演—去噪”范式，这在图像质量与计算效率两方面都带来严峻挑战。反复反演会引入误差并在各编辑步骤间累积，从而使图像质量下降；而重新生成未发生变化的背景区域则带来可观的计算开销。本文提出 ExCave，一个免训练的多步编辑框架，通过挖掘跨编辑步骤的一致性来同时提升图像质量与计算效率。ExCave 引入反演共享机制，仅执行一次反演并在后续编辑中复用其一致性特征，从而显著减少误差。为消除冗余计算，我们提出 CacheDiff 方法，仅重新生成被编辑的区域，同时复用未变化背景区域的一致性特征。最后，我们设计了面向 GPU 的优化，将理论收益转化为端到端时延的实际降低。大量实验表明，ExCave 取得了更优的图像质量并大幅降低推理时延，为精确而高效的多步编辑确立了新范式。源代码见 https://github.com/ACA-Lab/ExCave 。
