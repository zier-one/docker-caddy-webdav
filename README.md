# Caddy WebDAV container
A WebDAV Server container with automatic HTTPS based on Caddy 2.

## Usage

### Basic 

Start a basic WebDAV Server listen 80 port:

```
docker run -d -p 80:80 -v webdav:/webdav leoppro/docker-caddy-webdav:latest
```

In this examples, a named volume `webdav` is mounted to `/webdav`, the files updated by WebDAV will store here.

### Specify the URL Path

Start a WebDAV, you can access `http://localhost/webdav_path` to connect the WebDAV Server:

```
docker run -d -p 80:80 -v webdav:/webdav \
    -e WD_PREFIX=/webdav_path \
    leoppro/caddy-webdav:latest
```

### Automatic TLS

Start a WebDAV Server with automatic HTTPS:

```
docker run -d -p 80:80 -p 443:443 -p 443:443/udp \
    -v webdav:/webdav \
    -v caddy_data:/data \
    -v caddy_config:/config \
    -e WD_ADDRESS=https://your_domain.com \
    leoppro/caddy-webdav:latest
```

Specify your domain name in `WD_ADDRESS`. The ports 80, 443 and 443(udp) are required for the ACME HTTP challenge, so open it. In addition to `webdav`, two more mount-points for volumes need to be provided: `/data` and `/config`. They are used to store certificates and configuration respectively. See more: https://hub.docker.com/_/caddy

### Authentication

Start a WebDAV with authentication. Specify your username and password in `WD_USERNAME` and `WD_PASSWORD`.:

```
docker run -d -p 80:80 -v webdav:/webdav \
    -e WD_USERNAME=foo \
    -e WD_PASSWORD=bar \
    leoppro/caddy-webdav:latest
```
