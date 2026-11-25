Real-Time, Lightweight, High Coverage Error Detection and Correction for CRYSTALS with Small-Modulus Paths
Authors：
[Ziying Ni](https://63dac.conference-program.com/?post_type=page&p=15&uid=102455780054677682)，[ayesha khalid](https://63dac.conference-program.com/?post_type=page&p=15&uid=916443)，[Yijun Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=41376164522760116571)，[Weiqiang Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=566243)，[Maire O'Neill](https://63dac.conference-program.com/?post_type=page&p=15&uid=966243)

## 中文标题

面向小模数路径 CRYSTALS 方案的实时、轻量、高覆盖错误检测与纠正

## 英文摘要

The Number Theoretic Transform (NTT) dominates the hardware latency of lattice-based post-quantum cryptography (PQC) and is vulnerable to soft errors and fault injection. Existing protection mechanisms either require re-computing, assume a Residue Number System (RNS) datapath, or provide error detection only without real-time correction. This work presents two lightweight architectures for real-time fault detection and correction for NTT modular multipliers targeting the non-RNS primes used in the CRYSTALS lattice-based PQC schemes. Method 1 exploits the pseudo-Mersenne structure of the CRYSTALS moduli to build ultra-lightweight dual-modulus residue paths for error detection. Method 2 introduces cross-basis single-modulus checks together with lookup-table-based single-bit correction and a mixed linear CRT scheme for multi-bit recovery. On Artix-7, the detection configurations incur 55–78% area overhead; single-bit detection achieves 100%, and multi-bit detection at least 99.01% or nearly 100% under the tested settings. The design requires no re-computation and has a shorter critical path delay and surpasses state-of-the-art and Triple Modular Redundancy (TMR) baselines in area, error coverage, and latency.

## 中文摘要

数论变换（NTT）是格基后量子密码（PQC）硬件延迟的主导因素，且易受软错误与故障注入的影响。现有防护机制要么需要重新计算，要么假定采用剩余数系统（RNS）数据通路，要么仅能检测错误而无法实时纠正。本工作针对 CRYSTALS 格基 PQC 方案中所用的非 RNS 素数，提出两种面向 NTT 模乘器的实时故障检测与纠正轻量级架构。方法一利用 CRYSTALS 模数的伪梅森（pseudo-Mersenne）结构，构建超轻量的双模数剩余路径以实现错误检测。方法二引入跨基单模数校验，结合基于查找表的单比特纠正与混合线性 CRT 方案以实现多比特恢复。在 Artix-7 上，检测配置的面积开销为 55%–78%；单比特检测覆盖率达 100%，在测试设置下多比特检测覆盖率至少为 99.01%，或接近 100%。该设计无需重新计算，关键路径延迟更短，并在面积、错误覆盖率与延迟方面优于现有最优方案及三模冗余（TMR）基线。

## 英文关键词

Error detection and correction, lattice-based post-quantum cryptography, CRYSTALS, FPGA

## 中文关键词

错误检测与纠正、格基后量子密码、CRYSTALS、FPGA
