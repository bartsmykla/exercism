#!/usr/bin/env bash

declare -A COLORS_MAP=(
    [black]=0
    [brown]=1
    [red]=2
    [orange]=3
    [yellow]=4
    [green]=5
    [blue]=6
    [violet]=7
    [grey]=8
    [white]=9
)

main() {
    local color_1="${1:?too few parameters}"
    local color_2="${2:?too few parameters}"
    local value_1="${COLORS_MAP[${color_1}]:?invalid color}"
    local value_2="${COLORS_MAP[${color_2}]:?invalid color}"

    echo "${value_1}${value_2}"
}

main "$@"
