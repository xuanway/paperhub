N3Litho: A GPU-Native Numerical-Neural Framework for 3D Mask Modeling, 3D Propagation, and 3D Aerial Image Simulation
Authors：
[yuyang chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=62610219687434538931)，[Zhen Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=65824847633068734601)，[Yinuo Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=37640199914727928941)，[Yiwen Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6416310257279704104)，[Wenxuan Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1566819450488483677)，[Jiaqi Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=301791953262832763)，[Jingyi Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2434541213894243641)，[Hao Geng](https://63dac.conference-program.com/?post_type=page&p=15&uid=64456419866376934351)

## 中文标题

N3Litho：面向三维掩模建模、三维传播与三维空间像仿真的 GPU 原生数值-神经框架

## 英文摘要

Accurate and efficient lithography simulation is critical for virtual fabrication and shift-left manufacturing. While thin-mask models and single-plane aerial images suffice at older nodes, advanced nodes require 3D in-resist aerial images to capture depth-dependent effects from mask thickness, sidewalls, and multilayer stacks. Rigorous EM solvers provide this fidelity but are too slow for ILT or full-chip use, and thin-mask learning methods fail to model the underlying vector field needed for 3D propagation. This paper introduces a new paradigm that reconstructs the 3D in-resist vector field from the image-plane vector field and 3D mask/film-stack parameters. Based on this insight, we develop N3Litho, a GPU-native numerical-neural framework that couples a GPU-accelerated vectorial Abbe solver with an NGP-based multi-resolution hash backbone for fast 3D field reconstruction. The method achieves near-EM fidelity with orders-of-magnitude speedup, and the resulting 3D aerial images can be directly used by resist models, OPC/ILT pipelines, and hotspot detection flows.

## 中文摘要

准确高效的光刻仿真对于虚拟制造与左移制造至关重要。虽然在较老节点上薄掩模模型与单平面空间像已足够，但先进节点需要三维光刻胶内空间像，以捕捉由掩模厚度、侧壁和多层膜堆引起的深度依赖效应。严格的电磁（EM）求解器能够提供这种保真度，但对于 ILT 或全芯片应用而言过慢，而薄掩模学习方法无法建模三维传播所需的底层矢量场。本文提出一种新范式，从像平面矢量场与三维掩模/膜堆参数重建三维光刻胶内矢量场。基于这一洞见，我们开发了 N3Litho，一个 GPU 原生的数值-神经框架，它将 GPU 加速的矢量 Abbe 求解器与基于 NGP 的多分辨率哈希骨干网络耦合，以实现快速的三维场重建。该方法以数量级的加速达到接近 EM 的保真度，所得三维空间像可直接用于光刻胶模型、OPC/ILT 流程与热点检测流程。
