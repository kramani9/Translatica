# Translatica

## Project Description

Translatica uses OpenAI and SO VITS SVG to generate a dub of a video lecture while maintaining the lectures tone and voice

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features](#features)
- [Contributing](#contributing)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation

`git clone https://github.com/voicepaw/so-vits-svc-fork.git' so-vits-fork for voice inference and training, follow svc install instructions

Insert all files from this repository directly into so-vits-svc-fork folder.

## Usage

Run:
```python interface.py```

Upload an mp4, choose a language to translate from and a language to translate to. Press Process Video.

## Configuration

Create a virtual environment via 
` python3 -m venv venv `
` source ./venv/bin/activate `

Create a .env file and copy the env_template.txt file after making the relevant changes regarding your google cloud service account (that will be interacting with the API's). Also include the account's json file in the so-vits-svc-fork folder.

You will also need to update the openAIAPI.py file with your openAI api key.


## Features

List and explain the key features of the project.

## Contributing

Guidelines for contributing to the project, including information about how to submit bug reports, feature requests, or pull requests.

## Authors

Krishna Ramani
Baaz Jhaj
Jeffrey Hsu

## Acknowledgments

Recognize and thank individuals or projects that have contributed to the development of the project.

