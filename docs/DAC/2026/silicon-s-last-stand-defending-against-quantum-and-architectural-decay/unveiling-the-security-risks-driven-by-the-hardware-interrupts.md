Unveiling the Security Risks Driven by the Hardware Interrupts
Authors：
[Zhihao Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=39765667239448407341)，[Pengfei Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67100257388396941571)，[Zhouyang Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=9115442521498747709)，[Yaxuan Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=9859666586121227136)，[Zeru Lan](https://63dac.conference-program.com/?post_type=page&p=15&uid=2412881496676575956)，[Jiliang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=395738577118476173)，[Chunlu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3018622213155594684)，[Gang Qu](https://63dac.conference-program.com/?post_type=page&p=15&uid=064143)，[Dongsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=209438080078268597)

## 中文标题

揭示硬件中断所引发的安全风险

## 英文摘要

The interrupt is a significant mechanism for computer systems to schedule hardware resources. We find that some hardware interrupts are not well-managed so that they can expose low-level events to unprivileged software, which introduce unanticipated security risks. We first design an automated testing framework to identify the interrupts’ working features and trigger conditions, which helps us discover six vulnerable interrupts. Next, we design a novel set of attack primitives for leaking secrets using them. Finally, we realize four attacks with the proposed attack primitives: leaking contents from a restricted directory, fingerprinting DNN model architectures, classifying processes, and enhancing Spectre attacks.

## 中文摘要

中断是计算机系统调度硬件资源的重要机制。我们发现，部分硬件中断未被妥善管理，会向非特权软件暴露底层事件，从而引入意料之外的安全风险。我们首先设计了一个自动化测试框架，用于识别中断的工作特性与触发条件，并据此发现六个存在脆弱性的中断。接着，我们设计了一组新颖的攻击原语，用以利用这些中断泄露秘密。最后，基于所提攻击原语，我们实现了四类攻击：从受限目录泄露内容、识别 DNN 模型架构指纹、对进程进行分类，以及增强 Spectre 攻击。

## 英文关键词

System Interface, Hardware Interrupt-Driven Attacks, Side Channel Attacks, Muti-Bit Transmission

## 中文关键词

系统接口、硬件中断驱动攻击、侧信道攻击、多位传输
