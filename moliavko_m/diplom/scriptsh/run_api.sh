#!/bin/bash


SCRIPT_DIR=$(dirname "$0")

TEST_DIR="$SCRIPT_DIR/../tests_api"

REPORT_DIR="$SCRIPT_DIR/../reports_api"

mkdir -p "$REPORT_DIR"

pytest -s -v "$TEST_DIR" --alluredir="$REPORT_DIR"