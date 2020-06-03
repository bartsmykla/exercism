#!/usr/bin/env bash

readonly SCRIPT_NAME=$(basename "${0}")

main() {
    if [[ $# != 1 ]]; then
        echo "Usage: ${SCRIPT_NAME} <person>" >&2
        return 1
    fi

    echo "Hello, ${1}"
}

main "$@"
