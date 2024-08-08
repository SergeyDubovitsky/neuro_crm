## Установка сертификатов для домена
Отредактировать файл `.env.letsencrypt` и указать домен в переменной `DOMAIN`

```yaml
```bash
docker compose up -d
```
Проверить dry-run
```bash
docker compose run --rm certbot 'certbot certonly --verbose --webroot --webroot-path /var/www/certbot/ --dry-run -d "$DOMAIN"'
```
Получить сертификат
```bash
docker compose run --rm certbot 'certbot certonly --verbose --webroot --webroot-path /var/www/certbot/ -d "$DOMAIN"'
```

Остановить сервисы
```bash
docker compose down
```
