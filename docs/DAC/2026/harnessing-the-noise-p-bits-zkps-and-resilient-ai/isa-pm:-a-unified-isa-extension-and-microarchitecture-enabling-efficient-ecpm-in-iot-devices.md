ISA-PM: A Unified ISA Extension and Microarchitecture Enabling Efficient ECPM in IoT Devices
Authors：
[Zhaoyuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=02947918825064890641)，[Kun Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8822640233255848955)，[Kui Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=130443)

## 中文标题

ISA-PM：在 IoT 设备中实现高效 ECPM 的统一 ISA 扩展与微架构

## 英文摘要

Elliptic curve cryptography (ECC) has become a preferred choice for securing resource-constrained Internet-of-Things (IoT) devices, offering strong security with compact key sizes. As the computational core of ECC, elliptic curve point multiplication (ECPM) dominates both the performance and silicon area of ECC coprocessors. However, implementing ECPM in area-constrained applications remains challenging due to its significant arithmetic complexity and the diversity of field parameters. Most existing hardware accelerators are tailored to a specific elliptic curve modulus, limiting their scalability and forcing costly redesigns to support multiple curves. To overcome this inflexibility, we propose ISA-PM, a unified instruction set architecture (ISA) extension and microarchitecture that supports flexible ECPM computation across various elliptic curves, including widely used Montgomery and short Weierstrass forms. To effectively reduce the design area of ISA-PM, we propose a three-phase computation scheme that decomposes complex ECPM operations into iterative execution of small bit-width modular operations. Furthermore, we develop a design space exploration method based on bit-width partitioning and operation parallelism to balance resource utilization and computational latency, ensuring efficient implementation under area constraints. Experimental results based on AMD Virtex-7 FPGA demonstrate that ISA-PM delivers up to 8.37× improvement in area–time product (ATP) over the state-of-the-art lightweight ECPM hardware accelerators.

## 中文摘要

椭圆曲线密码（ECC）以紧凑的密钥尺寸提供强安全性，已成为资源受限的物联网（IoT）设备安全保护的首选方案。作为 ECC 的计算核心，椭圆曲线点乘（ECPM）主导了 ECC 协处理器的性能与芯片面积。然而，由于算术复杂度高且域参数多样，在面积受限的应用中实现 ECPM 仍具有挑战性。现有大多数硬件加速器针对特定的椭圆曲线模数定制，限制了可扩展性，并迫使人们为支持多条曲线而进行代价高昂的重新设计。为克服这种不灵活性，我们提出 ISA-PM，一种统一的指令集架构（ISA）扩展与微架构，可支持跨多种椭圆曲线（包括广泛使用的 Montgomery 形式与短 Weierstrass 形式）的灵活 ECPM 计算。为有效降低 ISA-PM 的设计面积，我们提出三阶段计算方案，将复杂的 ECPM 运算分解为小位宽模运算的迭代执行。此外，我们开发了一种基于位宽划分与操作并行度的设计空间探索方法，以在资源利用率与计算延迟之间取得平衡，确保在面积约束下高效实现。基于 AMD Virtex-7 FPGA 的实验结果表明，与最先进的轻量级 ECPM 硬件加速器相比，ISA-PM 的面积-时间积（ATP）最高提升 8.37 倍。
