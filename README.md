# tensorflow_som_colours

## Requirements

This app requires the newest version of docker installed as of the writing of this README, June 6, 2018.

## Installation

To build the docker app:

```
docker build -t som_app .
```

## Execution / Run

```
docker run -p 5000:5000 som_app
```

The app will be then available in your browser @ `http://localhost:5000`
