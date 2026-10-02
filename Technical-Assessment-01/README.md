# GridWalker: Discrete Multi-Agent Spatial Drift Simulation

**Author:** Justin D. Vergara  
**Course & Section:** CS0065 (Intelligent Systems) / AN41  
**Professor:** Ms. Crisola G. Tan  
**Date:** October 2, 2026  

---

## 1. Project Overview
This repository contains the laboratory implementation and experimental documentation for **Technical Assessment 1: Random Walk Simulation Using AgentPy**. 

The simulation models multi-agent stochastic behavior across a bounded discrete grid. It explores the operational transition from an unconstrained isotropic random walk to a directional, bounded multi-agent system evaluated through trajectory path plotting, coordinate clamping, and spatial distribution metrics.

---

## 2. Repository Contents

* **`ta1_vergara.py`** — Python script executing both the baseline random walk and the updated multi-agent model with trajectory persistence and console telemetry.
* **`TA1_Vergara.pdf`** — Formal technical assessment report containing the lab overview, source code, and question evaluations.
* **`TA1 - Evidence_Vergara.pdf`** — Experimental evidence document showing library installation, baseline trial runs, and modified simulation test batches.

---

## 3. Simulation Architecture & Logic

### Coordinate Clamping
The environment operates under a closed, non-toroidal boundary constraint. Agent movements that exceed the grid indices are constrained within range using mathematical min/max clamping, preventing out-of-bounds errors and causing agents to glide along borders upon boundary contact.

### Path History Tracking
Each agent records its coordinate history from step zero onward. This spatial log allows the visualization pipeline to construct historical line trails displaying full transit trajectories from origin markers to terminal positions.

### Directional Movement Bias
Movement departures from uniform random walking are implemented using weighted probability selection:
* **Right `(1, 0)`:** 40% chance
* **Up `(0, 1)`:** 30% chance
* **Left `(-1, 0)`:** 20% chance
* **Down `(0, -1)`:** 10% chance

This bias directs the population systematically toward the upper-right quadrant of the grid during multi-step runs.

---

## 4. Visualizations & Telemetry

* **Trajectory Map:** Visualizes agent routes across the coordinate plane, distinguishing starting locations (squares) and final stopping points (triangles).
* **Final Spatial Distribution:** Scatter plot charting terminal resting points with labeled agent identifiers to inspect crowd formation and wall accumulation.
* **Console Displacement Log:** Prints beginning coordinates, ending coordinates, and calculated net vector displacements (Δx, Δy) for every agent upon simulation completion.