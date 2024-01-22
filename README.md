# Reference Generator

### Introduction
This python automation program creates a haravard referance for the user by having the user input the header, year of publish and URL of the web page. All references are stored in one location within a text file for easy retrievel.

### Prerequisites

You can follow these instructions to setup the developer environment:

- Install BeautifulSoup
- Install Requests

```
pip install beautifulsoup4
```

```
pip install requests
```

### Run Python Application
```
Referance.py
```

### Docker
Download Docker Desktop for Mac or Windows. This solution uses Python3 and Python libraries.<br/>

### Build Command

Build the image, this may take some time. After your image is built, you can view your image in the Images tab in Docker Desktop.
```
docker build -t reference-program-dockerisation .
```
The -t flag tags your image with a name, reference-program-dockerisation in this case. And the . lets Docker know where it can find the Dockerfile.

### Run Command

To run the program type this command:
```
docker run -i -t reference-program-dockerisation
```

### Run Unit Test
```
python -m unittest Test_Referance
```
