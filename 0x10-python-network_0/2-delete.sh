#!/bin/bash
# This script send a delete command to the file passed as an argument
curl -s -X DELETE "$1"
