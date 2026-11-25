DFA-DRIVE: A Cross-Layer Delay Fault Analysis and Optimization Framework for Robust Multi-Task Driving Perception
Authors：
[Nrusinga Charan Gantayat](https://63dac.conference-program.com/?post_type=page&p=15&uid=98716290299412265241)，[Philip Jacobson](https://63dac.conference-program.com/?post_type=page&p=15&uid=74741983895763720151)，[Matthew Marinella](https://63dac.conference-program.com/?post_type=page&p=15&uid=1576675952176370829)，[Ben Feinberg](https://63dac.conference-program.com/?post_type=page&p=15&uid=6460825959781354169)，[Jeff Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3292043392856372077)

## 中文标题

DFA-DRIVE：面向鲁棒多任务驾驶感知的跨层延迟故障分析与优化框架

## 英文摘要

Autonomous driving systems increasingly rely on deep neural network (DNN) based multi-task perception models for reliable, real time scene understanding. At nanoscale technology nodes, these workloads are highly susceptible to timing errors arising from temperature fluctuations, voltage droop, and device aging. Among these, temperature poses a critical challenge. Prolonged high thermal stress exacerbates delay faults, degrading perception accuracy and endangering safety critical operation. We present DFA-DRIVE, a cross-layer Delay Fault Analysis Framework for Autonomous Driving that bridges circuit-level timing analysis with system level resilience evaluation. DFA-DRIVE quantifies how temperature induced timing failures propagate through object detection, drivable area segmentation, and lane line segmentation, exposing task level reliability bottlenecks. Building on DFA-DRIVE, we introduce DFA-OPT, an adaptive hardware mapping algorithm that dynamically reassigns systolic array (SA) resources based on DNN layer and application level thermal sensitivity. Targeting the automotive reliability envelopes of AEC-Q100 Grade 0 (–40 °C to 150 °C) and Grade 1 (–40 °C to 125 °C), DFA-OPT restores near baseline accuracy of small, high reliable SA (e.g., 4×4) even when large SA (e.g., 256×256) experience accuracy drops of upto 4% at 150 °C, achieving comparable accuracy with fewer computation cycles.

## 中文摘要

自动驾驶系统日益依赖基于深度神经网络（DNN）的多任务感知模型，以实现可靠、实时的场景理解。在纳米级工艺节点下，此类工作负载极易受到由温度波动、电压跌落与器件老化引起的时序错误影响。其中，温度是尤为严峻的挑战。持续的高热应力会加剧延迟故障，降低感知精度并危及安全攸关的运行。我们提出 DFA-DRIVE，一个面向自动驾驶的跨层延迟故障分析框架，将电路级时序分析与系统级鲁棒性评估相衔接。DFA-DRIVE 量化温度引起的时序失效如何传播至目标检测、可行驶区域分割与车道线分割，从而揭示任务级可靠性瓶颈。在 DFA-DRIVE 的基础上，我们提出 DFA-OPT，一种自适应硬件映射算法，依据 DNN 层与任务级的热敏感度动态重新分配脉动阵列（SA）资源。面向 AEC-Q100 Grade 0（–40 °C 至 150 °C）与 Grade 1（–40 °C 至 125 °C）的汽车可靠性包络，即使大尺寸 SA（如 256×256）在 150 °C 时出现高达 4% 的精度下降，DFA-OPT 仍能借助小型高可靠 SA（如 4×4）恢复接近基线的精度，并以更少的计算周期取得可比精度。
