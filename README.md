# Neuro CRM

[![codecov](https://codecov.io/github/SergeyDubovitsky/neuro_crm/graph/badge.svg?token=CY4W2WIBAK)](https://codecov.io/github/SergeyDubovitsky/neuro_crm)

## Установка сертификатов для домена
Отредактировать файл `./docker/docker-compose.letsencrypt.yml` и указать 
домен в переменной `DOMAIN`

```yaml
```bash
docker compose -f ./docker/docker-compose.letsencrypt.yml up -d
```
Проверить dry-run
```bash
docker compose -f ./docker/docker-compose.letsencrypt.yml run --rm certbot 'certbot certonly --verbose --webroot --webroot-path /var/www/certbot/ --dry-run -d "$DOMAIN"'
```
Получить сертификат
```bash
docker compose -f ./docker/docker-compose.letsencrypt.yml run --rm certbot 'certbot certonly --verbose --webroot --webroot-path /var/www/certbot/ -d "$DOMAIN"'
```
