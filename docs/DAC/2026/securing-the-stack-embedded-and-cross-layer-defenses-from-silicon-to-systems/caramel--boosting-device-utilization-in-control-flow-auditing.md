CARAMEL: Boosting Device Utilization in Control Flow Auditing
Authors：
[Alexandra Lengert](https://63dac.conference-program.com/?post_type=page&p=15&uid=08188537313099879771)，[Adam Caulfield](https://63dac.conference-program.com/?post_type=page&p=15&uid=81538734180485342121)，[Ivan De Oliveira Nunes](https://63dac.conference-program.com/?post_type=page&p=15&uid=949443625787005612)

## 中文标题

CARAMEL：提升控制流审计中的设备利用率

## 英文摘要

Micro-Controller Units (MCUs) are widely used in safety-critical systems, making them attractive targets for attacks. This calls for lightweight defenses that remain effective despite software compromise. Control Flow Auditing (CF-Aud) is one such mechanism wherein a remote Verifier (Vrf) is guaranteed to receive evidence about the control flow path taken on a Prover MCU (Prv), even when Prv software is compromised. Despite promising benefits, current CF-Aud architectures unfortunately require a “busy-wait” phase where a hardware-anchored root-of-trust (RoT) in Prv retains execution control to ensure delivery of control flow evidence to Vrf. This drastically reduces CPU utilization on Prv. In this work, we address this limitation with an architecture for Contention Avoidance in Runtime Auditing with Minimized Execution Latency (CARAMEL). CARAMEL is a hardware-software RoT co-design that enables Prv applications to resume while control flow evidence is transmitted to Vrf. This significantly reduces contention due to transmission delays and improves CPU utilization without giving up on security. Key to CARAMEL is our design of a new RoT with a self-contained (and minimal) dedicated communication interface. CARAMEL’s implementation and accompanying evaluation are made open-source. Our results show substantially improved CPU utilization at modest hardware cost.

## 中文摘要

微控制器（MCU）广泛用于安全关键系统，因而成为颇具吸引力的攻击目标。这要求即便软件已被攻陷仍能保持有效的轻量级防御。控制流审计（CF-Aud）便是这样一种机制：远程验证者（Vrf）被保证能够获得证明者 MCU（Prv）上所执行控制流路径的证据，即使 Prv 的软件已被攻陷。尽管前景可观，现有 CF-Aud 架构却需要一个“忙等”阶段，即 Prv 中由硬件锚定的可信根（RoT）保持执行控制权，以确保控制流证据送达 Vrf，这大幅降低了 Prv 的 CPU 利用率。在本工作中，我们通过一种用于运行时审计中竞争规避与执行延迟最小化（Contention Avoidance in Runtime Auditing with Minimized Execution Latency，CARAMEL）的架构来解决这一局限。CARAMEL 是一种硬件-软件 RoT 协同设计，使 Prv 应用能够在控制流证据向 Vrf 传输的同时恢复执行。这显著减少了传输延迟造成的竞争，并在不牺牲安全性的前提下提升了 CPU 利用率。CARAMEL 的关键在于我们设计了一种具有自包含（且极简）专用通信接口的新型 RoT。CARAMEL 的实现与配套评估均已开源。结果表明，我们以适度的硬件代价大幅提升了 CPU 利用率。
