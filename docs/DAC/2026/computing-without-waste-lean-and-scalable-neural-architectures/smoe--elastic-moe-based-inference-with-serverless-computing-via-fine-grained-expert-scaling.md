Smoe: Elastic MoE-Based Inference with Serverless Computing via Fine-Grained Expert Scaling
Authors：
[Xiaofei Yue](https://63dac.conference-program.com/?post_type=page&p=15&uid=00643431274709905571)，[Ziming Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=067079871260242006)，[Jiongchi Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5358980283737154945)，[Huidong Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=0882738464605402632)，[Zhaoxuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=49898124216175777231)，[Tingting Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=5963119447382350714)，[Jianwei Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=13548133920903114011)

## 中文标题

sMoE：通过细粒度专家伸缩实现基于无服务器计算的弹性 MoE 推理

## 英文摘要

Mixture-of-Experts (MoE) architecture enables large-scale inference via sparse activation, but skewed, time-varying expert popularity leads to cost-inefficiency. Serverless computing is an attractive substrate due to its fine-grained resource elasticity and billing. Even so, achieving cost-efficient and SLO-compliant scaling for each expert with intra-and inter-layer dependencies under concurrent requests remains fraught with challenges. In this paper, we present sMoE, a topology-aware elastic auto-scaler for serverless MoE inference. Our insight is to treat the deployment of a MoE inference pipeline as a DAG of experts and non-MoE segments. Building on this, sMoE is designed as a deep reinforcement learning-based solution. Specifically, it encodes expert-and layer-level runtime features with DAGNN by propagating cross-layer semantics. Coupled with a layer-wise pointer network, sMoE captures intra-layer semantics to jointly decide vertical, horizontal configurations, and concurrency setting for each expert at runtime. Experimental results show that sMoE reduces serving cost by 21.4%–39.2% compared to state-of-the-art solutions, while meeting stringent P95 latency SLOs.

## 中文摘要

混合专家（MoE）架构通过稀疏激活实现大规模推理，但专家热度偏斜且随时间变化，导致成本效率低下。无服务器计算凭借细粒度的资源弹性与计费方式，成为颇具吸引力的承载平台。即便如此，在并发请求下，针对存在层内与层间依赖的每个专家实现成本高效且满足 SLO 的伸缩，仍然充满挑战。本文提出 sMoE，一种面向无服务器 MoE 推理的拓扑感知弹性自动伸缩器。我们的洞察是将 MoE 推理流水线的部署视为由专家与非 MoE 片段构成的 DAG。在此基础上，sMoE 被设计为基于深度强化学习的方案。具体而言，它通过 DAGNN 传播跨层语义，从而编码专家级与层级运行时特征。结合逐层指针网络，sMoE 捕获层内语义，在运行时联合决定每个专家的垂直配置、水平配置与并发设置。实验结果表明，与最先进方案相比，sMoE 将服务成本降低 21.4%–39.2%，同时满足严格的 P95 延迟 SLO。
