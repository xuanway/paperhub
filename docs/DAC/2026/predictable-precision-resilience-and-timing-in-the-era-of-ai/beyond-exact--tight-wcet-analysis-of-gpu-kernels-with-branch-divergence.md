Beyond Exact: Tight WCET Analysis of GPU Kernels with Branch Divergence
Authors：
[Shuai Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=904843)，[Chen Jie](https://63dac.conference-program.com/?post_type=page&p=15&uid=96820136283869091101)，[Yaowei Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=30896832343324792971)，[Mingyue Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=4207571490745664305)，[Xiaotian Dai](https://63dac.conference-program.com/?post_type=page&p=15&uid=173243)，[Nan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=2342521319934363234)

## 中文标题

超越精确：含分支发散的 GPU 内核紧致 WCET 分析

## 英文摘要

The increasing adoption of GPUs in real-time systems necessitates precise timing analysis for GPU thread blocks to ensure overall system predictability. However, the uncertainties of branch executions within GPU warps impose significant barriers for predicting the worst-case execution time (WCET) of the thread block. Existing WCET analysis for thread blocks typically assumes deterministic warp execution paths, which is unrealistic given the dynamic control flows of threads within the warps. Moreover, as the warp scheduler operates as a black box, the analysis must rely on relaxed scheduling assumptions, resulting in overly-pessimistic bounds in order to cover edge scenarios. This paper first establishes the need for static analysis by showing how branch divergence can trigger timing anomalies and influence block WCETs. We then develop an exact WCET analysis for a GPU thread block under the same scheduling constraints as prior work while not imposing any warp execution path assumptions. Furthermore, by enforcing a practical constraint on warp executions, we present a tighter analysis that enhances system predictability. Experiments show that the proposed analysis under warp execution constraints significantly reduces the WCET estimations of GPU thread blocks (by 19.13% on average and up to 39.39%).

## 中文摘要

GPU 在实时系统中的日益普及，要求对 GPU 线程块进行精确的时序分析，以保证系统整体的可预测性。然而，GPU warp 内部分支执行的不确定性，为预测线程块的最坏执行时间（WCET）设置了显著障碍。现有的线程块 WCET 分析通常假设 warp 执行路径确定，考虑到 warp 内线程的动态控制流，这一假设并不现实。此外，由于 warp 调度器是黑盒，分析必须依赖宽松的调度假设，为覆盖边界情形而导致过于悲观的界。本文首先展示分支发散如何触发时序异常并影响线程块 WCET，从而确立静态分析的必要性。随后，我们在与先前工作相同的调度约束下、且不施加任何 warp 执行路径假设，建立了 GPU 线程块的精确 WCET 分析。进一步地，通过对 warp 执行施加一项实际约束，我们提出一种更紧致的分析以增强系统可预测性。实验表明，所提出的在 warp 执行约束下的分析显著降低了 GPU 线程块的 WCET 估计（平均 19.13%，最高 39.39%）。
