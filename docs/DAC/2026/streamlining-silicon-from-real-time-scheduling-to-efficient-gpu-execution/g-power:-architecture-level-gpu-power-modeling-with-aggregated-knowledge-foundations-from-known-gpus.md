G-Power: Architecture-Level GPU Power Modeling with Aggregated Knowledge Foundations from Known GPUs
Authors：
[Qijun Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7306866826013265809)，[Yao Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6294307449303409391)，[Shang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7888404795171209433)，[Mengming Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=69110175844035149381)，[Chen Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9659998036895331133)，[Dongbo Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=03089480572854093851)，[Zhiyao Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=263843)

## 中文标题

G-Power：借助已知 GPU 聚合知识基座的架构级 GPU 功耗建模

## 英文摘要

Graphics Processing Units (GPUs) have been serving as critical computation resources for large-scale parallel computations. With increasing chip complexity, power efficiency has become an important design objective for modern GPUs. GPU power optimization relies on fast power evaluation, requiring architecture-level GPU power model. However, because of the time-consuming power label collection, only simple microbenchmarks are adopted for training. The limitation of microbenchmarks as training data incurs low accuracy for existing architecture-level GPU power models like AccelWattch. To address the limitation of microbenchmarks as training data, we propose G-Power, an architecture-level GPU power modeling framework that utilizes additional known GPU chips to provide additional knowledge. G-Power utilizes the aggregated knowledge foundation from additional known GPU chips and then performs fine-tuning on our target GPU. To provide foundations with additional known GPU chips and capture the similarity to utilize these foundations for fine-tuning, G-Power adopts a three-phase algorithm consisting of 1) pre-training with additional known chips, 2) attention-inspired aggregation, and 3) fine-tuning on our target GPU. We evaluate G-Power on four modern NVIDIA GPUs, demonstrating high accuracy. G-Power can achieve a low MAPE of 14% and a high correlation coefficient 𝑅of 0.88 on average, which are 22% lower MAPE and 0.36 higher 𝑅than AccelWattch.

## 中文摘要

图形处理器（GPU）一直是大规模并行计算的关键算力资源。随着芯片复杂度上升，能效已成为现代 GPU 的重要设计目标。GPU 功耗优化依赖快速的功耗评估，因而需要架构级 GPU 功耗模型。然而，由于功耗标签采集耗时，现有工作只能采用简单的微基准进行训练。训练数据局限于微基准，导致 AccelWattch 等现有架构级 GPU 功耗模型精度偏低。为突破微基准作为训练数据的局限，我们提出 G-Power，一个利用额外已知 GPU 芯片提供额外知识的架构级 GPU 功耗建模框架。G-Power 利用来自额外已知 GPU 芯片的聚合知识基座，并在目标 GPU 上进行微调。为提供来自额外已知 GPU 芯片的知识基座并捕捉相似性以用于微调，G-Power 采用三阶段算法：1）在额外已知芯片上预训练，2）受注意力机制启发的聚合，3）在目标 GPU 上微调。我们在四款现代 NVIDIA GPU 上评估 G-Power，展现出很高的精度。G-Power 平均可达到 14% 的低 MAPE 和 0.88 的高相关系数 R，相较 AccelWattch 的 MAPE 低 22%、R 高 0.36。

## 英文关键词

Power model, machine learning

## 中文关键词

功耗模型、机器学习
