Adaptive Read Retry Table Extension for Enhanced Data Reliability in 3D NAND Flash Memory
Authors：
[Han-Yu Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=27051617081389750771)，[Chen-Xing Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5946423534974240637)，[Jen-Wei Hsieh](https://63dac.conference-program.com/?post_type=page&p=15&uid=35794224152285828341)，[Hung-Pin Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=58888330509481686721)，[Yuan-Hao Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=014843)

## 中文标题

面向 3D NAND 闪存数据可靠性增强的自适应读重试表扩展

## 英文摘要

3D NAND flash is widely used from PCs to data centers, but its major weakness is data reliability. As data is retained, charge leakage causes read errors. Vendors mitigate this using the read retry mechanism, which iteratively applies predefined read reference voltage combinations, called read retry parameters (RRPs), stored in a read retry table (RRT). However, the limited number of RRPs can lead to RRP burnout, a condition where all read retry parameter entries have been exhausted without successful data recovery. In such cases, the data becomes undecodable and the corresponding block is marked as bad, degrading both capacity and lifetime of the NAND flash. Experiment showed that even a small portion of recovey failures may lead to significant capacity loss. We propose an Adaptive RRT Extension framework, integrating two key mechanisms: WL-Aware Interpolated Retry (WIR) and Multi-Dimensional Guided Retry (MDGR), to expand recovery capability. Experiments show that our method recovers up to 99% of failed pages and preserves up to 99% and 84% of usable capacity under 12-and 30-month retention, respectively—where the baseline retains only 90% or reaches end-of-life.

## 中文摘要

3D NAND 闪存广泛应用于从个人计算机到数据中心的各类场景，但其主要弱点在于数据可靠性。随着数据驻留时间延长，电荷泄漏会导致读错误。厂商借助读重试机制缓解该问题：该机制迭代地施加预定义的读参考电压组合，即读重试参数（read retry parameter, RRP），并将其存储于读重试表（read retry table, RRT）中。然而，RRP 数量有限可能引发 RRP 耗尽（RRP burnout），即所有读重试参数条目均已用尽却仍未成功恢复数据。此时数据无法解码，相应块被标记为坏块，从而同时损害 NAND 闪存的容量与寿命。实验表明，即使只有小比例的恢复失败，也可能导致显著的容量损失。我们提出自适应 RRT 扩展框架，集成两项关键机制——WL 感知插值重试（WL-Aware Interpolated Retry, WIR）与多维引导重试（Multi-Dimensional Guided Retry, MDGR）——以扩展恢复能力。实验表明，我们的方法可恢复高达 99%的失效页，并在 12 个月与 30 个月数据驻留条件下分别保持高达 99%与 84%的可用容量；相比之下，基线仅能保持 90%，或已进入寿命终止状态。

## 英文关键词

3D NAND flash, SSD, read retry, read retry table, retention error, data reliability, bad block management, storage lifetime

## 中文关键词

3D NAND 闪存、SSD、读重试、读重试表、驻留错误、数据可靠性、坏块管理、存储寿命
