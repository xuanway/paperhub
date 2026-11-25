From Characterization to Microarchitecture: Designing an Elegant and Reliable BFP-Based NPU
Authors：
[Jie Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=71305096419031320321)，[Jiapeng Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=30384709835922261001)，[Hao Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=6994959995200007163)，[Xiaomeng Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=1215682152008109171)，[Tinglue Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0310428917140105595)，[Ran Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=7384841273738841016)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)

## 中文标题

从特性刻画到微架构：设计优雅且可靠的基于 BFP 的 NPU

## 英文摘要

Block Floating-Point (BFP) is emerging as an attractive data format for edge Neural Processing Units (NPUs), combining wide dynamic range with high hardware efficiency. However, its behavior under hardware faults and suitability for safety-critical deployments remain underexplored. Here, we present the first in-depth empirical reliability study of BFP-based NPUs. Using RTL-level fault injection on NPUs, our bit-and path-level analysis reveals pronounced heterogeneous vulnerabilities and shows conventional end-to-end check becomes ineffective under nonlinear block scaling. Guided by these insights, we design a fault-tolerant BFP-based NPU microarchitecture that aligns the BFP computational semantics with reliability constraints. The design uses a row/column-wise blocking strategy to decouple the fixed-point mantissa computations from the scalar exponent path, and introduces ultra-lightweight protection mechanisms for each. Experimental results demonstrate our design achieves near–dual modular redundancy reliability with only 3.55% geometric mean performance overhead and less than 2% hardware cost.

## 中文摘要

块浮点（BFP）正成为一种对边缘神经处理单元（NPU）颇具吸引力的数据格式，它兼具宽动态范围与高硬件效率。然而，其在硬件故障下的行为以及面向安全关键部署的适用性仍缺乏充分研究。本文首次对基于 BFP 的 NPU 开展深入的实证可靠性研究。通过在 NPU 上进行 RTL 级故障注入，我们的位级与路径级分析揭示了显著的异构脆弱性，并表明在非线性块缩放条件下，传统的端到端校验会失效。在这些洞见的指导下，我们设计了一种容错的基于 BFP 的 NPU 微架构，使 BFP 的计算语义与可靠性约束相一致。该设计采用按行/列分块的策略，将定点尾数计算与标量指数路径解耦，并为二者分别引入超轻量级保护机制。实验结果表明，我们的设计以仅 3.55% 的几何平均性能开销和低于 2% 的硬件成本，达到了接近双模冗余（DMR）的可靠性。
