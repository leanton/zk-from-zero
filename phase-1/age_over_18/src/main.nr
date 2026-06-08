fn main(dob: u32, current_date: pub u32) {
    validate_date_format(dob);
    validate_date_format(current_date);
    let threashold_date = current_date - 180000;
    assert(dob <= threashold_date);
}

fn validate_date_format(date: u32) {
    let day = date % 100;
    let month = (date / 100) % 100;
    let year = date / 10_000;

    assert(day >= 1 & day <= 31);
    assert(month >= 1 & month <= 12);
    assert(year >= 1900);
}

#[test]
fn test_dob_passes() {
    main(20000101, 20260101);
}

#[test(should_fail)]
fn test_fails_if_young() {
    main(20210101, 20260101);
}

#[test(should_fail)]
fn test_fails_if_invalid_date() {
    main(20000132, 20260101);
}
