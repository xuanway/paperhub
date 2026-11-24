# Cloudless Tomorrow: A Memory-Centric System for Self-Improving Device-Cloud LLM Agents

**中文标题**：无云明日：面向自提升端云 LLM 智能体的以内存为中心的系统

**所属 Session**：[Session 16: AI Agents](index.md) · [ATC 2026](../index.md)

**作者**：Zeyu Qiu (Huazhong University of Science and Technology), Yaohui Wang (Huazhong University of Science and Technology), Shuyi Wang (Huazhong University of Science and Technology), Yu Kuang (Huazhong University of Science and Technology), Qinbin Li (Huazhong University of Science and Technology), XIAOFEI LIAO (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology)

## 英文摘要
LLM agents are increasingly deployed across devices and the cloud: on-device execution provides low latency and reduced network dependence, while cloud execution offers stronger reasoning capability for difficult workflow states. Existing device-cloud mechanisms are mainly router-based or distillation-based, but routers repeatedly offload similar hard states without improving future on-device execution, while distillation typically requires costly model adaptation. We present WorkflowPage, a memory-centric system that turns cloud fallback into reusable on-device capability. Instead of routing each query or distilling cloud models, WorkflowPage migrates cloud-generated execution experience to the device as structured workflow pages. Each page groups related successor states that share an execution prefix and binds them to reusable skills, enabling soft state addressing, page-fault recovery, topology-aware prefetching, and utility-based eviction under bounded device memory. By managing agent experience as page-structured memory rather than flat prompt context, WorkflowPage allows devices to progressively absorb cloud-side task-solving experience, reduce cloud reliance and latency, and largely preserve the quality of cloud-assisted agents.

## 中文摘要
LLM 智能体正越来越多地跨设备与云端部署：端侧执行带来低延迟并减少对网络的依赖，云端执行则为困难的工作流状态提供更强的推理能力。现有端云机制主要基于路由或蒸馏，但路由器会反复将相似的困难状态下放到云端，却不改善未来的端侧执行，而蒸馏通常需要代价高昂的模型适配。我们提出 WorkflowPage，一个以内存为中心的系统，把云端回退转化为可复用的端侧能力。WorkflowPage 并不对每个查询做路由，也不蒸馏云端模型，而是将云端产生的执行经验以结构化工作流页的形式迁移到设备。每个页把共享同一执行前缀的相关后继状态聚合在一起，并将它们绑定到可复用的技能，从而在有界设备内存下实现软状态寻址、缺页恢复、拓扑感知预取和基于效用的驱逐。通过把智能体经验作为页结构化的内存而非扁平的提示上下文来管理，WorkflowPage 使设备能够逐步吸收云端的任务求解经验，降低对云的依赖与延迟，并在很大程度上保持云辅助智能体的质量。

## 英文关键词
Device-Cloud, LLM Agents, Self-Improving

## 中文关键词
端云协同，LLM 智能体，自提升

[返回 Session 16](index.md) · [返回 ATC 2026](../index.md)
