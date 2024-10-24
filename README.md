# passphrase

Simple python script to generate strong passwords with russian words.

## Example usage

With docker image:

```shell
docker run --rm funbiscuit/passphrase
```

With custom phrase template:

```shell
docker run --rm funbiscuit/passphrase adj noun verb adj noun
```

Supported word codes:
* adj - adjective
* noun - noun
* verb - verb
