#!/usr/bin/env bash
set -euo pipefail
repo=${1:-/opt/terrones/portfolio}
cd "$repo"
docker network inspect terrones-edge >/dev/null 2>&1 || docker network create terrones-edge >/dev/null
docker compose --env-file .release.env config --quiet
docker compose --env-file .release.env up -d --no-build
container=$(docker compose --env-file .release.env ps -q portfolio)
for _ in $(seq 1 30); do
  [[ "$(docker inspect --format '{{.State.Health.Status}}' "$container")" == healthy ]] && exit 0
  sleep 2
done
docker compose --env-file .release.env logs --tail=100 portfolio >&2
exit 1
