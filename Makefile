asn=6
subdir=brevets

.PHONY : liverefresh
liverefresh: clean live

kill:
	docker compose down

live: clean
	docker compose -f docker-compose-live.yml up -d

livebuild: clean
	docker compose -f docker-compose-live.yml build

run: clean
	docker compose up -d
	
runbuild: clean
	docker compose build

blogs:
	docker compose logs brevets --follow

alogs:
	docker compose logs api --follow

breventer:
	docker compose exec -it brevets /bin/bash

apienter:
	docker compose exec -it api /bin/bash

purge: kill
	docker container kill `docker container ls -q -a` || true;
	docker container prune `docker container ls -q -a` || true;
	docker volume prune -a -f || true;
	docker image prune -a -f || true

clean: kill prune_containers rm_images prune_volumes
	@(echo "remove __pycache__"; rm -rf **/*/__pycache__ || true)
	
prune_volumes:
	@(echo "prune volumes"; docker volume prune -a -f || true)

prune_containers:
	docker container prune -f || true

rm_images:
	@(echo "remove top level images";\
	docker image rm --no-prune `docker images -q project${asn}-brevets` `docker images -q project${asn}-api` || true)

prune_images:
	@(echo "prune all images"; docker image prune -f -a || true)

