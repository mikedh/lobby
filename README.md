lobby
=====

A limit order book system written in Python. `lobby` is forked from [PyLOB](https://github.com/DrAshBooth/PyLOB) and all changes are also licensed as MIT. Updated to install with `pip` and work with Python 3.


`lobby` is a fully functioning fast simulation of a limit-order-book financial exchange, developed for modelling. The aim is to allow exploration of automated trading strategies that deal with "Level 2" market data.

It is written in Python, single-threaded and opperates a standard price-time-priority. It supports both market and limit orders, as well as add, cancel and update functionality. The model is based on few simplifying assumptions, chief of which is zero latency: if a trader issues a new quote, that gets processed by the exchange, all other traders can react to it before any other quote is issued.

Install
=============
`lobby` uses only the standard library, and can be installed from PyPi:

```
pip install lobby
```

