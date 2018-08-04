fn main() {
    println!("{}", square_of_sum(10));
    println!("{}", sum_of_squares(10));
    println!("{}", difference(10));
}

fn square_of_sum(n: usize) -> usize {
    let sum: usize = (1..n + 1).sum();

    sum.pow(2)
}

fn sum_of_squares(n: usize) -> usize {
    (1..n + 1).map(|n| { n.pow(2) }).sum()
}

fn difference(n: usize) -> usize {
    square_of_sum(n) - sum_of_squares(n)
}
