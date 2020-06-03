#!/usr/bin/env bash

readonly SCRIPT_NAME=$(basename "${0}")

main() {
    if [[ $# != 1 ]]; then
        echo "Usage: ${SCRIPT_NAME} <string>" >&2
        return 1
    fi

    if ! command -v rev >/dev/null 2>&1; then
        echo "${SCRIPT_NAME}: couldn't find 'rev'. Aborting" >&2
        return 1
    fi

    rev <<< "${1}"
}

main "$@"
