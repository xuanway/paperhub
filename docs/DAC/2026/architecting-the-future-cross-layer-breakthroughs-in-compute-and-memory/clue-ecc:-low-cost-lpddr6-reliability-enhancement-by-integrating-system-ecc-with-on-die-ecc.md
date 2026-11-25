CLUE-ECC: Low-Cost LPDDR6 Reliability Enhancement by Integrating System ECC with On-Die ECC
Authors：
[Youngbae Kong](https://63dac.conference-program.com/?post_type=page&p=15&uid=344281489772803831)，[Jae-Youn Hong](https://63dac.conference-program.com/?post_type=page&p=15&uid=922743)，[Jongwoo Jeon](https://63dac.conference-program.com/?post_type=page&p=15&uid=8465377134848427331)，[Junki Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=89510931769883453071)，[Young Jung Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=87679106865309815371)，[Joon-Sung Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=061143)

## 中文标题

CLUE-ECC：通过将系统 ECC 与片上 ECC 集成实现低成本 LPDDR6 可靠性增强

## 英文摘要

DRAM scaling to meet the growing memory demands of edge devices increases vulnerability to peripheral-induced multi-bit faults, making symbol-level error correcting codes (ECCs) essential. The emerging LPDDR6 standard introduces a 12-bit data beat that misaligns with industry-standard Reed-Solomon (RS) codes designed for power-of-two symbol widths. This misalignment creates a dilemma in which the 8-bit RS code lacks sufficient correction capability, while the 12-bit RS code exceeds the parity budget. To ensure reliability while maintaining the parity budget, this paper presents CLUE-ECC. CLUE-ECC synergistically handles the 16-bit on-die parity and the 16-bit system ECC parity as a single combined 32-bit parity, providing on-die correction of any error within a single beat. CLUE-ECC operates within the standard 288-bit LPDDR6 packet while preserving the original 8-bit RS error correction capability of the system ECC. Evaluations show that CLUE-ECC delivers consistently superior error handling and achieves hardware savings of 14.83% in area and 24.18% in power, compared to a conventional 12-bit RS code, highlighting the efficiency of CLUE-ECC.

## 中文摘要

为满足边缘设备日益增长的存储需求，DRAM 的微缩使其更易受到外围电路引发的多位故障影响，因而符号级纠错码（ECC）变得不可或缺。新兴的 LPDDR6 标准引入了 12 位数据节拍（beat），这与面向 2 的幂次符号宽度设计的工业标准里德-所罗门（RS）码不匹配。这种不匹配造成两难局面：8 位 RS 码纠错能力不足，而 12 位 RS 码又超出校验位预算。为在保持校验位预算的同时确保可靠性，本文提出 CLUE-ECC。CLUE-ECC 将 16 位片上校验位与 16 位系统 ECC 校验位协同处理为单一的 32 位组合校验位，可在单个数据节拍内实现任意错误的片上纠正。CLUE-ECC 在标准 288 位 LPDDR6 数据包内工作，同时保留系统 ECC 原有的 8 位 RS 纠错能力。评估表明，与传统 12 位 RS 码相比，CLUE-ECC 具有始终更优的错误处理能力，并在面积上节省 14.83%、在功耗上节省 24.18% 的硬件开销，凸显了 CLUE-ECC 的高效性。
