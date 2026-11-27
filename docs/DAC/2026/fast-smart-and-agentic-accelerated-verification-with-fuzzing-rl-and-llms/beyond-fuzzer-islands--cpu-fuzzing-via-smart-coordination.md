Beyond Fuzzer Islands: CPU Fuzzing via Smart Coordination
Authors：
[Yuchen Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4116076772303443402)，[Jialin Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=45764671121687500671)，[Yushu Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=3629806380220939574)，[Renshuang Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0838499797073653763)，[Ning Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0664891654584882089)，[Weiwei Shan](https://63dac.conference-program.com/?post_type=page&p=15&uid=0055055425813703702)，[Xinwei Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7117674552267504328)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)

## 中文标题

超越模糊测试孤岛：借助智能协同的 CPU 模糊测试

## 英文摘要

Despite recent progress, every CPU fuzzer explores only a narrow slice of the vast micro-architectural state space due to its fixed mutation and feedback biases. While different fuzzers thus excel in disjoint regions, naïve combination fails because of conflicting strategies, seed pollution, and early saturation. LiFU introduces micro-architecture-aware orchestration that dynamically profiles heterogeneous fuzzers, detects complementary strengths, decreases harmful interactions, and steers each fuzzer in real time using coverage and bug feedback, augmented by semantic seed triage. Evaluated on the BOOM core, LiFU achieves 93.4% line, 43.6% FSM, and 95.7% condition coverage (90.1%, 75.0%, 78.3% on Rocket) with around 40% fewer tests than the best standalone fuzzer, consistently closing long-standing verification gaps in modern CPU.

## 中文摘要

尽管近来取得了进展，但每个 CPU 模糊测试器都因其固定的变异与反馈偏好，只能在庞大的微架构状态空间中探索很窄的一部分。因此，不同模糊测试器在互不相交的区域各有所长，而简单组合却会因策略冲突、种子污染和过早饱和而失败。LiFU 引入微架构感知的编排机制，能够动态剖析异构模糊测试器、识别其互补优势、减少有害交互，并利用覆盖率与缺陷反馈实时引导各模糊测试器，同时辅以语义化的种子分诊。在 BOOM 核上的评测显示，LiFU 达到 93.4%的行覆盖率、43.6%的 FSM 覆盖率和 95.7%的条件覆盖率（在 Rocket 上分别为 90.1%、75.0%和 78.3%），而所用测试数量比最佳单一模糊测试器少约 40%，持续弥合了现代 CPU 中长期存在的验证缺口。
