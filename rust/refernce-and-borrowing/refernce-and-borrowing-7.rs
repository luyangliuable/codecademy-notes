// Remove something to make it work
// Don't remove a whole line !

fn main() {
    after();
}

fn before() {
    todo!();
    let mut s = String::from("hello");

    let r1 = &mut s;
    let r2 = &mut s;

    println!("{}, {}", r1, r2);

    println!("Success!");
}

fn after() {
    let mut s = String::from("hello");

    let r1 = &mut s;
    // let r2 = &mut s;

    println!("{}, {}", r1, r1);

    println!("Success!");
}
