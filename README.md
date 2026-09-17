Python Podman Calculator

An interactive Python calculator containerized and run using Podman. This project demonstrates basic Python programming along with container image creation and interactive container execution.

Features

* Addition
* Subtraction
* Multiplication
* Division
* Modulo
* Square Root
* Power
* Interactive operation selection

Technologies

* Python 3.12
* Podman
* Containerfile

Project Structure

```text
python-podman-calculator/
├── calculator.py
├── Containerfile
└── README.md
```

## Build the Image

```bash
podman build -t calculator:v1 .
```

## Run the Calculator

```bash
podman run --rm -it calculator:v1
```

## How It Works

text
User
 ↓
Choose Operation
 ↓
Enter Number(s)
 ↓
Python Calculator
 ↓
Display Result

Podman Concepts Practiced

* Containerfile
* Base images
* podman build
* Container images
* podman run`
* Interactive containers using -it
* Container lifecycle using --rm

Learning Purpose

This project was created as a hands-on exercise while learning containerization with Podman.
