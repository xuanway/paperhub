PMU-Faker: The Apparently Harmless Performance Monitoring Unit Events Are Actually Harmful
Authors：
[Zeru Lan](https://63dac.conference-program.com/?post_type=page&p=15&uid=2412881496676575956)，[Pengfei Qiu](https://63dac.conference-program.com/?post_type=page&p=15&uid=67100257388396941571)，[Yaxuan Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=9859666586121227136)，[Ziyan Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=114693857308364559)，[Zhihao Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=39765667239448407341)，[Jiayi Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=7427825191365237934)，[Chunlu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3018622213155594684)，[Dongsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=209438080078268597)，[Gang Qu](https://63dac.conference-program.com/?post_type=page&p=15&uid=064143)

## 中文标题

PMU-Faker：看似无害的性能监控单元事件实则有害

## 英文摘要

Previous studies have verified that some special Performance Monitoring Unit (PMU) events are insecure. In this work, we further disclose that even the PMU events are securely designed and implemented, they are capable of constructing malicious attacks. We develop and implement a fuzz testing framework to automatically identify and verify numerous PMU events. Based on which, we successfully discover 118 vulnerable PMU events. Leveraging these identified events, we introduce PMU-Faker, a precise timing mechanism that can implement most of the timing-based side channel attacks without timer. To accommodate variations in instruction-triggered cycle durations, PMU-Faker provides two timing mechanisms with varying levels of granularity, thereby balancing precision and adaptability. Moreover, we successfully utilizing PMU-Faker to implement four attacks including executing transient execution attacks, extracting AES’s key, conducting attacks against Intel Software Guard Extensions (SGX), and achieving cross-virtual machine information leakage.

## 中文摘要

以往研究已证实，某些特殊的性能监控单元（PMU）事件是不安全的。在本工作中，我们进一步揭示：即使 PMU 事件在设计实现上是安全的，它们仍可被用于构造恶意攻击。我们开发并实现了一个模糊测试框架，以自动识别与验证大量 PMU 事件，并据此成功发现 118 个存在脆弱性的 PMU 事件。利用这些事件，我们提出 PMU-Faker——一种精确的计时机制，能够在无计时器的情况下实现大多数基于时间的侧信道攻击。为适应不同指令触发周期时长的差异，PMU-Faker 提供两种不同粒度的计时机制，从而在精度与适应性之间取得平衡。此外，我们成功利用 PMU-Faker 实施了四类攻击，包括执行瞬态执行攻击、提取 AES 密钥、针对 Intel 软件保护扩展（SGX）的攻击，以及实现跨虚拟机信息泄露。

## 英文关键词

Performance Monitoring Unit, Side-channel Attack, Transient Execution Attack, Timing Mechanism, Processor Security

## 中文关键词

性能监控单元、侧信道攻击、瞬态执行攻击、计时机制、处理器安全
