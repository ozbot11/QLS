# QLS

## Research Question

Can a hybrid quantum‑classical linear‑system solver—combining classical ridge pre‑conditioning with a NISQ‑compatible HHL‑style circuit—achieve lower wall‑clock time and ≤ 10⁻³ relative error than state‑of‑the‑art GPU‑accelerated solvers (cuSOLVER) when inverting 256 × 256 to 512 × 512 equity‑return covariance matrices used in multi‑factor risk models?

## Literature Gap

Despite steady progress, today’s quantum‑finance and quantum‑linear‑algebra studies remain confined to proof‑of‑concept settings: they top out at a few‑qubit toy portfolios, simulator‑only variational sweeps, or logical‑level encodings of 10²–10³‑dimensional matrices—and rarely report end‑to‑end wall‑clock cost, energy use, or robustness under drifting hardware noise. Missing, therefore, is a benchmark that (i) tackles **real‑market portfolios of ≥ 32 assets** and **256 × 256 sparse systems** drawn from production CFD grids, (ii) runs **cross‑platform** on both superconducting and trapped‑ion devices **and** GPU‑accelerated simulators to expose architecture dependence, and (iii) measures **application‑level fidelity against wall‑clock time, carbon footprint, and noise‑recalibration overhead**. Our study fills this gap by delivering the first noise‑aware, hardware‑executed quantum workflow coupling large‑scale block‑encoded solvers and variational optimizers to live finance data—while systematically mapping accuracy‑cost tradeoffs and optimizer‑hyperparameter landscapes, information previous work has simulated only at miniature scale or omitted altogether.