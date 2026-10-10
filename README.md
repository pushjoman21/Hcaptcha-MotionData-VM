<div align="center">

# hCaptcha MotionData VM Disassembler

A disassembler for the bytecode virtual machine behind hCaptcha's MotionData collection, written as a study of JavaScript VM internals.

![Status](https://img.shields.io/badge/status-archived-lightgrey?style=flat-square)
![Purpose](https://img.shields.io/badge/purpose-educational-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

</div>

> [!IMPORTANT]
> **Archived research · Educational use only**
> This repository documents past research and is no longer maintained. The analyzed system has changed since publication, so the findings are **outdated** and may not reflect current versions.
> The material is provided solely for educational and defensive security purposes. It must not be used to circumvent protections, automate access without authorization, or violate any platform's terms of service.

> [!NOTE]
> At hCaptcha's request this repository was temporarily taken offline. It has been republished in its original, outdated state purely as an educational artifact and will not receive further updates.

---

## Overview

Many client-side protection scripts hide their logic inside a custom bytecode VM. This project takes the MotionData VM's bytecode and string table and translates them into a readable instruction listing, making the VM's control flow and data handling easier to study. Opcode names were assigned during analysis and are descriptive rather than official.

## Repository Structure

| Path | Description |
|------|-------------|
| `dissambler.py` | Disassembler: opcode table and decoding loop |
| `utils/utils.py` | Helper functions |
| `input/bytecode.txt` | Captured VM bytecode |
| `input/stringtable.txt` | Captured VM string table |
| `output/disassembled.txt` | Resulting instruction listing |

## Usage

```bash
python dissambler.py
```

## Research Topics

- Design of stack-based JavaScript virtual machines
- Opcode recovery and bytecode disassembly
- Obfuscation through virtualization

---

## Legal Notice

hCaptcha is a trademark of Intuition Machines, Inc. This project is independent and is not affiliated with, sponsored or endorsed by hCaptcha.

The software is provided "as is", without warranty of any kind. The author accepts no liability for any misuse.

## Contact & Takedown Requests

Vendors with concerns about this repository can reach out at **jomandiscord@gmail.com**. Content will be reviewed and adjusted or removed promptly where appropriate.
