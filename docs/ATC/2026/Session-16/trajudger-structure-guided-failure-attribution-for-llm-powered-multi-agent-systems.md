# TraJudger: Structure-Guided Failure Attribution for LLM-Powered Multi-Agent Systems

**中文标题**：TraJudger：面向 LLM 驱动的多智能体系统的结构引导故障归因

**所属 Session**：[Session 16: AI Agents](index.md) · [ATC 2026](../index.md)

**作者**：Yongxin Zhao (Nankai University), Shenglin Zhang (Nankai University), Wenwei Gu (Nankai University), Zijing Que (Nankai University), Weiwen Qian (Nankai University), Yongqian Sun (Nankai University), Li Shi (Alibaba Group), Wei Li (Alibaba Group), Liping Zhang (Alibaba Group), Dan Pei (Tsinghua University)

## 英文摘要
LLM-powered multi-agent systems are increasingly deployed in production, yet diagnosing their failures remains a major operational challenge. Unlike failures in cloud architectures, which can often be diagnosed using structured diagnostic information, multi-agent system failures are embedded in unstructured natural-language interactions, cascade silently across semantic boundaries, and defy attribution due to a lack of prior domain knowledge. Existing LLM-as-a-Judge approaches treat execution trajectories holistically, misattributing cascaded failures and fabricating plausible but ungrounded explanations. To overcome the limitations of existing methods, we present TraJudger, a structure-guided failure attribution system deployed in production at a global top-tier online shopping service provider. TraJudger constructs a Hierarchical Cognitive Graph from raw trajectories to recover explicit inter-step dependencies, deploys four category-specific specialist agents for typed failure detection, and performs graph-constrained backward tracing to ground root-cause identification in verified dependency paths. On 121 production and 126 benchmark failure trajectories, TraJudger achieves a relative improvement of at least 15% and 13.3% over state-of-the-art methods at the agent and step levels. TraJudger has been deployed at C𝑜𝑚𝑝𝑎𝑛𝑦A for over one month, reducing average time-to-attribution from 30 minutes to under one minute.

## 中文摘要
LLM 驱动的多智能体系统正越来越多地部署于生产环境，但对其故障进行诊断仍是重大的运维挑战。与云架构中的故障不同——后者通常可借助结构化诊断信息定位——多智能体系统的故障嵌入在非结构化的自然语言交互之中，跨语义边界静默级联，并且由于缺乏先验领域知识而难以归因。现有的 LLM-as-a-Judge 方法把执行轨迹当作整体处理，会错误归因级联故障，并编造看似合理却缺乏依据的解释。为克服现有方法的局限，我们提出 TraJudger，一个结构引导的故障归因系统，已部署于全球顶级在线购物服务提供商的生产环境。TraJudger 从原始轨迹构建分层认知图，以恢复显式的步间依赖关系；部署四个类别专用的专家智能体进行分类型故障检测；并执行图约束的后向追踪，把根因识别建立在经过验证的依赖路径之上。在 121 条生产轨迹和 126 条基准轨迹上，TraJudger 在智能体级和步骤级分别相较最先进方法取得至少 15% 和 13.3% 的相对提升。TraJudger 已在 CompanyA 部署一个多月，将平均归因时间从 30 分钟缩短至 1 分钟以内。

## 英文关键词
Failure Attribution, LLM-Powered Multi-Agent Systems, Trajectory Analysis

## 中文关键词
故障归因，LLM 驱动的多智能体系统，轨迹分析

[返回 Session 16](index.md) · [返回 ATC 2026](../index.md)
