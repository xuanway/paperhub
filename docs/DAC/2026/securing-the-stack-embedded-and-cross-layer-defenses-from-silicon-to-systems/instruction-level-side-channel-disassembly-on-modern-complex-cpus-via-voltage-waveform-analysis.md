Instruction-Level Side-Channel Disassembly on Modern Complex CPUs via Voltage Waveform Analysis
Authors：
[Yucheng Ji](https://63dac.conference-program.com/?post_type=page&p=15&uid=28471054730052146851)，[Ruibin Xia](https://63dac.conference-program.com/?post_type=page&p=15&uid=3105305216638777496)，[Hanyuan Zou](https://63dac.conference-program.com/?post_type=page&p=15&uid=28102862127526587011)，[Yingqi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=59806127051986494961)，[Weidong Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=30570720817238664321)，[Jiaxing Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=08358372684117887841)，[Dongsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=209438080078268597)

## 中文标题

基于电压波形分析的现代复杂 CPU 指令级侧信道反汇编

## 英文摘要

Power side-channel attacks allow adversaries to recover executed instructions and reconstruct program flow from power traces. However, existing approaches have primarily focused on low-frequency embedded platforms with relatively simple processor designs. When applied to modern commercial CPUs, complex microarchitectural behaviors, such as out-of-order execution and deep pipelining, introduce substantial execution variability and noise, severely hindering reliable instruction recovery from power measurements. In this work, we present the first systematic demonstration of instruction-level side-channel disassembly on a commercial x86 processor operating at 3.1 GHz. We construct a large-scale dataset containing 645 instructions—including AVX/SSE extensions—and more than 50,000 voltage waveform samples collected under realistic multi-threaded operating conditions. To capture cross-cycle dependencies, we propose a novel end-to-end sequence-to-sequence framework that directly reconstructs instruction sequences from voltage waveforms, integrating CNN-Conformer encoders for feature learning and Transformer decoders for sequence generation. Experiments show that our method achieves 34.70% sequence prediction accuracy, outperforming static segmentation and classifier-based baselines.

## 中文摘要

功耗侧信道攻击使攻击者能够从功耗轨迹中恢复已执行的指令并重构程序流。然而，现有方法主要针对处理器设计相对简单的低频嵌入式平台。当应用于现代商用 CPU 时，乱序执行、深流水线等复杂微架构行为会引入大量执行变异与噪声，严重阻碍从功耗测量中可靠地恢复指令。本文首次系统性地展示了在 3.1 GHz 的商用 x86 处理器上进行指令级侧信道反汇编。我们构建了一个大规模数据集，包含 645 条指令（包括 AVX/SSE 扩展）以及在真实多线程运行条件下采集的 5 万余条电压波形样本。为捕捉跨周期依赖关系，我们提出一种新颖的端到端序列到序列框架，可直接从电压波形重构指令序列，该框架集成了用于特征学习的 CNN-Conformer 编码器和用于序列生成的 Transformer 解码器。实验表明，我们的方法取得了 34.70% 的序列预测准确率，优于基于静态分割和基于分类器的基线方法。
