use poseidon::poseidon::bn254::hash_1;

fn main(x: Field, y: pub Field) {
    let hash = hash_1([x]);
    assert(hash == y);
}

#[test]
fn test_correct_hash() {
    let secret = 1;
    let expected_hash = 0x29176100eaa962bdc1fe6c654d6a3c130e96a4d1168b33848b897dc502820133; // hardcoded hash for poseidon
    println(f"secret: {secret}, hash: {expected_hash}");
    main(secret, expected_hash);
}

#[test(should_fail)]
fn test_incorrect_hash() {
    let secret = 1;
    let expected_hash = 123;
    println(f"secret: {secret}, hash: {expected_hash}");
    main(secret, expected_hash);
}
