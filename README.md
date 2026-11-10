# Digital Detective (`digital-detective-8471`)

> **Diwali Independent Learning Assignment**  
> An investigative journey into core computer science fundamentals: hardware architectures, operating systems, command-line interfaces, programming execution models, data representations, version control, and computer networking.

---

## 1. Project Overview & Purpose

Welcome to **The Digital Detective** repository. This project was developed as an independent learning assignment to investigate and demystify the internal mechanics of modern computer systems. Through eight structured missions, the assignment progresses from foundational hardware components to high-level networking protocols.

Each mission was investigated, documented, and committed separately to demonstrate a transparent, incremental learning progression.

---

## 2. Mission Index

Every mission contains its own dedicated documentation, code artifacts, and privacy-safe visual evidence:

| Mission | Title | Directory & Documentation | Status | Highlights & Key Deliverables |
| :---: | :--- | :--- | :---: | :--- |
| **00** | **Workspace Setup** | [mission-00-setup/README.md](./mission-00-setup/README.md) | **Completed** | GitHub workspace initialization, directory scaffolding, and Git author configuration. |
| **01** | **Computer Basics & IPOS** | [mission-01-computer-basics/README.md](./mission-01-computer-basics/README.md) | **Completed** | The Input-Processing-Output-Storage cycle, hardware vs. software classification, and everyday computing systems. |
| **02** | **Terminal & File Management** | [mission-02-terminal/README.md](./mission-02-terminal/README.md) | **Completed** | Command-line navigation, safe file manipulation (`>` vs. `>>`, `cp` vs. `mv`), UNIX pipes, and Homebrew package manager. |
| **03** | **Operating System Mechanics** | [mission-03-operating-system/README.md](./mission-03-operating-system/README.md) | **Completed** | Kernel telemetry (`Darwin arm64`), process scheduling (PID/PPID), absolute vs. relative paths, and POSIX permissions (`rwx`). |
| **04** | **How Programs Run** | [mission-04-programs/README.md](./mission-04-programs/README.md) | **Completed** | Working [`hello.py`](./mission-04-programs/hello.py), compiler vs. interpreter comparison, and Python's hybrid bytecode/PVM model. |
| **05** | **Numbers & Data Representation** | [mission-05-numbers-data/README.md](./mission-05-numbers-data/README.md) | **Completed** | Manual radix conversions (Decimal $\leftrightarrow$ Binary $\leftrightarrow$ Hex), Python verification, working [`number_converter.py`](./mission-05-numbers-data/number_converter.py), and ASCII/UTF-8 text encoding. |
| **06** | **Git & GitHub Collaboration** | [mission-06-git-github/README.md](./mission-06-git-github/README.md) | **Completed** | Staging vs. committing, feature branch `update-about`, [Pull Request #1](https://github.com/Tejasrastogi/Digital-Detective-8471/pull/1) lifecycle, and Git command glossary. |
| **07** | **Networking & Web Protocols** | [mission-07-networking/README.md](./mission-07-networking/README.md) | **Completed** | LAN/MAN/WAN topologies, router and DNS concepts, ICMP ping latency tests, DNS lookups, and the 6-step website lifecycle. |
| **08** | **Final Report & Synthesis** | [mission-08-final-report/README.md](./mission-08-final-report/README.md) | **Completed** | Comprehensive audit review, checklist verification, corrections log, and final submission verification. |

Visual evidence, terminal outputs, and verification records are preserved in the [`evidence/`](./evidence) directory.

---

## 3. Topics Explored

- **Computer Architecture**: Transducers, CPU registers, Arithmetic Logic Unit (ALU), memory buses, volatile RAM vs. non-volatile NVMe flash storage.
- **Operating Systems**: Kernel responsibilities, preemptive multitasking, Process Identifiers (PIDs), memory virtualization, device drivers, and POSIX permissions.
- **Command-Line Interface (CLI)**: Navigation (`pwd`, `cd`), directory listings (`ls -lah`), output redirection (`>`, `>>`), UNIX pipelines (`|`), and package managers.
- **Program Execution**: Machine code binaries vs. interpreted source code, ahead-of-time (AOT) compilation, dynamic interpretation, and Python's intermediate bytecode architecture (`.pyc` / PVM).
- **Data Representation**: Positional number bases (base-2 binary, base-10 decimal, base-16 hexadecimal), 4-bit nibbles, byte structures, 7-bit ASCII, and variable-length UTF-8 encoding.
- **Version Control & Collaboration**: Git object model, working directory vs. staging index vs. repository history, branch isolation, and GitHub Pull Request peer review workflows.
- **Computer Networking**: Network topologies (LAN, MAN, WAN), packet switching, routing, Domain Name System (DNS) resolution hierarchies, transport reliability (TCP/TLS), and application protocols (HTTP/HTTPS).

---

## 4. How to Run the Number Converter

The repository includes a Python command-line number converter created in Mission 5 that converts positive decimal integers into their binary (base-2) and hexadecimal (base-16) equivalents.

### Prerequisites:
- Python 3.8 or higher installed on your machine.

### Execution Steps:
1. Open your terminal and navigate to the `mission-05-numbers-data` folder:
   ```bash
   cd mission-05-numbers-data
   ```
2. Run the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
3. Enter any positive integer when prompted:
   ```text
   ==========================================
         Digital Detective Number Converter  
   ==========================================
   Enter a decimal number: 42

   --- Conversion Results ---
   Decimal (Base 10):     42
   Binary (Base 2):       0b101010
   Hexadecimal (Base 16): 0X2A
   --------------------------
   ```

---

## 5. My Learning Summary

Through the completion of the Digital Detective assignment, several foundational computing principles were explored and internalized:

1. **The Universal IPOS Loop**:
   Understood how every digital task—from typing a simple sentence to loading a webpage—maps onto the physical Input $\to$ Processing $\to$ Output $\to$ Storage loop across hardware buses, CPU registers, and SSD memory blocks.
2. **The Operating System as an Abstraction Layer**:
   Gained appreciation for the OS kernel, which provides safe abstractions (virtual memory, processes, file descriptors) so that user software can run concurrently without hardware conflicts or security violations.
3. **Compilation vs. Interpretation Trade-offs**:
   Learned why performance-critical systems utilize compiled languages (C, Rust, Go) for direct CPU execution, while high-level interpreted and hybrid environments (Python, JavaScript) prioritize developer productivity and cross-platform flexibility.
4. **Data Representation & Universal Standards**:
   Understood that computers only process binary electrical states. Hexadecimal provides compact human notation for bytes, while encoding standards (UTF-8) allow international text and symbols to be transmitted globally without corruption.
5. **Team Collaboration through Version Control**:
   Mastered professional Git workflows: isolating features on dedicated branches, crafting clean commits with descriptive messages, and proposing changes via GitHub Pull Requests for peer review before merging into `main`.
6. **The Interconnected Web**:
   Traced the path of a URL request from local browser input, through DNS resolution and dynamic packet-switched routing across the global Internet, to encrypted TLS/TCP handshakes and HTTP server responses.

---

## 6. Privacy & Security Compliance

In strict adherence to assignment guidelines:
- **No Personal Data**: All private computer usernames, local device hostnames, serial numbers, local network IP addresses, and Wi-Fi SSIDs have been completely removed or sanitized with `[redacted]`.
- **Image Redactions**: All terminal evidence screenshots in [`evidence/`](./evidence) have been processed using Gaussian blur filters over sensitive prompts and local IP addresses.
- **Granular Git History**: Each mission was documented and committed as an independent, meaningful milestone.

---

## 7. Repository Link & Submission

- **GitHub Repository**: [https://github.com/Tejasrastogi/Digital-Detective-8471](https://github.com/Tejasrastogi/Digital-Detective-8471)
- **Author**: Tejas Rastogi
- **License**: Educational Learning Project (Newton School)
