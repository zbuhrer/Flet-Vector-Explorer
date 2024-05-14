# Vector Explorer (Now in Flet!)

This is a work in progress. It only sort of works — use at your own risk, lol

This is a fork of the Vector Explorer app, which was itself a [fork which GrinningHermit made](https://github.com/GrinningHermit/Vector-Explorer-Tool/) of the Cosmo explorer. What a wild ride this little robot has gone on.

## Requirements

* [updated version of the Wirepod Vector SDK](https://github.com/kercre123/wirepod-vector-python-sdk) from kercre123. This is required to run the app; running the original SDK doesn't work well (much at all as far as I can tell) — follow the instructions carefully for installing the SDK, so it doesn't break any current attempts to get Vector working
* a wirepod-enabled Vector robot
  * So obviously you should have a working wirepod instance on your network

### How To Set This Up

I haven't gotten this to run on hardware other than my own yet, so *your mileage may vary*. Let's play with it together if it doesn't work on your machine.

#### Steps

1. git clone this repo
2. make a Python venv

  ```shell
  python3 -m venv venv
  ```

3. source your venv

  ```shell
  source venv/bin/activate
  ```

4. install dependencies from `requirements.txt` into your venv

  ```shell
  pip install -r requirements
  ```

5. `flet .`

### What works So Far

#### Chat

What this does is opens a connection with the default (only?) robot you have authenticated to your wirepod. You can type into the field and click the "Say" button to make Vector say a string of text. This is kind of buggy, but I used it during my process to confirm that the SDK was working correctly at all outside of Flet. It was the first component that I made from scratch before I found the Vector Explorer Tool which GrinningHermit made.

![Explorer Chat](./docs/img/explorer_chat.gif)

#### Remote Control

When I found GH's Vector Explorer, I wanted to replicate the functionality in Flet.

![Remote Control](./docs/img/explorer_remotecontrol.gif)

It doesn't seem like this does much, but when you click that "Connect" button, it starts a Flask server that we can use to replicate the original functionality of the Vector Explorer Tool via (socketed) API calls via Flet controls.
