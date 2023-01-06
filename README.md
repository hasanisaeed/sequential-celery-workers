### Scenario:

> Three different projects that work together! 

- `c1` send data to `c2`

- `c2` receive data from `c1` and send data to `c3`

- `c3` receive data from `c2` and return results to `c2`

- `c2` return results to `c1`

### Run celery workers in their folders

```bash

cd c1/
python main.py    # run main file to start sending data
    
celery -A tasks worker -l INFO

cd c2/
celery -A tasks worker -l INFO

cd c3/
celery -A tasks worker -l INFO
```

> Warning: update your `broker` and `backend` urls!
