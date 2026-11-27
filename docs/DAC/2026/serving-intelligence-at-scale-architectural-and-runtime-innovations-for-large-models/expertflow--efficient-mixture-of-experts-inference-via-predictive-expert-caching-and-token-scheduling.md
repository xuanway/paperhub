Expertflow: Efficient Mixture-of-Experts Inference via Predictive Expert Caching and Token Scheduling
Authors：
[Xin He](https://63dac.conference-program.com/?post_type=page&p=15&uid=89946739011506255751)，[Shunkang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=87345074691867548181)，[Kaijie Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9386802101984828259)，[Shaohuai Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=66053018619523190151)，[Yuxin Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6549377294499819169)，[Zihao Zeng](https://63dac.conference-program.com/?post_type=page&p=15&uid=9966982004432928687)，[Zhenheng Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=29808284496537151001)，[Xiaowen Chu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8760333532370472477)，[Haiyan Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=5428492865776115155)，[Ivor Tsang](https://63dac.conference-program.com/?post_type=page&p=15&uid=33822871994854066201)，[Yew Soon Ong](https://63dac.conference-program.com/?post_type=page&p=15&uid=31014158394421511221)

## 中文标题

ExpertFlow：基于预测式专家缓存与 token 调度的 MoE 高效推理

## 英文摘要

Sparse Mixture-of-Experts (MoE) models can outperform dense large language models at similar computation by activating only a small set of experts per token. However, stacking many expert modules introduces substantial parameter memory, which makes MoE models difficult to deploy in memory-constrained environments such as single-GPU devices. Offloading alleviates this issue by storing inactive experts in CPU memory and loading them on demand, but existing methods remain limited: static caches disregard input-dependent routing, and methods that train separate models to predict expert usage ahead of time are often inaccurate or require significant training cost. We propose ExpertFlow, a lightweight MoE inference system that addresses this routing dependency through three coordinated components: 1) a transformer-based routing path predictor that estimates expert usage across all MoE layers in a single forward pass, 2) a token scheduler that groups tokens with similar predicted routes to improve expert utilization, and 3) a predictive expert cache that loads only the required experts while correcting mispredictions at runtime. Together, these components enable efficient expert loading and execution, reducing GPU memory usage by up to 93.72% and improving inference throughput by up to 10× over strong offloading baselines on a single GPU.

## 中文摘要

稀疏混合专家（MoE）模型通过对每个 token 仅激活少量专家，在相近计算量下可超越稠密大语言模型。然而，堆叠大量专家模块引入了庞大的参数内存，使 MoE 模型难以在单 GPU 等内存受限环境中部署。卸载通过将未激活专家存放于 CPU 内存并按需加载来缓解该问题，但现有方法仍有局限：静态缓存忽略了依赖输入的专家路由，而训练额外模型来预先预测专家使用情况的方法往往不够准确，或需要高昂的训练成本。我们提出 ExpertFlow，一种轻量级 MoE 推理系统，通过三个协同组件解决上述路由依赖问题：1）基于 Transformer 的路由路径预测器，在单次前向传播中估计所有 MoE 层的专家使用情况；2）token 调度器，将预测路由相似的 token 分组，以提高专家利用率；3）预测式专家缓存，仅加载所需专家，并在运行时纠正预测错误。这些组件协同实现了高效的专家加载与执行，在单 GPU 上相较强卸载基线将 GPU 显存占用最多降低 93.72%，并将推理吞吐最多提升 10 倍。

## 英文关键词

Large Language Model (LLM), Mixture-of-Experts (MoE), Hybrid System

## 中文关键词

大语言模型（LLM）、混合专家（MoE）、混合系统
