
# Capstone Project – Kids' Math Quest

This folder contains all documentation for the **Kids' Math Quest** capstone project.  The goal is to design and build a web‑based math learning game for K–3 students, featuring adaptive practice, mastery tracking, and engaging quest‑style progression.

## Project overview

* **Target audience**: Children in kindergarten through third grade who are learning single‑digit addition, subtraction, and number comparison.
* **Core features**:
  * Short practice sessions with immediate feedback and stars/encouragement.
  * "Worlds" organised by skill area (e.g., Addition World, Subtraction World) with increasing difficulty.
  * Session summaries such as "You answered 8/10 correctly in Add," along with a probability of mastery for each skill.
  * Adaptive question selection through a back‑end API at `/api/questions/next?skill=...` that uses logged attempt history to adjust difficulty.
  * User accounts with persistent state so children can track progress across sessions.

## Documentation

Use this subfolder to organise planning documents for the capstone:

* `requirements.md` – functional and non‑functional requirements.
* `architecture.md` – high‑level architecture diagram and description of the React front‑end and Node/Express back‑end.
* `api-design.md` – specification for API endpoints and data models.
* `ui-mockups/` – sketches or screenshots of proposed user interfaces.
* `testing.md` – test plan covering unit, integration, and user acceptance tests.
* `project-plan.md` – timeline of milestones, backlog items, and iteration goals.

Feel free to add additional files (e.g., research notes, meeting summaries, user feedback) as the project develops.
