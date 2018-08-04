extern crate regex;

use regex::Regex;

pub fn reply(message: &str) -> &str {
    let msg = message.trim().to_string();
    let mut chars = msg.chars();
    let re = Regex::new(r"^.*?[A-Z]+.*?$").unwrap();
    let uppercase = if msg.to_uppercase() == msg && re.is_match(message) { true } else { false };

    match (&chars.next_back(), &chars.next_back()) {
        (Some(a), Some(b)) if *a == '!' && *b == '?' => "Calm down, I know what I'm doing!",
        (Some(a), Some(_)) if *a == '?' && uppercase => "Calm down, I know what I'm doing!",
        (Some(a), Some(_)) if *a == '!' && uppercase => "Whoa, chill out!",
        (Some(a), Some(_)) if *a == '?' => "Sure.",
        (Some(_), Some(_)) if uppercase => "Whoa, chill out!",
        (None, None) => "Fine. Be that way!",
        (_, _) => "Whatever.",
    }
}
