Janus: Compiler-Based Defense Against Transient Execution Attacks Using ARM Hardware Primitives
Authors：
[Ciyan Ouyang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4277591427064845047)，[Peinan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=345143)，[Yubiao Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7821412821609413114)，[Dan Meng](https://63dac.conference-program.com/?post_type=page&p=15&uid=922343)，[Rui Hou](https://63dac.conference-program.com/?post_type=page&p=15&uid=942543)

## 中文标题

Janus：利用 ARM 硬件原语的基于编译器的瞬态执行攻击防御

## 英文摘要

We present Janus, a compiler-based security framework that mitigates transient execution attacks like Spectre and control-flow hijacking on ARM64 platforms. Janus integrates speculative execution and control flow dependencies with PA modifiers, using PA and BTI microarchitectural features to prevent control-flow speculation attacks and secure both control flow and speculative execution through existing control-flow integrity mechanisms. To optimize performance, Janus minimizes overhead by merging defense operations across different defense layers (modifier fusion) and reusing registers of protected variables (carrier reuse), while maintaining strong security guarantees. Evaluation on SPEC CPU2017 shows an average performance overhead of 3.85%, with real-world applications exhibiting overheads ranging from 2.97% to 7.80%. Janus offers effective speculative execution security and low performance and code size overhead, making it a robust solution for ARM-based systems.

## 中文摘要

我们提出 Janus，一个基于编译器的安全框架，可在 ARM64 平台上缓解 Spectre 等瞬态执行攻击与控制流劫持。Janus 将推测执行与控制流依赖同 PA 修饰符相结合，利用 PA 与 BTI 的微架构特性防止控制流推测攻击，并借助现有的控制流完整性机制同时保障控制流与推测执行的安全。为优化性能，Janus 通过跨不同防御层合并防御操作（修饰符合并）以及复用受保护变量的寄存器（载体复用）来最小化开销，同时保持强安全保证。在 SPEC CPU2017 上的评测显示平均性能开销为 3.85%，真实应用的开销介于 2.97% 与 7.80% 之间。Janus 提供了有效的推测执行安全保障，且性能与代码体积开销很低，是面向 ARM 系统的稳健解决方案。

## 英文关键词

transient execution attacks, ARM Pointer Authentication, compiler hardening

## 中文关键词

瞬态执行攻击、ARM 指针认证、编译器加固
