On-Demand Multi-Task Sparsity for Efficient Large-Model Deployment on Edge Devices
Authors：
[Lianming Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=24782986961059859661)，[Haibo Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6495954545041763869)，[Qiao Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=6393363691648557937)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)，[Chun Jason Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=0429261838049077539)

## 中文标题

面向边缘设备高效大模型部署的按需多任务稀疏性

## 英文摘要

Sparsity is essential for deploying large models on resource constrained edge platforms. However, optimizing sparsity patterns for individual tasks in isolation ignores the significant I/O overhead incurred during frequent task switching. We introduce an on-demand multi-task sparsity framework specifically designed to minimize switching costs by maximizing parameter reuse. Unlike monolithic approaches, we decompose weights into reusable block-granular units and align sparse structures across tasks to maximize overlap. By dynamically loading only the small differential set of blocks required for the next task, our method effectively mitigates the cold-start latency inherent in traditional monolithic approaches. Experiments on a real-world autonomous driving platform demonstrate that our framework achieves superior switching efficiency, accelerating task switching by over 6.6× on average compared to existing sparsity methods.

## 中文摘要

稀疏性对于在资源受限的边缘平台上部署大模型至关重要。然而，孤立地为单个任务优化稀疏模式，会忽略频繁任务切换过程中产生的显著 I/O 开销。我们提出一种按需多任务稀疏框架，专门通过最大化参数复用来最小化切换开销。与整体式方法不同，我们将权重分解为可复用的块粒度单元，并在任务之间对齐稀疏结构以最大化重叠。通过仅动态加载下一任务所需的小规模差分歧块，我们的方法有效缓解了传统整体式方法固有的冷启动延迟。在真实自动驾驶平台上的实验表明，我们的框架实现了更优的切换效率，相比现有稀疏方法平均将任务切换加速 6.6 倍以上。

## 英文关键词

Multi-Task Switch, Model Sparsity, Dynamic Weight Loading, Autonomous Driving, Vision–Language Models

## 中文关键词

多任务切换、模型稀疏、动态权重加载、自动驾驶、视觉-语言模型
