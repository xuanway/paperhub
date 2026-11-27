---
title: "PinDrop: Breaking the Silence on SDCs in a Large-Scale Fleet"
description: "HPCA 2026 · Best Paper Candidates"
tags:
  - "HPCA2026"
  - "Best Paper Candidates"
---

# PinDrop: Breaking the Silence on SDCs in a Large-Scale Fleet

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Best Paper Candidates。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Best Paper Candidates</p>
</div>

**论文链接**：
**作者**：Peter W. Deutsch Massachusetts Institute of Technology/Meta , Harish D. Dixit Meta , Gautham Vunnam Meta , Carl Moran Meta , Eleanor Ozer Meta , Sriram Sankar Meta
**会议**：HPCA 2026

---

## 中文标题

PinDrop：打破大规模机群中 SDC 的沉默

## 英文摘要

Silent Data Corruptions (SDCs) pose a significant and often hidden threat to the reliability of large-scale computing infrastructure, as they can silently compromise data integrity without immediate detection. Detecting such behaviors at hyper-scale is often challenging due to their intermittent nature and the vast diversity of hardware and workloads in a large-scale fleet. This work addresses these challenges by introducing PinDrop, a characterization methodology that leverages continuous, high-frequency testing infrastructure across millions of servers to gather information about SDCs at scale. By leveraging extensive test-suites tailored to mimic real-world applications and exercise a wide range of CPU features, we provide the most comprehensive characterization of SDC failures to date, analyzing over 500 million test executions across millions of devices. Our findings reveal that 0.035% of tested machines suffer from at least one SDC failure during their lifetime. Examining years of data (rather than just a testing snapshot in time), we observe SDCs emerging long after initial deployment and persisting over time. Detailed analysis shows that an average of 0.0024% of tested machines begin failing in each quarter they are tested beyond an initial burn-in period, confirming a fundamental need for continuous testing. Our findings also provide further insights into SDC behaviors at-scale, including failure breakdowns across architectures, test families, specific core IDs, and output-level behaviors.

## 中文摘要

静默数据损坏（SDC）对大规模计算基础设施的可靠性构成重大且常被忽视的威胁，因为它可在无即时检测的情况下静默破坏数据完整性。在超大规模下检测此类行为往往十分困难，原因在于其间歇性以及大规模机群中硬件与负载的巨大多样性。本工作通过引入 PinDrop 来应对这些挑战：这是一种表征方法，利用覆盖数百万台服务器的持续高频测试基础设施，大规模收集 SDC 信息。借助为模拟真实应用并覆盖广泛 CPU 特性而定制的丰富测试套件，我们提供了迄今最全面的 SDC 失效表征，分析了跨数百万设备的超过 5 亿次测试执行。我们发现，0.035% 的受测机器在其生命周期内至少遭遇一次 SDC 失效。通过考察多年数据（而非某一时点的测试快照），我们观察到 SDC 在初始部署很久之后才出现并持续存在。详细分析显示，在初始老化期之后，受测机器平均每季度有 0.0024% 开始失效，证实了持续测试的根本必要性。我们的发现还就大规模 SDC 行为提供了进一步洞见，包括按架构、测试族、具体核心 ID 以及输出级行为的失效分解。
