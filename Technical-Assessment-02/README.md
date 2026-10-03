# VacuumReflex: Discrete Rule-Based Agent Simulation

**Author:** Justin D. Vergara  
**Course & Section:** CS0065 (Intelligent Systems) / AN41  
**Professor:** Ms. Crisola G. Tan  
**Date:** October 3, 2026  

---

## 1. Project Overview

This repository contains the laboratory implementation and experimental documentation for **Technical Assessment 2: Rule-Based Agent**.

The simulation models the operational and perceptual dynamics of a simple reflex vacuum cleaner agent operating in discrete spatial environments. It explores condition-action rule evaluation, deterministic binary toggling between two chambers, and stochastic dirty-room targeting across a three-room topology evaluated through dynamic state transitions and text-based grid visualizers.

---

## 2. Repository Contents

* `TA2_Vergara.py` — Complete executable Python script containing the environment definitions, reflex agent classes, interactive simulation loops, and menu-driven CLI interface.
* `TA2_Vergara.pdf` — Formal technical assessment report compiling the laboratory instructions, complete source code, execution outputs, and analytical question evaluations.
* `TA2 - Evidence_Vergara.pdf` — Experimental evidence document displaying code slice screenshots alongside live terminal execution traces for both the two-room benchmark and three-room grid runs.

---

## 3. Simulation Architecture & Logic

### Environment Abstraction & State Representation
Rooms are structured via dictionary key-value mappings storing discrete cleanliness states (`"Clean"` or `"Dirty"`). Sensory evaluation hooks (`is_dirty`) inspect chamber contamination, while actuator methods (`clean_room`) mutate the target key to a sanitized state upon command.

### Condition-Action Reflex Rules (Tasks 1–3)
The agent operates under a simple reflex model with zero internal history, evaluating its immediate percept at every step:
* **Rule 1 (Sanitize):** If the currently occupied room status is `Dirty`, trigger the cleaning actuator to update the room state to `Clean`.
* **Rule 2 (Relocate):** If the currently occupied room status is `Clean`, trigger the movement mechanism to toggle position to the opposite room (`A` $\leftrightarrow$ `B`).

### Multi-Chamber Stochastic Navigation (Bonus Task)
The spatial topology is expanded to three discrete chambers (`A`, `B`, and `C`). When the current room is clean, the agent queries the environment for remaining dirty nodes and randomly selects a target from the dirty pool. If all chambers are registered as clean, the agent falls back to random patrol vectors across adjacent clean nodes.

---

## 4. Visualizations & Telemetry

* **Console Step Telemetry (2-Room Model):** Logs pre-action agent locations, specific condition-action rules fired (`Cleaned Room` vs. `Moved to Room`), and real-time environment state dictionaries after every execution cycle.
* **Interactive Retry Subsystem:** Built-in loop control allowing instant reruns with updated room parameters or step thresholds without restarting the CLI session.
* **Text-Based Spatial Grid (3-Room Model):** Renders evenly spaced ASCII bounding boxes with fixed cell boundaries, mapping live chamber contamination states alongside the dynamic position marker (`[*AGENT*]`) across all coordinates.

---

## 5. Execution Instructions

1. Clone or download the repository files into a local workspace.
2. Open the terminal or command prompt in the directory containing `TA2_Vergara.py`.
3. Run the script:
   ```bash
   python TA2_Vergara.py