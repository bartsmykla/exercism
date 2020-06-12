#!/usr/bin/env bash

readonly SCRIPT_NAME=$(basename "${0}")

declare -a ORDER=( 3 5 7 )
declare -A DROPS=( [3]=Pling [5]=Plang [7]=Plong )

main() {
    if (( $# != 1 )) || [[ ! "${1}" =~ ^-?[0-9]+$ ]]; then
        echo "Usage: ${SCRIPT_NAME} <number>" >&2
        return 1
    fi

    local number; number="${1}"
    local result; result=""

    for key in "${ORDER[@]}"; do
        if (( "${number}" % "${key}" == 0 )); then
            result+="${DROPS[${key}]}"
        fi
    done

    echo "${result:-${number}}"
}

main "$@"
