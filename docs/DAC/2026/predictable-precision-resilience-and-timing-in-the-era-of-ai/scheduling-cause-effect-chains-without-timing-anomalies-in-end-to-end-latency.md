Scheduling Cause-Effect Chains Without Timing Anomalies in End to End Latency
Authors：
[Yixuan Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=485843)，[Bo Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=585843)，[Yinkang Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=385843)，[Haoyuan Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=285843)，[Cheng Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9722161818012809504)，[Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=52002988756729828161)，[Lei Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=852843)，[teng wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=652843)，[Wenqi Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=425843)，[Xi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=872843)

## 中文标题

端到端时延中无时序异常的因果链调度

## 英文摘要

In real-time systems, both individual task execution and data propagation must meet strict timing constraints. Cause–effect (CE) chains are widely used to analyze such behaviors by end-to-end latency. However, timing anomalies (TAs) can distort it, where a local reduction in execution times leads to an increase in the overall end-to-end latency. As a result, precisely analyzing the upper bounds of the latency becomes challenging, and such systems typically exhibit larger upper bounds than TA-eliminated systems. Existing studies either eliminate TAs by completely sacrificing average latency to simplify analysis or, despite adopting complex safe analysis methods, do not eliminate TAs effectively, still having high latencies. To address this issue, we identify two basic causes of TAs in end-to-end latency. Based on these causes, we propose the first treatment that eliminates TAs in the latency with negligible average latency loss using Deterministic Data Flow (DDF). We further formally prove its TA-free property. Therefore, we can get a precise upper bound for latency when all jobs execute with their worst-case execution times. Experimental results show that it effectively reduces the maximum end-to-end latency, the average latency, and latency jitter compared with the state-of-the-art (SOTA) method.

## 中文摘要

在实时系统中，单个任务的执行与数据的传播都必须满足严格的时序约束。因果（cause–effect，CE）链被广泛用于分析此类端到端时延行为。然而，时序异常（timing anomaly，TA）会使其失真：局部执行时间的缩短反而导致整体端到端时延的增加。因此，精确分析时延上界变得困难，此类系统通常表现出比消除 TA 的系统更大的上界。已有研究要么以完全牺牲平均时延为代价消除 TA 以简化分析，要么虽采用复杂的安全分析方法，却未能有效消除 TA，仍然具有较高的时延。为解决该问题，我们识别出端到端时延中 TA 的两类基本成因。基于这些成因，我们提出首个利用确定性数据流（Deterministic Data Flow，DDF）在时延中消除 TA、且平均时延损失可忽略的方法，并进一步形式化证明了其无 TA 特性。因此，当所有作业均以其最坏执行时间运行时，我们可以获得精确的时延上界。实验结果表明，与最先进（SOTA）方法相比，该方法有效降低了最大端到端时延、平均时延以及时延抖动。

## 英文关键词

Real-time systems, End-to-End Latency, Timing Anomalies

## 中文关键词

实时系统、端到端时延、时序异常
