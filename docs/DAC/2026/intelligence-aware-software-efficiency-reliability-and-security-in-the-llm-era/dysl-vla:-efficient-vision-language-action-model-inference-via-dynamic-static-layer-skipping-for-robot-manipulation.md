DySL-VLA: Efficient Vision-Language-Action Model Inference via Dynamic-Static Layer-Skipping for Robot Manipulation
Authors：
[Zebin Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=17827585784550662921)，[Yijiahao Qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=5740536195665541507)，[Tong Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=21842765951470382951)，[Bo Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1437181486312215528)，[Shaoshan Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=013643)，[Meng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=414843)

## 中文标题

DySL-VLA：面向机器人操作的静动态跳层高效视觉-语言-动作模型推理

## 英文摘要

Vision-Language-Action (VLA) models have shown remarkable success in robotic tasks like manipulation by fusing a language model’s reasoning with a vision model’s 3D understanding. However, their high computational cost remains a major obstacle for real-world applications that require real-time performance. We observe that the actions within a task have varying levels of importance: critical steps demand high precision, while less important ones can tolerate more variance. Leveraging this insight, we propose DySL-VLA, a novel framework that addresses computational cost by dynamically skipping VLA layers based on each action’s importance. DySL-VLA categorizes its layers into two types: informative layers, which are consistently executed, and incremental layers, which can be selectively skipped. To intelligently skip layers without sacrificing accuracy, we invent a prior-post skipping guidance mechanism to determine when to initiate layer-skipping. We also propose a skip-aware two-stage knowledge distillation algorithm to efficiently train a standard VLA into a DySL-VLA. Our experiments indicate that DySL-VLA achieves 2.1% improvement in success length over Deer-VLA on the Calvin dataset, while simultaneously reducing trainable parameters by a factor of 85.7 and providing a 3.75× speedup relative to the RoboFlamingo baseline at iso-accuracy. Our code is available on https://github.com/PKU-SEC-Lab/DYSL_VLA.

## 中文摘要

视觉-语言-动作（VLA）模型通过将语言模型的推理能力与视觉模型的三维理解能力相融合，在操作等机器人任务中取得了显著成功。然而，其高昂的计算开销仍是要求实时性能的实际应用的主要障碍。我们观察到，同一任务内各动作的重要性存在差异：关键步骤需要高精度，而较不重要的步骤可以容忍更大的偏差。基于这一观察，我们提出 DySL-VLA，这是一个新颖的框架，通过根据每个动作的重要性动态跳过 VLA 层来降低计算开销。DySL-VLA 将其层分为两类：始终执行的信息层，以及可被选择性跳过的增量层。为了在不牺牲精度的前提下智能地跳层，我们提出一种先验-后验跳层引导机制，用以判定何时启动跳层。我们还提出一种跳层感知的两阶段知识蒸馏算法，可将标准 VLA 高效训练为 DySL-VLA。实验表明，DySL-VLA 在 Calvin 数据集上相对 Deer-VLA 将成功长度提升 2.1%，同时将可训练参数减少 85.7 倍，并在同等精度下相对 RoboFlamingo 基线取得 3.75 倍加速。我们的代码已开源于 https://github.com/PKU-SEC-Lab/DYSL_VLA。

## 英文关键词

Vision-Language-Action Model, Layer Skipping, Robot Manipulation

## 中文关键词

视觉-语言-动作模型、跳层、机器人操作
