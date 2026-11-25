Torr: Towards Brain-Inspired Task-Oriented Reasoning via Cache-Oriented Algorithm-Architecture Co-Design
Authors：
[Hyunwoo Oh](https://63dac.conference-program.com/?post_type=page&p=15&uid=05645374820751851621)，[SungHeon Jeong](https://63dac.conference-program.com/?post_type=page&p=15&uid=3960049205650996177)，[Suyeon Jang](https://63dac.conference-program.com/?post_type=page&p=15&uid=68835759722959446361)，[Hanning Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=902743)，[Sanggeon Yun](https://63dac.conference-program.com/?post_type=page&p=15&uid=49158696194380247701)，[Tamoghno Das](https://63dac.conference-program.com/?post_type=page&p=15&uid=20131471467038532701)，[Mohsen Imani](https://63dac.conference-program.com/?post_type=page&p=15&uid=377143)

## 中文标题

TorR：通过面向缓存的算法—架构协同设计实现类脑任务导向推理

## 英文摘要

Task-oriented object detection (TOOD) atop CLIP offers open-vocabulary, prompt-driven semantics, yet dense per-window computation and heavy memory traffic hinder real-time, power-limited edge deployment. We present TorR, a brain-inspired algorithm–architecture co-design that replaces CLIP-style dense alignment with a hyperdimensional (HDC) associative reasoner and turns temporal coherence into reuse. On the algorithm side, TorR reformulates alignment as HDC similarity and graph composition, introducing partial-similarity reuse via (i) query caching with per-class score accumulation, (ii) exact 𝛿-updates when only a small set of hypervector bits change, and (iii) similarity/load-gated bypass under high system load. On the architecture side, TorR instantiates a lane-scalable, bit-sliced item memory with bank/precision gating and a lightweight controller that schedules bypass/𝛿/full paths to meet RT-30/RT-60 targets as object counts vary. Synthesized in a TSMC 28 nm process and exercised with a cycle-accurate simulator, TorR sustains real-time throughput with millijoule-scale energy per window (≈50 mJ at 60 FPS; ≈113 mJ at 30 FPS) and low latency jitter, while delivering competitive AP@0.5 across five task prompts (mean 44.27%) within a bounded margin to strong VLM baselines, but at orders-of-magnitude lower energy. The design exposes deployment-time configurability (effective dimension 𝐷′, thresholds, precision) to trade accuracy, latency, and energy for edge budgets.

## 中文摘要

基于 CLIP 的任务导向目标检测（TOOD）提供开放词汇、提示驱动的语义，然而逐窗口的密集计算和沉重的内存流量阻碍了其在实时、功耗受限的边缘部署。我们提出 TorR，一种类脑的算法—架构协同设计，用超维（HDC）联想推理器替代 CLIP 风格的稠密对齐，并将时间相干性转化为复用。在算法层面，TorR 将对齐重构为 HDC 相似度与图组合，通过以下方式引入部分相似度复用：(i) 带逐类分数累积的查询缓存；(ii) 当仅少量超向量比特发生变化时的精确 𝛿 更新；(iii) 高系统负载下由相似度/负载门控的旁路。在架构层面，TorR 实例化了一个通道可扩展、位切片的项存储器，具备 bank/精度门控，以及一个轻量控制器，可根据目标数量变化调度旁路/𝛿/完整路径以满足 RT-30/RT-60 目标。在 TSMC 28 nm 工艺下综合并用周期精确模拟器进行验证，TorR 在保持实时吞吐的同时，每窗口能耗仅为毫焦量级（60 FPS 时约 50 mJ；30 FPS 时约 113 mJ），且延迟抖动低；同时在五个任务提示上提供有竞争力的 AP@0.5（平均 44.27%），与强 VLM 基线的差距有限，但能耗低数个数量级。该设计暴露了部署时可配置性（有效维度 𝐷′、阈值、精度），以便针对边缘预算权衡精度、延迟与能耗。
