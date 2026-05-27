# zk-from-zero

Public log of my 12-week Noir + Rust ZK ultra-learning sprint.

Practice-first: ship circuits, hosts, and tooling before reading papers. Rust is woven through every phase as the glue between Noir, Barretenberg, and the world. Theory only deep enough to make the practice click.

## The plan at a glance

- **Phase 1 — Just Ship Noir (Weeks 1-2):** five working circuits + a Rust CLI wrapper around `nargo`.
- **Phase 2 — Real Apps, On-Chain (Weeks 3-4):** axum host, Barretenberg bindings, private voting app, a taste of Aztec.nr.
- **Phase 3 — Open the Black Box (Weeks 5-6):** read and patch the Noir compiler, dig into ACVM, optimize constraint counts.
- **Phase 4 — The Math, On Demand (Weeks 7-8):** implement field arithmetic, Schnorr, Pedersen, KZG in Rust — first by hand, then with arkworks.
- **Phase 5 — Deep PLONK (Weeks 9-10):** port plonkathon to Rust, read the PLONK / UltraHonk papers, trace a proof from Noir source to Solidity verifier.
- **Phase 6 — Ship Something Real (Weeks 11-12):** capstone — zk-email, private reputation oracle, Noir/Aztec contribution, or a Rust SDK for my circuits.

See [`ULTRALEARN_PLAN.md`](./ULTRALEARN_PLAN.md) for the detailed plan.

## Stack

- **Noir / Nargo** — circuit language and toolchain
- **Barretenberg** — proving backend (Rust bindings, `bb.js` as fallback)
- **Rust** — `axum` for hosts, `arkworks` for crypto primitives
- **Aztec.nr** — fully private smart contracts
- **Solidity** — on-chain verifiers (Sepolia)

## The rules

1. **One shipped artifact per week minimum.** Pushed commit beats a read paper. Each phase lives in its own folder (`phase-1/`, `phase-2/`, …) — the repo tree is the progress log.
2. **Resist top-down urges.** When confused in Noir, finish the messy version first, *then* go down a layer.
3. **Use Rust to debug Noir, and Noir to clarify Rust.** When stuck in Noir, drop into Rust to inspect, instrument, or rewrite. When stuck in Rust, write a tiny circuit to clarify what constraint you're trying to express. The two debug each other.
4. **Public artifacts.** GitHub repos, short writeups. The Noir/Aztec community is small and active — visible work compounds fast.
5. **Have fun.** Curiosity is the engine — if a phase stops being interesting, follow the thread that is, even if it breaks the plan.
