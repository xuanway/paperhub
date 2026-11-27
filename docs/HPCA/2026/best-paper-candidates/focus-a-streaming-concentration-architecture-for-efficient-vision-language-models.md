---
title: "Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models"
description: "HPCA 2026 · Best Paper Candidates"
tags:
  - "HPCA2026"
  - "Best Paper Candidates"
---

# Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Best Paper Candidates。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Best Paper Candidates</p>
</div>

**论文链接**：
**作者**：Chiyue Wei Duke University , Cong Guo Duke University , Junyao Zhang Duke University , Haoxuan Shan Duke University , Yifan Xu Duke University , Ziyue Zhang Duke University , Yudong Liu Duke University , Qinsi Wang Duke University , Changchun Zhou Duke University , Hai "Helen" Li Duke University , Yiran Chen Duke University
**会议**：HPCA 2026

---

## 中文标题

Focus：面向高效视觉语言模型的流式浓缩架构

## 英文摘要

Vision-Language Models (VLMs) have demonstrated strong performance on tasks such as video captioning and visual question answering. However, their growing scale and video-level inputs lead to significant computational and memory overhead, posing challenges for real-time deployment on hardware accelerators. While prior work attempts to reduce redundancy via token pruning or merging, these methods typically operate at coarse granularity and incur high runtime overhead due to global token-level operations. In this study, we propose Focus, a Streaming Concentration Architecture that efficiently accelerates VLM inference through progressive, fine-grained redundancy elimination. Focus introduces a multilevel concentration paradigm that hierarchically compresses vision-language inputs at three levels: (1) semantic-guided token pruning based on textual prompts, (2) spatial-temporal block-level concentration using localized comparisons, and (3) vector-level redundancy removal via motion-aware matching. All concentration steps are tightly co-designed with the architecture to support streaming-friendly, on-chip execution. Focus leverages GEMM tiling, convolution-style layout, and cross-modal attention to minimize off-chip access while enabling high throughput. Implemented as a modular unit within a systolic-array accelerator, Focus achieves 2.4× speedup and 3.3× reduction in energy, significantly outperforming state-of-the-art accelerator in both performance and energy efficiency. Full-stack implementation of Focus is open-sourced at https://github.com/dubcyfor3/Focus.

## 中文摘要

视觉语言模型（VLM）在视频描述与视觉问答等任务上表现优异，但其规模不断增长且输入升至视频级，带来显著的计算与内存开销，给硬件加速器上的实时部署带来挑战。已有工作试图通过 token 剪枝或合并来降低冗余，但这些方法通常粒度较粗，且因全局 token 级操作而产生较高运行时开销。本研究提出 Focus，一种流式浓缩架构，通过渐进式细粒度冗余消除来高效加速 VLM 推理。Focus 引入多级浓缩范式，从三个层次逐级压缩视觉语言输入：（1）基于文本提示的语义引导 token 剪枝；（2）利用局部比较的时空块级浓缩；（3）通过运动感知匹配的向量级冗余消除。所有浓缩步骤都与架构紧耦合协同设计，以支持流式友好的片上执行。Focus 利用 GEMM 分块、卷积式布局与跨模态注意力，最大限度减少片外访问并实现高吞吐。Focus 作为脉动阵列加速器中的模块化单元实现，取得 2.4 倍加速与 3.3 倍能耗降低，在性能与能效上均显著优于最先进的加速器。Focus 的全栈实现开源于 https://github.com/dubcyfor3/Focus。
