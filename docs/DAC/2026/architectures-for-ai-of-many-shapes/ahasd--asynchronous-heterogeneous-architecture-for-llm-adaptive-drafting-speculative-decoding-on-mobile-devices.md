AHASD: Asynchronous Heterogeneous Architecture for LLM Adaptive Drafting Speculative Decoding on Mobile Devices
Authors：
[Zirui Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=62039458015431583651)，[zhihua fan](https://63dac.conference-program.com/?post_type=page&p=15&uid=2114510187179282683)，[Wenxing Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=3068187692236305973)，[Haibin Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=70512365310535428731)，[Fulin Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=03536989485852330741)，[Wenming Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=180243)，[Xiaochun Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=1343405397210277197)

## 中文标题

AHASD：面向移动设备上 LLM 自适应起草投机解码的异步异构架构

## 英文摘要

Speculative decoding enhances the inference efficiency of large language models (LLMs) by generating drafts using a small draft language model (DLM) and verifying them in batches with a large target language model (TLM). However, adaptive drafting inference on a mobile single-NPU-PIM system faces idle overhead in traditional operator-level synchronous execution and wasted computation in asynchronous execution due to fluctuations in draft length. This paper introduces AHASD, a task-level asynchronous mobile NPU-PIM heterogeneous architecture for speculative decoding. Notably, AHASD achieves parallel drafting on the PIM and verification on a single NPU through task-level DLM-TLM decoupling and specifically, it incorporates Entropy-History-Aware Drafting Control and Time-Aware Pre-Verification Control to dynamically manage adaptive drafting algorithm execution and pre-verification timing, suppressing invalid drafting based on low-confidence drafts. Additionally, AHASD integrates Attention Algorithm Units and Gated Task Scheduling Units within LPDDR5-PIM to enable attention link localization and sub-microsecond task switching on the PIM side. Experimental results for different LLMs and adaptive drafting algorithms show that AHASD achieves up to 4.2× in throughput and 5.6× in energy efficiency improvements over a GPU-only baseline, and 1.5× in throughput and 1.24× in energy efficiency gains over the state-of-the-art GPU+PIM baseline, with hardware overhead below 3% of the DRAM area.

## 中文摘要

投机解码通过使用小型起草语言模型（DLM）生成草稿，并用大型目标语言模型（TLM）对其批量验证，从而提升大型语言模型（LLM）的推理效率。然而，在移动端单 NPU-PIM 系统上进行自适应起草推理时，传统的算子级同步执行存在空闲开销，而异步执行又会因起草长度波动而产生无效计算。本文提出 AHASD，一种面向投机解码的任务级异步移动 NPU-PIM 异构架构。值得注意的是，AHASD 通过任务级的 DLM-TLM 解耦，在单个 NPU 上实现了 PIM 上的并行起草与 NPU 上的验证；具体而言，它引入熵历史感知起草控制与时间感知预验证控制，动态管理自适应起草算法的执行与预验证时机，从而抑制基于低置信度草稿的无效起草。此外，AHASD 在 LPDDR5-PIM 中集成注意力算法单元与门控任务调度单元，以在 PIM 侧实现注意力链路局部化与亚微秒级任务切换。针对不同 LLM 与自适应起草算法的实验结果表明，相较于仅 GPU 基线，AHASD 最高取得 4.2× 的吞吐提升与 5.6× 的能效提升；相较于最先进的 GPU+PIM 基线，取得 1.5× 的吞吐提升与 1.24× 的能效提升，且硬件开销低于 DRAM 面积的 3%。
