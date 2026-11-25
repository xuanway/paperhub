Algorithm and Hardware Co-Design for Efficient Complex-Valued Uncertainty Estimation
Authors：
[Zehuan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=46808341015186520381)，[Hao (Mark) Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=4403856072958050686)，[He Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=692143)，[Wayne Luk](https://63dac.conference-program.com/?post_type=page&p=15&uid=690243)

## 中文标题

面向高效复值不确定性估计的算法与硬件协同设计

## 英文摘要

Complex-Valued Neural Networks (CVNNs) have significant advantages in handling tasks that involve complex numbers. However, existing CVNNs are unable to quantify predictive uncertainty. We propose, for the first time, dropout-based Bayesian Complex-Valued Neural Networks (BayesCVNNs) to enable uncertainty quantification for complex-valued applications, exhibiting broad applicability and efficiency for hardware implementation due to modularity. Furthermore, as the dual-part nature of complex values significantly broadens the design space and enables novel configurations based on layer-mixing and part-mixing, we introduce an automated search approach to effectively identify optimal configurations for both real and imaginary components. To facilitate deployment, we present a framework that generates customized FPGA-based accelerators for BayesCVNNs, leveraging a set of optimized building blocks. Experiments demonstrate the best configuration can be effectively found via the automated search, attaining higher performance with lower hardware costs compared with manually crafted models. The optimized accelerators achieve approximately 4.5× and 13× speedups on different models with less than 10% power consumption compared to GPU implementations, and outperform existing work in both algorithm and hardware aspects. Our code is publicly available at: https://github.com/zehuanzhang/BayesCVNN.git.

## 中文摘要

复值神经网络（CVNN）在处理涉及复数的任务时具有显著优势。然而，现有 CVNN 无法量化预测不确定性。我们首次提出基于 dropout 的贝叶斯复值神经网络（BayesCVNN），为复值应用实现不确定性量化，并因其模块化特性而具有广泛的适用性与硬件实现效率。此外，由于复值的双部（实部与虚部）特性显著拓展了设计空间，并支持基于层混合与部分混合的新颖配置，我们引入自动化搜索方法，以有效确定实部与虚部组件的最优配置。为便于部署，我们提出一个框架，利用一组经过优化的构建模块为 BayesCVNN 生成定制化 FPGA 加速器。实验表明，通过自动化搜索可有效找到最佳配置，相比人工设计的模型以更低的硬件成本获得更高的性能。优化后的加速器在不同模型上相较 GPU 实现取得约 4.5 倍与 13 倍的加速，而功耗低于 10%，并在算法与硬件两方面均优于已有工作。代码已公开：https://github.com/zehuanzhang/BayesCVNN.git。
