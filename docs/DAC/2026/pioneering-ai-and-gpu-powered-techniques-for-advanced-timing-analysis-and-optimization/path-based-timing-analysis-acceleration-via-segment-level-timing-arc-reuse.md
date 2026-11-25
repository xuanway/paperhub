Path-Based Timing Analysis Acceleration via Segment-Level Timing Arc Reuse
Authors：
[Yuyang Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=8432721704885972621)，[Xiangfei Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=13666140776421162511)，[Leyun Tian](https://63dac.conference-program.com/?post_type=page&p=15&uid=54684549801941577081)，[Chang Meng](https://63dac.conference-program.com/?post_type=page&p=15&uid=124843)，[Qing He](https://63dac.conference-program.com/?post_type=page&p=15&uid=16397864485345247811)，[Longxing Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=079143)

## 中文标题

基于段级时序弧复用的路径级时序分析加速

## 英文摘要

Path-Based Static Timing Analysis (PBA) ensures sign-off accuracy but suffers from excessive runtime. We propose a novel PBA acceleration framework that reduces computational complexity through segment-level timing arc reuse, rather than merely speeding up per-arc computations. By decomposing timing paths into multi-fanin-bounded segments, we enable delay reuse across structurally identical contexts. A dual-indexed SegHashMap caches segment delays under varying input slews using red-black trees. To ensure error-bound reuse, we train a slew-sensitive timing model with multi-view NLDM embedding and Sobolev-aligned supervision to preserve delay gradients. Our segment-centric engine reconstructs path delays via reusable segments with bounded pessimism. Experiments show our method achieves an average 195× speedup over parallel PBA baselines while preserving accuracy and pessimism, and 2–3× faster than GPU-based methods on CPU alone.

## 中文摘要

路径级静态时序分析（PBA）可保证签核精度，但运行时间过长。我们提出一种新颖的 PBA 加速框架，通过段级时序弧复用降低计算复杂度，而非仅仅加速单条弧的计算。我们将时序路径分解为受多扇入边界约束的段，从而在结构相同的上下文中实现延迟复用。双索引 SegHashMap 使用红黑树缓存不同输入转换（slew）下的段延迟。为确保误差有界的复用，我们训练了一个对 slew 敏感的时序模型，采用多视角 NLDM 嵌入与 Sobolev 对齐监督以保持延迟梯度。我们的段中心引擎通过可复用的段以有界悲观度重建路径延迟。实验表明，该方法在保持精度与悲观度的同时，相较并行 PBA 基线平均取得 195 倍加速，且仅用 CPU 即比基于 GPU 的方法快 2–3 倍。
