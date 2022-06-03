# MapRoulette Photo Challenge Creator

*This is early stage work and not ready to use*

It would be interesting to create MapRoulette Challenges based on geotagged photos. This Python script is meant to make that easy. It takes a folder with geotagged images from your own computer, uploads them and creates the MapRoulette Challenge with a photo for each task. The photo shows up in the task instructions.

## Instructions for Use

### Preparation

To set up your local Python environment, follow these steps:

1. Clone this repo

`git clone git@github.com:mvexel/maproulette-photo-challenge.git`

2. Navigate into the local directory

`cd maproulette-photo-challenge`

3. Create a virtual Python environment

`python3 -m venv venv`

4. Activate the virtual environment

`source venv/bin/activate`

5. Install the dependencies (`maproulette` and `requests`)

`pip install -r requirements.txt`


### Configuration

All configuration is done in a configuration file you need to create in the root directory of this repository. An annotated example is provided as `config-example.py`. You should create a copy of this file, name it `config.py`, and adapt the settings to match your workflow.

### Running

After you configured your environment properly, you should be ready to run the script:

`python create_challenge.py`

I strongly advise to use `staging.maproulette.org` for initial testing.

## Development

Currently, only Imgur is supported, but using the `Hoster` interface, you should be able to add other image hosting options pretty easily.