# hello-world
My first repository
The very exciting readme file has been updated.

## IGP Manager Interaction Example

This repository now includes a simple Python application for interacting with the IGP Manager website. The code is organized as a package named `igp` with the following modules:

- `config.py` – stores HTTP headers and the base URL used for requests
- `login.py` – contains a helper function for authenticating with the site

The `main.py` file demonstrates using these modules to log in. Credentials are provided as command line arguments.

All dependencies are listed in `requirements.txt`. The application is designed with AWS Lambda in mind, making it easy to adapt each module into a Lambda handler.
