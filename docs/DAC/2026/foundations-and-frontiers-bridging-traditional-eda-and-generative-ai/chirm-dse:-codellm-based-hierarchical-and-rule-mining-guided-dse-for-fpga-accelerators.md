CHiRM-DSE: CodeLLM-Based Hierarchical and Rule-Mining Guided DSE for FPGA Accelerators
Authors：
[Shi Chao](https://63dac.conference-program.com/?post_type=page&p=15&uid=7331806124890202513)，[teng wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=652843)，[Zhu Qinggang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3236825820815772821)，[Qianyu Cheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=452843)，[Jing Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=14736847864820468471)，[Wenqi Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=425843)，[Lei Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=852843)，[Zhou Xuehai](https://63dac.conference-program.com/?post_type=page&p=15&uid=6181174387158167145)

## 中文标题

CHiRM-DSE：面向 FPGA 加速器的基于 CodeLLM 的分层与规则挖掘引导 DSE

## 英文摘要

High-Level Synthesis (HLS) lowers the barrier to FPGA development by allowing a wider range of programmers to design hardware accelerators. However, determining the appropriate synthesis directives (pragmas) remains a major challenge, particularly for developers without hardware expertise. As designs grow more complex and the pragma search space expands, choosing the right pragmas becomes essential for achieving low resource usage and high performance. Automated design space exploration (DSE) provides an effective solution to this challenge. The enormous search space and time-consuming design-point evaluation highlight the need for efficient search strategies. However, existing search strategies mostly rely on inefficient exhaustive search, hyperparameter-sensitive metaheuristic methods, or dedicated methods that are difficult to port and generalize. To address these issues, we propose a rule-mining-based search strategy that efficiently guides exploration toward the most promising regions of the design space. In addition, we introduce a design space decomposition method to prune the search space, as well as a CodeLLM-based design-point evaluation method, which is both faster than directly invoking HLS tools, and more accurate than prior GNN-based approaches. Experimental results on four widely-used HLS benchmarks demonstrate that, under the same time budget, our DSE framework achieves better Quality of Results (QoR) than the state of the art. Our demo code is released at https://github.com/ScopeHLS/CHiRM-DSE

## 中文摘要

高层综合（HLS）允许更广泛的程序员参与硬件加速器设计，从而降低了 FPGA 开发的门槛。然而，确定合适的综合指示（pragma）仍是一项主要挑战，对于缺乏硬件专业知识的开发者尤为如此。随着设计日益复杂、pragma 搜索空间不断扩大，选择合适的 pragma 对于实现低资源占用与高性能至关重要。自动化设计空间探索（DSE）为这一挑战提供了有效解决方案。庞大的搜索空间与耗时的设计点评估，凸显了高效搜索策略的必要性。然而，现有搜索策略大多依赖低效的穷举搜索、对超参数敏感的超启发式方法，或难以移植与泛化的专用方法。为解决这些问题，我们提出一种基于规则挖掘的搜索策略，可高效引导探索走向设计空间中最具前景的区域。此外，我们引入一种设计空间分解方法来剪枝搜索空间，并提出一种基于 CodeLLM 的设计点评估方法，它既比直接调用 HLS 工具更快，也比此前基于 GNN 的方法更准确。在四个广泛使用的 HLS 基准上的实验结果表明，在相同时间预算下，我们的 DSE 框架取得了优于现有最佳方法的结果质量（QoR）。演示代码已发布于 https://github.com/ScopeHLS/CHiRM-DSE

## 英文关键词

FPGA accelerator design, High-Level Synthesis (HLS), Design Space Exploration (DSE), CodeLLM, Rule Mining, AI-guided synthesis optimization, AI for EDA

## 中文关键词

FPGA 加速器设计、高层综合（HLS）、设计空间探索（DSE）、CodeLLM、规则挖掘、AI 引导的综合优化、面向 EDA 的 AI
