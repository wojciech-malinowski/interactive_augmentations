# interactive_augmentations

interactive_augmentations is a package allowing to explore Albumentations' augmentations in Jupyter Notebook.
![alt text](https://github.com/wojciech-malinowski/interactive_augmentations/blob/main/examples/example.jpg)


## Installation

In order to install the package run the following command.
```bash
!pip install git+git://github.com/wojciech-malinowski/interactive_augmentations.git
```

## Usage

```python
import interactive_augmentations

#list containing paths to your images
img_paths = []
explorer = AugmentationsExplorer(img_paths)

explorer.choose_augmentation()
```

## Examples
Go [here](https://github.com/wojciech-malinowski/interactive_augmentations/blob/main/examples/Untitled.ipynb) to check out a notebook with examples of the package in use.


## Comments
Not all augmentations which can be found in [Albumentatinos](https://github.com/albumentations-team/albumentations) are supported at the moment. The number of the currently supported ones is 44. (20/10/2020)


## License
[MIT](https://choosealicense.com/licenses/mit/)
