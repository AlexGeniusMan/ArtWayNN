# ArtWayNN


| Python | Docker |
|-----------|-----------|
| ![example workflow](https://github.com/RTUITLab/ArtWayNN/actions/workflows/3.6.yml/badge.svg) ![example workflow](https://github.com/RTUITLab/ArtWayNN/actions/workflows/3.7.yml/badge.svg) ![example workflow](https://github.com/RTUITLab/ArtWayNN/actions/workflows/3.8.yml/badge.svg) | ![example workflow](https://github.com/RTUITLab/ArtWayNN/actions/workflows/docker.yml/badge.svg) |

**Contents:**
* [Run service](#run)
* [Docs](#docs)
* [Usage](#usage)


## Run service
<a name="run"></a>

### With Docker
Build:

`docker build -t artwaynn .`

And run

`docker run -it -p 5000:8000 artwaynn`

### With Docker Compose
With docker-compose service start up at 5000 port by default:

`docker-compose up --build`

or

`docker-compose up --build -d` in daemon mode


## Docs
<a name="setup"></a>
Documentation is available at [http://localhost:5000/docs](http://localhost:5000/docs)


## Usage
<a name="usage"></a>
:warning:There may be another hostname instead of `localhost`. 
```
import base64
import requests

def get_image_label(path: str):
    index_to_label = {
        0: "Test",
        1: "Medal",
        2: "PC",
        3: "Search",
        4: "Projector",
        5: "Idea",
        6: "Telescope",
        7: "Briefcase",
        8: "Trofy",
        9: "Cap",
    }

    with open(path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode("utf-8")
    response = requests.post("http://localhost:5000/predict/", json={"base64_str": base64_str})

    preds = response.json()
    index = preds.index(max(preds))

    return index_to_label[index]
```