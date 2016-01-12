Nginx Reverse Proxy
===================

Deloys simple feature-restricted Nginx reverse proxy configurations (using weighted round-robin by default).

Requirements
------------

nginx-common

Role Variables
--------------

* `nginx_reverse_endpoints`:  list of endpoints

Each endpoint should be configured with the following variables:

  * `name`: endpoint identifier string
  * `domains`: list of domains to be served
  * `lb_method`: optional load balancing method (hash, ip_hash, or least_conn - see [upstream module documentation](http://nginx.org/en/docs/http/ngx_http_upstream_module.html))
  * `backends`: list of backend servers (see accepted [format](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#server))

Example Playbook
----------------

```
---
- hosts: localhost
  become: yes
  roles:
    - role: nginx-reverse
      nginx_reverse_endpoints:
        - name: example-app
          domains:
            - example.net
          backends:
            - localhost:8080 weight=2
            - localhost:8081
          lb_method: least_conn
```    
