# Phase 1 — Just Ship Noir

**Weeks 1-2.** Learn Noir's syntax and the prove/verify loop by shipping five small circuits, plus a thin Rust CLI that wraps `nargo`.

## Goal

Ship 5 working Noir circuits + a Rust CLI wrapper around `nargo`, all visible in this folder.

## Deliverables

- [x] `hello/` — prove `x != y`
- [x] `preimage/` — prove knowledge of a Poseidon preimage of a public hash
- [x] `age_over_18/` — private DOB satisfies a public constraint
- [x] `merkle/` — prove an element is in a tree without revealing which
- [ ] `signature/` — ECDSA or EdDSA verification inside a circuit
- [ ] `cli/` — Rust CLI: takes inputs, writes `Prover.toml`, runs the proof, parses output

## How to run

Populated as each subproject lands. Typical loop (Nargo 1.0 beta; `nargo prove`/`verify` are gone — proving moved to Barretenberg's `bb` CLI):

```
cd <circuit>
nargo check                          # generate Prover.toml / Verifier.toml templates
nargo execute                        # compile + run; writes target/<name>.json (ACIR) and target/<name>.gz (witness)
bb prove -b ./target/hello.json -w ./target/hello.gz --write_vk -o target
bb verify -p ./target/proof -k ./target/vk
```

## Notes

Running log of what shipped, what broke, and what's next lives in [`PROGRESS.md`](./PROGRESS.md).

## References

- [Noir docs](https://noir-lang.org/docs) — language reference and prove/verify walkthroughs
- [Nargo install](https://noir-lang.org/docs/getting_started/quick_start) — `noirup` and toolchain setup
- [Awesome Noir](https://github.com/noir-lang/awesome-noir) — curated circuits, libraries, and tutorials
- [`noir-examples`](https://github.com/noir-lang/noir-examples) — reference circuits, including Merkle and signature patterns
- [Noir stdlib](https://noir-lang.org/docs/noir/standard_library) — Poseidon, ECDSA, EdDSA, Merkle helpers
- [`nargo` CLI reference](https://noir-lang.org/docs/reference/nargo_commands) — commands the Rust wrapper will shell out to
- Top-level [`README.md`](../README.md) and [`ULTRALEARN_PLAN.md`](../ULTRALEARN_PLAN.md) — the broader 12-week plan this phase sits in
