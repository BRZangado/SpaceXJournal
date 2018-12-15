# SpaceX Journal

SpaceX Launches Journal

The goal of the project is to visualize in a simplified way data obtained through the [Space X API](https://api.spacexdata.com/v3/launches/).

Data obtained: <br>
Next launch <br>
Future launches <br>
Latest launch <br>
Past launches |
Information on launches, rockets and launch site

### Methodology

The applied methodology involves concepts of object oriented programming, clean code and SOLID. However, the approach that best represents the current state of the program is the application of dynamic programming concepts. In order to avoid excess requests and repetitive tasks, besides the dependence of the connection with the external API, a database was implemented that stores the collected information for future reading, facilitating the retrieval of this data and even the search speed.

### How to use

First, install the necessary dependencies

```
pip install -r requirements.txt
```

And then execute the program

```
python3 main.py
```

### Unittests

```
python -m unittest discover tests
```

### Test Coverage

```
coverage report
```

