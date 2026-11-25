Finding Behavior Bugs in IoT Messaging Protocols with Automated Oracle Generation and Monitoring
Authors：
[Qingpeng Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=90613451524580256671)，[Zhengxiong Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=7742600016684910885)，[Yuanliang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=68084503999232733931)，[Fuchen Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=4903699100820810442)，[Yu Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=572143)

## 中文标题

面向 IoT 消息协议的行为缺陷检测：自动预言生成与监控

## 英文摘要

IoT messaging protocols, which govern critical device communications and resource management, have emerged as a significant attack surface in IoT systems. Behavior bugs—specification violations that manifest without observable crashes—pose severe security risks, potentially enabling unauthorized data access and device compromise. Detecting such bugs requires a comprehensive understanding of protocol specifications for oracle generation and communication semantics for accurate oracle monitoring, a challenge beyond existing approaches. This paper introduces ARES, a fully automated framework that synthesizes executable behavior oracles from protocol specifications for real-time compliance monitoring. ARES first transforms specifications into structured oracles using LLM-driven behavior filtering and condition supplementation. Then, during real-time monitoring, ARES employs scenario-aware analysis to accurately determine the most appropriate oracle among potentially overlapping candidates. We evaluate ARES on six widely used IoT protocol implementations and identify 25 new bugs, of which 18 have been confirmed or fixed, and 10 CVEs were assigned due to their severity.

## 中文摘要

IoT 消息协议掌管关键设备通信与资源管理，已成为 IoT 系统中的重要攻击面。行为缺陷——即在无可观测崩溃情况下显现的规范违背——构成严重的安全风险，可能使未授权数据访问与设备被攻陷成为可能。检测此类缺陷需要全面理解协议规范以生成预言（oracle），并理解通信语义以准确监控预言，这超出了现有方法的能力。本文提出 ARES，一个全自动框架，可从协议规范中合成可执行的行为预言，用于实时合规监控。ARES 首先借助 LLM 驱动的行为筛选与条件补充，将规范转换为结构化预言；随后在实时监控过程中采用场景感知分析，在可能重叠的候选预言中准确判定最合适的预言。我们在六种广泛使用的 IoT 协议实现上评估 ARES，发现 25 个新缺陷，其中 18 个已被确认或修复，并因其严重性获得 10 个 CVE 编号。

## 英文关键词

IoT Messaging Protocol, Protocol Testing

## 中文关键词

IoT 消息协议、协议测试
