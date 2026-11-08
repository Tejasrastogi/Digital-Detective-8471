# Mission 0: Create Your GitHub Workspace

## 1. Overview & Mission Objective
- **Assignment**: The Digital Detective — Diwali Independent Learning Assignment
- **Mission**: Mission 0 — Create your GitHub workspace
- **Repository Name**: `Digital-Detective-8471`
- **GitHub URL**: `https://github.com/<username>/Digital-Detective-8471`
- **Mission Objective**: Create a correctly named public repository and prepare a clear, standardized folder structure for all missions.
- **Privacy Standard**: In strict accordance with the assignment guidelines, no personal information (such as local computer username, personal email, device name, machine serial number, local Wi-Fi SSID, or IP address) is published.

---

## 2. Tasks Completed
1. **Repository Naming**: Followed the required assignment naming specification (`digital-detective-[last 4 digits of USN]`: `Digital-Detective-8471`).
2. **Local Project Workspace**: Established a clean local directory for the project (`./Digital-Detective-8471`).
3. **Mission Directory Structure**: Created dedicated subdirectories for all required missions (`mission-00-setup` through `mission-08-final-report`) and the `evidence/` directory.
4. **Documentation Files**: Created root `README.md` and initialized documentation files inside every mission directory.
5. **Tool & Environment Verification**: Confirmed active versions and operational readiness of Git and Python.
6. **Remote Synchronization**: Connected local workspace to GitHub remote repository (`origin`) on the default `main` branch.

---

## 3. Environment & Tools Verified
Primary system tools required for all subsequent missions were verified via the terminal:

| Tool | Verification Command | Version Checked | Status |
| :--- | :--- | :--- | :--- |
| **Git** | `git --version` | `git version 2.55.0` | Operational |
| **Python** | `python3 --version` | `Python 3.12.10` | Operational |
| **Operating System** | `uname -srm` | `Darwin (macOS arm64)` | Operational |
| **Shell** | `echo $SHELL` | `/bin/zsh` | Operational |

> **Privacy Note**: System hostnames, hardware serial numbers, and local user paths have been omitted from command outputs to maintain complete privacy and security.

---

## 4. Repository Structure & Files Created
The workspace adheres strictly to the required mission structure:

```text
Digital-Detective-8471/
├── .gitignore                          # Ignores OS-specific cache files (.DS_Store)
├── README.md                           # Master assignment overview & mission index
├── evidence/                           # Privacy-safe screenshots and verification logs
│   ├── Screenshot 2026-11-07 at 10.59.33 AM.png
│   ├── Screenshot 2026-11-07 at 11.16.50 AM.png
│   ├── Screenshot 2026-11-07 at 11.17.23 AM.png
│   └── Screenshot 2026-11-07 at 11.17.39 AM.png
├── mission-00-setup/
│   └── README.md                       # Setup details, environment, & repository info
├── mission-01-computer-basics/
│   └── README.md                       # IPOS, hardware, software, & everyday systems
├── mission-02-terminal/
│   └── README.md                       # Terminal activities & command investigations
├── mission-03-operating-system/
│   └── README.md                       # OS processes, paths, storage, & permissions
├── mission-04-programs/
│   └── README.md                       # Python test, compilation, & interpretation
├── mission-05-numbers-data/
│   ├── README.md                       # Number conversion & character encoding analysis
│   └── number_converter.py             # Python CLI number conversion tool
├── mission-06-git-github/
│   └── README.md                       # Git branch, PR, & distributed workflow tasks
├── mission-07-networking/
│   └── README.md                       # Networking fundamentals, sockets, & observations
└── mission-08-final-report/
    └── README.md                       # Final synthesis & submission checklist
```

---

## 5. Technical Understanding

### What is a Repository?
A **Git repository** (repo) is a version-controlled workspace managed by Git that records historical snapshots of project files over time. It consists of:
- **Working Tree**: The local files currently visible and being actively edited in the project folder.
- **Staging Area (Index)**: A preparatory holding area where changes are curated and formatted before committing.
- **Git Database (`.git/`)**: A directed acyclic graph (DAG) of cryptographically hashed commit objects storing historical snapshots, commit messages, authorship, and branch pointers.
- **Remote Synchronization**: By pushing changes to a remote host (GitHub), the repository serves as a secure, decentralized backup and collaboration hub.

### Why is the Structure Organised by Mission?
1. **Separation of Concerns**: Each mission investigates an isolated computing layer (e.g., hardware architecture, terminal manipulation, kernel execution, data encoding, computer networking). Organizing by mission prevents cross-contamination of code, reports, and evidence.
2. **Incremental Git History**: Dedicated directories allow atomic commits for each assignment milestone, creating a clean chronological log of progress.
3. **Structured Evaluation**: Evaluators can directly access each module's findings and corresponding proof without searching through unrelated files.

---

## 6. Setup Challenges & Resolutions

1. **Git Tracking of Directories**:
   - *Problem*: Git tracks file blobs rather than empty directories. Creating folders without files caused them to remain untracked by version control.
   - *Resolution*: Created initial `README.md` placeholder files in each mission folder, ensuring the entire planned hierarchy is committed and tracked.

2. **Shell Wildcard Expansion (`touch ./*/README.md`)**:
   - *Problem*: Relying on shell globbing can sometimes fail to match newly created subdirectories or produce incomplete results.
   - *Resolution*: Verified directory contents with `ls -la` and confirmed each individual `README.md` was created explicitly.

3. **Privacy Compliance & Sanitization**:
   - *Problem*: Standard terminal prompts display the active computer username (`user@device`), and screenshots or logs can inadvertently leak private host information.
   - *Resolution*: Enforced strict privacy sanitization across all documentation, replacing local user paths with relative paths and verifying that no private hardware, network, or identity data is exposed.

---

## 7. Visual Verification Evidence

All verification records for Mission 0 are preserved in the `evidence/` directory and embedded below:

### Evidence 1: Terminal Workspace Setup & Folder Creation
Execution of `git clone`, navigating to the project directory, creating the full sequence of mission directories (`mission-00-setup` through `mission-08-final-report`), touching initial README files, and verifying folder contents with `ls -l` and `ls -a`.

![Terminal Workspace Initialization](../evidence/Screenshot%202026-11-07%20at%2010.59.33%E2%80%AFAM.png)

---

### Evidence 2: Mission Verification & Explicit README Creation
Verification of individual subfolders (`mission-00-setup`, `mission-01-computer-basics`) and explicit `touch` operations across all mission subdirectories to guarantee that each mission folder contains its markdown documentation file.

![Terminal Verification and Touch](../evidence/Screenshot%202026-11-07%20at%2011.16.50%E2%80%AFAM.png)

---

### Evidence 3: Graphical File Tree in Finder
Overview of the complete `Digital-Detective-8471` workspace in the macOS Finder, verifying the existence of the root `README.md`, the `evidence/` directory, and all 9 mission folders.

![Finder Workspace Overview](../evidence/Screenshot%202026-11-07%20at%2011.17.23%E2%80%AFAM.png)

---

### Evidence 4: Mission Subfolder Inspection
Inspection within a representative mission directory (`mission-07-networking`) confirming the presence of the mission markdown documentation file (`README.md`).

![Finder Mission Subfolder Inspection](../evidence/Screenshot%202026-11-07%20at%2011.17.39%E2%80%AFAM.png)
