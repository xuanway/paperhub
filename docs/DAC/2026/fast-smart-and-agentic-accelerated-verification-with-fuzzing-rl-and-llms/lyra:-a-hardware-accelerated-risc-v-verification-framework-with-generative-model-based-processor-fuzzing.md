Lyra: A Hardware-Accelerated RISC-V Verification Framework with Generative Model-Based Processor Fuzzing
Authors：
[Juncheng Huo](https://63dac.conference-program.com/?post_type=page&p=15&uid=51963397112364181941)，[Yunfan Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=52909671877349841921)，[Xinxin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0946806569955931993)，[Sa Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4683934013598003811)，[Yungang Bao](https://63dac.conference-program.com/?post_type=page&p=15&uid=899243)，[Xitong Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=09143022307039896371)，[Kan Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=2618898955484321074)

## 中文标题

Lyra：基于生成模型处理器模糊测试的硬件加速 RISC-V 验证框架

## 英文摘要

As processor designs grow more complex, verification remains bottlenecked by slow software simulation and low-quality random test stimuli. Recent research has applied software fuzzers to hardware verification, but these rely on semantically blind random mutations that may generate shallow, low-quality stimuli unable to explore complex behaviors. These limitations result in slow coverage convergence and prohibitively high verification costs. In this paper, we present Lyra, a heterogeneous RISC-V verification framework that addresses both challenges by pairing hardware-accelerated verification with an ISA-aware generative model. Lyra executes the DUT and reference model concurrently on an FPGA SoC, enabling high-throughput differential checking and hardware-level coverage collection. Instead of creating verification stimuli randomly or through simple mutations, we train a domain-specialized generative model, LyraGen, with inherent semantic awareness to generate high-quality, semantically rich instruction sequences. Empirical results show Lyra achieves up to 1.27× higher coverage and accelerates end-to-end verification by up to 107× to 3343× compared to state-of-the-art software fuzzers, while consistently demonstrating lower convergence difficulty.

## 中文摘要

随着处理器设计日益复杂，验证工作仍受制于缓慢的软件仿真与低质量的随机测试激励。近期研究已将软件模糊测试器用于硬件验证，但这些方法依赖语义盲目的随机变异，可能生成浅层、低质量的激励，无法探索复杂行为。上述局限导致覆盖率收敛缓慢、验证成本高得难以承受。本文提出 Lyra，一种异构 RISC-V 验证框架，通过将硬件加速验证与具备 ISA 感知能力的生成模型相结合，同时应对这两方面挑战。Lyra 在 FPGA SoC 上并发执行 DUT 与参考模型，从而实现高吞吐的差分检查与硬件级覆盖率收集。Lyra 不采用随机生成或简单变异的方式构造验证激励，而是训练了领域专用的生成模型 LyraGen，其内建语义感知能力，可生成高质量、语义丰富的指令序列。实验结果表明，与当前最先进的软件模糊测试器相比，Lyra 的覆盖率最高提升 1.27 倍，端到端验证加速最高达 107 倍至 3343 倍，同时始终表现出更低的收敛难度。

## 英文关键词

Verification, RISC-V, LLM, FPGA

## 中文关键词

验证、RISC-V、LLM、FPGA
