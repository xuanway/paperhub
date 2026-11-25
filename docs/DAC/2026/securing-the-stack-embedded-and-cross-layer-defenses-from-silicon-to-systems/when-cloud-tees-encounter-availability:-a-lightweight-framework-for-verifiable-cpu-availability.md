When Cloud TEEs Encounter Availability: A Lightweight Framework for Verifiable CPU Availability
Authors：
[Shangjie Pan](https://63dac.conference-program.com/?post_type=page&p=15&uid=686903807506444044)，[Haochuan Lei](https://63dac.conference-program.com/?post_type=page&p=15&uid=9500894831626398743)，[Yinghao Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5707723965200323177)，[Dongrong Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=26717175694383714001)，[Dong Du](https://63dac.conference-program.com/?post_type=page&p=15&uid=86596197499044950961)，[Hang Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=947343)，[Xiaowei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=614143)

## 中文标题

当云 TEE 遭遇可用性：面向可验证 CPU 可用性的轻量级框架

## 英文摘要

Trusted Execution Environments (TEEs) provide confidentiality and integrity, but their reliance on untrusted schedulers makes them vulnerable to CPU Denial-of-Service (DoS) attacks, compromising availability. Existing solutions either enlarge the Trusted Computing Base (TCB), rely on static closed-world workload assumptions that block dynamic enclave admission, or require hardware modifications. We propose AvaTEE, a lightweight framework for verifiable CPU availability in TEEs. AvaTEE uniquely integrates resource negotiation into remote attestation, providing a verifiable resource commitment pre-deployment. At runtime, a trusted scheduler performs dynamic monitoring and preemptive arbitration to mitigate DoS attacks. We evaluate AvaTEE on an FPGA. The results demonstrate that it (1) provides robust protection under contention, where native TEEs suffer a 94.8% performance loss and up to a 19.7× slowdown; (2) incurs negligible overhead (less than 2%) during enclave startup and normal runtime; and (3) maintains near-native performance, with only 1.70% average overhead compared to Keystone.

## 中文摘要

可信执行环境（TEE）提供机密性与完整性，但其对不可信调度器的依赖使其易受 CPU 拒绝服务（DoS）攻击，从而危及可用性。现有方案要么扩大可信计算基（TCB），要么依赖静态的封闭世界负载假设而阻碍动态 enclave 准入，要么需要硬件改动。我们提出 AvaTEE，一个用于 TEE 中可验证 CPU 可用性的轻量级框架。AvaTEE 独到地将资源协商融入远程证明，在部署前提供可验证的资源承诺。在运行时，可信调度器执行动态监控与抢占式仲裁，以缓解 DoS 攻击。我们在 FPGA 上对 AvaTEE 进行了评估。结果表明：(1) 它在资源竞争下提供了稳健保护，而原生 TEE 在此情形下性能损失达 94.8%、最慢可达 19.7 倍；(2) 在 enclave 启动与正常运行期间开销可忽略（低于 2%）；(3) 保持接近原生的性能，相比 Keystone 平均开销仅 1.70%。
