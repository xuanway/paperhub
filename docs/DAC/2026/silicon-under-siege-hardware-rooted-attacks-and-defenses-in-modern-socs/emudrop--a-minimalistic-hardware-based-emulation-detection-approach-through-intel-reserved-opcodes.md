Emudrop: A Minimalistic, Hardware-Based Emulation Detection Approach Through Intel Reserved Opcodes
Authors：
[Kaiyuan Rong](https://63dac.conference-program.com/?post_type=page&p=15&uid=44607160024331571721)，[Ke Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=96415502067965457851)，[Pengfei Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67100257388396941571)，[Dapeng Ju](https://63dac.conference-program.com/?post_type=page&p=15&uid=33959432853905687861)，[Dongsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=209438080078268597)

## 中文标题

EmuDRop：一种通过 Intel 保留操作码实现的极简硬件级仿真检测方法

## 英文摘要

Emulation-based dynamic analysis detects malicious software by observing runtime behavior in a controlled environment. Malware increasingly adopts evasion techniques to recognize such environments and hide malicious activities. In this paper, we propose EmuDRop, a minimalistic emulation-detection attack that exploits Intel reserved opcodes. EmuDRop leverages microarchitectural differences between real hardware and emulators to identify emulated execution. We reverse-engineer reserved opcodes, characterize their microarchitectural effects, and evaluate EmuDRop on five Intel CPU cores and QEMU, a widely used and representative emulator. The results show that EmuDRop reliably identifies emulated environments.

## 中文摘要

基于仿真的动态分析通过在受控环境中观察运行时行为来检测恶意软件。恶意软件正越来越多地采用规避技术来识别此类环境并隐藏恶意活动。本文提出 EmuDRop，一种利用 Intel 保留操作码的极简仿真检测攻击。EmuDRop 借助真实硬件与仿真器之间的微架构差异来识别仿真执行。我们对保留操作码进行逆向工程，刻画其微架构效应，并在五种 Intel CPU 核心以及广泛使用且具代表性的仿真器 QEMU 上评估 EmuDRop。结果表明，EmuDRop 能够可靠地识别仿真环境。

## 英文关键词

Emulation Detection, Reserved Opcodes, Microarchitectural Behavior, Timing Attack, Exception Analysis

## 中文关键词

仿真检测、保留操作码、微架构行为、时序攻击、异常分析
