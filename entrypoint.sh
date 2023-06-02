#!/bin/sh -eux
if [ ! -f /etc/caddy/Caddyfile ]; then
    gomplate -f /etc/caddy/Caddyfile.tmpl -o /etc/caddy/Caddyfile
    caddy fmt --overwrite /etc/caddy/Caddyfile
fi
exec "$@"