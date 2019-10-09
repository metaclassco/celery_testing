This is a sample project to show:
* how we can check that Celery workers are active;
* how we can inform our team with Slack notifications in other case.

Before building Docker container SLACK_TOKEN must to be passed as env variable
```shell script
export SLACK_TOKEN=<your-slack-token>
```
Then you can build container as usual
```shell script
docker-compose build
```
and run with
```shell script
docker-compose up  # or docker-compose up -d
```

To test Slack notifications on worker fail you can do next:
- go to running container with `docker-compose exec worker bash` and stop Celery in it;
- build container without started Celery worker:
  ```shell script
  export TEST_FAILURE=true
  docker-compose build
  ```

To build initial container you need to call 
```shell script
unset TEST_FAILURE
```