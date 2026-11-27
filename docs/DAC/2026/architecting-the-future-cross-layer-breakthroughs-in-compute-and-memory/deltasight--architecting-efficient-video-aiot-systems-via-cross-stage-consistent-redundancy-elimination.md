Deltasight: Architecting Efficient Video AIoT Systems via Cross-Stage Consistent Redundancy Elimination
Authors：
[Qinyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7475078041391369105)，[Cen Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=62497620160228347521)，[Jingkai Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=25324035296743765961)，[Yawen Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1516334843451907751)，[Hongen Shao](https://63dac.conference-program.com/?post_type=page&p=15&uid=95691822553337335711)，[Xiaofeng Zou](https://63dac.conference-program.com/?post_type=page&p=15&uid=87195645169767408041)，[Ziqian Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=36723394078646709111)

## 中文标题

Deltasight：通过跨阶段一致冗余消除构建高效视频 AIoT 系统

## 英文摘要

The high energy cost of video AIoT systems stems from redundant operations across sensing, transmission, and computation. While prior work optimizes individual stages, the lack of cross-stage coordination forces each stage to re-detect redundancy, limiting overall efficiency. We present DeltaSight, an algorithm–hardware co-design architecture that establishes a sensor-side unified redundancy criterion serving as the common basis for redundancy elimination throughout the pipeline. Algorithmically, we generate this criterion via sensor-side block-level redundancy detection whose output matches the granularity of downstream computation, complemented by a semantic-aware sampling strategy that adapts precision to task relevance. An architecture is designed to support this algorithm with minimal hardware additions. DeltaSight gains 2.4× sensor-side and 1.7× end-to-end energy efficiency, with slight accuracy improvements.

## 中文摘要

视频 AIoT 系统的高能耗源于感知、传输与计算各环节中的冗余操作。已有工作虽对各个阶段分别进行优化，但缺乏跨阶段协同，迫使每个阶段重复检测冗余，从而限制了整体效率。我们提出 DeltaSight，一种算法-硬件协同设计架构，它在传感器侧建立统一的冗余判据，作为贯穿整条流水线进行冗余消除的共同基础。在算法层面，我们通过传感器侧的块级冗余检测生成该判据，其输出与下游计算的粒度相匹配，并辅以一种语义感知的采样策略，使精度随任务相关性自适应调整。我们设计了一种架构，以极少的硬件开销支持该算法。DeltaSight 在传感器侧获得 2.4 倍、在端到端获得 1.7 倍的能效提升，同时精度略有提高。
