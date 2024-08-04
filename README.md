# Neuro CRM

## Установка сертификатов для работы с https на VPS

```bash
docker compose -f docker-compose.nginx.yml up -d
```
Проверить dry-run
```bash
docker compose -f docker-compose.nginx.yml exec certbot /bin/sh -c 'certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d "$DOMAIN"'
```
Получить сертификат
```bash
docker compose -f docker-compose.nginx.yml exec certbot /bin/sh -c 'certbot certonly --webroot --webroot-path /var/www/certbot/ -d "$DOMAIN"'
```
