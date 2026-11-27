---
title: "Intermittence-Aware Cache Compression"
description: "HPCA 2026 · Caching and Prefetching"
tags:
  - "HPCA2026"
  - "Caching and Prefetching"
---

# Intermittence-Aware Cache Compression

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Caching and Prefetching。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Caching and Prefetching</p>
</div>

**论文链接**：
**作者**：Gan Fang Purdue University , Jianping Zeng Arizona State University , Yuchen Zhou Purdue University , Changhee Jung Purdue University, USA
**会议**：HPCA 2026

---

## 中文标题

感知间歇性的缓存压缩

## 英文摘要

Cache compressions are proven effective in improving the performance of caches in conventional processors. They compress data into a smaller size, allowing caches to accommodate more blocks. This helps reduce cache misses and expensive memory accesses, ultimately improving performance. However, conventional cache compression is less effective for energy harvesting systems (EHSs) which experience frequent power failure, as many compressed blocks end up not being used before their loss upon power outage. This wastes hard-won energy, which would otherwise be used for making more program progress. To address this issue, this paper introduces Kagura, an adaptive cache compression extension with frequent power failure in mind. Specifically, Kagura disables cache compression when it finds out that many cached blocks are unlikely to be reused before the next power outage. That way, Kagura avoids the energy waste on useless compressions/decompressions, and the resulting speedup is on par with the ideal intermittence-aware cache compressor. Experimental results show that when combined with an existing cache compressor, Kagura reduces the total energy consumption by an average of 4.53% (up to 16.21%) and improves the performance by an average of 4.74% (up to 17.87%) compared to the baseline EHS without cache compression.

## 中文摘要

缓存压缩已被证明能有效提升传统处理器中缓存的性能。它把数据压缩到更小的尺寸，使缓存能容纳更多数据块，从而减少缓存缺失与昂贵的内存访问，最终提升性能。然而，对于频繁遭遇断电的能量采集系统（EHS）而言，传统缓存压缩效果较差，因为许多压缩后的数据块在断电丢失之前根本未被使用。这浪费了来之不易的能量，而这些能量本可用于推进更多程序执行。为解决该问题，本文提出 Kagura，一种针对频繁断电场景的自适应缓存压缩扩展。具体而言，当 Kagura 发现许多缓存块在下次断电前不太可能被复用时，便关闭缓存压缩。如此，Kagura 避免了无用压缩/解压缩造成的能量浪费，其带来的加速比与理想的感知间歇性缓存压缩器相当。实验结果表明，与未使用缓存压缩的基线 EHS 相比，Kagura 与现有缓存压缩器结合使用时，平均降低总能耗 4.53%（最高 16.21%），平均提升性能 4.74%（最高 17.87%）。
