pub fn factors(n: u64) -> Vec<u64> {
    unimplemented!("This should calculate the prime factors of {}", n)
}

struct Primes {
    current: u64,
    primes: Vec<u64>,
}

impl Iterator for Primes {
    type Item = u64;

    fn next(&mut self) -> Option<u64> {

    }
}