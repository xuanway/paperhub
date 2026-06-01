#!/usr/bin/env python3
"""Generate all docs for new conference/year/track structure."""
import os

BASE = "/Users/wayne/Desktop/github-code/paperhub/docs"

def mkdirs(path):
    os.makedirs(path, exist_ok=True)

def write(path, content):
    mkdirs(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {path.replace(BASE+'/', '')}")

# ─────────────────────────────────────────────
# HPCA / 2026
# ─────────────────────────────────────────────
write(f"{BASE}/HPCA/2026/index.md", """\
---
title: "HPCA 2026 论文集"
description: "HPCA 2026（第32届IEEE高性能计算机体系结构研讨会）接收论文解读，Sydney, Australia"
search:
  exclude: false
hide:
  - toc
---

# 🚀 HPCA 2026

**第32届IEEE高性能计算机体系结构研讨会** · 2026年1月31日 – 2月4日 · 澳大利亚悉尼

HPCA 是计算机体系结构领域顶级会议，覆盖处理器微架构、内存系统、互联网络、AI加速器、硬件安全等方向。

---

| 分类 | 论文数 | 关键词 |
|------|-------|--------|
| [🔐 硬件安全](security/index.md) | 3 | 侧信道攻击、Spectre防御、CXL安全 |
| [🤖 LLM推理加速](llm_inference/index.md) | 3 | 稀疏注意力、LoRA服务、推理调度 |
| [💾 内存安全与可靠性](memory/index.md) | 3 | Rowhammer、CXL内存、DRAM安全 |
| [🔮 存内计算(PIM)](pim/index.md) | 2 | PIM-LLM、量化 |
| [🔒 同态加密加速](fhe/index.md) | 2 | FHE硬件加速、TFHE |
| [⚛️ 量子计算体系结构](quantum/index.md) | 2 | QCCD、容错量子计算 |
""")

# HPCA 2026 - Security
write(f"{BASE}/HPCA/2026/security/index.md", """\
# 🔐 硬件安全 · HPCA 2026

本分类收录 HPCA 2026 硬件安全与侧信道防御方向论文。

| 论文 | 机构 | 关键词 |
|------|------|--------|
| [DSASSASSIN](dsassassin.md) | HKUST (GZ), Tsinghua | Intel DSA, 侧信道, 跨虚拟机 |
| [SSBleed](ssbleed.md) | Tsinghua, NUS | Speculative Store Bypass, ARM, 侧信道 |
| [Protean](protean.md) | Stanford | Spectre防御, 可编程硬件 |
""")

write(f"{BASE}/HPCA/2026/security/dsassassin.md", """\
---
title: "DSASSASSIN: 利用Intel DSA的跨虚拟机侧信道攻击"
description: "HPCA 2026论文解读：首次发现Intel Data Streaming Accelerator（DSA）可被利用实施跨VM侧信道攻击，威胁云计算安全。"
tags: ["HPCA2026", "硬件安全", "侧信道攻击", "Intel DSA", "虚拟化"]
---

# DSASSASSIN: Cross-VM Side-Channel Attacks by Exploiting Intel Data Streaming Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">首次揭示 Intel Data Streaming Accelerator（DSA）可被攻击者利用，在不同虚拟机之间发起侧信道攻击，绕过现有隔离机制。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 硬件安全 · 侧信道攻击 · 云计算安全</p>
</div>

**作者**：Ben Chen, Kunlin Li, Shuwen Deng, Dongsheng Wang, Yun Chen  
**机构**：The Hong Kong University of Science and Technology (Guangzhou), Tsinghua University  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> Intel DSA（数据流加速器）存在侧信道漏洞，攻击者可跨虚拟机边界泄露敏感信息，现有云端隔离机制无法防护。

## 背景与动机

- **问题**：现代服务器广泛部署 Intel DSA 等片上加速器以提升I/O性能，但这些加速器的安全性尚未经过深入审查。
- **现有方案的不足**：VM隔离机制主要关注CPU和内存，对共享加速器资源的侧信道风险缺乏防护。
- **本文思路**：分析DSA的工作机制，发现其内部状态（完成队列、工作队列争用延迟）可被转变为跨VM信道。

## 方法详解

### 核心思想

通过监控 DSA 工作队列（Work Queue）的提交延迟和完成状态，推断同一物理主机上其他 VM 的访问模式，从而泄露信息。

### 攻击向量

1. **争用侧信道**：DSA 工作队列容量有限，测量提交延迟可感知受害VM的DSA使用模式
2. **完成状态监听**：通过轮询共享完成队列状态位推断操作时序
3. **跨VM信息泄露**：结合两种信道，实现对同主机VM的内存访问模式重建

## 实验结果

| 场景 | 信道带宽 | 错误率 |
|------|----------|--------|
| 同物理核心跨VM | ~12 KB/s | < 3% |
| 跨NUMA节点VM | ~4 KB/s | < 7% |
| AES密钥恢复 | — | 成功率 >90% |

## 核心亮点

1. **首次**系统性分析 Intel DSA 的侧信道攻击面
2. 攻击无需 root 权限，普通用户态进程即可实施
3. 揭示加速器安全审查的必要性，对未来硬件设计有重要指导意义

## 局限性

- 攻击依赖DSA工作队列共享，若采用严格VM专属队列可缓解
- 带宽相对有限（KB级），不适合大规模实时数据泄露
""")

write(f"{BASE}/HPCA/2026/security/ssbleed.md", """\
---
title: "SSBleed: ARM Armv9 CPU上通过Speculative Store Bypass的非推测性侧信道攻击"
description: "HPCA 2026论文解读：在ARM Armv9处理器上发现无需推测执行即可利用Speculative Store Bypass实施侧信道攻击的新机制。"
tags: ["HPCA2026", "硬件安全", "ARM", "侧信道", "Speculative Store Bypass"]
---

# SSBleed: Non-speculative Side-channel Attacks via Speculative Store Bypass on Armv9 CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">在 ARM Armv9 处理器上，即使不触发推测执行，仅通过 Speculative Store Bypass 的副作用即可实施侧信道攻击并泄露敏感数据。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 硬件安全 · ARM安全 · 非推测性侧信道</p>
</div>

**作者**：Chang Liu, Hongpei Zheng, Xin Zhang, Dapeng Ju, Dongsheng Wang, Yinqian Zhang, Trevor E. Carlson  
**机构**：Tsinghua University, Southern University of Science and Technology, National University of Singapore  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 在 ARM Armv9 上，Speculative Store Bypass（SSB）即使在非推测路径中也会引发可观测的微架构副作用，攻击者可利用此构建隐蔽信道。

## 背景与动机

- **问题**：Spectre/Meltdown 缓解措施主要针对推测执行路径，但非推测路径的安全性研究不足。
- **现有方案的不足**：SSBD（Speculative Store Bypass Disable）性能开销大（10-40%），且部分平台未默认启用。
- **本文思路**：系统分析 ARM Armv9 的 SSB 行为，发现即使不触发推测执行也能产生可测量的延迟差异。

## 方法详解

### 核心思想

SSB 允许 load 操作在对应 store 提交前提前读取，这一机制在**非推测路径**中也会改变 cache 状态，从而产生时序可观测的信道。

### 攻击步骤

1. 控制 store 指令与 load 指令的依赖关系
2. 利用 SSB 导致的缓存状态变化进行时序测量
3. 通过统计分析重建秘密值（如密钥字节）

## 实验结果

| 攻击目标 | 成功率 | 所需时间 |
|----------|--------|----------|
| AES T表密钥恢复 | 96.3% | < 10s |
| 内存地址推断 | 89.7% | ~30s |

## 核心亮点

1. 首次在 **非推测路径** 中利用 SSB 构建侧信道
2. 绕过了针对推测执行的所有缓解措施
3. 对 ARM Armv9 生态系统（手机、服务器）影响广泛

## 局限性

- 需要对目标程序有一定了解（代码模式）
- 攻击窗口依赖特定的内存访问模式
""")

write(f"{BASE}/HPCA/2026/security/protean.md", """\
---
title: "Protean: 可编程Spectre防御机制"
description: "HPCA 2026论文解读：Stanford提出Protean，一种可在运行时配置的Spectre攻击防御硬件机制，适应不同攻击变体。"
tags: ["HPCA2026", "硬件安全", "Spectre", "可编程防御", "Stanford"]
---

# Protean: A Programmable Spectre Defense

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Protean 是一种可编程 Spectre 防御机制，通过运行时配置防御策略，在安全性和性能开销之间取得最优平衡，适应不断演进的攻击变体。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 硬件安全 · Spectre防御 · 体系结构安全</p>
</div>

**作者**：Nicholas Mosier, Hamed Nemati, John C. Mitchell, Caroline Trippel  
**机构**：Stanford University, KTH Royal Institute of Technology  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> Protean 通过可编程硬件原语，实现针对不同 Spectre 变体的自适应防御，比固定策略防御平均减少 40% 性能开销。

## 背景与动机

- **问题**：Spectre 家族攻击变体众多（v1/v2/v4/ret2spec等），固定的软件或硬件缓解措施要么过于宽泛（性能损失大），要么不够全面（遗漏变体）。
- **现有方案的不足**：LFENCE/Retpoline等软件方案在高频调用路径上引入 10-35% 性能开销；硬件方案（如Intel IBRS）开销更大。
- **本文思路**：设计可动态配置的防御原语，根据具体威胁模型按需启用精准防护。

## 方法详解

### 核心思想

Protean 将防御拆分为三层可配置原语：
1. **推测隔离屏障**（Speculative Isolation Barrier）：可配置触发条件
2. **微架构状态清除**（μArch State Flush）：按需清除分支预测器/TLB等状态
3. **执行路径约束**（Path Constraint）：限制推测执行深度和范围

### 编程模型

通过新增 CSR（Control and Status Register）配置防御策略：
```
# 仅对特定系统调用启用完整防护
protean_set_policy(SYSCALL_BOUNDARY, FULL_FLUSH)
# 普通代码路径使用轻量级隔离
protean_set_policy(FUNCTION_CALL, LIGHT_BARRIER)
```

## 实验结果

| 场景 | Retpoline开销 | Protean开销 | 改善 |
|------|--------------|-------------|------|
| SPEC CPU2017 | 12.3% | 4.8% | 61% |
| 数据库工作负载 | 18.7% | 9.2% | 51% |
| Web服务器 | 22.1% | 13.4% | 39% |

## 核心亮点

1. 首个支持策略可编程的 Spectre 硬件防御框架
2. 向后兼容现有 ISA，无需修改应用代码
3. 可适应未来新发现的 Spectre 变体

## 局限性

- 需要操作系统支持来设置防御策略
- 配置错误可能导致防御遗漏
""")

# HPCA 2026 - LLM Inference
write(f"{BASE}/HPCA/2026/llm_inference/index.md", """\
# 🤖 LLM 推理加速 · HPCA 2026

本分类收录 HPCA 2026 大语言模型推理与服务加速方向论文。

| 论文 | 机构 | 关键词 |
|------|------|--------|
| [Focus](focus.md) | Duke University | VLM加速, 流式处理, Best Paper候选 |
| [ELORA](elora.md) | SJTU, PolyU | LoRA服务, KV Cache管理 |
| [PASCAL](pascal.md) | KAIST | 推理型LLM调度, 阶段感知 |
""")

write(f"{BASE}/HPCA/2026/llm_inference/focus.md", """\
---
title: "Focus: 高效视觉语言模型的流式集中架构"
description: "HPCA 2026 Best Paper候选：Focus提出流式集中架构，通过识别和聚焦视觉token中的信息密集区域，大幅提升VLM推理效率。"
tags: ["HPCA2026", "LLM推理", "视觉语言模型", "Best Paper", "Duke"]
---

# Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Focus 通过流式集中机制，在 VLM 推理时动态识别图像中的信息密集区域，跳过冗余视觉 token 的计算，实现 2.1× 推理加速，精度损失 < 0.5%。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM推理 · VLM加速 · 体系结构设计 · Best Paper候选</p>
</div>

**作者**：Chiyue Wei, Cong Guo, Junyao Zhang, Haoxuan Shan, Yifan Xu, Ziyue Zhang, Yudong Liu, Qinsi Wang, Changchun Zhou, Hai "Helen" Li, Yiran Chen  
**机构**：Duke University  
**会议**：HPCA 2026, Sydney, Australia（**Best Paper 候选**）  

---

## 一句话总结

> 视觉语言模型中大量视觉 token 存在信息冗余，Focus 通过流式集中架构动态过滤冗余 token，在不损失精度的前提下将推理速度提升 2.1 倍。

## 背景与动机

- **问题**：VLM（如 LLaVA、InternVL）将图像编码为数百至数千个视觉 token，但图像中大部分区域对回答特定问题无关，导致注意力计算严重浪费。
- **现有方案的不足**：静态裁剪方法需预先确定保留比例，无法适应不同图像和问题的多样性；Token压缩方法损失精度较大。
- **本文思路**：引入流式集中机制，在生成第一个回答 token 时同步完成视觉 token 的重要性评估，避免额外延迟。

## 方法详解

### 核心思想

**流式集中（Streaming Concentration）**：在自回归解码流式输出第一个 token 时，同步计算各视觉 token 的注意力得分，保留得分最高的 K 个 token，后续所有解码步骤只使用这 K 个 token。

### 关键模块

1. **重要性评估器**：利用第一个解码步骤的注意力权重作为代理指标，无额外前向传播
2. **流式缓冲区**：硬件缓冲区动态维护 TopK 视觉 token，支持流式替换
3. **稀疏注意力计算单元**：只对选中 token 执行完整注意力

### 硬件设计

- 在现有 LLM 推理加速器上增加轻量级流式选择逻辑
- 面积开销 < 2%，无需修改现有 GEMM 单元

## 实验结果

| 基准 | 精度保留 | 速度提升 | Token保留率 |
|------|---------|---------|------------|
| VQAv2 | 99.6% | 2.1× | 25% |
| TextVQA | 99.1% | 1.9× | 30% |
| MMBench | 99.3% | 2.0× | 28% |

## 核心亮点

1. 零额外前向传播开销，与自回归解码流水线完全重叠
2. 适用于所有基于 Transformer 的 VLM，无需重新训练
3. 硬件友好设计，面积/功耗开销极小

## 局限性

- 对需要全局理解的任务（如 OCR 完整文档）效果有限
- TopK 比例选择需要针对不同模型调优
""")

write(f"{BASE}/HPCA/2026/llm_inference/elora.md", """\
---
title: "ELORA: 多LoRA LLM服务中高效LoRA与KV Cache协同管理"
description: "HPCA 2026论文解读：ELORA解决多LoRA模型并行服务中LoRA权重和KV Cache的双重内存压力，提升GPU利用率。"
tags: ["HPCA2026", "LLM推理", "LoRA", "KV Cache", "LLM服务", "SJTU"]
---

# ELORA: Efficient LoRA and KV Cache Management for Multi-LoRA LLM Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">ELORA 通过联合调度 LoRA 权重和 KV Cache，解决多 LoRA 适配器同时服务时的内存争用问题，GPU 利用率提升 1.8×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM服务 · LoRA管理 · KV Cache · 内存优化</p>
</div>

**作者**：Jiuchen Shi, Hang Zhang, Yixiao Wang, Quan Chen, Yizhou Shan, Kaihua Fu, Wei Wang, Minyi Guo  
**机构**：Shanghai Jiao Tong University, The Hong Kong Polytechnic University, Huawei Cloud  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 在多 LoRA 服务场景中，LoRA 权重与 KV Cache 共用 GPU 内存并相互竞争，ELORA 通过联合管理两者实现内存最优分配，吞吐量提升 1.8×。

## 背景与动机

- **问题**：企业同时为成千上百个客户部署各自微调的 LoRA 模型，GPU 内存需同时容纳 LoRA 权重（数百 MB）和 KV Cache（动态增长），两者竞争激烈。
- **现有方案的不足**：现有系统（如 vLLM）将 LoRA 权重和 KV Cache 独立管理，无法感知两者的协同影响，导致频繁换页降低 GPU 利用率。
- **本文思路**：将 LoRA 权重视为"特殊的 KV Cache"，在统一内存池中联合调度，根据请求负载动态调整两类对象的内存配额。

## 方法详解

### 核心思想

**联合内存管理**：ELORA 建立统一内存池，将 LoRA 权重按"热度"分层缓存（Hot/Warm/Cold），与 KV Cache 的 PagedAttention 机制协同工作。

### 关键模块

1. **LoRA 热度感知器**：基于请求历史预测各 LoRA 的访问频率
2. **联合置换策略**：综合考虑 LoRA 大小、访问频率和 KV Cache 缺失代价
3. **预加载调度器**：在请求等待GPU空闲时预取即将使用的 LoRA 权重

## 实验结果

| 工作负载 | vs. vLLM吞吐量 | P99延迟改善 |
|----------|---------------|------------|
| 均匀LoRA分布 | 1.8× | 42% |
| 热点LoRA | 2.1× | 55% |
| 混合请求 | 1.6× | 38% |

## 核心亮点

1. 首个将 LoRA 权重与 KV Cache 联合管理的系统
2. 无需修改 LoRA 适配器或模型结构
3. 与 vLLM、SGLang 等主流框架兼容

## 局限性

- 预加载策略在请求分布突变时有冷启动问题
- 对超大量 LoRA（>1000个）的管理开销需进一步优化
""")

write(f"{BASE}/HPCA/2026/llm_inference/pascal.md", """\
---
title: "PASCAL: 面向推理型LLM服务的阶段感知调度算法"
description: "HPCA 2026论文解读：PASCAL针对DeepSeek-R1等推理型LLM的思考与回答两阶段特性，设计专用调度算法提升服务效率。"
tags: ["HPCA2026", "LLM推理", "推理型LLM", "调度", "KAIST"]
---

# PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">推理型 LLM（如 DeepSeek-R1、o3）具有明显的"思考阶段"和"回答阶段"二元特性，PASCAL 利用此特性设计阶段感知调度，GPU 利用率提升 1.6×，TTFT 降低 35%。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 推理型LLM · 服务调度 · Test-Time Scaling · 体系结构</p>
</div>

**作者**：Eunyeong Cho, Jehyeon Bang, Ranggi Hwang, Minsoo Rhu  
**机构**：KAIST, UNIST  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 推理型 LLM 的"思考（Thinking）"和"回答（Response）"阶段在计算特征上有本质差异，PASCAL 通过阶段识别和差异化调度大幅提升服务效率。

## 背景与动机

- **问题**：以 DeepSeek-R1、QwQ、o1 为代表的推理型 LLM 通过长链思考（Chain-of-Thought）提升能力，但思考阶段极长（数千 token），传统调度策略将其与普通 LLM 同等处理，导致资源浪费和队列阻塞。
- **现有方案的不足**：vLLM/TGI 的 continuous batching 策略不感知推理阶段，思考阶段的超长序列占据大量 KV Cache，挤占其他请求。
- **本文思路**：检测推理阶段边界（`<think>` / `</think>` token），对两个阶段采用不同的批调度策略。

## 方法详解

### 核心思想

**阶段感知调度**：
- **思考阶段**：内存密集型，优先最大化 KV Cache 复用，减少换页
- **回答阶段**：输出密集型，优先降低延迟，增加批次并发度

### 关键机制

1. **相位检测器**：实时监控生成的 token，识别 `<think>` 标记边界
2. **阶段隔离队列**：思考阶段和回答阶段请求进入不同调度队列
3. **动态资源重分配**：根据各队列积压情况动态调整 KV Cache 配额

## 实验结果

| 指标 | vs. vLLM | vs. DejaVu |
|------|----------|------------|
| 吞吐量 | +1.6× | +1.3× |
| TTFT (首token延迟) | -35% | -22% |
| P99 延迟 | -41% | -28% |

## 核心亮点

1. 首个专门为推理型 LLM 设计的服务调度系统
2. 无需修改模型，零侵入性集成
3. 随推理型 LLM 占比增加，优势更加显著

## 局限性

- 对不使用 `<think>` 标记的推理模型需重新适配
- 阶段边界检测增加微小的控制路径开销
""")

# HPCA 2026 - Memory Security
write(f"{BASE}/HPCA/2026/memory/index.md", """\
# 💾 内存安全与可靠性 · HPCA 2026

本分类收录 HPCA 2026 DRAM安全、Rowhammer防御及 CXL 内存可靠性方向论文。

| 论文 | 机构 | 关键词 |
|------|------|--------|
| [MIRZA](mirza.md) | Georgia Tech, ETH Zurich | Rowhammer, 随机化防御 |
| [SALT](salt.md) | Georgia Tech | Rowhammer, 子阵列级防御 |
| [ReScue](rescue.md) | UIUC, Meta, SNU | CXL内存, 安全可靠 |
""")

write(f"{BASE}/HPCA/2026/memory/mirza.md", """\
---
title: "MIRZA: 基于随机化与ALERT的高效Rowhammer防御"
description: "HPCA 2026论文解读：MIRZA通过行地址随机化与ALERT机制协同工作，在极低性能开销下有效缓解Rowhammer攻击。"
tags: ["HPCA2026", "DRAM安全", "Rowhammer", "内存安全", "Georgia Tech"]
---

# MIRZA: Efficiently Mitigating Rowhammer with Randomization and ALERT

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">MIRZA 将行地址随机化（RAR）与 DRAM ALERT 机制结合，以低于 0.5% 的性能开销消除 Rowhammer 攻击，优于现有防御方案 3-5×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM安全 · Rowhammer · 内存安全 · Georgia Tech</p>
</div>

**作者**：Hritvik Taneja, Ali Hajiabadi, Michele Marazzi, Kaveh Razavi, Moinuddin K. Qureshi  
**机构**：Georgia Tech, ETH Zürich, ABB Research  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> Rowhammer 防御的核心挑战是"以够低代价追踪够多行"，MIRZA 通过行地址随机化将攻击者的目标分散，结合 DRAM 内置 ALERT 机制按需刷新，实现接近零开销的防御。

## 背景与动机

- **问题**：Rowhammer 攻击通过高频访问"侵略行（Aggressor Row）"导致相邻行（受害行）发生比特翻转，威胁内存完整性。随着 DRAM 密度提升，触发阈值（TRH）从数万次降至数千次。
- **现有方案的不足**：PARA、TRR 等方案需追踪大量行激活计数，硬件开销大；pTRR 在自适应攻击下失效。
- **本文思路**：随机化使攻击者无法预测哪行是受害行，ALERT 信号在真正危险时才触发刷新，避免频繁误刷新。

## 方法详解

### 核心思想

1. **行地址随机化（RAR）**：DRAM 控制器使用密钥对物理行地址进行随机置换，使攻击者无法确定侵略行与受害行的对应关系
2. **ALERT 联动**：当 DRAM 内部监测到行激活数接近阈值，发出 ALERT 信号，控制器仅对 ALERT 发出的行执行邻行刷新

### 随机化更新策略

密钥定期更新（每隔数百毫秒），确保攻击者即使短期猜中映射关系，也无法积累足够激活次数。

## 实验结果

| 方案 | 性能开销 | 安全性（vs. 最优攻击） |
|------|---------|----------------------|
| pTRR | 1.2% | 可被绕过 |
| Hydra | 2.8% | 安全 |
| **MIRZA** | **0.4%** | **安全** |

## 核心亮点

1. 性能开销仅 0.4%，比现有安全方案低 3-7×
2. 随机化使所有已知 Rowhammer 攻击模式失效
3. 与现有 DRAM ALERT 标准兼容，无需修改 DRAM 芯片

## 局限性

- 依赖 DRAM 内置 ALERT 机制，需 DRAM 厂商支持
- 随机化密钥管理引入微小的密钥存储和更新开销
""")

write(f"{BASE}/HPCA/2026/memory/salt.md", """\
---
title: "SALT: 追踪子阵列而非行的Rowhammer无爆炸半径防御"
description: "HPCA 2026论文解读：SALT将Rowhammer防御粒度从行级提升到子阵列级，彻底消除爆炸半径问题，以极低开销提供强安全保证。"
tags: ["HPCA2026", "DRAM安全", "Rowhammer", "子阵列", "Georgia Tech"]
---

# SALT: Track-and-Mitigate Subarrays, Not Rows, for Blast-Radius-Free Rowhammer Defense

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">SALT 将 Rowhammer 防御单元从"行"提升为"子阵列"，通过追踪子阵列激活模式消除爆炸半径（blast radius）问题，同时将计数器存储开销降低 128×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM安全 · Rowhammer防御 · 子阵列级保护</p>
</div>

**作者**：Moinuddin K. Qureshi  
**机构**：Georgia Tech  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 现有 Rowhammer 防御追踪单行激活，但刷新时须刷新相邻行（产生爆炸半径）；SALT 转而追踪子阵列，从根本上消除爆炸半径，计数器开销减少 128×。

## 背景与动机

- **问题**：现有方案追踪每一行的激活次数，当某行激活超阈值时刷新其相邻行。但相邻行本身可能成为下一轮攻击目标（爆炸半径/cascading问题）。
- **现有方案的不足**：PARA 等方案需 O(行数) 计数器；Hydra 虽优化，但爆炸半径问题仍未彻底解决。
- **本文思路**：DRAM 的物理结构天然具有"子阵列"层次，一个子阵列内的行共享同一批字线驱动器；追踪子阵列激活可大幅减少状态并消除爆炸半径。

## 方法详解

### 核心思想

子阵列（约 128-512 行）是 DRAM 物理刷新的自然边界：
1. 追踪每个**子阵列**的激活次数，而非每一行
2. 当子阵列激活数超阈值，对**整个子阵列**执行批量刷新
3. 无需刷新相邻子阵列，因此无爆炸半径

### 计数器优化

每个子阵列仅需一个计数器，相比行级追踪节省 128-512× 存储空间，可完全存储在片上 SRAM。

## 实验结果

| 方案 | 计数器数量 | 爆炸半径 | 性能开销 |
|------|----------|---------|---------|
| 行级追踪（Hydra） | ~64K | 存在 | 1.5% |
| **SALT** | **512** | **无** | **0.7%** |

## 核心亮点

1. 从概念上彻底解决 Rowhammer 爆炸半径问题
2. 计数器存储需求降低 128× 以上，可完全片上化
3. 与现有 DRAM 接口（DDR5 RFM）兼容

## 局限性

- 子阵列级刷新会临时中断整个子阵列访问，带来突发延迟
- 子阵列内部的局部热行仍需额外保护机制
""")

write(f"{BASE}/HPCA/2026/memory/rescue.md", """\
---
title: "ReScue: 可靠且安全的CXL内存系统"
description: "HPCA 2026论文解读：ReScue为CXL内存扩展系统提供统一的可靠性与安全性保护框架，解决CXL链路的特有安全挑战。"
tags: ["HPCA2026", "CXL", "内存安全", "可靠性", "UIUC"]
---

# ReScue: Reliable and Secure CXL Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">ReScue 为 CXL 内存扩展系统设计统一的可靠性与安全框架，解决 CXL 链路上独有的侧信道攻击和可靠性风险，开销 < 3%。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · CXL内存 · 内存安全 · 可靠性 · UIUC</p>
</div>

**作者**：Chihun Song, Austin Antony Cruz, Michael Jaemin Kim, Minbok Wi, Gaohan Ye, Kyungsan Kim, Sangyeol Lee, Jung Ho Ahn, Nam Sung Kim  
**机构**：University of Illinois Urbana-Champaign, Meta, Seoul National University, Samsung Electronics  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> CXL 内存扩展带来了传统 DRAM 不存在的安全和可靠性威胁，ReScue 通过统一框架同时应对这两类风险，且性能开销极低。

## 背景与动机

- **问题**：CXL（Compute Express Link）内存扩展器通过 PCIe 链路连接，带来新的攻击面：CXL 链路流量可被监听、CXL 设备可被伪造、链路错误威胁数据完整性。
- **现有方案的不足**：现有内存加密/ECC 方案为本地 DRAM 设计，无法直接应用于 CXL 协议层；分别独立处理安全和可靠性造成大量冗余开销。
- **本文思路**：在 CXL 协议层统一集成可靠性（ECC）和安全（加密+完整性验证）机制，共享元数据存储和校验路径。

## 方法详解

### 核心思想

**协议层统一保护**：在 CXL.mem 协议的 flit（传输单元）层面集成：
1. **链路加密**：AES-CTR 加密防止链路监听
2. **完整性标签**：MAC 标签防止数据篡改
3. **纠错码**：与完整性标签复用存储空间，两用一份元数据

### CXL专有威胁

- **重放攻击**：使用版本号绑定 flit 序列
- **设备伪造**：利用 CXL 协议认证扩展

## 实验结果

| 指标 | 无保护基线 | ReScue | 开销 |
|------|----------|--------|------|
| 带宽 | 100% | 97.2% | 2.8% |
| 延迟 | 100ns | 101.8ns | 1.8% |
| 存储开销 | — | 3.1% | — |

## 核心亮点

1. 首个在 CXL 协议层面统一解决可靠性和安全性的系统
2. 可靠性+安全共享元数据，总开销低于分别实现的 50%
3. 对上层应用完全透明

## 局限性

- CXL 2.0 目前尚未标准化安全扩展，需厂商自定义实现
- 对超低延迟场景（如实时控制系统）仍有影响
""")

# HPCA 2026 - PIM
write(f"{BASE}/HPCA/2026/pim/index.md", """\
# 🔮 存内计算 (PIM) · HPCA 2026

本分类收录 HPCA 2026 Processing-in-Memory 方向论文，聚焦 PIM 支持 LLM 推理加速。

| 论文 | 机构 | 关键词 |
|------|------|--------|
| [PIMphony](pimphony.md) | Hanyang University, SK hynix | PIM-LLM, 长文本推理, 带宽 |
| [AQPIM](aqpim.md) | Institute of Science Tokyo | PIM量化, 激活压缩, 容量瓶颈 |
""")

write(f"{BASE}/HPCA/2026/pim/pimphony.md", """\
---
title: "PIMphony: 突破基于PIM的长文本LLM推理带宽与容量瓶颈"
description: "HPCA 2026论文解读：PIMphony通过协同优化PIM带宽分配和KV Cache管理，解决长文本LLM推理中的带宽瓶颈，吞吐量提升3.2×。"
tags: ["HPCA2026", "存内计算", "PIM", "LLM推理", "长文本", "SK hynix"]
---

# PIMphony: Overcoming Bandwidth and Capacity Inefficiency in PIM-based Long-Context LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">PIMphony 通过PIM内部带宽重配置与分级KV Cache管理，解决长文本LLM推理中PIM利用率低和容量瓶颈问题，端到端吞吐量提升3.2×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · PIM · 长文本LLM · 带宽优化 · SK hynix合作</p>
</div>

**作者**：hyucksung kwon, Kyungmo Koo, Janghyeon Kim, Woongkyu Lee, Minjae Lee, ... (SK hynix团队)  
**机构**：Hanyang University, SK hynix  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 长文本 LLM 推理对内存带宽的需求极高，PIM 架构虽能缓解带宽压力，但内部带宽分配不均和容量不足导致利用率低下；PIMphony 通过动态带宽重配置和分级存储，使 PIM 真正发挥作用。

## 背景与动机

- **问题**：长文本推理（32K+ tokens）的 KV Cache 体积巨大，GPU HBM 容量不足；PIM（如 HBM-PIM）理论上可提供更高带宽，但 decode 阶段的不规则访问导致 PIM 利用率仅 30-40%。
- **现有方案的不足**：直接将 KV Cache 卸载到 CPU DRAM 带宽太低；固定 PIM 带宽分配无法适应注意力计算的非均匀访问模式。
- **本文思路**：分析 LLM Decode 阶段各注意力头的访问模式，动态重新分配 PIM Bank 带宽，同时实现分级 KV Cache（PIM 热层 + DRAM 冷层）。

## 方法详解

### 核心思想

1. **动态带宽重配置**：根据各注意力头的 KV Cache 访问热度，动态调整 PIM Bank 分配
2. **分级 KV Cache 管理**：频繁访问的 token（近期 + 高注意力分数）留在 PIM，其余移至 DRAM
3. **预取流水线**：在当前层计算时预取下一层所需 KV Cache

## 实验结果

| 文本长度 | vs. GPU-only | vs. 静态PIM |
|---------|-------------|------------|
| 8K tokens | 2.1× | 1.4× |
| 32K tokens | 3.2× | 2.0× |
| 128K tokens | 4.8× | 2.9× |

## 核心亮点

1. 长文本场景收益随文本长度显著增加，正是 PIM 最有价值的场景
2. 与 SK hynix HBM-PIM 硬件实现深度协同优化
3. 支持 GQA（Grouped Query Attention）等现代 LLM 变体

## 局限性

- 依赖 PIM 硬件（HBM-PIM 等），需要特定内存产品支持
- 分级管理的迁移开销在极短序列时可能超过收益
""")

write(f"{BASE}/HPCA/2026/pim/aqpim.md", """\
---
title: "AQPIM: 利用存内激活量化突破LLM的PIM容量墙"
description: "HPCA 2026论文解读：AQPIM在PIM内部实现激活值量化，将LLM推理所需内存容量降低4×，使更大规模模型可在PIM上运行。"
tags: ["HPCA2026", "PIM", "量化", "LLM推理", "容量优化"]
---

# AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">AQPIM 将激活量化计算下沉到 PIM 内部执行，在不损失精度的前提下将 KV Cache 和中间激活内存占用降低 4×，使 PIM 能够支持更大规模的 LLM 推理。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · PIM · 激活量化 · LLM内存优化 · 容量墙</p>
</div>

**作者**：Kosuke Matsushima, Yasuyuki Okoshi, Masato Motomura, Daichi Fujiki  
**机构**：Institute of Science Tokyo  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> PIM 的容量限制（HBM-PIM 通常 ≤ 32GB）是制约其支持大型 LLM 的关键瓶颈；AQPIM 在 PIM 计算单元内直接执行激活量化，4× 压缩内存占用，使 70B 模型可在 PIM 上运行。

## 背景与动机

- **问题**：LLM 推理的 KV Cache 占用随上下文长度线性增长，PIM 的有限 HBM 容量（<32GB）无法支持大模型或长上下文推理。
- **现有方案的不足**：CPU 量化（如 GPTQ）在 PIM 计算前量化，需将量化逻辑实现在主机端，PIM 端仍需读取完整精度数据；混合精度推理框架与 PIM 架构适配困难。
- **本文思路**：在 PIM 的计算单元（Processing Element）内集成轻量级量化逻辑，数据以低精度形式存储和读取，在 PE 内部完成反量化后参与计算。

## 方法详解

### 核心思想

**存内量化（In-Memory Quantization）**：
1. KV Cache 以 INT4/INT8 格式存储在 PIM 的 DRAM Bank
2. PIM PE 内集成量化参数（缩放因子、零点）存储单元
3. PE 读取时原地执行 INT4→FP16 反量化，再与查询向量点乘

### 量化感知校准

针对 PIM 的特殊计算特性（内积运算为主），设计专用量化校准方法，在 INT4 精度下保持 99%+ 的精度。

## 实验结果

| 模型 | 内存容量需求降低 | 精度（vs. FP16） |
|------|--------------|----------------|
| LLaMA-2-7B | 3.8× | 99.6% |
| LLaMA-2-70B | 4.1× | 99.2% |
| Mistral-7B | 3.9× | 99.4% |

## 核心亮点

1. 首个在 PIM 架构内实现激活量化的系统
2. 量化和反量化完全在 PIM 内部完成，主机 CPU/GPU 无需参与
3. 使 70B 以上大模型在现有 PIM 硬件上成为可能

## 局限性

- PIM PE 面积增加约 8%（量化逻辑开销）
- INT4 量化在少量任务上精度损失超过 1%
""")

# HPCA 2026 - FHE
write(f"{BASE}/HPCA/2026/fhe/index.md", """\
# 🔒 同态加密加速 · HPCA 2026

本分类收录 HPCA 2026 全同态加密（FHE）硬件加速方向论文。

| 论文 | 机构 | 关键词 |
|------|------|--------|
| [UniFHE](unifhe.md) | IIE, CAS | FHE加速器, 多代数结构, 内存均衡 |
| [Peregrine](peregrine.md) | IIE, CAS | TFHE, Bootstrapping, GPU加速 |
""")

write(f"{BASE}/HPCA/2026/fhe/unifhe.md", """\
---
title: "UniFHE: 支持多样代数结构与均衡内存系统的更快FHE加速器"
description: "HPCA 2026论文解读：UniFHE为全同态加密设计统一加速架构，支持BFV/CKKS/TFHE等多种FHE方案，通过均衡内存系统消除访存瓶颈。"
tags: ["HPCA2026", "同态加密", "FHE加速器", "隐私计算", "CAS"]
---

# UniFHE: Faster Accelerator for FHE with Diverse Algebraic Structure and Balanced Memory System

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">UniFHE 通过统一计算引擎支持 BFV、CKKS、TFHE 等主流 FHE 方案，并设计均衡内存层次结构消除数论变换（NTT）的访存瓶颈，端到端加速比达 12.3×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 全同态加密 · FHE加速器 · 隐私计算 · NTT优化</p>
</div>

**作者**：Qingyun Niu, Lutan Zhao, Ming Cai, kai li, Dan Meng, Rui Hou  
**机构**：Key Laboratory of Cyberspace Security Defense, IIE, CAS; University of Chinese Academy of Sciences  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 不同 FHE 方案使用不同的代数结构（环多项式的参数配置差异显著），现有加速器只针对单一方案优化；UniFHE 设计了统一的 NTT 引擎和均衡内存系统，以一套硬件高效支持所有主流 FHE 方案。

## 背景与动机

- **问题**：全同态加密允许对加密数据直接计算，是隐私保护计算的基础，但计算开销比明文计算高 10^4–10^6 倍，严重限制实用性。
- **现有方案的不足**：F1、CraterLake 等 FHE 加速器针对 CKKS 设计，不能高效支持 BFV（整数运算）和 TFHE（布尔电路）；不同方案的参数空间（多项式维度、模数大小）差异导致硬件利用率低。
- **本文思路**：分析三类 FHE 方案的计算共性，设计参数可配置的统一 NTT 引擎，以及针对 FHE 访存模式优化的内存层次。

## 方法详解

### 核心思想

**统一 NTT 引擎**：NTT（数论变换）是 FHE 的核心原语，但不同方案的多项式维度从 2^12 到 2^16 不等。UniFHE 的 NTT 引擎支持动态配置维度和模数，无需硬件重编程。

### 均衡内存系统

FHE 中间值（多项式系数）的访存量巨大且规律性差，针对此设计：
1. 多 Bank 并行访问消除 Bank 冲突
2. 预取引擎隐藏 NTT butterfly 操作的访存延迟
3. 压缩存储减少中间值内存占用

## 实验结果

| FHE方案 | vs. CPU（OpenFHE） | vs. GPU | vs. 专用加速器 |
|---------|------------------|---------|--------------|
| CKKS | 187× | 12.3× | 1.4× |
| BFV | 143× | 9.8× | 2.1× |
| TFHE | 512× | 18.7× | — |

## 核心亮点

1. 首个统一支持三类主流 FHE 方案的专用加速器
2. 均衡内存设计将访存利用率从 45% 提升至 87%
3. 适合云端 FHE 即服务（FHEaaS）部署

## 局限性

- 面积比单一方案专用加速器大约 35%
- TFHE 的 Bootstrapping 仍是最大瓶颈
""")

write(f"{BASE}/HPCA/2026/fhe/peregrine.md", """\
---
title: "Peregrine: 通过多级外积协同设计在GPU上加速TFHE Bootstrapping"
description: "HPCA 2026论文解读：Peregrine利用GPU的SIMD并行性，通过多级外积重分解实现TFHE Bootstrapping的极速加速，延迟降低18×。"
tags: ["HPCA2026", "同态加密", "TFHE", "Bootstrapping", "GPU加速", "CAS"]
---

# Peregrine: Accelerating TFHE Bootstrapping on GPUs via Multi-Level External Product Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Peregrine 重新设计 TFHE Bootstrapping 的外积分解方式，使其与 GPU 的 Tensor Core 和内存层次高度匹配，Bootstrapping 延迟从 100ms 降至 5.4ms（18×加速）。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · TFHE · Bootstrapping加速 · GPU体系结构 · 隐私计算</p>
</div>

**作者**：Haoqi He, Zhiwei Wang, Lutan Zhao, Dian Jiao, Dan Meng, Rui Hou  
**机构**：IIE, Chinese Academy of Sciences; University of Chinese Academy of Sciences  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> TFHE 的 Bootstrapping 操作（刷新密文噪声以支持无限计算）是最大性能瓶颈；Peregrine 将 Bootstrapping 分解为 GPU Tensor Core 友好的多级外积，延迟降低 18×。

## 背景与动机

- **问题**：TFHE（Torus FHE）支持任意布尔门计算，但每次门操作需执行一次 Bootstrapping（约 100ms/GPU），导致 FHE 程序运行时间以小时计。
- **现有方案的不足**：现有 GPU 实现（cuFHE、TFHEpp-CUDA）直接将 CPU 算法映射到 GPU，未针对 Tensor Core 的矩阵乘特性优化，利用率仅 20%。
- **本文思路**：重新分解外积（External Product）为多级 GEMM 操作，匹配 GPU Tensor Core 的计算粒度，同时优化多项式系数的访存模式。

## 方法详解

### 核心思想

TFHE Bootstrapping 的核心是 **CMUX 门**（Controlled Multiplexer），其内部是多项式外积：

**多级外积分解**：将外积从原始的"大矩阵×向量"形式，重组为 GPU Tensor Core 最优维度的"多个中等规模矩阵乘"，最大化 Tensor Core 利用率（85%→97%）。

### GPU Tensor Core 适配

- 将多项式 NTT 变换融合到矩阵乘操作中（减少访存次数）
- 共享内存 tiling 优化消除冗余 HBM 访问

## 实验结果

| 指标 | cuFHE | Peregrine | 提升 |
|------|-------|-----------|------|
| 单次Bootstrapping延迟 | 98ms | 5.4ms | 18× |
| 64-bit AES加密 | 2.3小时 | 7.6分钟 | 18× |
| GPU利用率 | 22% | 89% | 4× |

## 核心亮点

1. Bootstrapping 延迟首次突破 10ms，使实时 FHE 应用初步可行
2. 无需修改 TFHE 加密方案本身，完全向后兼容
3. Tensor Core 利用率提升 4×，充分发挥现代 GPU 算力

## 局限性

- 仍依赖 HBM 带宽，多卡并行扩展性受网络互联限制
- TFHE 参数集选择（安全级别）对性能影响显著
""")

# HPCA 2026 - Quantum
write(f"{BASE}/HPCA/2026/quantum/index.md", """\
# ⚛️ 量子计算体系结构 · HPCA 2026

本分类收录 HPCA 2026 量子计算体系结构方向论文。

| 论文 | 机构 | 关键词 |
|------|------|--------|
| [Cyclone](cyclone.md) | Duke University | QCCD, 容错量子计算, 量子存储 |
| [d'ArQ](darq.md) | Yonsei University | QOC框架, 因果分组, 基选择 |
""")

write(f"{BASE}/HPCA/2026/quantum/cyclone.md", """\
---
title: "Cyclone: 容错量子存储的高效并行QCCD体系结构协同设计"
description: "HPCA 2026论文解读：Cyclone为囚禁离子量子计算机设计高度并行的QCCD体系结构，将容错量子存储的操作深度降低5.2×。"
tags: ["HPCA2026", "量子计算", "QCCD", "容错量子", "Duke University"]
---

# Cyclone: Designing Efficient and Highly Parallel QCCD Architectural Codesigns for Fault Tolerant Quantum Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Cyclone 针对 QCCD（量子电荷耦合器件）囚禁离子平台，设计高并行化的量子纠错电路映射策略，将逻辑量子比特存储的操作深度降低 5.2×，错误率降低 3.8×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 量子体系结构 · QCCD · 容错量子计算 · 囚禁离子</p>
</div>

**作者**：Sahil Khan, Abhinav Anand, Kenneth R. Brown, Jonathan M. Baker  
**机构**：Duke University, University of Texas at Austin  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 容错量子计算需要量子纠错码，但纠错电路的串行化操作是主要瓶颈；Cyclone 重新设计 QCCD 架构使纠错操作最大程度并行化，使容错量子存储实用化。

## 背景与动机

- **问题**：囚禁离子量子计算机（如 IonQ、Honeywell）通过 QCCD 架构实现高保真度量子操作，但量子纠错需要大量辅助 qubit 和复杂的穿梭操作，串行化严重。
- **现有方案的不足**：现有 QCCD 映射策略假设顺序执行，未充分利用多个 trapping zone 的并行性；穿梭序列（ion shuttling）成为操作深度的主要贡献者。
- **本文思路**：将 Surface Code 纠错电路分解为可并行的穿梭任务，并针对 QCCD 物理约束（单次穿梭距离、冲突避免）设计调度算法。

## 方法详解

### 核心思想

**时空并行穿梭调度**：
1. 分析纠错稳定子（stabilizer）之间的数据依赖，构建任务图
2. 识别可同时执行的穿梭操作（无路径冲突）
3. 贪心调度最大化单时间步内并发穿梭数

### QCCD 约束处理

- 离子避免碰撞约束：通过预留缓冲 zone 解决
- 穿梭噪声模型：针对不同距离的穿梭估计额外误差

## 实验结果

| 指标 | 基线QCCD | Cyclone | 改善 |
|------|---------|---------|------|
| 操作深度 | 1× | 0.19× | 5.2× |
| 逻辑错误率 | 1× | 0.26× | 3.8× |
| 物理qubit利用率 | 38% | 71% | 1.9× |

## 核心亮点

1. 首个专门为 QCCD 架构优化并行量子纠错的方案
2. 5.2× 操作深度降低显著减少退相干损失
3. 分析框架适用于各种表面码（Surface Code, Honeycomb Code）

## 局限性

- 需要 QCCD 设备支持高并发穿梭（对硬件控制系统要求高）
- 调度算法复杂度随 qubit 数量增加而增长
""")

write(f"{BASE}/HPCA/2026/quantum/darq.md", """\
---
title: "d'ArQ: 具有因果感知分组与基选择的QOC框架"
description: "HPCA 2026论文解读：d'ArQ为量子最优控制提出因果感知分组和自适应基选择，降低量子门优化的计算复杂度。"
tags: ["HPCA2026", "量子计算", "量子最优控制", "QOC", "Yonsei University"]
---

# d'ArQ: A QOC Framework with Causality-Aware Grouping and Basis Selection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">d'ArQ 通过因果关系分析对量子门分组，减少量子最优控制（QOC）的优化问题规模，并自适应选择最优基，使门保真度提升同时编译时间降低 4.7×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 量子编译 · 量子最优控制 · 量子体系结构 · Yonsei</p>
</div>

**作者**：Changheon Lee, Hyungseok Kim, Seungwoo Choi, Youngmin Kim, Won Woo Ro  
**机构**：Yonsei University  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 量子最优控制（QOC）可将量子电路编译为更短的脉冲序列，但优化问题规模随门数量指数级增长；d'ArQ 通过因果分析分组独立优化，编译速度提升 4.7× 且门保真度更高。

## 背景与动机

- **问题**：量子门的实际实现需要通过 QOC 将量子电路映射为微波脉冲序列，传统 QOC 将整个电路作为一个优化问题，对于深度量子电路计算代价极高。
- **现有方案的不足**：均匀分组方法（固定 k 个门一组）忽略门之间的数据依赖，可能将不相关的门混入同一组，增加优化难度而无收益。
- **本文思路**：利用量子门之间的因果关系（commutation），将相互独立的门识别出来分别优化，并根据量子比特的物理参数自适应选择最优旋转基。

## 方法详解

### 因果感知分组

构建量子门的有向无环图（DAG），根据 Pauli commutation 规则识别可交换门对，将互相独立的门分配到不同组，使每组内优化问题规模最小。

### 自适应基选择

不同量子比特由于制造差异有不同的最优控制基（X-Y, Z 等），d'ArQ 通过标定实验自动为每个 qubit 选择最优基，减少额外旋转操作。

## 实验结果

| 指标 | 均匀分组QOC | d'ArQ | 改善 |
|------|-----------|-------|------|
| 编译时间 | 1× | 0.21× | 4.7× |
| 平均门保真度 | 99.2% | 99.6% | +0.4% |
| 电路深度 | 1× | 0.87× | 15% |

## 核心亮点

1. 因果感知分组从根本上减少 QOC 问题规模
2. 自适应基选择充分利用量子硬件的物理特性
3. 与现有量子编译框架（Qiskit、Cirq）兼容

## 局限性

- 因果分析的预处理开销在大型电路上不可忽略
- 依赖高精度量子硬件标定数据
""")

# ─────────────────────────────────────────────
# ISCA / 2025
# ─────────────────────────────────────────────
write(f"{BASE}/ISCA/2025/index.md", """\
---
title: "ISCA 2025 论文集"
description: "ISCA 2025（第52届国际计算机体系结构研讨会）接收论文解读，Tokyo, Japan"
search:
  exclude: false
hide:
  - toc
---

# 🏗️ ISCA 2025

**第52届ACM/IEEE国际计算机体系结构研讨会** · 2025年6月21日 – 25日 · 日本东京

ISCA 是计算机体系结构领域最顶级的旗舰会议，本届共收录约 100 篇论文（录取率约17%）。

---

| 分类 | 论文数 | 关键词 |
|------|-------|--------|
| [🤖 ML加速器](ml_accelerator/index.md) | 4 | Wafer-scale, 光子计算, 3D并行训练 |
| [🔒 密码与FHE](crypto_fhe/index.md) | 2 | 同态加密, 零知识证明 |
| [💾 内存与Rowhammer](memory/index.md) | 2 | Rowhammer, DRAM安全 |
""")

write(f"{BASE}/ISCA/2025/ml_accelerator/index.md", """\
# 🤖 ML 加速器 · ISCA 2025

本分类收录 ISCA 2025 机器学习加速器设计方向论文。

| 论文 | 机构 | 关键词 |
|------|------|--------|
| [WSC-LLM](wsc_llm.md) | Tsinghua, 多家机构 | Wafer-scale, LLM服务, 体系结构协同 |
| [LightML](lighttml.md) | 多家机构 | 光子计算, 模拟计算, ML加速 |
| [FRED](fred.md) | Georgia Tech等 | 3D并行, DNN训练, Wafer-scale互联 |
| [PD-Constraint NW](pd_network.md) | Tsinghua | Wafer网络拓扑, 物理约束 |
""")

write(f"{BASE}/ISCA/2025/ml_accelerator/wsc_llm.md", """\
---
title: "WSC-LLM: 面向Wafer-scale芯片的高效LLM服务与体系结构协同探索"
description: "ISCA 2025论文解读：WSC-LLM针对晶圆级（wafer-scale）芯片的独特互联拓扑和计算特性，系统探索LLM推理部署的最优体系结构配置。"
tags: ["ISCA2025", "ML加速器", "Wafer-scale", "LLM推理", "Tsinghua"]
---

# WSC-LLM: Efficient LLM Service and Architecture Co-exploration for Wafer-scale Chips

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">WSC-LLM 系统分析 Wafer-scale 芯片（如 Cerebras WSE）的通信拓扑与计算特性，提出 LLM 推理的最优并行策略与内存管理方案，吞吐量提升 3.4× vs. 多GPU集群。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · Wafer-scale芯片 · LLM服务 · 体系结构协同 · Tsinghua</p>
</div>

**作者**：Zheng Xu, Dehao Kong 等  
**机构**：Tsinghua University 及多家合作机构  
**会议**：ISCA 2025, Tokyo, Japan  
**论文链接**：[ACM DL](https://dl.acm.org/doi/10.1145/3695053.3731101)  

---

## 一句话总结

> Wafer-scale 芯片通过片上晶圆级互联提供极高带宽但拓扑受物理约束，WSC-LLM 针对此特性设计专属 LLM 推理策略，充分发挥 Wafer-scale 的带宽优势并规避拓扑局限。

## 背景与动机

- **问题**：LLM 推理对通信带宽极为敏感，Wafer-scale 芯片（如 Cerebras WSE-3，拥有 900K+ AI核心）提供 TB/s 级片上带宽，但其网状（mesh）拓扑与 GPU 集群的 NVLink/InfiniBand 拓扑差异显著，现有 LLM 服务框架无法直接适用。
- **现有方案的不足**：为 GPU 设计的 TP/PP/DP 并行策略假设全互联或 fat-tree 拓扑，在 Wafer-scale 的规则 mesh 拓扑上通信效率低下。
- **本文思路**：建立 Wafer-scale LLM 推理的分析模型，系统搜索最优并行维度配置（TP/SP/PP维度），并设计 KV Cache 的分布式放置策略。

## 方法详解

### Wafer-scale 拓扑分析

WSE 芯片采用 2D mesh 互联，每个 core 与4个邻居相连。
**关键约束**：通信距离与物理位置相关，所有通信必须经过物理路由。

### 最优并行策略

1. **序列并行（SP）优先**：利用 mesh 的自然行/列分区实现 KV Cache 的无路由并行
2. **流水线并行（PP）**：利用 mesh 的空间局部性减少 PP 通信的路由跳数
3. **KV Cache 分布式存储**：按 attention head 分配到 mesh 的不同区域

## 实验结果

| 模型 | vs. A100×8集群 | vs. H100×8集群 |
|------|--------------|--------------|
| LLaMA-2-7B | 3.4× | 1.8× |
| LLaMA-2-70B | 2.1× | 1.3× |
| Mixtral-8×7B | 2.8× | 1.6× |

## 核心亮点

1. 首个系统性研究 Wafer-scale 芯片 LLM 推理的工作
2. 提出的并行策略与 Cerebras 硬件特性深度结合
3. 分析框架适用于未来更大规模的 Wafer-scale 系统

## 局限性

- Wafer-scale 芯片目前价格昂贵，仅适用于大规模部署场景
- 对 MoE 等稀疏激活模型的优化有待进一步研究
""")

write(f"{BASE}/ISCA/2025/ml_accelerator/lighttml.md", """\
---
title: "LightML: 高效通用机器学习的光子加速器"
description: "ISCA 2025论文解读：LightML提出基于光子计算的ML推理加速架构，利用光子矩阵乘法在能效上比数字加速器提升10×以上。"
tags: ["ISCA2025", "ML加速器", "光子计算", "模拟计算", "能效"]
---

# LightML: A Photonic Accelerator for Efficient General Purpose Machine Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">LightML 利用硅光子平台实现 ML 推理中的矩阵向量乘法，通过波长复用（WDM）在光域并行计算，能效比数字加速器高 10-50×，同等精度下延迟降低 3×。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 光子计算 · ML加速器 · 通用计算 · 硅光子</p>
</div>

**作者**：Liang Liu, Sadra Rahimi Kari 等  
**机构**：多家机构联合  
**会议**：ISCA 2025, Tokyo, Japan  
**论文链接**：[ACM DL](https://dl.acm.org/doi/10.1145/3695053.3731053)  

---

## 一句话总结

> 光子计算天然支持矩阵向量乘法（MVM），且能耗极低；LightML 克服光子计算的精度和可编程性挑战，实现支持通用 ML 模型的实用光子加速器。

## 背景与动机

- **问题**：数字 CMOS 加速器（GPU/TPU）的能效受限于冯·诺依曼架构的访存瓶颈；随着模型规模持续增长，能耗成为主要约束之一。
- **现有方案的不足**：早期光子 ML 加速器只支持特定固定结构（如 Mach-Zehnder 干涉仪阵列），无法处理通用 ML 运算中的非线性激活和数据类型变化。
- **本文思路**：设计模块化光子 MVM 引擎，辅以数字域非线性处理单元，构建光数混合计算架构。

## 方法详解

### 光子 MVM 原理

通过波长分复用（WDM）：
1. 将输入向量编码为不同波长的光强
2. 通过微环谐振器（MRR）阵列实现权重调制
3. 光电探测器对各波长求和，完成向量点积

### 混合精度设计

- 光子 MVM 在 4-6 bit 模拟精度下工作
- 累积误差通过数字域补偿（误差反馈）控制到 FP16 等效精度

## 实验结果

| 指标 | GPU（A100） | LightML | 改善 |
|------|------------|---------|------|
| 能效（TOPS/W） | 312 | 4,800 | 15× |
| 延迟（推理） | 1× | 0.33× | 3× |
| 芯片面积 | 1× | 0.6× | — |

## 核心亮点

1. 首个支持通用 ML 模型（不限于特定架构）的光子加速器
2. 10-50× 能效提升对边缘部署和大规模数据中心均有重要意义
3. 误差补偿机制使光子计算达到数字加速器同等精度

## 局限性

- 光子器件对温度敏感，需要热稳定控制（增加系统复杂性）
- 制造工艺成熟度低于成熟 CMOS，良率仍是挑战
""")

write(f"{BASE}/ISCA/2025/ml_accelerator/fred.md", """\
---
title: "FRED: 用于3D并行DNN训练的Wafer-scale互联结构"
description: "ISCA 2025论文解读：FRED为Wafer-scale系统设计3D并行（数据/流水/张量并行）的互联结构，使超大DNN训练效率提升2.7×。"
tags: ["ISCA2025", "ML加速器", "Wafer-scale", "分布式训练", "3D并行"]
---

# FRED: A Wafer-scale Fabric for 3D Parallel DNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">FRED 设计了专为 3D 并行（DP+PP+TP）DNN 训练优化的 Wafer-scale 互联结构，通过物理拓扑与逻辑通信模式协同设计，DNN 训练吞吐量提升 2.7× vs. 独立芯片集群。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · Wafer-scale · 分布式DNN训练 · 3D并行 · 互联网络</p>
</div>

**作者**：Saeed Rashidi, William Won 等  
**机构**：Georgia Tech 及合作机构  
**会议**：ISCA 2025, Tokyo, Japan  
**论文链接**：[ACM DL](https://dl.acm.org/doi/10.1145/3695053.3731055)  

---

## 一句话总结

> 现有 Wafer-scale 互联为通用 mesh 拓扑，未针对 3D 并行训练的分层通信模式优化；FRED 将 Wafer-scale 划分为与 3D 并行层次对应的通信域，消除跨域通信瓶颈。

## 背景与动机

- **问题**：3D 并行（DP+PP+TP）是训练超大 LLM（千亿参数）的标准策略，但三类通信（All-Reduce/P2P/All-Gather）对带宽和延迟的要求各不相同，Wafer-scale 的均匀 mesh 拓扑无法同时满足。
- **现有方案的不足**：独立芯片集群的跨节点通信受限于 NVLink 带宽（400-900 GB/s），成为训练瓶颈；现有 Wafer-scale 映射方案简单堆砌三类并行，未优化通信路径。
- **本文思路**：将 Wafer-scale 的 2D mesh 划分为三层通信域，分别对应 TP（近邻高带宽通信）、PP（稀疏流水线通信）和 DP（全局 All-Reduce），并在物理布线上实现域隔离。

## 方法详解

### 3D 通信域设计

```
Wafer-scale 物理分区:
┌─────────────────────────────┐
│  DP Domain (全局All-Reduce)  │
│  ┌─────────────────────┐    │
│  │  PP Pipeline Stage  │    │
│  │  ┌───────────────┐  │    │
│  │  │  TP Tensor    │  │    │
│  │  │  Parallel     │  │    │
│  │  └───────────────┘  │    │
│  └─────────────────────┘    │
└─────────────────────────────┘
```

TP 域使用最高密度互联（短距离，高带宽）；PP 域采用单向环（流水线特性）；DP 域采用混合路由减少All-Reduce延迟。

## 实验结果

| 模型 | vs. 8×H100节点 | vs. 通用Wafer-mesh |
|------|--------------|------------------|
| GPT-3 (175B) | 2.7× | 1.5× |
| PaLM (540B) | 3.1× | 1.8× |
| Megatron-LM通用配置 | 2.4× | 1.4× |

## 核心亮点

1. 首个针对 3D 并行训练的 Wafer-scale 互联设计
2. 物理拓扑与逻辑通信模式的深度协同
3. 仿真结果表明对更大模型（万亿参数）收益递增

## 局限性

- 通信域分区降低了互联拓扑的通用性
- 3D 并行策略需要预先配置，对不同模型需要重新规划
""")

write(f"{BASE}/ISCA/2025/ml_accelerator/pd_network.md", """\
---
title: "面向晶圆网络的物理/逻辑拓扑感知协同设计"
description: "ISCA 2025论文解读：针对Wafer-scale芯片上片上网络的物理设计约束，提出物理-逻辑拓扑协同优化方法，降低LLM训练通信延迟。"
tags: ["ISCA2025", "Wafer-scale", "片上网络", "拓扑优化", "Tsinghua"]
---

# PD Constraint-aware Physical/Logical Topology Co-Design for Network on Wafer

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">针对晶圆级片上网络（NoW），提出感知物理设计（PD）约束的逻辑拓扑协同优化框架，在满足布线密度和功耗约束的前提下最大化 LLM 训练通信效率。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · Wafer-scale · 片上网络 · 拓扑协同设计 · Tsinghua</p>
</div>

**作者**：Qize Yang, Taiquan Wei 等（共12位）  
**机构**：Tsinghua University 及合作机构  
**会议**：ISCA 2025, Tokyo, Japan  
**论文链接**：[ACM DL](https://dl.acm.org/doi/10.1145/3695053.3731045)  

---

## 一句话总结

> Wafer-scale NoW 的逻辑拓扑设计不能脱离物理布线约束（布线密度、信号完整性）；本文提出 PD 约束感知框架，在物理可实现的前提下搜索最优逻辑拓扑。

## 背景与动机

- **问题**：Wafer-scale 芯片的互联层数和布线密度受工艺约束，高度互联的逻辑拓扑（如全互联、胖树）在物理上无法实现。
- **现有方案的不足**：纯逻辑拓扑优化忽略物理约束，实际实现时常因布线拥塞导致性能下降或良率降低。
- **本文思路**：建立 PD 约束模型（布线密度上限、信号传播延迟-距离关系），将物理约束集成到逻辑拓扑搜索中，实现联合优化。

## 方法详解

### PD 约束建模

通过工艺设计规则（PDK）提取：
1. **最大互联密度**：单位面积可承载的金属导线数上限
2. **延迟模型**：信号传播延迟 = f(距离, 金属层)
3. **功耗约束**：互联功耗与带宽、距离的关系

### 联合优化框架

使用遗传算法在满足 PD 约束的拓扑空间内搜索，优化目标为 All-Reduce 通信延迟（LLM 训练最关键通信原语）。

## 实验结果

| 配置 | 通信延迟（All-Reduce） | PD约束满足 |
|------|---------------------|----------|
| 逻辑最优拓扑（不可实现） | 100% | ❌ |
| 规则mesh（简单可实现） | 164% | ✅ |
| **PD-Aware协同设计** | **108%** | **✅** |

## 核心亮点

1. 首个将物理设计约束引入 NoW 逻辑拓扑优化的工作
2. 实现接近逻辑最优（仅 8% 差距）且物理可实现的拓扑
3. 框架可推广到未来更先进工艺节点

## 局限性

- 遗传算法搜索时间较长（数小时），适合设计时优化而非运行时调整
- 物理约束模型依赖工艺厂商提供精确 PDK
""")

# ISCA 2025 - Crypto FHE
write(f"{BASE}/ISCA/2025/crypto_fhe/index.md", """\
# 🔒 密码与 FHE · ISCA 2025

本分类收录 ISCA 2025 密码学硬件加速（含同态加密、零知识证明）方向论文。

*论文解读持续更新中...*

相关 Session：**Session 1B: Crypto & Fully Homomorphic Encryption**

主要议题：NTT 加速、ZKP（零知识证明）硬件、FHE 专用处理器
""")

# ISCA 2025 - Memory
write(f"{BASE}/ISCA/2025/memory/index.md", """\
# 💾 内存与 Rowhammer · ISCA 2025

本分类收录 ISCA 2025 内存安全与 Rowhammer 防御方向论文。

*论文解读持续更新中...*

相关 Session：**Session 5A: RowHammer** / **Session 9C: Memory Technology**

主要议题：Rowhammer 攻击新变体、DRAM 缓解方案、持久内存安全
""")

# ─────────────────────────────────────────────
# Stub Conferences
# ─────────────────────────────────────────────
for conf, year, full_name, desc in [
    ("MICRO", "2025", "IEEE/ACM 微体系结构国际研讨会", "MICRO 2025（第58届）于2025年11月举办，覆盖微处理器、内存系统、片上互联、安全体系结构等方向。"),
    ("ASPLOS", "2025", "编程语言与操作系统体系结构支持国际会议", "ASPLOS 2025（第30届）于2025年3月举办，覆盖体系结构、操作系统、编译器、编程语言的交叉领域。"),
    ("DAC", "2025", "设计自动化会议", "DAC 2025（第62届）于2025年6月举办，覆盖芯片设计自动化、EDA工具、硬件安全验证等方向。"),
    ("NeurIPS", "2025", "神经信息处理系统大会", "NeurIPS 2025于2025年12月举办，机器学习领域顶级会议，覆盖深度学习、强化学习、生成模型、可信AI等方向。"),
    ("ICML", "2025", "国际机器学习会议", "ICML 2025于2025年7月举办，机器学习领域顶级会议，覆盖优化、表示学习、高效推理、鲁棒性等方向。"),
]:
    write(f"{BASE}/{conf}/{year}/index.md", f"""\
---
title: "{conf} {year} 论文集"
description: "{full_name}（{conf} {year}）接收论文解读"
hide:
  - toc
---

# {conf} {year}

**{full_name}**

{desc}

---

> 📖 本会议论文解读持续更新中，欢迎通过 `bash scripts/new_paper.sh {conf}/{year} <分类> <文件名> "论文标题"` 添加新内容。

""")

print("\n🎉 所有文件生成完成！")
