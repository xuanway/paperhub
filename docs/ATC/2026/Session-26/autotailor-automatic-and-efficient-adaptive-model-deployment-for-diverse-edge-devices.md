# AutoTailor: Automatic and Efficient Adaptive Model Deployment for Diverse Edge Devices

**中文标题**：AutoTailor：面向多样边缘设备的自动高效自适应模型部署

**所属 Session**：[Session 26: LLM Inference III](index.md) · [ATC 2026](../index.md)

**作者**：Mengyang Liu (Southeast University, University of Macau), Chenyu Lu (HKUST (GZ)), Haodong Tian (Tsinghua University), Fang Dong (Southeast University), Ruiting Zhou (Southeast University), Wei Wang (HKUST), Dian Shen (Southeast University), Guangtong Li (Southeast University), Ye Wan (Southeast University), Li Li (University of Macau)

## 英文摘要
On-device machine learning (ML) has become a fundamental component of emerging mobile applications. Adaptive model deployment delivers efficient inference for heterogeneous device capabilities and performance requirements through customizing neural architectures. SuperNet-based approaches offer a promising solution by generating numerous model variants from a pre-trained ML model. However, applying SuperNet in existing frameworks requires tedious model-aware development and time-consuming hardware-aware profiling, which limits their practical adoption. We present AutoTailor, the first framework to enable automated, end-to-end SuperNet-based adaptive model deployment for edge devices. Unlike manual SuperNet construction, AutoTailor employs a computation graph-guided compilation approach to automatically transform user-provided ML models into SuperNets. To support efficient specialization, AutoTailor incorporates learning-free latency and accuracy predictors, enabling low-cost yet accurate performance prediction. Our extensive evaluations demonstrate that AutoTailor reduces the lines of code for SuperNet construction by 10.8–34.5×, reduces predictor profiling time by 2.2–11.5×, and achieves up to 15.60% absolute accuracy improvement and 60.03% latency reduction compared to state-of-the-art approaches across diverse models and devices.

## 中文摘要
端侧机器学习（ML）已成为新兴移动应用的基础组成部分。自适应模型部署通过定制神经网络架构，为异构的设备能力与性能需求提供高效推理。基于 SuperNet 的方法通过从预训练 ML 模型生成大量模型变体，提供了一种颇具前景的解决方案。然而，在现有框架中应用 SuperNet 需要繁琐的、感知模型的开发工作以及耗时的、感知硬件的性能剖析，这限制了它的实际采用。我们提出 AutoTailor，这是首个面向边缘设备实现自动化、端到端、基于 SuperNet 的自适应模型部署的框架。与人工构建 SuperNet 不同，AutoTailor 采用计算图引导的编译方法，自动将用户提供的 ML 模型转换为 SuperNet。为支持高效特化，AutoTailor 引入了免学习的延迟与精度预测器，从而实现低成本且准确的性能预测。我们的大量评测表明，与最先进方法相比，AutoTailor 将构建 SuperNet 的代码行数减少 10.8–34.5×，将预测器剖析时间减少 2.2–11.5×，并在多样模型与设备上实现最高 15.60% 的绝对精度提升和 60.03% 的延迟降低。

## 英文关键词
adaptive model deployment, supernets, neural architecture compilers, edge computing

## 中文关键词
自适应模型部署，超网络，神经网络架构编译器，边缘计算

[返回 Session 26](index.md) · [返回 ATC 2026](../index.md)
