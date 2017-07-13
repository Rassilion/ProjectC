# Docker Support
Start server
```
 docker-compose up
```
Reset and populate db
```
 docker-compose run --rm web python -m app.script
```
Import Problems from md
```
docker-compose run --rm web python -m problems.import_db
```

# Website
Classic Bootstrap look needs to change.

# CodeJudge
Prototype working but its need security tests. Probably chroot setup will enough. And there is only solutions for "Müzekere eşyaları" Problem

