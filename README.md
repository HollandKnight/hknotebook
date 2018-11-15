# HK Lawyer Notebook

**A Jupyter notebook designed for lawyers.**

![alt text](https://github.com/jndewey/dashboard/blob/master/dashboard/Screenshot_2018-10-06%20%20lawyer_notebook-0(5).png)

![alt text](https://github.com/jndewey/dashboard/blob/master/dashboard/Screenshot_2018-10-06%20%20lawyer_notebook-0(6).png)

![alt text](https://github.com/jndewey/dashboard/blob/master/dashboard/Screenshot_2018-10-06%20%20lawyer_notebook-0(7).png)
***

## Try it live

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/HollandKnight/notebooks/master)

Once binder loads, open lawyer_notebook.ipynb.  Once opened, click the "Appmode" button.
***

## Description

A collection of simple, yet powerful tools for lawyers to do their jobs better and more efficiently. By leveraging data analytics, natural language processing, machine learning, network graphing and other open source solutions, users are able to produce better quality work faster and more efficiently. Many of these tools are still under active development, so the H&K Lawyer Notebook is reserved for our more intrepid lawyers.

***
## Deployment

1. Install [Docker](https://docs.docker.com/engine/installation/).
2. git clone this repository
3. `docker build --tag appmode_dev ./`
4. `docker run --init -ti -p8888:8888 appmode_dev`
5. Browse to `http://localhost:8888/apps/lawyer_notebook.ipynb`
