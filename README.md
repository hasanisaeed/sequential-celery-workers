### Scenario:

`c1` send data to `c2`

`c2` send data to `c3`

`c3` return results to `c2`

`c2` return results to `c1`

### Run celery workers in their folders

    cd c1/
    python main.py // run main file to start sending data
    
    celery -A tasks worker -l INFO

    cd c2/
    celery -A tasks worker -l INFO

    cd c3/
    celery -A tasks worker -l INFO


> Warning: update your `broker` and `backend` urls!
