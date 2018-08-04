pub fn square_of_sum(n: usize) -> usize {
    let sum: usize = (1..n + 1).sum();

    sum.pow(2)
}

pub fn sum_of_squares(n: usize) -> usize {
    (1..n + 1).map(|n| n.pow(2)).sum()
}

pub fn difference(n: usize) -> usize {
    square_of_sum(n) - sum_of_squares(n)
}