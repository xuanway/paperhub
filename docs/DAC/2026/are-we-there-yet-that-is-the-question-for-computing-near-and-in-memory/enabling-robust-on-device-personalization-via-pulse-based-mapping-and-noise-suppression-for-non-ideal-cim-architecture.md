Enabling Robust On-Device Personalization via Pulse-Based Mapping and Noise Suppression for Non-Ideal CIM Architecture
Authors：
[Yiyang Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=96601922528127878511)，[Xinyu Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=08302318746149025771)，[Zhenge Jia](https://63dac.conference-program.com/?post_type=page&p=15&uid=73074348703888030031)，[Shaocong Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=25710633120223055031)

## 中文标题

面向非理想 CIM 架构，通过脉冲映射与噪声抑制实现稳健的端侧个性化

## 英文摘要

Computing-in-memory (CIM) architectures alleviate the data movement bottleneck by performing neural computations directly within memory arrays, which significantly addresses the resource constraints for edge AI applications. As edge applications increasingly demand user-specific adaptation, on-device deep model personalization has become essential for supporting evolving environments, privacy-sensitive data, and low-latency intelligence. However, in CIM-based systems, deep model parameters cannot be efficiently extracted for external fine-tuning due to the high cost of reading, digitizing, and transferring analog device states. Consequently, personalization is expected to be executed directly on the CIM hardware through in-situ weight updates. Prior works have focused primarily on improving inference robustness under non-ideal CIM conditions, leaving the problem of robust on-device fine-tuning fundamentally unaddressed. To fill the gap, we propose CIM-MP, a hardware–software co-optimized framework enabling stable and accurate on-device personalization under noisy CIM conditions. CIM-MP introduces a pulse-based mapping strategy that ensures convergence during in-memory weight updates. To further enhance robustness, we propose a Feature Variation Elimination (FVE) mechanism to mitigate feature-map noise in forward propagation, and a Gradient Adaptive Purification (GAP) mechanism to refine gradients during backpropagation. Experiments show that CIM-MP achieves up to 35.1% accuracy improvement over state-of-the-art approaches, demonstrating the feasibility of efficient and robust on-device learning directly on CIM platforms.

## 中文摘要

存内计算（CIM）架构通过在存储阵列内直接执行神经计算来缓解数据搬运瓶颈，从而显著应对边缘 AI 应用的资源约束。随着边缘应用日益需要面向特定用户的适配，端侧深度模型个性化已成为支撑环境演化、隐私敏感数据和低延迟智能的关键。然而在基于 CIM 的系统中，由于读取、数字化并传输模拟器件状态的成本很高，深度模型参数难以被高效提取用于外部微调。因此，个性化预期通过原位权重更新直接在 CIM 硬件上执行。此前的工作主要聚焦于提升非理想 CIM 条件下推理的稳健性，而稳健的端侧微调问题从根本上仍未得到解决。为填补这一空白，我们提出 CIM-MP，一个软硬件协同优化的框架，可在含噪 CIM 条件下实现稳定且准确的端侧个性化。CIM-MP 引入基于脉冲的映射策略，确保存内权重更新过程中的收敛性。为进一步增强稳健性，我们提出特征变化消除（FVE）机制以缓解前向传播中的特征图噪声，并提出梯度自适应净化（GAP）机制以在反向传播中精炼梯度。实验表明，CIM-MP 相比最先进方法最高取得 35.1% 的精度提升，证明了直接在 CIM 平台上进行高效且稳健的端侧学习的可行性。

## 英文关键词

Computing-in-Memory, ReRAM, On-device Personalization

## 中文关键词

存内计算、ReRAM、端侧个性化
