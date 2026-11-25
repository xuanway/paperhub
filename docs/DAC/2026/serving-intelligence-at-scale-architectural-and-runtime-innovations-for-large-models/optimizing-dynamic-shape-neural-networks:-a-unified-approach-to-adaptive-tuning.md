Optimizing Dynamic-Shape Neural Networks: A Unified Approach to Adaptive Tuning
Authors：
[Zheng Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4127877253901159648)，[Donglin Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2880474523319576932)，[Xiaobo Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=34913606060183303221)，[Yili Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=44569009036476478871)，[Dazhao Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=25421689254305110821)

## 中文标题

优化动态形状神经网络：自适应调优的统一方法

## 英文摘要

Dynamic-shape neural networks are increasingly adopted in fields such as natural language processing and computer vision, where they effectively handle inputs with variable-length texts and dynamic-resolution images. Enhancing execution speed is crucial for saving time and reducing costs. However, dynamic shape neural networks pose significant optimization challenges, as hand-tuned libraries lack the flexibility to accommodate a wide range of dynamic shapes, and statically compiled kernels incur high computational overhead due to repeated kernel compilation. To address these issues, we propose DyTuner, an adaptive operator-level tuning framework for dynamic-shape neural networks. DyTuner uses a unified, system-compatible interface and an adaptive algorithm to efficiently tune kernels for varying shapes, significantly improving end-to-end performance and reducing redundant compilations. DyTuner is implemented based on the PyTorch framework and evaluated with seven popular dynamic-shape neural networks. Experimental results demonstrate that DyTuner effectively optimizes dynamic-shape workloads, achieving speedups of up to 1.41× and 1.64× over state-of-the-art solutions, BladeDISC and TorchInductor, respectively.

## 中文摘要

动态形状神经网络正日益被自然语言处理与计算机视觉等领域采用，可有效处理变长文本和动态分辨率图像等输入。提升执行速度对于节省时间和降低成本至关重要。然而，动态形状神经网络带来显著的优化挑战：手工调优的算子库缺乏应对大量动态形状的灵活性，而静态编译的内核因反复编译而带来高昂的计算开销。为解决这些问题，我们提出 DyTuner，一个面向动态形状神经网络的自适应算子级调优框架。DyTuner 采用统一的、与系统兼容的接口和自适应算法，为不同形状高效地调优内核，显著提升端到端性能并减少冗余编译。DyTuner 基于 PyTorch 框架实现，并在七个流行的动态形状神经网络上进行评估。实验结果表明，DyTuner 可有效优化动态形状工作负载，相较最先进方案 BladeDISC 和 TorchInductor 分别实现最高 1.41 倍和 1.64 倍的加速。

## 英文关键词

Dynamic-Shape Neural Networks, Bayesian Optimization, Adaptive Tuning, GPU, Kernel Acceleration

## 中文关键词

动态形状神经网络、贝叶斯优化、自适应调优、GPU、内核加速
