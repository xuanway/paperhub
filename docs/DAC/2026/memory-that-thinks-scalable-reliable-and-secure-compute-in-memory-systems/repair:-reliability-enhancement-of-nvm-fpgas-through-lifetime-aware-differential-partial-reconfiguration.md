REPAIR: Reliability Enhancement of NVM FPGAs Through Lifetime-Aware Differential Partial Reconfiguration
Authors：
[Miran Tobar](https://63dac.conference-program.com/?post_type=page&p=15&uid=416385972552460744)，[Hassan Nassar](https://63dac.conference-program.com/?post_type=page&p=15&uid=212743)，[Joerg Henkel](https://63dac.conference-program.com/?post_type=page&p=15&uid=853343)

## 中文标题

REPAIR：通过寿命感知的差分部分重构提升 NVM FPGA 的可靠性

## 英文摘要

Non-Volatile Memory (NVM)-based Field Programmable Gate Arrays (FPGAs) have attracted attention due to lower power consumption, higher logic density, and instant-on capability from retained configuration data. However, NVM cells have limited write endurance and higher latency than SRAM, which can affect long-term reliability, especially under frequent Partial reconfiguration (PR). Although PR improves design efficiency by updating only part of the logic, it imposes lifetime limitations, particularly on NVM-based Look Up Tables (LUTs). In this paper, we introduce REPAIR, a framework that minimizes LUT reconfiguration through PR without changing the normal CAD flow. REPAIR uses a lifetime-aware fixed placement technique in the Preprocessing stage to reduce LUT reconfigurations. Moreover, it includes a postprocessing tool that generates differential partial bitstreams, writing only the changed LUT configuration bits between consecutive configurations. Finally, at runtime it incorporates a low-overhead scheduler to optimize LUT updates within the reconfiguration path. Together, these mechanisms reduce write stress on NVM cells, enhance the lifetime and reliability of Non-Volatile FPGAs (NVFPGAs) while preserving the performance and flexibility benefits of PR. Our experimental results show that REPAIR extends the operational lifetime of NVFPGAs by at least 7× compared to a baseline PR using commercial tools.

## 中文摘要

基于非易失存储器（NVM）的现场可编程门阵列（FPGA）因功耗更低、逻辑密度更高，且可凭借保持的配置数据实现瞬时启动而备受关注。然而，NVM 单元的写入耐久性有限且延迟高于 SRAM，可能影响长期可靠性，在频繁部分重构（PR）条件下尤为突出。尽管 PR 通过仅更新部分逻辑提升了设计效率，却带来了寿命限制，对基于 NVM 的查找表（LUT）尤为显著。本文提出 REPAIR，一个在不改变常规 CAD 流程的前提下通过 PR 最小化 LUT 重构的框架。REPAIR 在预处理阶段采用寿命感知的固定布局技术以减少 LUT 重构；此外还包含一个后处理工具，用于生成差分部分比特流，仅写入相邻两次配置之间发生变化的 LUT 配置位；最后在运行时引入低开销调度器，以优化重构路径内的 LUT 更新。上述机制共同降低了 NVM 单元的写入压力，在保留 PR 的性能与灵活性优势的同时提升了非易失 FPGA（NVFPGA）的寿命与可靠性。实验结果表明，与使用商用工具的基线 PR 相比，REPAIR 可将 NVFPGA 的工作寿命至少延长 7 倍。
