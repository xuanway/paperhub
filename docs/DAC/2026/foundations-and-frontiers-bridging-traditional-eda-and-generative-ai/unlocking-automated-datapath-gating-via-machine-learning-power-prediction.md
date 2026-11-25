Unlocking Automated Datapath Gating via Machine Learning Power Prediction
Authors：
[Felipe Marranghello](https://63dac.conference-program.com/?post_type=page&p=15&uid=581343)，[Giulia Meuli](https://63dac.conference-program.com/?post_type=page&p=15&uid=20616504444096028071)，[Barkha Gupta](https://63dac.conference-program.com/?post_type=page&p=15&uid=62654032207936557061)，[Alessandro Tempia Calvino](https://63dac.conference-program.com/?post_type=page&p=15&uid=5501486752926311501)，[Eleonora Testa](https://63dac.conference-program.com/?post_type=page&p=15&uid=481343)，[Walter Lau Neto](https://63dac.conference-program.com/?post_type=page&p=15&uid=59524603394751228521)，[Patrick Vuillod](https://63dac.conference-program.com/?post_type=page&p=15&uid=881343)，[Luca Amaru](https://63dac.conference-program.com/?post_type=page&p=15&uid=071343)

## 中文标题

借助机器学习功耗预测实现自动化数据通路门控

## 英文摘要

Clock gating and data gating are established techniques for reducing dynamic power. However, performing automated data gating during logic synthesis remains challenging due to the difficulty of accurately estimating power savings and identifying common Observability Don’t Care (ODC) conditions for the enabling logic. This work introduces a novel methodology that addresses both challenges: it introduces a novel SAT-based technique to compute valid ODC conditions and employs a machine learning-based power model to predict power improvements with high accuracy. The approach is integrated into an industrial synthesis flow and achieves efficient, fully automated data gating. We show that, when multiple datapaths exist, gating always yields compatible ODCs from a functional point of view, and introduce the concept of structurally compatible ODCs. Experimental results demonstrate an average total power reduction of -1% (up to -13.9%) post place & route, with negligible area and runtime overhead, establishing a new paradigm for ML-driven power optimization in next-generation EDA tools.

## 中文摘要

时钟门控与数据门控是降低动态功耗的成熟技术。然而，在逻辑综合过程中实现自动化数据门控仍具挑战，原因在于难以准确估计功耗节省量，也难以确定使能逻辑的公共可观测无关项（ODC）条件。本工作提出一种新方法以同时应对这两项挑战：引入一种新颖的基于 SAT 的技术来计算有效 ODC 条件，并采用基于机器学习的功耗模型以高精度预测功耗改善。该方法已集成到工业综合流程中，实现了高效、全自动的数据门控。我们证明，当存在多条数据通路时，从功能角度看门控总能产生相互兼容的 ODC，并提出结构兼容 ODC 的概念。实验结果表明，在布局布线后总功耗平均降低 1%（最高达 13.9%），而面积与运行时间开销可忽略，为下一代 EDA 工具中由机器学习驱动的功耗优化树立了新范式。

## 英文关键词

datapath gating, dynamic power, power optimization, machine learning, power prediction

## 中文关键词

数据通路门控、动态功耗、功耗优化、机器学习、功耗预测
