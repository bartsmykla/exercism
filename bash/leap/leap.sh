#!/usr/bin/env bash

readonly SCRIPT_NAME=$(basename "${0}")

main() {
    if (( $# != 1 )) || [[ ! "${1}" =~ ^[0-9]+$ ]]; then
        echo "Usage: ${SCRIPT_NAME} <year>" >&2
        return 1
    fi

    local year; year="${1}"

    if (( "${year}" % 4 != 0 )) || ( (( "${year}" % 100 == 0 )) && \
        (( "${year}" % 400 != 0 )) );
    then
        echo "false"
        return 0
    fi

    echo "true"
}

main "$@"
