Procyon: Promoting Fine-Grained Multi-Tenancy to Optimize Sparse Streaming Accelerators
Authors：
[Ubaid Bakhtiar](https://63dac.conference-program.com/?post_type=page&p=15&uid=05850350556556524501)，[Jeremy Xu Sha](https://63dac.conference-program.com/?post_type=page&p=15&uid=30304352209367365721)，[Helya Hosseini](https://63dac.conference-program.com/?post_type=page&p=15&uid=985843)，[Bahar Asgari](https://63dac.conference-program.com/?post_type=page&p=15&uid=195843)

## 中文标题

Procyon：推广细粒度多租户以优化稀疏流式加速器

## 英文摘要

Sparsity has become a defining characteristic of modern workloads, motivating the development of specialized accelerators to mitigate the challenges inherent to sparsity. Sparse streaming accelerators have proved to be an effective solution, yet current designs are restricted to single-workload execution. Additionally, they exhibit significant underutilization in processing elements (PEs) due to their non-zero scheduling strategies. To address these limitations, we propose Procyon, a fine-grain multi-tenancy framework that fuses the PE instruction streams of multiple workloads into a unified execution schedule. This allows instructions from different workloads to execute on the same PE, thereby, improving its utilization and enabling concurrent execution of multiple workloads on a single accelerator instance. We evaluate Procyon on AMD Alveo U55C FPGA using the SuiteSparse workloads and show that it substantially reduces PE underutilization that results in 3× speedup over state-of-the-art sparse streaming accelerators (Serpens and Chasoň), and reaches a peak throughput of 61.2 GFLOP/s.

## 中文摘要

稀疏性已成为现代负载的定义性特征，推动了专用加速器的发展，以缓解稀疏性所固有的挑战。稀疏流式加速器已被证明是有效的解决方案，但当前设计仅限于单负载执行。此外，由于其非零调度策略，它们在处理单元（PE）上存在显著的利用率不足。为解决这些局限，我们提出 Procyon，一个细粒度多租户框架，将多个负载的 PE 指令流融合为统一的执行调度。这使得来自不同负载的指令可在同一 PE 上执行，从而提高其利用率，并在单个加速器实例上实现多负载的并发执行。我们在 AMD Alveo U55C FPGA 上使用 SuiteSparse 负载评估 Procyon，结果表明它大幅减少了 PE 利用率不足，相比最先进的稀疏流式加速器（Serpens 与 Chasoň）取得 3× 的加速，并达到 61.2 GFLOP/s 的峰值吞吐。
