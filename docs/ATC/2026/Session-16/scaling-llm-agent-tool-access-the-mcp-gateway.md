# Scaling LLM Agent Tool Access: The MCP Gateway

**中文标题**：扩展 LLM 智能体的工具访问：MCP 网关

**所属 Session**：[Session 16: AI Agents](index.md) · [ATC 2026](../index.md)

**作者**：Mingxin Li (Nanjing University and Alibaba Cloud), Enge Song (Alibaba Cloud), Yueshang Zuo (Alibaba Cloud), Xiaodong Liu (Alibaba Cloud), Rong Wen (Fudan University and Alibaba Cloud), Qiang Fu (RMIT University), Gianni Antichi (Politecnico di Milano), Jian He (Alibaba Cloud), Jing Tie (Alibaba Cloud), Zhou Shao (Alibaba Cloud), Xiaobo Xue (Alibaba Cloud), Xiong Xiao (Alibaba Cloud), Luyao Zhong (Alibaba Cloud), Shaokai Zhang (Alibaba Cloud), Jiangu Zhao (Alibaba Cloud), Jianyuan Lu (Alibaba Cloud), Shize Zhang (Alibaba Cloud), Xiaoqing Sun (Alibaba Cloud), Changgang Zheng (Alibaba Cloud), Zihao Fan (Alibaba Cloud), Haonan Li (Alibaba Cloud), Tian Pan (Alibaba Cloud), Xiaomin Wu (Alibaba Cloud), Yang Song (Alibaba Cloud), Xing Li (Zhejiang University and Alibaba Cloud), Biao Lyu (Alibaba Cloud), Meng Li (Nanjing University), Haipeng Dai (Nanjing University), Guihai Chen (Nanjing University), Shunmin Zhu (Alibaba Cloud)

## 英文摘要
LLM agents increasingly rely on tool calling to complete tasks. Model Context Protocol (MCP) standardizes tool calling between LLM agents and tool providers. It reduces integration cost and drives rapid growth in tool scale. In production deployments, tool access becomes difficult to scale. On the tool provider side, legacy services are not directly callable through MCP; the rapid protocol development creates ongoing compatibility cost. On the agent side, the number of mounted tools is limited by the LLM context window and inference overhead; mounting a large tool set increases token usage and inference latency and can reduce task success rate. Moreover, for stateful MCP backends with multiple replicas, preserving session affinity increases client-side complexity. We present a cloud-scale MCP Gateway system. It breaks the direct-connect model on the data plane and offloads legacy service integration, consolidating incompatible MCP variants, access control, tool recommendation, and session-aware routing at the gateway. The conversion module supports 315 OpenAPI services in the cloud and integrates MCP transport variants. Session-aware routing decouples the scalability of the gateway layer and the MCP service layer. The hybrid retrieval engine sustains 98% Top-15 recall; it scales agent tool access to 3,000+ tools with improved tool selection accuracy. We also share the lessons learned from deploying the gateway system in production.

## 中文摘要
LLM 智能体越来越依赖工具调用来完成任务。模型上下文协议（MCP）标准化了 LLM 智能体与工具提供方之间的工具调用，降低了集成成本并推动工具规模快速增长。在生产部署中，工具访问变得难以扩展。在工具提供方一侧，遗留服务无法直接通过 MCP 调用；协议的快速演进带来持续的兼容性成本。在智能体一侧，可挂载的工具数量受限于 LLM 上下文窗口和推理开销；挂载大量工具会增加 token 用量与推理延迟，并可能降低任务成功率。此外，对于具有多个副本的有状态 MCP 后端，保持会话亲和性会增加客户端复杂度。我们提出一个云规模的 MCP 网关系统。它打破数据平面上的直连模型，将遗留服务集成卸载到网关，把互不兼容的 MCP 变体、访问控制、工具推荐和会话感知路由集中到网关。其转换模块支持云上 315 个 OpenAPI 服务，并集成了多种 MCP 传输变体。会话感知路由将网关层与 MCP 服务层的可扩展性解耦。混合检索引擎保持 98% 的 Top-15 召回率；它将智能体的工具访问扩展到 3000 多个工具，并提高了工具选择准确率。我们还分享了在生产中部署该网关系统的经验教训。

## 英文关键词
Model Context Protocol, Gateway, Cloud Networks

## 中文关键词
模型上下文协议，网关，云网络

[返回 Session 16](index.md) · [返回 ATC 2026](../index.md)
