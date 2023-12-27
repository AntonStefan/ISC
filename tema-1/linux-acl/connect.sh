#!/bin/bash
# OpenSSH-based web tunnelling script.

SSHKEY="${1:-id_rsa}"
LOCAL_PORT=8888
# username@desiredip
DEST=janitor@141.85.228.32
SOCKET=/tmp/janitorsshsocket

function cleanup() {
	[[ ! -f "$SOCKET" ]] || \ 
		ssh -S "$SOCKET" -O exit "$DEST" >/dev/null 2>&1 || true
}
trap cleanup EXIT

set -e

ssh -M -S "$SOCKET" -i "$SSHKEY"  "$DEST"
ssh -S "$SOCKET" -O check "$DEST"

ALLOCATED_PORT=$(ssh -S "$SOCKET" "$DEST" get-forward-port)
if [[ -z "$ALLOCATED_PORT" ]]; then
	exit 1
fi
echo "Allocated server port: $ALLOCATED_PORT"
ssh -S "$SOCKET" -O forward -o "ExitOnForwardFailure=yes" -L "$LOCAL_PORT:localhost:$ALLOCATED_PORT" "$DEST"

ssh -S "$SOCKET" "$DEST" start