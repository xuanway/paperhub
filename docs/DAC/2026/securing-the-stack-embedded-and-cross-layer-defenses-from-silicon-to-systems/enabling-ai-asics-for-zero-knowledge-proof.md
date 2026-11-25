Enabling AI ASICs for Zero Knowledge Proof
Authors：
[Jianming Tong](https://63dac.conference-program.com/?post_type=page&p=15&uid=2067527402484541245)，[Jingtian Dang](https://63dac.conference-program.com/?post_type=page&p=15&uid=336204133900391445)，[Simon Langowski](https://63dac.conference-program.com/?post_type=page&p=15&uid=7826178777516270174)，[Tianhao Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=963588903982668818)，[Asra Ali](https://63dac.conference-program.com/?post_type=page&p=15&uid=4850232369002083564)，[Jeremy Kun](https://63dac.conference-program.com/?post_type=page&p=15&uid=5782469029552616642)，[Jevin Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=57052619959538493661)，[Srinivas Devadas](https://63dac.conference-program.com/?post_type=page&p=15&uid=9707815605210864713)，[Tushar Krishna](https://63dac.conference-program.com/?post_type=page&p=15&uid=785143)

## 中文标题

面向零知识证明的 AI ASIC 使能

## 英文摘要

Zero-knowledge proof (ZKP) provers remain costly because multi-scalar multiplication (MSM) and number-theoretic transforms (NTTs) dominate runtime as they need significant computation. AI ASICs such as TPUs provide massive matrix throughput and SotA energy efficiency. We present MORPH, the first framework that reformulates ZKP kernels to match AI-ASIC execution. We introduce Big-𝑇complexity, a hardware-aware complexity model that exposes heterogeneous bottlenecks and layout-transformation costs ignored by Big-𝑂. Guided by this analysis, (1) at arithmetic level, MORPH develops an MXU-centric extended-RNS lazy reduction that converts high-precision modular arithmetic into dense low-precision GEMMs, eliminating all carry chains, and (2) at dataflow level, MORPH constructs a unified-sharding layout-stationary TPU Pippenger MSM and optimized 3/5-step NTT that avoid on-TPU shuffles to minimize costly memory reorganization. Implemented in JAX, MORPH enables TPUv6e8 to achieve up-to 10× higher throughput on NTT and comparable throughput on MSM than GZKP. Our code: https://github.com/EfficientPPML/MORPH.

## 中文摘要

零知识证明（ZKP）证明者依然代价高昂，因为多标量乘法（MSM）和数论变换（NTT）需要大量计算，主导了运行时间。TPU 等 AI ASIC 可提供海量矩阵吞吐和业界领先的能效。我们提出 MORPH，这是首个将 ZKP 内核重构以匹配 AI ASIC 执行方式的框架。我们引入 Big-T 复杂度，一种硬件感知的复杂度模型，可揭示被 Big-O 忽略的异构瓶颈与布局变换开销。在此分析指导下，(1) 在算术层面，MORPH 提出以 MXU 为中心的扩展 RNS 惰性归约，将高精度模运算转化为稠密的低精度 GEMM，从而消除所有进位链；(2) 在数据流层面，MORPH 构建了统一分片、布局固定的 TPU Pippenger MSM 以及优化的 3/5 步 NTT，避免 TPU 上的 shuffle 操作，以尽量减少代价高昂的存储重组。MORPH 在 JAX 中实现，使 TPUv6e8 在 NTT 上相比 GZKP 取得最高 10 倍的吞吐提升，在 MSM 上吞吐相当。代码：https://github.com/EfficientPPML/MORPH
