---
title: "Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Tropical: Enhancing SLO Attainment in Disaggregated LLM Serving via SLO-Aware Multiplexing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132617">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132617</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型服务，SLO感知调度 </p>
</div>


---

## 研究概要
本文提出Tropical调度器，面向LLM分布式推理解决聚合、分离架构各自短板：分离架构预fill排队严重TTFT差，同机架构预fill干扰解码TPOT恶化。设计SLO感知多路复用机制，利用解码时延余量调度预fill，平衡排队与干扰。真实长文本负载下90%SLO达标请求提升2.09倍，相较分离架构P90 TTFT提升9倍。

## 背景和动机
1. LLM推理分为预fill、解码两阶段，分别对应TTFT、TPOT两项时延SLO，现有两类部署架构各有缺陷，无法同时保障两项指标。
2. 非分离同机部署：预fill与解码共享GPU，资源利用率高，但长预fill会阻塞解码，造成TPOT大幅超标。
3. 分离式部署：预fill、解码隔离worker，无计算干扰，但算力割裂，预fill队列堆积，长尾TTFT极差；静态配比无法适配动态输入长度负载。
4. 现有worker角色切换方案开销大，切换解码至预fill需迁移KV缓存，极易破坏TPOT时延约束。
5. 真实业务输入token长尾分布，预fill负载波动剧烈，静态资源分配长期存在算力闲置/过载失衡问题。

## 相关工作
1. 同机LLM推理(vLLM/Sarathi-Serve)：块预fill缓解干扰，但无法控制长文本带来的解码阻塞，TPOT长尾严重。
2. 分离式推理(DistServe/Mooncake)：消除阶段干扰，但算力隔离导致预fill排队时延爆炸，动态负载下资源匹配差。
3. 动态角色切换调度：切换解码worker做预fill存在KV迁移开销，易触发TPOT SLO违约。
4. 通用DNN SLO调度：未针对LLM预fill/解码两阶段异步生成特性设计余量复用策略。
5. 流式QoE优化(Andes/Llumnix)：侧重输出平滑，未从worker资源复用层面平衡TTFT与TPOT。

## 本文解决方案
### 1 SLO时延余量(Slack)量化模型
定义单步解码TPOT余量：解码理论时延与SLO阈值差值，余量充足时插入预fill不会破坏用户体验；区分长短预fill，短预fill排队痛点更突出。
### 2 多路复用切换调度器(Multiplexing Toggle)
两类worker：专用预fill worker、复用worker；全局监控队列、HBM水位、解码余量，双路径分发请求。
### 3 双路径流量分发策略
路径1：预fill负载高、解码余量不足时送入专用worker，避免干扰；路径2：解码存在充足余量，直接在复用worker混合执行预fill+解码，削减排队。
### 4 动态worker职能自适应
解码资源紧张时复用worker转为纯预fill；预fill队列积压、解码余量充足时开放混合多路；搭配块预fill进一步平滑干扰。
### 5 离线时延预估模块
离线剖析不同长度预fill、解码执行耗时，实时预测排队与执行时延，保守决策避免SLO突破阈值。

## 实验分析
1. 实验环境：A100 80GB集群，InternLM-20B长上下文模型，Mooncake真实业务负载，基线vLLM、块预fill vLLM、DistServe。
2. SLO达标量：同等到达速率下，Tropical可满足2.09倍符合双时延SLO的请求，帕累托最优兼顾TTFT/TPOT。
3. 长尾时延：对比DistServe P90 TTFT提升9倍；对比原生vLLM P90 TPOT提升2.8倍，仅小幅牺牲TPOT上限。
4. 排队时延：分离架构预fill排队长尾极高，Tropical复用算力大幅削减P90排队时间，仅高负载略高于vLLM。
5. 负载适配：长短输入混合场景优势显著，长文本下干扰可控，短文本消除排队瓶颈，CDF曲线无严重长尾。

## 研究启发
1. 预fill与解码不存在绝对隔离/同机最优解，应基于解码时延余量动态混合调度，兼顾两类SLO约束。
2. LLM负载输入长度长尾特性决定静态worker配比无法适配流量波动，算力弹性复用是核心优化方向。
3. 时延余量Slack是可挖掘算力资源，在不破坏用户流式体验前提下消化预fill积压请求。
4. 长文本与短文本优化侧重不同：短文本主要矛盾是排队，长文本核心风险是预fill带来的解码干扰。
5. 调度决策需引入离线时延预估做保守判定，盲目混合多路会引发大规模SLO违约。
