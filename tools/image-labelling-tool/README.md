# Image Labelling Tool
This repository is a fork of a project released [here](https://bitbucket.org/ueacomputervision/image-labelling-tool).
The original originals are Geoffrey French, Dr. M. Fisher and Dr. M. Mackiewicz at University of East Anglia.

The code is modified to work better with SLIC initialization.
Also, this repository provides a complete example to train an object detection model with annotated data.

## Installation
```
$ pip install -e .
```

## Usage
```bash
# This starts up interactive annotator.
# If slic option is supplied, it starts with precomputed segmentations based on SLIC.
$ python flask_app.py [--slic] [--image_dir PATH_TO_DIR] [--label_names label_names.yml]
```
SLIC option should not be set for those who only want to annotate by bounding boxes.
The option can be helpful for segmenting an image. Please be aware the superpixel segmentation is not always perfect.

The annotations will be stored in the same directory where the corresponding images exist.
The annotaions are stored by `.json` files containing all the parameters.

I provided a convenient script to translate raw `.json` into a label image.
This can be helpful for annotating semantig segmentation datasets.
```bash
# Convert annotated json to labels
$ python convert_json_to_label.py [--image_dir PATH_TO_DIR] [--label_names label_names.yml]
```

## Example

#### Annotation

```bash
$ python flask_app.py --image_dir examples/simple/images --label_names examples/simple/label_names_example.yml --file_ext jpg
$ python convert_json_to_label.py --image_dir examples/simple/images --label_names examples/simple/label_names_example.yml
```

If you want to initialize an image with superpixel initialization, use `--slic` option.
Please use `--file_ext` to specify the file extension of images.

![](https://github.com/yuyu2172/image-labelling-tool/blob/master/examples/simple/screenshot.png)


#### Full example to train an object detection model with annotated dataset
In the examples, there is a training script for SSD that uses dataset that is created by this annotation tool.
SSD is one of the state of the art deep learning based object detection model.

The implementation uses ChainerCV, a computer vision library.
The library is created to lower the barrier of entry to use deep learning based computer vision models.

The more details can be found in [`examples/ssd`](https://github.com/yuyu2172/image-labelling-tool/tree/master/examples/ssd).


# (Original README starts here) UEA Computer Vision - Image Labelling Tool

#### A light-weight image labelling tool for Python designed for creating segmentation datasets.

Operates as a browser-based application, either embedded as a widget within [IPython Notebook](http://ipython.org)
or embedded within a web page as part of a web application.

Currently supports simple polygonal labels.


### IPython Notebook widget example

The supplied IPython notebook example creates a labelling tool widget and displays it within the notebook.
API usage is demonstrated further down.

### Flask web app example

An example Flask-based web app is provided that displays the labelling tool within a web page. To start it,
run `python flask_app.py` and open `127.0.0.1:5000` within a browser.


### Libraries, Credits and License

Incorporates the public domain [json2.js](https://github.com/douglascrockford/JSON-js) library.
Uses [d3.js](http://d3js.org/), [jQuery](https://jquery.com/), [jQuery UI](https://jqueryui.com/)
and [PolyK](http://polyk.ivank.net/).

This software was developed by Geoffrey French in collaboration with Dr. M. Fisher and
Dr. M. Mackiewicz at the [School of Computing Sciences](http://www.uea.ac.uk/computing)
at the [University of East Anglia](http://www.uea.ac.uk) as part of a project funded by
[Marine Scotland](http://www.gov.scot/Topics/marine).

It is licensed under the MIT license.
