Efficient HLS Accelerator Floorplan on Multi-Die FPGA Aided by Graph Neural Networks
Authors：
[Haoran Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=7213328960922784117)，[teng wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=652843)，[Qianyu Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=452843)，[Zhendong Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=772843)，[Wenqi Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=425843)，[Lei Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=852843)，[Xi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=872843)，[Xuehai Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=513843)

## 中文标题

图神经网络辅助的多 die FPGA 上高效 HLS 加速器布局规划

## 英文摘要

High-level synthesis (HLS) and multi-die FPGAs have been widely applied in large-scale accelerator design. To address cross-die boundary delays and local congestion issues in HLS designs on multi-die FPGAs, prior work proposed a coarse-grained floorplanning and pipelining method to improve frequency performance. However, achieving higher frequency still requires multiple iterative implementations in Vitis to tune parameters, incurring significant time overhead. To accelerate this process, we propose a graph neural network (GNN) based floorplan quality predictor at the FPGA slot level, achieving an accuracy of 84.13% and an F1-score of 0.86 in the congestion prediction task, with an average inference latency of only 0.58 ms. Compared with the traditional tool flow that requires tens of hours, our method enables millisecond-level floorplan parameter fine-tuning, improving an unroutable and 318.2 MHz case to 329.2 MHz and 330.3 MHz, respectively. Furthermore, we integrate our method into the HLS design-space exploration framework, achieving an average frequency improvement of 11.2%, with the maximum improvement reaching 23.8%. The execution time of all benchmarks is reduced by 30.9%.

## 中文摘要

高层综合（HLS）与多 die FPGA 已广泛应用于大规模加速器设计。针对多 die FPGA 上 HLS 设计中的跨 die 边界延迟与局部拥塞问题，已有工作提出粗粒度布局规划与流水化方法以提升频率性能。然而，要获得更高频率仍需在 Vitis 中多次迭代实现以调优参数，带来显著的时间开销。为加速该过程，我们提出一种在 FPGA slot 层面基于图神经网络（GNN）的布局规划质量预测器，在拥塞预测任务上达到 84.13% 的准确率与 0.86 的 F1 分数，平均推理延迟仅 0.58 ms。与传统需要数十小时的工具流程相比，我们的方法可实现毫秒级的布局规划参数微调，将一个原本无法布通的案例与一个 318.2 MHz 的案例分别提升至 329.2 MHz 和 330.3 MHz。此外，我们将该方法集成到 HLS 设计空间探索框架中，平均频率提升 11.2%，最高提升达 23.8%，所有基准的执行时间缩短 30.9%。

## 英文关键词

High-Level Synthesis, Multi-Die FPGA, Floorplan, Frequency, Congestion

## 中文关键词

高层综合、多 die FPGA、布局规划、频率、拥塞
