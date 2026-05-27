# Reverse Ultra-Learning Plan: Noir + Rust ZK

Practice-first, with Rust woven through every phase. Assumes Rust fluency — we go straight to using it as a tool, not learning it.

12-week sprint, ~15-20 hrs/week. Heavy on building. Theory only deep enough to make the practice click.

---

## Phase 1: Just Ship Noir (Weeks 1-2)

You're learning Noir's syntax and the prove/verify loop. Rust stays minimal here because Noir is the new thing.

**Do, in order:**
- Install Nargo. Hello-world circuit: prove `x != y`.
- Hash preimage: prove you know the Poseidon preimage of a public hash.
- Age-over-18: private DOB satisfies a public constraint.
- Merkle membership: prove an element is in a tree without revealing which.
- Signature verification inside a circuit (ECDSA or EdDSA).

**Light Rust touch:** write a small `cargo` CLI that wraps `nargo` — takes inputs, writes `Prover.toml`, runs the proof, parses output. Trivial but you'll extend it constantly through later phases.

**Output:** 5 working circuits + a Rust wrapper, all in a public repo.

---

## Phase 2: Real Apps, On-Chain (Weeks 3-4)

Rust becomes the glue between circuits and the world.

- Use **Barretenberg's Rust bindings** (or `bb.js` if bindings are unstable for your target) to generate proofs programmatically instead of via `nargo`. This is how production systems do it.
- Build an **axum** backend that accepts user input → generates witness → calls Barretenberg → returns proof. Frontend posts proof to a Solidity verifier on Sepolia.
- Build a **private voting app**: anyone in a Merkle tree votes once, nullifier prevents double-voting. Tree maintenance, nullifier tracking, and proof submission all live in your Rust service. This is the canonical exercise — do it.
- Try **Aztec.nr** — write a private smart contract. Different from "Noir + Solidity verifier" and shows you a fully private execution environment.

**Concrete exercise:** rewrite your Phase 1 Merkle circuit's off-chain tree management in Rust. You now have Noir circuit + Rust host talking to each other. That's the real shape of every ZK app.

**Mandatory friction:** you'll hit a constraint blow-up or a "this is too slow" wall. Good — that's your hook into Phase 3.

---

## Phase 3: Open the Black Box (Weeks 5-6)

Now ask what Noir is actually doing. Rust earns its keep here.

- **Clone `noir-lang/noir`**. Build it locally. Trace `nargo compile` — find the lexer, parser, type checker, ACIR generator. You don't need to understand all of it; see the shape.
- Add a tiny patch: a new error message, a small stdlib function, a lint. PR it or keep it local. Editing the compiler demystifies it.
- Read **`acvm-repo`** (the ACIR VM) — small, self-contained. This is where circuits become constraints.
- Use `nargo info` and `nargo compile --print-acir` on your Phase 1 circuits. Count constraints. Optimize one circuit to half its size.
- Write a Rust tool that loads a compiled ACIR file and counts gates by type. You now have your own Noir tooling.
- Learn what **Plonkish arithmetization** is — Barretenberg uses UltraPlonk/UltraHonk. You don't need to derive it, you need to know why lookups and custom gates make your Noir code efficient.
- Read Vitalik's QAP post now — it lands differently than if you'd read it cold.

---

## Phase 4: The Math, On Demand (Weeks 7-8)

Rust is your math playground. Pull in only the theory previous phases left you curious about.

- Implement from scratch in Rust: finite field over a small prime, Schnorr signatures, Pedersen commitments, Fiat-Shamir via a simple sponge. ~300 lines total.
- Redo each using **arkworks** (`ark-ff`, `ark-ec`, `ark-poly`). Compare your toy code to production code — arkworks' generic-over-curves idioms start making sense.
- Implement **KZG polynomial commitment** in Rust with arkworks. ~200 lines. You now understand what Barretenberg does when it commits to your witness polynomial.
- Skim **Justin Thaler's "Proofs, Arguments, and Zero-Knowledge"** chapters 1-5 selectively, only parts that explain mechanics you've already touched.

This is where Rust + theory fuse. You're not reading about polynomials, you're computing with them.

---

## Phase 5: Deep PLONK (Weeks 9-10)

Build a real prover.

- Do **plonkathon in Rust**. Original is Python; port it or find a Rust fork. Implement a working PLONK prover and verifier. One focused week. This is the single best exercise in ZK — do not skip.
- Read the PLONK paper. Then **UltraHonk** docs (Aztec's current backend). You'll recognize most of it.
- Read **Barretenberg**'s C++ source for one component (e.g., Poseidon gate implementation). You won't write C++, but you'll recognize structure from your Rust PLONK.
- Read the **`bb`** Rust bindings source. You can now trace a proof from Noir source → ACIR → Rust glue → C++ prover → Solidity verifier.
- Optional stretch: write one circuit in **Halo2** (Rust, lower-level than Noir). You'll appreciate Noir more.

---

## Phase 6: Ship Something Real (Weeks 11-12)

Capstone with serious Noir + Rust integration. Pick one:

- **zk-email in Noir** with a Rust host that parses DKIM signatures, generates witnesses, orchestrates proving.
- **Private reputation oracle**: Rust service ingests data → Noir circuit proves aggregate properties → on-chain verifier. End-to-end.
- **Contribute to Noir or Aztec**: pick an issue in `noir-lang/noir`, `aztec-packages`, or a stdlib repo (`noir-bignum`, `noir-edwards`). The team is responsive, the medium is Rust, contributions get noticed.
- **Rust SDK for your own circuits**: type-safe wrappers, witness generation, proof caching. This is what Aztec, Aragon ZK, and others ship.

---

## Rust's Role at Each Phase

| Phase | What Rust does for you |
|-------|---|
| 1 | CLI glue around `nargo` |
| 2 | Production host: web service, witness gen, proof submission |
| 3 | Reading and patching Noir's own compiler |
| 4 | Implementing crypto primitives, using arkworks |
| 5 | Building a full PLONK prover |
| 6 | Open-source contributions, SDK design |

---

## Why Noir + Rust Is the Right Stack

- **Noir** teaches you to think in circuits — declarative, constraint-based.
- **Rust** is the language of the infra: Barretenberg bindings, Noir's compiler, arkworks, every major zkVM.
- Together you can ship a complete ZK product *and* hack on the infrastructure underneath it. Rare combo, and the Aztec/Noir ecosystem specifically rewards it.

---

## Resources

- **noir-lang.org** docs, Aztec's **Awesome Noir** repo, **noir-examples**
- **`noir-lang/noir`** source — your most important repo from Phase 3 on
- **arkworks** docs and `ark-curves` benchmarks
- **plonkathon** (Python) — port to Rust
- **Halo2 book** (zcash.github.io/halo2) — teaches Plonkish thinking even if you don't ship Halo2
- **Berkeley ZKP MOOC** (rdi.berkeley.edu/zk-learning) — selectively, when curiosity strikes

---

## The Rules

1. **One shipped artifact per week minimum.** Pushed commit beats a read paper.
2. **Resist top-down urges.** When confused in Noir, finish the messy version first, *then* go down a layer.
3. **Use Rust to debug Noir, and Noir to clarify Rust.** When stuck in Noir, drop into Rust to inspect, instrument, or rewrite. When stuck in Rust, write a tiny circuit to clarify what constraint you're trying to express. The two debug each other.
4. **Public artifacts.** GitHub repos, short writeups. The Noir/Aztec community is small and active — visible work compounds fast.
