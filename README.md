# Neuro CRM

[![cov](https://SergeyDubovitsky.github.io/neuro_crm/badges/coverage.svg)](https://github.com/SergeyDubovitsky/neuro_crm/actions)

## Установка сертификатов для работы с https на VPS

```bash
docker compose -f docker-compose.nginx.yml up -d
```
Проверить dry-run
```bash
docker compose -f docker-compose.nginx.yml exec certbot /bin/sh -c 'certbot certonly --verbose --webroot --webroot-path /var/www/certbot/ --dry-run -d "$DOMAIN"'
```
Получить сертификат
```bash
docker compose -f docker-compose.nginx.yml exec certbot /bin/sh -c 'certbot certonly --webroot --webroot-path /var/www/certbot/ -d "$DOMAIN"'
```
