Akirarust: Re-Thinking LLM-Aided Rust Repair Using a Feedback-Guided Thinking Switch
Authors：
[Renshuang Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0838499797073653763)，[Yichong Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6115010905495054133)，[Pan Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=315543)，[Xiaoxiang Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7310101624669898445)，[Zhenling Duan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8011578913877915401)，[Tinglue Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0310428917140105595)，[Yuchen Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4116076772303443402)，[Jie Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=631231741892609642)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)

## 中文标题

Akirarust：基于反馈引导思维切换的 LLM 辅助 Rust 修复再思考

## 英文摘要

Eliminating undefined behaviors (UBs) in Rust programs requires a deep semantic understanding to enable accurate and reliable repair. While existing studies have demonstrated the potential of LLMs to support Rust code analysis and repair, most frameworks remain constrained by inflexible templates or lack grounding in executable semantics, resulting in limited contextual awareness and semantic incorrectness. Here, we present AkiraRust, an LLM-driven repair and verification framework that incorporates a finite-state machine to dynamically adapt its detection and repair flow to runtime semantic conditions. AkiraRust introduces a dual-mode reasoning strategy that coordinates fast and slow thinking across multiple agents. Each agent is mapped to an FSM state, and a waveform-driven transition controller manages state switching, rollback decisions, and semantic check pointing, enabling context-aware and runtime-adaptive repair. Experimental results show that AkiraRust achieves about 92% semantic correctness and delivers a 2.2× average speedup compared to SOTA.

## 中文摘要

消除 Rust 程序中的未定义行为（UB）需要深层的语义理解，才能实现准确可靠的修复。尽管已有研究展示了 LLM 在支持 Rust 代码分析与修复方面的潜力，但多数框架受制于僵化的模板，或缺乏可执行语义的支撑，导致上下文感知能力有限且语义不正确。本文提出 AkiraRust，一个 LLM 驱动的修复与验证框架，它引入有限状态机，使检测与修复流程能够根据运行时语义条件动态调整。AkiraRust 提出双模式推理策略，在多个智能体之间协调快思考与慢思考。每个智能体映射到一个 FSM 状态，并由波形驱动的转移控制器管理状态切换、回滚决策与语义检查点，从而实现上下文感知且运行时自适应的修复。实验结果表明，AkiraRust 达到约 92% 的语义正确率，相比 SOTA 平均加速 2.2×。
