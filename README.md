# Neuro CRM

Установка сертификатов для работы с https на VPS

```bash
docker compose -f docker-compose.mginx.yml up -d
docker compose -f docker-compose.mginx.yml exec certbot certonly --webroot --webroot-path /var/www/certbot/ --dry-run -d $DOMAIN
```

