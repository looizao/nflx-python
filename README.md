# nflx-python

## Run container
docker compose up --build

## Get into created container
?
docker compose exec app bash
?

## Execute tests inside container
python -m unittest __seedwork.tests.unit.domain.test_unit_value_objects