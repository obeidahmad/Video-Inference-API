# Video-Inference-API

This is a repository for a semantic segmentation inference API of a video using the [BMW-IntelOpenVINO-Segmentation-Inference-API](https://github.com/BMW-InnovationLab/BMW-IntelOpenVINO-Segmentation-Inference-API).

## Prerequisites

- OS:
  - Ubuntu 20.04
  - Windows 10 pro/enterprise
- Docker

### Check for prerequisites

To check if you have docker-ce installed:

```sh
docker --version
```

### Install prerequisites

#### Ubuntu
Use the following command to install docker on Ubuntu:

```sh
chmod +x install_prerequisites.sh && source install_prerequisites.sh
```
#### Windows 10

To [install Docker on Windows](https://docs.docker.com/docker-for-windows/install/), please follow the link.


## Build The Docker Image

In order to build the project run the following command from the project's root directory:

```sh
docker build -t video_inference_api -f docker/Dockerfile .
```

## Run The Docker Container

If you wish to deploy this API using **docker**, please issue the following run command.

To run the API, go the to the API's directory and run the following:

#### Using Linux based docker:

```sh
docker run -itv $(pwd)/data:/data -p <port_of_your_choice>:8080 video_inference_api
```
#### Using Windows based docker:
##### Using PowerShell:
```sh
docker run -itv ${PWD}/data:/data -p <port_of_your_choice>:8080 video_inference_api
```
##### Using CMD:
```sh
docker run -itv %cd%/data:/data -p <port_of_your_choice>:8080 video_inference_api
```

#### Connect with other container:
Make sure all containers are in the same network. Add the following option to the docker command:
```sh
--net <network_name>
```
Refer to [Use bridge networks | Docker Documentation](https://docs.docker.com/network/bridge/) for more information about bridge networks

\
The <docker_host_port> can be any unique port of your choice.\
The <network_name> is a bridged network name of your choice.

The API file will run automatically, and the service will listen to http requests on the chosen port.

## API Endpoints

To see all available endpoints, open your favorite browser and navigate to:

```
http://<machine_IP>:<docker_host_port>/docs
```

### Endpoints summary

#### /inference (POST)

Perform inference on a video using the specified model and returns the resulting video as a response.


## More Information
Refer to [BMW-IntelOpenVINO-Segmentation-Inference-API](https://github.com/BMW-InnovationLab/BMW-IntelOpenVINO-Segmentation-Inference-API) for more information on how to add models
