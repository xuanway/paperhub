BREW-RC: Bit-Exact Recovery of ECCs from Write Timing in ReRAM Crossbars
Authors：
[Tyler Sheaves](https://63dac.conference-program.com/?post_type=page&p=15&uid=0205292538273059851)，[Alric Althoff](https://63dac.conference-program.com/?post_type=page&p=15&uid=4177824272600962904)，[Dustin Richmond](https://63dac.conference-program.com/?post_type=page&p=15&uid=06314994177460618921)

## 中文标题

BREW-RC：从 ReRAM 交叉阵列写时序中比特级精确恢复 ECC

## 英文摘要

We present BREW-RC, a non-invasive technique that uses a novel timing side channel to reverse engineer error-correcting codes (ECCs) in ReRAM crossbar memories. ECCs extend data words with parity bits, forming codewords. These parity bits cannot be read directly, but BREW-RC reveals them by using write latency variability to determine the aggregate polarity of codeword transitions. Timing perturbations caused by ECC parity bit updates are encoded as a SAT instance whose solution yields the bit-exact parity submatrix. Knowledge of the parity submatrix enables: (1) improved timing models for side-channel attacks/mitigations and latency-sensitive applications, and (2) ECC-aware reliability characterization of devices whose error correction capabilities are unadvertised. We demonstrate BREW-RC on two commercial ReRAM products, recovering the complete ECC from multiple samples of each.

## 中文摘要

我们提出 BREW-RC，一种利用新颖时序侧信道对 ReRAM 交叉阵列存储器中的纠错码（ECC）进行逆向工程的非侵入式技术。ECC 以校验位扩展数据字，构成码字。这些校验位无法被直接读取，而 BREW-RC 借助写延迟的可变性判定码字跳变的聚合极性，从而将其揭示出来。由 ECC 校验位更新所引起的时序扰动被编码为 SAT 实例，其解可给出比特级精确的校验子矩阵。掌握校验子矩阵可带来两方面收益：(1) 为侧信道攻击/防御以及延迟敏感应用提供更优的时序模型；(2) 对未公开纠错能力的器件开展 ECC 感知的可靠性表征。我们在两款商用 ReRAM 产品上演示了 BREW-RC，并从每款产品的多个样本中恢复了完整 ECC。

## 英文关键词

Reverse engineering, Resistive RAM, Hardware security

## 中文关键词

逆向工程、阻变存储器、硬件安全
