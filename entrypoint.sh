#!/bin/sh -eux
gomplate -f /etc/caddy/Caddyfile.tmpl -o /etc/caddy/Caddyfile
caddy fmt --overwrite /etc/caddy/Caddyfile
exec "$@"