Phantom Walk: Reducing the Post-Migration Translation Path via Proactive Translation Dissemination in Multi-GPU Systems
Authors：
[Jihun Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=80487001044586093211)，[Jaesang Moh](https://63dac.conference-program.com/?post_type=page&p=15&uid=9580151362065867698)，[Tae Hee Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=0519593218320928626)

## 中文标题

Phantom Walk：通过多 GPU 系统中主动的地址翻译传播缩短迁移后翻译路径

## 英文摘要

Multi-GPU systems rely on unified virtual memory to provide a global address space, which inevitably triggers page migrations. Our analysis shows that reducing migrations further is difficult even with advanced policies. These migrations invalidate page table entries (PTEs) across GPUs and generate migration-induced misses (M-misses), which constitute a large portion of all translation requests and significantly degrade performance. This paper introduces Phantom Walk, which accelerates M-miss address translation by reducing GPU-local page faults and page table walks through a shorter post-migration translation path. Our evaluation shows that Phantom Walk improves overall performance by 44.37% on average.

## 中文摘要

多 GPU 系统依赖统一虚拟内存提供全局地址空间，这不可避免地会触发页迁移。我们的分析表明，即使采用先进策略，进一步减少迁移也很困难。这些迁移会使各 GPU 的页表项（PTE）失效并产生迁移引发的缺失（M-miss），后者占全部翻译请求的很大一部分，并显著降低性能。本文提出 Phantom Walk，它通过更短的迁移后翻译路径减少 GPU 本地缺页与页表遍历，从而加速 M-miss 地址翻译。我们的评估表明，Phantom Walk 平均将整体性能提升了 44.37%。

## 英文关键词

multi-GPU, address translation, page migration, invalidation

## 中文关键词

多 GPU、地址翻译、页迁移、失效
