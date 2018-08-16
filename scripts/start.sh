echo ">>> setting up environment"
export PROJECT=timesheet

echo ">>> stopping all existing running services"
docker-compose stop -t 0
docker-compose down -v

echo ">>> building required images"
docker-compose build

echo ">>> running the stack"
docker-compose up -d db web nginx

echo ">>> bootstrapping the system"
docker-compose exec -T web ./scripts/wait-for-it.sh db
docker-compose exec -T web python /opt/root/manage.py migrate
docker-compose exec -T web python /opt/root/data/input/config_ritcco_empty.py
docker-compose exec -T web python /opt/root/manage.py collectstatic --no-input

echo ">>> DONE!"
exit 0
