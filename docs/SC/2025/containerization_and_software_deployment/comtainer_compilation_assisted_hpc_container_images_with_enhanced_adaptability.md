---
title: "coMtainer: Compilation-Assisted HPC Container Images with Enhanced Adaptability"
description: "SC 2025 · Containerization and Software Deployment · Yuhao Gu; Haoquan Chen; Xianjie Chen; Jiangsu Du; Zhiguang Chen; Nong Xiao; Xian"
tags:
  - "SC2025"
  - "Containerization and Software Deployment"
---

# coMtainer: Compilation-Assisted HPC Container Images with Enhanced Adaptability

**中文标题：** 编译辅助的高适应性 HPC 容器镜像

**所属 Session：** [Containerization and Software Deployment](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Containerization and Software Deployment。</p>
<p class="paper-seo-summary__tags">SC 2025 · Containerization and Software Deployment</p>
</div>

**作者**：Yuhao Gu; Haoquan Chen; Xianjie Chen; Jiangsu Du; Zhiguang Chen; Nong Xiao; Xianwei Zhang; Yutong Lu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap234&sess=sess171)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The increasing interconnectivity of HPC systems has highlighted the need for efficient application migration across different environments. Containers, widely adopted for this purpose, simplify deployment but often fail to deliver optimal performance due to the separated build and execution container workflow. This leads to generic container images that miss out on system-specific software stack advantages, a challenge we define as the adaptability issue. We propose coMtainer, a compilation-assisted image transformation framework that embeds build-time information into images. This enables remote HPC systems to specialize and rebuild the container using native toolchains and libraries. coMtainer preserves image neutrality while resolving the adaptability issue, allowing optimized execution without user involvement. Moreover, the embedded metadata unlocks advanced compiler optimizations such as LTO and PGO. We implement and evaluate coMtainer across a variety of real-world HPC applicati

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
