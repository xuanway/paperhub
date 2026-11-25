Leveraging Invariants for Scalable Verification of RISC-V Cryptography Extensions
Authors：
[Kim Fahrni](https://63dac.conference-program.com/?post_type=page&p=15&uid=50711123145298566151)，[Katharina Ceesay-Seitz](https://63dac.conference-program.com/?post_type=page&p=15&uid=06155412788952055141)，[Denis Zuppiger](https://63dac.conference-program.com/?post_type=page&p=15&uid=2186792236659496756)，[Kaveh Razavi](https://63dac.conference-program.com/?post_type=page&p=15&uid=7063130398759267587)

## 中文标题

利用不变量实现 RISC-V 密码学扩展的可扩展验证

## 英文摘要

RISC-V has recently ratified a vector cryptography extension. Exhaustive formal verification of hardware designs that implement this extension is crucial for security. However, scaling verification for designs with such large bit-widths is challenging. We present the first formal verification of Marian, an open-source implementation of the RISC-V vector cryptography extensions. We show that proof modularization enables us to obtain an unbounded proof for Marian. Together with our systematic invariant identification, we reach a speedup of 2.7×. Our evaluation shows that invariants that assert properties of counters, such as bounds or directions, or handshakes are particularly effective in improving the verification times. We show the generalizability and reusability of our invariant identification methodology by formally verifying another custom implementation of RISC-V vector cryptography extensions. During verification, we found a violation that turned out to be a flaw in the specification, which is now being updated.

## 中文摘要

RISC-V 近期正式批准了向量密码学扩展。对实现该扩展的硬件设计进行穷尽式形式验证，对安全性至关重要。然而，对此类大位宽设计的验证进行扩展十分困难。我们首次给出 Marian（RISC-V 向量密码学扩展的一个开源实现）的形式验证。我们表明，证明模块化使我们能够为 Marian 获得无界证明。结合我们系统化的不变量识别，我们取得了 2.7 倍加速。评测表明，断言计数器性质（如边界或方向）或握手性质的不变量，对缩短验证时间尤为有效。我们通过形式验证另一个 RISC-V 向量密码学扩展的自定义实现，展示了该不变量识别方法的通用性与可复用性。在验证过程中，我们发现了一处违规，其最终被证明是规范中的缺陷，该规范目前正在修订。

## 英文关键词

Formal verification, invariants, hardware security, accelerators

## 中文关键词

形式验证、不变量、硬件安全、加速器
