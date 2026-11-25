Slicemoe: Bit-Sliced Expert Caching Under Miss-Rate Constraints for Efficient MoE Inference
Authors：
[Yuseon Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=5211726504378555252)，[Sangjin Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=6931698093276395635)，[Jungjun Oh](https://63dac.conference-program.com/?post_type=page&p=15&uid=49645038213445125931)，[Gwangtae Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=5234563924517782774)，[Byeongcheol Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=86237849640593227351)，[Hoi-Jun Yoo](https://63dac.conference-program.com/?post_type=page&p=15&uid=95077588560233239951)

## 中文标题

SliceMoE：未命中率约束下面向高效 MoE 推理的位切片专家缓存

## 英文摘要

MoE models offer efficient scaling through conditional computation, but their large parameter size and expensive expert offloading make on-device deployment challenging. Existing acceleration techniques such as prefetching or expert clustering often increase energy usage or reduce expert diversity. We present SliceMoE, an energy-efficient MoE inference framework for miss-rate–constrained deployment. SliceMoE introduces Dynamic Bit-Sliced Caching (DBSC), which caches experts at slice-level granularity and assigns precision on demand to expand effective expert capacity. To support mixed-precision experts without memory duplication, we propose Calibration-Free Asymmetric Matryoshka Quantization (AMAT), a truncation-based scheme that maintains compatibility between low-bit and high-bit slices. We further introduce Predictive Cache Warmup (PCW) to reduce early-decode cold misses by reshaping cache contents during prefill. Evaluated on DeepSeek-V2-Lite and Qwen1.5-MoE-A2.7B, SliceMoE reduces decode-stage energy consumption by up to 2.37× and 2.85×, respectively, and improves decode latency by up to 1.81× and 1.64×, while preserving near–high-bit accuracy. These results demonstrate that slice-level caching enables efficient on-device MoE deployment.

## 中文摘要

MoE 模型通过条件计算实现了高效的规模扩展，但其庞大的参数规模和昂贵的专家卸载开销使端侧部署颇具挑战。已有的预取、专家聚类等加速技术往往会增加能耗或降低专家多样性。我们提出 SliceMoE，一种面向未命中率受限场景的节能 MoE 推理框架。SliceMoE 引入动态位切片缓存（DBSC），以切片粒度缓存专家并按需分配精度，从而扩展有效专家容量。为在不产生存储副本的前提下支持混合精度专家，我们提出免校准的非对称 Matryoshka 量化（AMAT），这是一种基于截断的方案，可保持低比特与高比特切片之间的兼容性。我们进一步引入预测式缓存预热（PCW），通过在 prefill 阶段重塑缓存内容来减少解码初期的冷未命中。在 DeepSeek-V2-Lite 与 Qwen1.5-MoE-A2.7B 上的评测表明，SliceMoE 分别将解码阶段能耗最多降低 2.37× 和 2.85×，解码延迟最多改善 1.81× 和 1.64×，同时保持接近高比特的精度。这些结果表明，切片级缓存能够支撑高效的端侧 MoE 部署。

## 英文关键词

Mixture-of-Experts (MoE) inference, bit-sliced architecture, mixed-precision, and cache-aware routing

## 中文关键词

混合专家（MoE）推理、位切片架构、混合精度、缓存感知路由
