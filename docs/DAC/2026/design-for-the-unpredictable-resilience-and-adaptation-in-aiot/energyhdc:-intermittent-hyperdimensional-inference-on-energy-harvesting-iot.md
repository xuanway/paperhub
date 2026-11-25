Energyhdc: Intermittent Hyperdimensional Inference on Energy-Harvesting IoT
Authors：
[YUSHENG LIU](https://63dac.conference-program.com/?post_type=page&p=15&uid=4503744321368231839)，[Yong-Cheng Liaw](https://63dac.conference-program.com/?post_type=page&p=15&uid=7454865025081726408)，[Shuo-Han Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=204843)

## 中文标题

EnergyHDC：面向能量采集物联网的间歇式超维推理

## 英文摘要

Ambient energy harvesting technologies offer the promise of perpetual operation for batteryless Internet of Things (IoT) devices; however, their execution is frequently halted by unpredictable power failures. Traditional methods to ensure correctness, such as software checkpointing (e.g., Mementos) and newer systems for deep neural networks (e.g., DynBal), are burdened by substantial energy and latency overheads for progress preservation, limiting their use on ultra-low-power platforms. This paper introduces EnergyHDC, an energy-aware inference system designed for intermittent operation by integrating Hyperdimensional Computing (HDC). The system pairs HDC’s algorithmic robustness with fine-grained energy adaptation using three key contributions: (1) an energy-proportional checkpointing that optimizes preservation granularity against available energy; (2) a dimension-first reordering that slashes per-checkpoint storage; and (3) a priority-based pruning that allows for compile-time energy-accuracy trade-offs. Evaluated on an MSP432P401R microcontroller platform under intermittent power, EnergyHDC demonstrates up to 214× speedup compared to Mementos. It also achieves 19.6× faster inference than DynBal under similar accuracy and realistic energy-harvesting conditions. These results validate that a co-design approach, coupling energy-aware execution with HDC’s intrinsic robustness, can reframe intermittence from a system constraint into an opportunity for efficient edge intelligence.

## 中文摘要

环境能量采集技术为无电池物联网（IoT）设备的持续运行带来了希望；然而，其执行过程常常因不可预测的断电而中断。用于保证正确性的传统方法，例如软件检查点（如 Mementos）以及面向深度神经网络的较新系统（如 DynBal），在保存进度方面承受着可观的能量与延迟开销，限制了它们在超低功耗平台上的应用。本文提出 EnergyHDC，一种通过集成超维计算（HDC）而面向间歇运行设计的能量感知推理系统。该系统将 HDC 的算法鲁棒性与细粒度能量自适应相结合，包含三项关键贡献：(1) 能量比例检查点，根据可用能量优化保存粒度；(2) 维度优先重排序，大幅削减每次检查点的存储开销；(3) 基于优先级的剪枝，支持编译时的能量—精度权衡。在间歇供电的 MSP432P401R 微控制器平台上评估，EnergyHDC 相比 Mementos 最高实现 214× 加速；在相近精度和真实能量采集条件下，其推理速度也比 DynBal 快 19.6×。这些结果验证了将能量感知执行与 HDC 内在鲁棒性相耦合的协同设计方法，能够将间歇性从系统约束重新诠释为高效边缘智能的机遇。
