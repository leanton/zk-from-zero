type Hash = Field;
type Value = Field;

use poseidon::poseidon::bn254::{hash_1, hash_2};

fn main(leaf: Value, path: [Hash; 3], indices: [bool; 3], root: pub Hash) {
    let mut current: Field = hash_1([leaf]); // step 0: hash raw value
    for i in 0..3 {
        if indices[i] == false {
            current = hash_2([current, path[i]]);
        } else {
            current = hash_2([path[i], current]);
        }
    }
    assert(current == root);
}

#[test]
fn test_valid_proof() {
    // 8 leaves
    let h0 = hash_1([1]);
    let h1 = hash_1([2]);
    let h2 = hash_1([3]);
    let h3 = hash_1([4]);
    let h4 = hash_1([5]);
    let h5 = hash_1([6]);
    let h6 = hash_1([7]);
    let h7 = hash_1([8]);

    // level 1
    let h01 = hash_2([h0, h1]);
    let h23 = hash_2([h2, h3]);
    let h45 = hash_2([h4, h5]);
    let h67 = hash_2([h6, h7]);

    // level 2
    let h0123 = hash_2([h01, h23]);
    let h4567 = hash_2([h45, h67]);

    // root
    let root = hash_2([h0123, h4567]);

    // prove leaf 1
    let leaf = 1;
    let path = [h1, h23, h4567];
    let indices = [false, false, false];
    main(leaf, path, indices, root);

    // prove leaf 2
    let leaf = 2;
    let path = [h0, h23, h4567];
    let indices = [true, false, false];
    main(leaf, path, indices, root);
}
