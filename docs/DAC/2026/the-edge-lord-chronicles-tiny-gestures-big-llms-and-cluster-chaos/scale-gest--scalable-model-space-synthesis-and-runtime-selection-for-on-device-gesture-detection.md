Scale-Gest: Scalable Model-Space Synthesis and Runtime Selection for On-Device Gesture Detection
Authors：
[Abdul Basit](https://63dac.conference-program.com/?post_type=page&p=15&uid=4436572530276582735)，[Saim Rehman](https://63dac.conference-program.com/?post_type=page&p=15&uid=7110595057294220691)，[Muhammad Shafique](https://63dac.conference-program.com/?post_type=page&p=15&uid=560343)

## 中文标题

Scale-Gest：面向端侧手势检测的可扩展模型空间合成与运行时选择

## 英文摘要

Realizing on-device ML-based gesture detection under tight realtime performance, energy and memory constraints is challenging, especially when considering mobile devices with varying battery-power levels. Existing EdgeAI deployments typically rely on a single fixed detector, limiting optimization opportunities. We present Scale-Gest, a novel run-time adaptive gesture detection framework that expands the detector space into a dense family of tiny-YOLO architectures. We introduce multiple novel device-calibrated ACE (Accuracy-Complexity-Energy) profiles by analyzing different model-resolution-stride operating points. A lightweight run-time controller selects an appropriate ACE mode under user-defined and battery constraints, while a motion-aware hand-gesture-tracking ROI gate crops the input for reduced complexity detection. To evaluate performance of our system in real-world car driving scenarios, we introduce a temporally-annotated Driver Simulated Gesture (DSG-18) dataset. Scale-Gest maintains event-level F1 while significantly reducing energy and latency compared to single-detector approaches. On a battery-powered laptop running gesture streams, our ACE controller reduces per-frame energy by ≈4× (from ≈6.9 mJ to ≈1.6 mJ) while maintaining high gesture-detection performance (event-level F1 ≈0.8–0.9) and low mean latency (≈6 ms).

## 中文摘要

在严格的实时性能、能耗与内存约束下实现基于机器学习（ML）的端侧手势检测颇具挑战，尤其是当需要考虑电池电量各异的移动设备时。现有 EdgeAI 部署通常依赖单一固定检测器，限制了优化空间。我们提出 Scale-Gest，一种新颖的运行时自适应手势检测框架，它将检测器空间扩展为一个密集的 tiny-YOLO 架构族。通过分析不同的模型-分辨率-步长工作点，我们引入了多种新颖的、经设备校准的 ACE（精度-复杂度-能耗）配置。轻量级运行时控制器在用户定义约束与电池约束下选择合适的 ACE 模式，同时由运动感知的手势跟踪 ROI 门控对输入进行裁剪，以降低检测复杂度。为在真实汽车驾驶场景中评估系统性能，我们提出了带时间标注的驾驶员模拟手势（DSG-18）数据集。与单检测器方法相比，Scale-Gest 在保持事件级 F1 的同时显著降低了能耗与延迟。在运行手势流的电池供电笔记本上，我们的 ACE 控制器将每帧能耗降低约 4 倍（从约 6.9 mJ 降至约 1.6 mJ），同时保持较高的手势检测性能（事件级 F1 约 0.8–0.9）与较低的平均延迟（约 6 ms）。
