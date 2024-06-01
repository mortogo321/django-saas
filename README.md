# Django SAAS
Django - Vuejs

## UP
``` bash
docker compose -f docker/docker-compose.yaml up -d --build
```

## Exec command
``` bash
# migrations
docker exec -it api sh -c "python manage.py migrate"
```
## Down
``` bash
docker compose -f docker/docker-compose.yaml down --rmi all --remove-orphans
```

Web: http://localhost  
Api: http://localhost/api  
