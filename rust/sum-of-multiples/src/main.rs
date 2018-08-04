pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    (1..limit).filter(|i| factors.iter().any(|f| i % f == 0)).sum()
}

fn main() {
    println!("{}", sum_of_multiples(20, &[3, 5]))
}