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
  * SSL can optionally be configured:
    * `ssl_enabled`: set to `true` to enable SSL. These variables must also be specified if SSL is enabled:
      * `ssl_certificate`: path to SSL certificate
      * `ssl_certificate_key`: path to SSL certificate key


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
        - name: example-ssl-app
          domains:
            - example-ssl.net
          backends:
            - localhost:8083
            - localhost:8084
          ssl_enabled: true
          ssl_certificate: /etc/nginx/ssl/example-ssl.net.crt
          ssl_certificate_key: /etc/nginx/ssl/example-ssl.net.key

```    
