Reconnaissance: Correctly Tracking Multiple Secrets Using Reveal/conceal Paradigms
Authors：
[Amund Bergland Kvalsvik](https://63dac.conference-program.com/?post_type=page&p=15&uid=47336670479413050821)，[Magnus Sjalander](https://63dac.conference-program.com/?post_type=page&p=15&uid=390243)

## 中文标题

Reconnaissance：利用 reveal/conceal 范式正确追踪多源秘密

## 英文摘要

Secure speculation schemes are critical for defeating speculative side-channel attacks, but often incur notable performance penalties, encouraging research into optimization strategies. One such optimization strategy, ReCon, improves performance by exploiting previous non-speculative data leakage to remove protections for already leaked data. However, we find that ReCon can leak secrets when an instruction depends on multiple sources of potentially secret data. We show how interactions between Speculative Taint Tracking (STT) and ReCon result in ReCon undermining STT’s security guarantees. We address this oversight through a low-impact multi-source tracking mechanism that we call ReConnaissance. Together with a detailed microarchitecture, we show that, on average, ReConnaissance only lowers the overhead-reduction of ReCon from 23.5% to 18.3% on SPEC2017.

## 中文摘要

安全推测方案对抵御推测执行侧信道攻击至关重要，但通常带来明显的性能损失，这促使研究者探索优化策略。其中一种优化策略 ReCon 通过利用先前非推测性的数据泄露来解除对已泄露数据的保护，从而提升性能。然而，我们发现当一条指令依赖多个可能为秘密数据的来源时，ReCon 会泄露秘密。我们展示了推测污点追踪（STT）与 ReCon 之间的交互如何导致 ReCon 破坏 STT 的安全保证。我们通过一种低影响的多源追踪机制 Reconnaissance 来弥补这一疏漏。结合详细的微架构设计，我们表明在 SPEC2017 上，Reconnaissance 平均仅将 ReCon 的开销降幅从 23.5% 降至 18.3%。
