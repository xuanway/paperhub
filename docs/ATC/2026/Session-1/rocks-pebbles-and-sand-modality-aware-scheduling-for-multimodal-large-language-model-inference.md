# Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference

**中文标题**：岩石、卵石与沙子：面向多模态大语言模型推理的模态感知调度

**所属 Session**：[Session 1: LLM Inference I](index.md) · [ATC 2026](../index.md)

**作者**：Konstantinos Papaioannou (IMDEA Software Institute), Thaleia Dimitra Doudali (IMDEA Software Institute)

## 英文摘要
Multimodal Large Language Models (MLLMs) power platforms like ChatGPT, Gemini, and Copilot, enabling rich interactions across text, images, and videos. Unlike text-only workloads, multimodal requests are inherently heterogeneous, differing by orders of magnitude in latency and memory footprint. Existing LLM serving systems, designed for homogeneous text workloads, struggle under this heterogeneity: large image and video requests monopolize GPU resources, causing severe head-of-line blocking and degrading the responsiveness of lightweight, latency-critical text queries. Recent multimodal serving systems mitigate this interference through disaggregation, isolating encoding and inference stages across GPUs. While effective at large scale, such designs introduce severe GPU underutilization in more practical, moderate-scale deployments. In response, we build RPS-Serve a modality-aware scheduling framework that leverages the extreme heterogeneity in multimodal workloads and introduces a simple abstraction: videos behave like rocks, images like pebbles, and text like sand. Then, it lets sand flow quickly through pebbles and rocks, maximizing GPU utilization while ensuring fast responsiveness for lightweight requests and controlled execution for heavier ones. To achieve this, RPS-Serve estimates the GPU admission cost of each request, classifies requests into rocks, pebbles, and sand using lightweight clustering, and applies priority-based scheduling with aging to balance performance across modalities. Evaluation across state-of-the-art MLLMs shows that RPS-Serve increases GPU utilization by 65% and reduces TTFT by up to 9.3×, on average across models, compared to disaggregation-based multimodal systems.

## 中文摘要
多模态大语言模型（MLLM）支撑着 ChatGPT、Gemini 和 Copilot 等平台，实现了跨文本、图像与视频的丰富交互。与纯文本负载不同，多模态请求本身具有异构性，其延迟与内存占用相差数个数量级。现有为同质文本负载设计的 LLM 服务系统在这种异构性下左右支绌：大型图像与视频请求会垄断 GPU 资源，造成严重的队头阻塞，并降低轻量、延迟敏感的文本查询的响应性。近期的多模态服务系统通过分离（disaggregation）将编码阶段与推理阶段隔离到不同 GPU 上，以缓解这种干扰。这类设计在大规模场景下颇为有效，但在更实际的中等规模部署中会引入严重的 GPU 利用率不足。为此，我们构建了 RPS-Serve，一个模态感知的调度框架，它利用多模态负载中的极端异构性，并引入一个简单的抽象：视频如同岩石，图像如同卵石，文本如同沙子。然后，它让沙子快速地流过卵石与岩石，在最大化 GPU 利用率的同时，确保轻量请求获得快速响应，而更重的请求得到受控的执行。为实现这一点，RPS-Serve 估算每个请求的 GPU 准入开销，使用轻量级聚类将请求划分为岩石、卵石和沙子，并应用带老化（aging）的优先级调度来平衡各模态之间的性能。在最先进的 MLLM 上的评估表明，与基于分离的多模态系统相比，RPS-Serve 将 GPU 利用率提升 65%，并在各模型平均意义上将 TTFT 最多降低 9.3 倍。

## 英文关键词
Multimodal Large Language Models, Multimodal Inference, Model Inference Serving, Scheduling, Resource Management, GPU Utilization

## 中文关键词
多模态大语言模型，多模态推理，模型推理服务，调度，资源管理，GPU 利用率

[返回 Session 1](index.md) · [返回 ATC 2026](../index.md)
