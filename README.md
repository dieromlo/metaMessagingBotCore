# metaMessagingBotCore

i built this tool to automate customer messages, keep track of products, and make sales operations much easier for my mom's business.

on the technical side, it's a clean automation pipeline and webhook listener. it runs on an asynchronous backend built with Python and Flask that connects directly to meta's graph API to handle routing and incoming data without external overhead.

uploaded this to GitHub to practice Git, improve my backend skills, and keep my projects organized!


## tech stack

* python (modular structural architecture)
* flask (lightweight webhook handling & routing)
* meta graph api (whatsapp cloud integration)
* ngrok (secure local tunneling for payload verification)

## architecture & features

* **webhook handler**: asynchronous endpoint designed to safely listen for, parse, and validate incoming messaging payloads directly from meta.
* **state engine (botBrain)**: engineered to track conversational states, map user inputs, and process business-specific logic (`src/botBrain.py`).
* **data persistence**: utilizes localized structures (`data/planes.json`) to manage inventory and client-facing routing dynamically.

## project structure

metaMessagingBotCore ── src ── botBrain.py # core logic & conversation state engine
                     └── whatsapp-receiver # local node modules for routing tests
                     └── data ── planes.json # inventory & dynamic response configurations
                     └── main.py # main server execution entry point
                     └── .gitignore # credential & binary protection shield