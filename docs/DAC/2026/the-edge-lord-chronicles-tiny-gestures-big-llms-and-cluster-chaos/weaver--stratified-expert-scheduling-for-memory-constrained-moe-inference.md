Weaver: Stratified Expert Scheduling for Memory-Constrained MoE Inference
Authors：
[Han Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=23380556917551751521)，[Jingwei Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=1666460592743559186)，[Junqing Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=24308083386360185041)，[Guangzhong Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=98230306995127546851)

## 中文标题

Weaver：面向内存受限 MoE 推理的分级专家调度

## 英文摘要

Mixture-of-Experts (MoE) models have achieved remarkable performance through sparse expert activation, yet deployment on resource-constrained platforms faces severe memory challenges as their parameter size exceeds device capacity, necessitating CPU offloading. While existing systems optimize data movement and leverage CPU computation during MoE layers, they leave the CPU underutilized during GPU attention computation. We present Weaver, a stratified scheduling framework that exploits this idle window through score-stratified expert treatment. Our key insight reveals asymmetric expert importance: low-scoring experts tolerate input approximation while high-scoring ones remain accuracy-critical. Weaver proactively executes predicted low-score experts on CPU during attention using prior-layer inputs, initiates stratified prefetching for high-score experts, and reactively balances remaining workload across heterogeneous resources. Evaluations on three representative MoE models demonstrate 1.47-3.58× average speedup over state-of-the-art accuracy-preserving offloading systems while maintaining model quality.

## 中文摘要

混合专家（MoE）模型通过稀疏专家激活取得了显著性能，但在资源受限平台上部署时，其参数规模超出设备容量，面临严峻的内存挑战，因而必须借助 CPU 卸载。现有系统在 MoE 层中优化数据移动并利用 CPU 参与计算，却在 GPU 注意力计算期间使 CPU 处于闲置状态。我们提出 Weaver，一个分级调度框架，通过按得分对专家分级处理来利用这一空闲窗口。我们的关键洞见揭示了专家重要性的不对称性：低分专家可以容忍输入近似，而高分专家对精度仍然关键。Weaver 在注意力计算期间利用前一层输入，主动在 CPU 上执行预测出的低分专家；对高分专家启动分级预取；并对剩余工作负载在异构资源间进行反应式均衡。在三个代表性 MoE 模型上的评估表明，与当前先进的保精度卸载系统相比，Weaver 平均加速 1.47–3.58 倍，同时保持模型质量。

## 英文关键词

Large Language Model (LLM), Mixture-of-Experts (MoE), Parameter Offloading

## 中文关键词

大语言模型（LLM）、混合专家（MoE）、参数卸载
