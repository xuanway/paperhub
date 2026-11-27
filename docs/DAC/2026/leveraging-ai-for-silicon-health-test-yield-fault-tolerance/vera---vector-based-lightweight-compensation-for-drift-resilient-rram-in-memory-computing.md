VeRA+: Vector-Based Lightweight Compensation for Drift-Resilient RRAM In-Memory Computing
Authors：
[Weirong Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=02999078427359962621)，[Kai Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=53969527950190915471)，[Zhen Kong](https://63dac.conference-program.com/?post_type=page&p=15&uid=7765254558947468759)，[Zhengke Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=81124943629090482301)，[Quan Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=98958884996573353571)，[Haoyuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=95182132527299620031)，[Junkai Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1961375374356723385)，[Jun Lan](https://63dac.conference-program.com/?post_type=page&p=15&uid=79012155358423686331)，[Yida Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=778916225111880004)，[Masanori Hashimoto](https://63dac.conference-program.com/?post_type=page&p=15&uid=19973706983457561851)，[Longyang Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=51399216808247560021)

## 中文标题

VeRA+：面向抗漂移 RRAM 存内计算的向量化轻量补偿

## 英文摘要

RRAM-based in-memory computing (IMC) offers high energy efficiency but suffers from conductance drift that severely degrades long-term accuracy. Existing approaches including retraining, noise-aware training, and Batch Normalization (BN)-based calibration either require RRAM rewriting, demand large storage overhead, or rely on online correction. We propose VeRA+, a lightweight drift compensation framework that reuses shared projection matrices and introduces only two compact drift-specific vectors per drift level. A drift-aware scheduling algorithm offline-trains a small set of VeRA+ parameters and selects the appropriate set over time without any on-chip retraining or data replay. VeRA+ preserves up to 99.77% of the drift-free accuracy after ten years of simulated drift and reduces storage overhead by more than three orders of magnitude compared with BN-based calibration. To validate VeRA+ under realistic device behavior, we extract one-week drift statistics from measurements on our fabricated 1T1R RRAM devices and use them to simulate realistic drifted weights. Under these measured drift conditions, VeRA+ achieves accuracy close to the drift-free baseline, providing an efficient and practical solution for long-term drift resilience in RRAM-IMC.

## 中文摘要

基于 RRAM 的存内计算（IMC）具有高能效优势，但受电导漂移影响，长期精度会严重退化。现有方法（包括重训练、噪声感知训练以及基于批归一化（BN）的校准）要么需要重写 RRAM，要么带来庞大的存储开销，要么依赖在线校正。我们提出 VeRA+，一个轻量级漂移补偿框架，它复用共享投影矩阵，并为每个漂移等级仅引入两个紧凑的漂移专用向量。一种漂移感知调度算法离线训练一小组 VeRA+ 参数，并在运行过程中随时间选择合适的一组，无需任何片上重训练或数据回放。在模拟十年漂移后，VeRA+ 仍能保持高达 99.77% 的无漂移精度，并将存储开销相较基于 BN 的校准降低三个数量级以上。为在真实器件行为下验证 VeRA+，我们从所制造的 1T1R RRAM 器件的测量结果中提取一周的漂移统计数据，并用其模拟真实的漂移权重。在这些实测漂移条件下，VeRA+ 达到接近无漂移基线的精度，为 RRAM-IMC 的长期抗漂移能力提供了高效且实用的解决方案。

## 英文关键词

resistive random access memory, long-term reliability, in-memory computing, drift, lightweight compensation

## 中文关键词

阻变存储器、长期可靠性、存内计算、漂移、轻量级补偿
