# Efficient Strict Serializability for Stateful Serverless Workflows via Workflow Reconciliation

**中文标题**：通过工作流调和为有状态无服务器工作流提供高效的严格可串行化

**所属 Session**：[Session 17: Scheduling and Serverless](index.md) · [ATC 2026](../index.md)

**作者**：Shenghao Ao (Department of Computer Science and Engineering, Shanghai Jiao Tong University), Zijun Li (Department of Computer Science and Engineering, Shanghai Jiao Tong University), Chuhao Xu (Department of Computer Science and Engineering, Shanghai Jiao Tong University), Quan Chen (Department of Computer Science and Engineering, Shanghai Jiao Tong University), Shuo Quan (Cloud Computing Research Institute, China Telecom), Yanan Yang (Cloud Computing Research Institute, China Telecom), Jie Wu (China Telecom Cloud Computing Research Institute; Temple University), Meiqi Zhu (China Telecom Cloud Technology Co., Ltd.), Yujun Wang (China Telecom Cloud Technology Co., Ltd.), Minyi Guo (Department of Computer Science and Engineering, Shanghai Jiao Tong University; Guizhou University)

## 英文摘要
Serverless computing, represented by Function-as-a-Service (FaaS), is increasingly adopted for deploying complex applications via stateful workflows. However, the lack of strong consistency (i.e., strict serializability) transaction support hinders its broader applicability. Existing solutions are inadequate, either offering only weak consistency or suffering severe performance degradation from concurrency control models that blindly retry requests after conflicts. We therefore present FaaSRep, a high-performance serverless framework that provides strict serializability through workflow reconciliation, which resolves conflicts by learning dependencies from an optimistic execution and using them to guide an organized retry. FaaSRep builds dependencies at validation time, using the validator’s global access view without extra execution-path communication. It further uses a hybrid optimistic/pessimistic protocol to preserve correctness when application-level aborts invalidate the learned order. To reduce the cost of reconciliation, FaaSRep re-executes only affected functions and uses placement information from the initial execution to establish a peer-to-peer fast path during retry. Compared with state-of-the-art systems on real-world applications, FaaSRep improves average throughput by 1.44– 2.73× over Concord and 3.81–9.01× over Beldi.

## 中文摘要
以函数即服务（FaaS）为代表的无服务器计算正越来越多地被用于通过有状态工作流部署复杂应用。然而，缺乏强一致性（即严格可串行化）的事务支持阻碍了其更广泛的应用。现有解决方案不够充分：它们要么只提供弱一致性，要么因在冲突后盲目重试请求的并发控制模型而遭受严重的性能退化。为此我们提出 FaaSRep，一个高性能无服务器框架，它通过工作流调和提供严格可串行化，即从一次乐观执行中学习依赖关系，并用这些依赖引导有组织的重试，从而解决冲突。FaaSRep 在验证阶段利用验证器的全局访问视图构建依赖，无需额外的执行路径通信。当应用级中止使已学到的顺序失效时，它进一步采用乐观/悲观混合协议来保持正确性。为降低调和开销，FaaSRep 仅重新执行受影响的函数，并利用初始执行中的放置信息在重试期间建立点对点快速路径。在真实应用上与最先进的系统相比，FaaSRep 相较 Concord 将平均吞吐提升 1.44–2.73×，相较 Beldi 提升 3.81–9.01×。

## 英文关键词
FaaS, Serverless Computing, Serverless Workflow, Transaction, Consistency

## 中文关键词
FaaS，无服务器计算，无服务器工作流，事务，一致性

[返回 Session 17](index.md) · [返回 ATC 2026](../index.md)
