# Fabulous Bot for Slack

<p align="center">
   <img align="centre" src="https://cdn-images-1.medium.com/max/800/1*BDwu0v1rHBpfFdYGx30yTw.png" alt="Fabulous Bot for Slack" width="200px" height="200px"/>
</p>


### Donate ($1) - Help us in creating more awesome open source projects

[<img src="https://www.paypalobjects.com/webstatic/mktg/logo/AM_mc_vs_dc_ae.jpg">](https://www.paypal.me/vikeshtiwari/1)

---

Never leave your Slack again!
------------------------------------

Fabulous Bot is a bot which does the basic work of searching from different
platforms and showing the results directly in your Slack channel.
Users don’t have to leave Slack, open browser and search for something.

## User will be able to

- search from Google, Wikipedia, YouTube etc—( top 3 results will be shown)
- Check weather of any city
- Search Query from Stack Overflow
- Get commits data of any repository, Branch or pull request
- Get stocks data
- Search images from Google Images, Flickr etc
- Do mathematical Calculations
- Check meaning of words — From Urban Dictionary
- View maps
- and will be able to perform lot more tasks.

[Read the full article here.](http://eulercoder.me/2017/09/eulercoder-project-series-fabulous-bot/)



# Installation

*Steps to Run this Bot Locally!*

- clone the repo
- Do `export SLACK_TOKEN='slack-api-token' `
- edit the Makefile and add `sudo` to the run, repl section and `sudo -H` in requirements section
- then `make repl` for local testing
- if `make repl` doesn't work, try with `sudo`
- *_Work on services folder only_*
- Check `gif service` for the reference.

*Note: for windows, edit Makefile and remove all instances of `sudo` and `sudo -H`*

*Running in a Docker contianer!*

- Clone the repo
- run `cd fabulous && docker build -t faboulous . && docker run -it fabulous`

# Getting Started

[Please read this article on Fabulous Bot](http://eulercoder.me/2017/09/eulercoder-project-series-fabulous-bot/)

# Contributing

Please read our [Contributing to Eulercoder Projects Wiki.](https://github.com/Eulercoder/fabulous/wiki/Contributing-to-Fabulous-Bot)



# Issues

Check [Issue tracker](https://github.com/eulercoder/fabulous/issues) for all the issues.

# Licence

[MIT](https://github.com/eulercoder/fabulous/blob/master/LICENSE) Licence (c) [Vikesh Tiwari](https://github.com/vicky002)

Built with :heart: in python and [Eulercoder](http://eulercoder.me)
