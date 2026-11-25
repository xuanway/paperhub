Mistletunnel: Attacking KASLR on Apple M-Series Silicon with a Novel TLB Side Channel
Authors：
[Hanyin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=77167121964783264501)，[Jin Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6060866764063484923)，[Rihui Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=46017660522228028601)，[Kaiyuan Rong](https://63dac.conference-program.com/?post_type=page&p=15&uid=44607160024331571721)，[Hongpei Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=65454221681834407711)，[Yun Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7245234199944961248)，[Jian Dong](https://63dac.conference-program.com/?post_type=page&p=15&uid=4795728822119914455)，[Dongsheng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=209438080078268597)

## 中文标题

MistleTunnel：利用新型 TLB 侧信道攻击 Apple M 系列芯片上的 KASLR

## 英文摘要

KASLR is a critical defense on macOS, whose implementation on M-series silicon and the latest macOS is further strengthened by hardware–software mitigations, with no practical bypass. We perform a systematic reverse-engineering of the TLB on M-series silicon and uncover a novel user–kernel TLB side-channel, TLBarge, that enables precise monitoring of kernel instruction execution. Leveraging TLBarge, we demonstrate MistleTunnel, the first attack that compromises macOS 26’s 15-bit KASLR by recovering its lower 8 bits. Operating solely through normal syscalls, MistleTunnel collapses the effective KASLR entropy to 0.39%, significantly reducing its intended security.

## 中文摘要

KASLR 是 macOS 上的一项关键防御机制，其在 M 系列芯片与最新版 macOS 上的实现通过软硬件协同的缓解措施得到进一步强化，目前尚无实用绕过手段。我们对 M 系列芯片上的 TLB 进行了系统性逆向工程，发现了一种新型的用户态–内核态 TLB 侧信道 TLBarge，它能够精确监控内核指令的执行。借助 TLBarge，我们实现了 MistleTunnel，这是首个攻破 macOS 26 的 15 位 KASLR 的攻击，成功恢复其低 8 位。MistleTunnel 仅通过常规系统调用即可运行，将有效的 KASLR 熵压缩至 0.39%，显著削弱了其本应具备的安全性。
