Parallel Combinational Equivalence Checking Through Factored Form Sharing
Authors：
[Nanjiang Qu](https://63dac.conference-program.com/?post_type=page&p=15&uid=98166242110711552161)，[Cong Tian](https://63dac.conference-program.com/?post_type=page&p=15&uid=1217395031420628102)，[Nan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=438256656644428177)，[Zhenhua Duan](https://63dac.conference-program.com/?post_type=page&p=15&uid=31557981042416792431)

## 中文标题

通过因子形式共享实现并行组合等价性检查

## 英文摘要

Combinational equivalence checking (CEC) is a key and often time-critical step in the IC design flow for verifying functional equivalence after synthesis and technology mapping. As designs scale, improving CEC efficiency has become a major challenge with wide-ranging consequences for the entire flow. In this paper, we propose a novel parallel CEC approach through factored form sharing. In particular, the factored form literal count (FFLC) closely reflects both the amount of shareable literal/CNF-encoding and the branching complexity encountered during satisfiability (SAT)-based verification. Therefore, FFLC, together with a lightweight branching complexity proxy, guides a sharing-aware seed-and-grow partitioning algorithm that exploits literal and CNF-encoding reuse while balancing estimated SAT-solving complexity. Implemented in ABC and evaluated on large-scale benchmarks with 40 physical CPU cores, our implementation delivers geometric-mean speedups of 45.57× (max. 6,595×) over single-threaded ABC, 1.53× (max. 17×) over a state-of-the-art (SOTA) CPU-parallel method, and 5.52× (max. 382×) over a SOTA GPU-parallel method.

## 中文摘要

组合等价性检查（CEC）是 IC 设计流程中用于验证综合与技术映射之后功能等价性的关键步骤，且往往对时序十分敏感。随着设计规模扩大，提升 CEC 效率已成为重大挑战，并对整个流程产生广泛影响。本文提出一种通过因子形式共享的并行 CEC 新方法。具体而言，因子形式的文字数（FFLC）密切反映了可共享的文字/CNF 编码数量，以及基于可满足性（SAT）验证过程中所遇到的分支复杂度。因此，FFLC 与一个轻量的分支复杂度代理指标共同引导一种感知共享的 seed-and-grow 划分算法，该算法在利用文字与 CNF 编码复用的同时平衡预估的 SAT 求解复杂度。我们在 ABC 中实现该方法，并在大规模基准上以 40 个物理 CPU 核进行评测：相对单线程 ABC 取得 45.57 倍的几何平均加速（最高 6,595 倍），相对最先进（SOTA）的 CPU 并行方法取得 1.53 倍（最高 17 倍），相对 SOTA 的 GPU 并行方法取得 5.52 倍（最高 382 倍）。

## 英文关键词

Combinational equivalence checking, electronic design automation, factored form, branching complexity, graph partitioning

## 中文关键词

组合等价性检查、电子设计自动化、因子形式、分支复杂度、图划分
