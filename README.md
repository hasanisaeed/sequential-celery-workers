### Scenario:

`c1` send data to `c2`

`c2` send data to `c3`

`c3` return results to `c2`

`c2` return results to `c1`

### Run celery workers in their folders

    cd c1/
    celery -A tasks worker -l INFO

    cd c2/
    celery -A tasks worker -l INFO

    cd c3/
    celery -A tasks worker -l INFO
