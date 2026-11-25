Stitch: Assertion-Guided Patching of On-Chip Protocol Implementations Using LLMs
Authors：
[Melisande Zonta-Roudes](https://63dac.conference-program.com/?post_type=page&p=15&uid=410569825755321302)，[Nora Hinderling](https://63dac.conference-program.com/?post_type=page&p=15&uid=24798656976715502221)，[Shweta Shinde](https://63dac.conference-program.com/?post_type=page&p=15&uid=565743)

## 中文标题

Stitch：利用 LLM 的断言引导式片上协议实现修补

## 英文摘要

Verification flows use Verification IPs (VIPs) to identify assertion violations. This is well-suited for on-chip protocols (e.g., AXI, AHB) with standard specifications (e.g., AMBA) for developers to write assertions that detect violations. Patching these violations, however, still requires manual effort. A good patch must not only fix the violation but also preserve functionality (e.g., pass the testsuite) without causing new violations. We propose Stitch, based on the intuition that given an implementation, a violated assertion, and a counterexample an LLM can try to synthesize patches. To evaluate Stitch, we develop a new dataset that comprises 100 violations in 11 implementations of 5 protocols (AXI, AHB, APB, Wishbone, and TileLink). Our first experiment reports 19% success rate across 4 LLMs (GPT4, GPT5, Gemini, and Claude). By analyzing the failed cases, we devise 3 improvement strategies: patch localization, violation specific context (cone of influence, counterexample), iterative feedback from model checker outputs over candidate patches. Our experiments show these strategies help Stitch achieve 61% patch success, with GPT5 dominating with 56%. We validate Stitch patches through simulation and on real hardware. We compare Stitch to 3 state-of-the-art non-LLM tools and existing patches.

## 中文摘要

验证流程使用验证 IP（VIP）来识别断言违例。对于具有标准规范（如 AMBA）的片上协议（如 AXI、AHB），这一方式很适合开发者编写断言以检测违例。然而，修补这些违例仍需人工投入。一个好的补丁不仅要修复违例，还必须在不引入新违例的前提下保持功能正确（例如通过测试集）。我们提出 Stitch，其基本想法是：给定一个实现、一条被违反的断言以及一个反例，LLM 可以尝试合成补丁。为评估 Stitch，我们构建了一个新数据集，涵盖 5 种协议（AXI、AHB、APB、Wishbone 与 TileLink）的 11 个实现中的 100 个违例。首个实验报告了 4 个 LLM（GPT4、GPT5、Gemini 与 Claude）上 19%的成功率。通过分析失败案例，我们设计了 3 种改进策略：补丁定位、违例相关上下文（影响锥、反例），以及基于模型检查器输出对候选补丁的迭代反馈。实验表明，这些策略使 Stitch 的补丁成功率达到 61%，其中 GPT5 以 56%的表现最佳。我们通过仿真和在真实硬件上验证了 Stitch 生成的补丁，并将 Stitch 与 3 个最先进的非 LLM 工具及现有补丁进行了比较。
