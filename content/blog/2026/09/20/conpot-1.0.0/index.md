---
title: "Conpot 1.0.0 released"
authors: ["Lukas Rist"]
date: "2026-09-20T16:20:00+02:00"
tags: ["conpot", "honeypot", "ics", "scada"]
---

The [Conpot](https://github.com/mushorg/conpot) team is proud to announce [version 1.0.0](https://github.com/mushorg/conpot/releases/tag/v1.0.0). This is a platform rewrite, not a point release. The honeypot still emulates ICS/SCADA services so you can collect attacker intelligence, but the runtime, templates, logging sinks, and several protocol libraries are new.

Treat this as a **breaking upgrade**: migrate templates and log consumers, then re-validate Docker ports and deployment scripts.

<!--more-->

[Conpot](https://github.com/mushorg/conpot) is a low-interaction ICS/SCADA honeypot. You configure device templates and protocol servers so scanners and operators see a plausible industrial system, while sessions and attacks land in structured logs. 1.0.0 keeps that mission and replaces the stack underneath it.

## Runtime and packaging

The gevent stack is gone. Protocol servers now run on **asyncio**. The CLI is a normal asyncio entrypoint: `python -m conpot` / `conpot.cli`.

Startup is less rigid: fewer hard restrictions at launch, and clearer operator UX. MAC-address spoofing was **removed**.

## Templates and databus (breaking)

Templates moved from **XML to TOML**, with a flatter layout: `templates/<name>/template.toml` (metadata + databus) plus per-protocol `*.toml`. Auxiliary files stay in subdirectories only when needed (for example HTTP `htdocs`).

The databus is decoupled from `SessionManager`. `get_value()` evaluates a mapping once. Random/generated value functions, extra SNMP-oriented emulators, and a simulated PLC-style emulator sit on that bus.

## Protocol changes

Protocol work in this release is mostly correctness, library upgrades, and crash/DoS hardening rather than brand-new industrial dialects:

- **S7:** parameter-length calculation, read/write, PLC-stop.
- **Modbus:** pymodbus, recv-path fixes, and a DoS fix for unbounded byte-at-a-time oversized reads.
- **IEC 104:** IOA and float endianness, types 100–103, friendlier I-frame logs.
- **ENIP/CIP:** exception/crash fixes, device-info handling, **cm-ethernetip**.
- **BACnet:** bacpypes3 plus BACnet/IP encode/decode.
- **HTTP:** aiohttp; template substitution no longer uses `HTMLParser`.
- **SNMP:** richer emulators, default listen port **16100**, no custom MIB compile path.
- **FTP / IPMI / TFTP:** FTP handler exception-loop fix, RFC 959 greeting expectations, IPMI IPv6/test and JSON logging fixes, FakeSession timeout before pyghmi init, TFTP test cleanup.

## Logging and sessions (breaking for sinks)

Attack logging is structured (schema version 1) across JSON, SQLite, syslog, HPFriends, and TAXII. Events carry `event_time` distinct from session start. Remote **IP and port**, and destination from the socket, are first-class fields. Syslog gets attack JSON explicitly.

HPFriends/JSON payloads use `session_id` / `protocol` / flat endpoints instead of the old `id` / `data_type` / remote tuples. Sessions can be deleted.

If you ingest Conpot into a SIEM, HPFriends, or a homegrown parser, update field mappings before you cut over.

## Get it, run it, contribute

Release notes and the full changelog live on GitHub: [Conpot 1.0.0](https://github.com/mushorg/conpot/releases/tag/v1.0.0).

Thanks to everyone who contributed since the last line of the 0.6-era tree, including first-time contributors who landed protocol, packaging, and test work over a long stretch of PRs. If you are running ICS honeypots, please try 1.0.0, file issues when templates or sinks surprise you, and consider sharing anonymized attack data with the community.

We are looking for operators and developers who care about industrial protocols. Issues and pull requests are welcome on [mushorg/conpot](https://github.com/mushorg/conpot).
