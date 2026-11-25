NIAQ: Adaptive Non-Ideality-Aware Qubit Readout for Long-Term Accuracy
Authors：
[Yuyang Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=00649289959229124841)，[Yi Sheng Chong](https://63dac.conference-program.com/?post_type=page&p=15&uid=7083540359758952499)，[Wang Ling Goh](https://63dac.conference-program.com/?post_type=page&p=15&uid=810843)，[Benjamin Lienhard](https://63dac.conference-program.com/?post_type=page&p=15&uid=7008907228415838397)，[Anh Tuan Do](https://63dac.conference-program.com/?post_type=page&p=15&uid=35848344950369924481)

## 中文标题

NIAQ：面向长期精度的自适应非理想性感知量子比特读出

## 英文摘要

High-accuracy qubit-state readout is critical for quantum computation. While existing hardware-based qubit-state discriminators assume stable readout statistics across measurement shots, realistic long-running tasks like chemistry simulation suffer from slow noise fluctuations and drift that severely degrade fidelity over time. We present NIAQ, an adaptive software–hardware co-design combining Kalman filtering for drift tracking with MLP discriminators for robustness against noise, together with degradation rate (%/hour) as a novel metric to quantify long-term stability. NIAQ achieves 88% qubit-state-readout accuracy in multi-qubit dataset that is equivalent to 1-day runtime, compared to the 61% baseline qubit-state discriminator, and yields 19× lower degradation rate. Optimized for low-power real-time operation on ASIC, post-synthesis results in 28-nm CMOS show 148mW power and 5ns delay, achieving 7.7× power and 6.4× latency improvements compared to the state-of-the-art.

## 中文摘要

高精度的量子态读出对量子计算至关重要。现有基于硬件的量子态判别器假设读出统计在多次测量中保持稳定，但化学模拟等真实的长时运行任务会受到缓慢噪声波动与漂移的影响，使保真度随时间严重退化。我们提出 NIAQ，一种自适应软硬件协同设计，它将用于漂移跟踪的 Kalman 滤波与对噪声鲁棒的 MLP 判别器相结合，并提出退化率（%/小时）作为量化长期稳定性的新指标。在模拟相当于 1 天运行时长的多比特数据集上，NIAQ 实现 88% 的量子态读出精度，而基线量子态判别器为 61%，同时退化率低 19 倍。面向 ASIC 上的低功耗实时运行进行优化后，28 nm CMOS 综合结果显示功耗为 148 mW、延迟为 5 ns，相较最先进工作分别实现 7.7 倍的功耗改进与 6.4 倍的延迟改进。

## 英文关键词

Quantum computing, Qubit readout, Qubit-state-discrimination

## 中文关键词

量子计算、量子比特读出、量子态判别
