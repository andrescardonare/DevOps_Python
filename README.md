# DevOps_Python

Created as a coding challenge for the EPAM Bootcamp — DevOps External course (LatAm, August 2025). It contains simple demo services and a reverse-proxy setup to practice container networking, proxying, and deployment workflows.

## Nginx reverse-proxy demo

This repository runs three local Python Flask containers behind a single nginx reverse proxy. The proxy is configured to expose only nginx to the host through a bridged network; the backend services run on an internal Docker network.

Files of interest (in `nginx/`):

- `proxy.conf` - nginx configuration with two routing approaches: SUBDOMAIN and PATH. The PATH approach is the default for local testing (`/site1/`, `/site2/`, `/site3/`).
- `Dockerfile.nginx` - builds the nginx image and bakes the proxy config and landing page into the image.
- `Dockerfile.app` - generic image used for the three backend Flask apps.
- `docker-compose.yml` - Compose file that starts `nginx` and three backend services (`web1`, `web2`, `web3`).

### Quick start (local)

From the repository root run:

```bash
# Build and start the demo (nginx publishes host ports 80 and 443)
docker compose -f nginx/docker-compose.yml up --build -d

# See logs
docker compose -f nginx/docker-compose.yml logs --tail=200
```

Open these URLs in a browser or use `curl`:

```bash
# Landing page with quick links
curl -i http://localhost/

# Site paths proxied by nginx
curl -i http://localhost/site1/
curl -i http://localhost/site2/
curl -i http://localhost/site3/
```

### Network isolation

- The Compose file creates two networks: `frontend` and `backend`.
	- `frontend`: nginx is attached here and publishes ports to the host (this is how users access the proxy).
	- `backend`: an internal network (Compose marks it `internal: true`) where the backend services live. Only containers attached to `backend` can reach the backends by their service names.

This means the backend Flask servers are NOT directly reachable from the host (they use `expose` in compose instead of `ports:`). This is intentional — the host should only be able to reach nginx.

### Troubleshooting

- If the landing page returns 404, rebuild the nginx image to ensure `index.html` was copied in:

```bash
docker compose -f nginx/docker-compose.yml up --build -d
```

- If a `/siteX/` request returns a 502/504, check logs:

```bash
docker compose -f nginx/docker-compose.yml logs --tail=200
docker logs dev-web1 --tail 200
docker logs dev-web2 --tail 200
docker logs dev-web3 --tail 200
```

- To verify nginx can reach backends from inside the container:

```bash
docker exec -it dev-proxy-nginx sh -c "curl -sS http://web1:8080/ | head -n 5"
```

- If you need temporary direct host access to a backend for debugging, add a `ports:` mapping to the backend service in `nginx/docker-compose.yml` (not recommended for long-term use), or run a temporary debugging container attached to the `backend` network.

### Notes & next steps

- The demo uses the Flask development server in backends (convenient for local testing). For production-like behavior, replace those commands with `gunicorn` and disable Flask debug mode.
- `proxy.conf` contains examples for both subdomain and path routing. The subdomain approach is preferable for complex apps; it requires DNS or `/etc/hosts` entries for local testing.

If you want, I can also:

- Move dependency installation into `nginx/Dockerfile.app` so images are reproducible and start faster.
- Replace Flask dev servers with `gunicorn` and update compose commands for a production-like setup.
- Clean the duplicate `sub_filter_types` warnings in `proxy.conf`.
