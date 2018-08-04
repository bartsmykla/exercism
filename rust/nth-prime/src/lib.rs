use std::u32;

pub fn nth(n: u32) -> Option<u32> {
    nth_prime(n)
}

struct Primes {
    primes: Vec<u32>,
    current: u32,
}

impl Primes {
    pub fn new() -> Primes {
        Primes {
            primes: vec![],
            current: 2,
        }
    }
}

impl Iterator for Primes {
    type Item = u32;

    fn next(&mut self) -> Option<u32> {
        for n in self.current..u32::MAX {
            if self.primes.iter().all(|k| { n % k != 0 }) {
                self.primes.push(n);
                self.current = n + 1;

                return Some(n);
            }
        }

        None
    }
}

fn nth_prime(n: u32) -> Option<u32> {
    if n == 0 { return None }

    let primes = Primes::new();

    let mut i = 1_u32;

    for p in primes {
        if i == n {
            return Some(p);
        }

        i += 1;
    }

    None
}