Semi-Virtual Addressing to Enhance Memory Safety on Microcontrollers
Authors：
[Unjang Yeo](https://63dac.conference-program.com/?post_type=page&p=15&uid=61320072733594295121)，[Kyeongwoo Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=01441188470146528161)，[Yeongpil Cho](https://63dac.conference-program.com/?post_type=page&p=15&uid=944756307868618097)

## 中文标题

半虚拟寻址：增强微控制器上的内存安全

## 英文摘要

Microcontrollers lack support for virtual addressing, limiting their ability to employ efficient memory protection mechanisms that rely on a spacious virtual address space. While integrating an MMU could overcome this limitation, it is often impractical due to increased hardware cost and unpredictable latency. To address this, we propose semi-virtual addressing—a lightweight technique that extends the effective address space of microcontrollers without full virtual memory support. This technique introduces a Lightweight Address Translation Module (LATM) that performs deterministic, computation-based address translation without page tables, enabling semi-virtual addressing with minimal translation overhead. Implemented on the RISC-V CORE-V-MCU, LATM expands its 575 KB physical address space to 2 GB of semi-virtual address space. We demonstrate the practicality of semi-virtual addressing by enabling heap randomization and type-safe allocation on the extended address space, efficiently enhancing memory protection.

## 中文摘要

微控制器不支持虚拟寻址，这限制了其采用依赖大容量虚拟地址空间的高效内存保护机制。虽然集成 MMU 可以克服这一限制，但硬件成本增加与延迟不可预测往往使其不切实际。为此，我们提出半虚拟寻址——一种无需完整虚拟内存支持即可扩展微控制器有效地址空间的轻量级技术。该技术引入轻量级地址转换模块（LATM），在没有页表的情况下执行确定性的、基于计算的地址转换，从而使半虚拟寻址的转换开销极小。在 RISC-V CORE-V-MCU 上实现后，LATM 将其 575 KB 的物理地址空间扩展为 2 GB 的半虚拟地址空间。我们通过在扩展地址空间上启用堆随机化与类型安全分配，展示了半虚拟寻址的实用性，高效地增强了内存保护。

## 英文关键词

Microcontroller, Semi-Virtual Addressing, Memory Protection

## 中文关键词

微控制器、半虚拟寻址、内存保护
