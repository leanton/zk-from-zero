# Phase 1 — Just Ship Noir

**Weeks 1-2.** Learn Noir's syntax and the prove/verify loop by shipping five small circuits, plus a thin Rust CLI that wraps `nargo`.

## Goal

Ship 5 working Noir circuits + a Rust CLI wrapper around `nargo`, all visible in this folder.

## Deliverables

- [ ] `hello/` — prove `x != y`
- [ ] `preimage/` — prove knowledge of a Poseidon preimage of a public hash
- [ ] `age-over-18/` — private DOB satisfies a public constraint
- [ ] `merkle/` — prove an element is in a tree without revealing which
- [ ] `signature/` — ECDSA or EdDSA verification inside a circuit
- [ ] `cli/` — Rust CLI: takes inputs, writes `Prover.toml`, runs the proof, parses output

## How to run

Populated as each subproject lands. Typical loop:

```
cd <circuit>
nargo check
nargo prove
nargo verify
```

## Notes

Running log of what shipped, what broke, and what's next lives in [`PROGRESS.md`](./PROGRESS.md).
