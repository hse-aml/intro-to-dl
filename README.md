# Introduction to Deep Learning course resources
https://www.coursera.org/learn/intro-to-deep-learning

### Offline instructions
Coursera Jupyter Environment can be slow if many learners use it heavily. Our tasks are compute-heavy and we recommend to run them on your hardware for optimal performance.

Follow the instructions on https://hub.docker.com/r/zimovnov/coursera-aml-docker/ to install Docker container with all necessary software installed.

After that you should see a Jupyter page in your browser.

Click **New -> Terminal** and execute: `git clone https://github.com/hse-aml/intro-to-dl.git`

Close the terminal and refresh Jupyter page, you will see **intro-to-dl** folder, go there, all the necessary notebooks are waiting for you.

First you need to download necessary resources, to do that open `download_resources.ipynb` and run cells for your week.

Now you can open a notebook for the corresponding week and work there just like in Coursera Jupyter Environment.

### If Docker doesn't work for you
We highly recommend to install docker environment, but if it's not an option, 
you can try to install the necessary python modules with Anaconda.

First, install Anaconda with **Python 3.5+** from [here](https://www.anaconda.com/download).

Download `conda_requirements.txt` from [here](https://github.com/ZEMUSHKA/coursera-aml-docker/blob/master/conda_requirements.txt).

Open terminal on Mac/Linux or "Anaconda Prompt" in Start Menu on Windows and run:
```
conda config --append channels conda-forge
conda config --append channels menpo
conda install --yes --file conda_requirements.txt
```

To start Jupyter Notebooks run `jupyter notebook` on Mac/Linux or "Jupyter Notebook" in Start Menu on Windows.
