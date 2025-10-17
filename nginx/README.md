Nginx proxy configuration examples

Files created:
- proxy.conf        : Example nginx configuration (subdomain and path-based examples)
- docker-compose.yml: Quick docker-compose to run nginx with the config

How to use

1) Edit the config
   - Replace web1.internal, web2.internal, web3.internal with your internal hostnames or IPs
   - If you want subdomain routing, configure DNS records like site1.proxy.example.com -> proxy IP
   - If you prefer path-based routing, use proxy.example.com and access sites at /site1/, /site2/, /site3/

2) Run locally with Docker Compose (quick test)
   - Ensure your backend containers are reachable by the nginx container (same docker network or use host networking)
   - Start nginx:
       docker-compose up -d
   - View logs:
       docker-compose logs -f nginx

3) Deploy to a real server
   - Copy the `proxy.conf` content to your nginx config directory, e.g. `/etc/nginx/conf.d/proxy.conf` or `/etc/nginx/sites-available/proxy.conf` and enable.
   - Test nginx config:
       sudo nginx -t
   - Reload nginx:
       sudo systemctl reload nginx

Tips and gotchas
- Prefer subdomain-based routing when possible to avoid brittle HTML rewriting.
- Use `proxy_redirect` to rewrite Location headers from backends.
- Use `proxy_cookie_domain` to rewrite cookie domains sent by backends.
- If backends return gzipped responses, disable Accept-Encoding for the proxied location when using `sub_filter`.
- For secure public deployments: enable TLS on the proxy, put backends on a private network, and enable firewall rules.

If you want, I can:
- Add a working docker-compose demo with 3 simple backend containers prewired to nginx for local testing.
- Generate an nginx config that uses variables and a single server block for all subdomains (advanced), or a systemd unit and letsencrypt setup script.

Tell me if you want the demo compose (with simple static backends) or the production-ready TLS-enabled example.
