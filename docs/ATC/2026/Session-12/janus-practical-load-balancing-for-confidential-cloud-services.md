# JANUS: Practical Load Balancing for Confidential Cloud Services

**中文标题**：JANUS：面向机密云服务的实用负载均衡

**官方议程标题**：Janus: Practical Load Balancing for Confidential Cloud Services

**所属 Session**：[Session 12: Security and Privacy](index.md) · [ATC 2026](../index.md)

**作者**：Qi Guo (Max Planck Institute for Informatics), Alice Dethise (Nokia Bell Labs), Ruichuan Chen (Nokia Bell Labs), Istemi Ekin Akkus (Nokia Bell Labs), Ivica Rimac (Nokia Bell Labs), Lieven Trappeniers (Nokia Bell Labs)

## 英文摘要
Confidential computing enables a cloud service to prove, by remote attestation, that it runs inside a Trusted Execution Environment (TEE). Recent work has bound this attestation to Transport Layer Security (TLS) so that a client can verify TEEs via the TLS channel, but these designs assume a client talking to a single specific attested server. Realistic cloud services, however, are not run on single servers: they are load-balanced, structured as a frontend fronting an elastic pool of backend servers. Extending current attested-TLS designs onto this pool is problematic, forcing either custom client logic, a Certificate Authority (CA) certificate issuance per backend server, or a fresh attestation on every connection. We present Janus, a practical load-balancing architecture for confidential cloud services. Specifically, a small attested frontend, running inside a TEE, holds the only client-facing TLS identity: it obtains a CA-issued X.509 certificate that carries its attestation evidence in a certificate extension. The frontend then admits backend servers, attesting each and signing its public key using a short-lived RFC-9345 Delegated Credential so that every backend serves client traffic under the frontend’s single attested identity. This also allows each backend to be attested only once at admission rather than per client connection. Janus piggybacks on what the TLS ecosystem has deployed or is developing — X.509 certificate extensions, ACME certificate issuance, and Delegated Credentials — so it complies with the current networking practices and trends, and changes nothing in the TLS protocol. It supports standard load-balancing modes (i.e., proxy and redirection). Our evaluation shows that the marginal connection-establishment cost of Janus is as low as 4 ms (in proxy mode) and 12 ms (in redirection mode), compared with vanilla TLS.

## 中文摘要
机密计算使云服务能够通过远程认证证明其运行在可信执行环境（TEE）之内。近期工作将这种认证与传输层安全（TLS）绑定，使客户端可以通过 TLS 信道验证 TEE，但这些设计都假设客户端与单个特定的、经过认证的服务器通信。然而，现实的云服务并不运行在单台服务器上：它们经过负载均衡，结构上由一个前端和其背后的弹性后端服务器池组成。将当前的认证 TLS 设计扩展到这样的服务器池上存在诸多问题，要么需要定制客户端逻辑，要么需要为每台后端服务器签发 CA 证书，要么需要在每条连接上重新进行一次认证。我们提出 Janus，一种面向机密云服务的实用负载均衡架构。具体而言，一个运行在 TEE 内的、经过认证的小型前端持有唯一的面向客户端的 TLS 身份：它获得一张由 CA 签发的 X.509 证书，该证书在证书扩展中携带其认证证据。前端随后接纳后端服务器，对每台后端进行认证，并使用短期的 RFC-9345 委托凭证（Delegated Credential）为其公钥签名，从而使每台后端都在前端的单一认证身份下服务客户端流量。这也使每台后端只需在接纳时认证一次，而不必在每条客户端连接上认证。Janus 依托 TLS 生态已经部署或正在发展的机制——X.509 证书扩展、ACME 证书签发和委托凭证——因此符合当前的网络实践与趋势，且不改变 TLS 协议的任何内容。它支持标准的负载均衡模式（即代理和重定向）。我们的评测表明，与原生 TLS 相比，Janus 的边际连接建立开销低至 4 ms（代理模式）和 12 ms（重定向模式）。

## 英文关键词
Confidential computing, trusted execution environment, delegated credential, cloud service, load balancing

## 中文关键词
机密计算，可信执行环境，委托凭证，云服务，负载均衡

[返回 Session 12](index.md) · [返回 ATC 2026](../index.md)
