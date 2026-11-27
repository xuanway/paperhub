Thrend: Mitigating Counting Thread-Based Fine-Grained Timing on Arm and Apple CPUs
Authors：
[Chang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67239484892132138811)，[feng shuaihu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67351734849321378571)，[Jiaqi Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=2182113981665739499)，[Hongpei Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=65454221681834407711)，[Aodong Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=97281504425173782971)，[Jian Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=4795728822119914455)，[Yuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=8960844496715770344)，[Trevor E. Carlson](https://63dac.conference-program.com/?post_type=page&p=15&uid=252143)，[Dongsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=209438080078268597)

## 中文标题

Thrend：缓解 Arm 与 Apple CPU 上基于计数线程的细粒度时序攻击

## 英文摘要

This paper presents Thrend, the first defense that mitigates counting threads used in timing side-channel attacks on Arm and Apple CPUs through real-time monitoring and scheduling. Thrend leverages fuzzing to automatically generate high-quality counting threads for training, and detects them by sampling hardware performance counters. For suspected counting threads, Thrend prevents effective timing measurements by co-scheduling the attacker threads and the counting threads on the same core. We implement Thrend on four Arm and Apple devices. Under a sampling rate of 100 Hz, Thrend achieves 99.71% detection accuracy, a 0% false-negative rate, and incurs less than 1.42% runtime overhead.

## 中文摘要

本文提出 Thrend，这是首个通过实时监控与调度来缓解 Arm 与 Apple CPU 上用于时序侧信道攻击的计数线程的防御方案。Thrend 利用模糊测试自动生成高质量的计数线程用于训练，并通过采样硬件性能计数器来检测它们。对于可疑的计数线程，Thrend 通过将攻击者线程与计数线程共同调度到同一核心上，使其无法进行有效的时序测量。我们在四款 Arm 与 Apple 设备上实现了 Thrend。在 100 Hz 采样率下，Thrend 达到 99.71% 的检测准确率、0% 的漏报率，运行时开销低于 1.42%。

## 英文关键词

side-channel defense; counting thread; performance monitoring

## 中文关键词

侧信道防御、计数线程、性能监控
