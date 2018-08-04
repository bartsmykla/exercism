pub fn build_proverb(list: Vec<&str>) -> String {
    if list.len() < 1 {
        return String::new();
    }

    let mut result = String::new();
    let mut current = list[0];

    for i in list.iter().skip(1) {
        result.push_str(format!("For want of a {} the {} was lost.\n", current, i).as_str());

        current = *i;
    }

    result.push_str(format!("And all for the want of a {}.", list[0]).as_str());

    result
}
