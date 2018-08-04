extern crate unicode_segmentation;

use unicode_segmentation::UnicodeSegmentation;

pub fn reverse(input: &str) -> String {
    let mut result = String::new();

    for c in UnicodeSegmentation::graphemes(input, true) {
        result.insert_str(0, c);
    }

    result
}
