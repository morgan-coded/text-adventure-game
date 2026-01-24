
# Kids' Math Quest & Computer Science Portfolio

This repository unifies all my Southern New Hampshire University computer‑science coursework and the final **Kids' Math Quest** capstone project.  It brings together prior work (such as operating‑system simulators and early system‑analysis documents) and provides dedicated places for upcoming assignments and project artifacts.

## What's in this repository

| Path | Description |
| --- | --- |
| `/client/` | React front‑end for the Kids' Math Quest game.  It will hold components, pages, and assets used to build the K–3 math learning interface. |
| `/server/` | Node/Express back‑end providing API endpoints (e.g., `GET /api/questions/next`) and data persistence for the math game. |
| `/src/` | Source code for earlier operating‑system simulators (file memory manager, memory allocation simulator, real‑time scheduler).  Keeping this code separate preserves prior work without mixing it with the capstone. |
| `/data/` | Sample input files for the OS simulators. |
| `/docs/` | Documentation.  This folder has subdirectories for the capstone (`capstone/`), OS simulators (`os‑simulators/`), the original Backyard Adventures case study (`backyard‑adventures/`), a degree‑audit summary (`degree‑audit/`), and individual course placeholders (`courses/`). |
| `/LICENSE` | License information. |

## How to use this repository

* **Capstone development**: work on the Kids' Math Quest game in `/client` and `/server`.  Architectural decisions, requirements, and test plans live in `docs/capstone/`.
* **Coursework**: each CS course has its own directory under `docs/courses/`.  Use these as drop‑off points for assignments, projects, and notes.
* **Legacy projects**: the OS simulator code and the Backyard Adventures case study remain for reference and portfolio purposes; they are clearly separated from the capstone work.

Feel free to adjust, rename, or extend these directories as you progress through the program.  The goal is to keep every artifact organised and easy to find, both for your own use and for reviewers evaluating your work.
