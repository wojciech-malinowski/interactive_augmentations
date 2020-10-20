import yaml
import albumentations as A
from functools import partial
import ipywidgets as widgets
from ipywidgets import Label, HBox, VBox, Image, interactive_output, Output
from ipywidgets import Button, RadioButtons, Dropdown, GridspecLayout
from ipywidgets import FloatText, FloatSlider, FloatRangeSlider
from ipywidgets import IntText, IntSlider, IntRangeSlider
from IPython.display import display, clear_output
import random
import cv2
from .params import parameters_dictionary

# disable the below error ocurring durin the import of albumentatinos
yaml.warnings({"YAMLLoadWarning": False})


class AugmentationExplorer:
    def __init__(self, augmentations=[], img_paths=None, num_rows=4, shape=None):
        """
        augmentations - list of augmentations to pass
        img_paths - a list of paths to the images
        num_rows - number of images that the augmentation will be tested on
        shape - desired shape of the images
        """
        self.augmentations = augmentations
        self.img_paths = img_paths
        self.aug_dict = parameters_dictionary

        path = random.choice(img_paths)
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if shape is None:
            shape = (image.shape[0], image.shape[1])
        channels = 1 if len(image) == 2 else image.shape[2]

        self.shape = shape
        self.channels = channels
        self.num_rows = num_rows
        self.options = list(sorted(self.aug_dict.keys()))

    def choose_augmentation(self):
        widget = Dropdown(
            options=self.options,
            value="Blur",
            disabled=False,
        )

        description = HBox([Label("Choose your augmentation")])
        out = Output()

        def on_change(change):
            if change["type"] == "change" and change["name"] == "value":
                with out:
                    self.create_parameter_widgets(change["new"])
                    clear_output(wait=True)

        widget.observe(on_change)
        display(description, widget, out)

        with out:
            self.create_parameter_widgets(self.options[0])
            clear_output(wait=True)

    def create_parameter_widgets(self, augmentation_name):
        """
        augmentation_name - name of the augmentation you want to test
        """
        function = partial(self.test_aug, augmentation_name=augmentation_name)

        ui_s = []
        widget_dict = {}

        for param_name, values in self.aug_dict[augmentation_name].items():
            if values[-2] == "width":
                lower = values[1]
                upper = self.shape[1]
            elif values[-2] == "height":
                lower = values[1]
                upper = self.shape[0]
            elif values[-2] == "channels-1":
                lower = values[1]
                upper = self.channels - 1
            elif values[-1] == "max":
                lower = values[1]
                upper = max(self.shape)
            else:
                lower = values[1]
                upper = values[2]

            if values[-1] == "odd" and values[0] in ["int" "int_range"]:
                step = 2
            elif values[-1] != "odd" and (
                values[0] == "int" or values[0] == "int_range"
            ):
                step = 1
            elif values[0] == "float" or values[0] == "float_range":
                step = 0.01

            if values[0] == "int":
                widget = IntSlider(
                    min=lower,
                    max=upper,
                    step=step,
                    orientation="horizontal",
                    # description=f'{param_name}:',
                    continuous_update=False,
                )

                widget_ = IntText(
                    description="",
                    continuous_update=False,
                    readout=True,
                    readout_format="d",
                )
                widgets.link((widget, "value"), (widget_, "value"))
                widgets_linked = VBox([widget, widget_])
                widgets_linked_with_description = HBox(
                    [Label(param_name), widgets_linked]
                )
                ui_s.append(widgets_linked_with_description)

                setattr(widgets_linked_with_description, "value", widget.value)

            elif values[0] == "int_range":
                widget = IntRangeSlider(
                    value=[1, 1] if values[-1] == "odd" else [0, 0],
                    min=lower,
                    max=upper,
                    step=step,
                    # description=f'{param_name}:',
                    disabled=False,
                    continuous_update=False,
                    orientation="horizontal",
                    readout=True,
                    readout_format="d",
                )
                widget_with_description = HBox([Label(param_name), widget])
                setattr(widget_with_description, "value", widget.value)

                ui_s.append(widget_with_description)

            elif values[0] == "float":
                widget = FloatSlider(
                    value=0,
                    min=lower,
                    max=upper,
                    step=step,
                    # description=f'{param_name}:',
                    disabled=False,
                    continuous_update=False,
                    orientation="horizontal",
                    readout=True,
                    readout_format=".2f",
                )
                widget_ = FloatText(
                    description="",
                    continuous_update=False,
                    readout=True,
                    readout_format=".2f",
                )
                widgets.link((widget, "value"), (widget_, "value"))
                widgets_linked = VBox([widget, widget_])
                widgets_linked_with_description = HBox(
                    [Label(param_name), widgets_linked]
                )
                ui_s.append(widgets_linked_with_description)

                setattr(widgets_linked_with_description, "value", widget.value)

            elif values[0] == "float_range":
                widget = FloatRangeSlider(
                    value=[0, 0],
                    min=lower,
                    max=upper,
                    step=step,
                    disabled=False,
                    continuous_update=False,
                    orientation="horizontal",
                    readout=True,
                    readout_format=".2f",
                )

                widget_with_description = HBox([Label(param_name), widget])
                ui_s.append(widget_with_description)
                setattr(widget_with_description, "value", widget.value)

            elif values[0] == "str" or values[0] == "bool":
                widget = RadioButtons(
                    options=[*values[1]], value=values[1][1], disabled=False
                )
                widget_with_description = HBox([Label(param_name), widget])
                setattr(widget_with_description, "value", widget.value)
                ui_s.append(widget_with_description)

            # ui_s.append(widget)
            widget_dict[f"{param_name}"] = widget

        out = interactive_output(function, widget_dict)

        display(*ui_s, out)

    def test_aug(self, augmentation_name, **params):
        """
        augmentation_name - name of the augmentation you will be testing
        params - parameters of the augmentations grabbed from the widgets
        """
        augmentation = getattr(A, augmentation_name)
        grid = GridspecLayout(self.num_rows, 3)
        grid.layout.justify_items = "center"
        caption_grid = GridspecLayout(1, 3)
        caption_grid.layout.justify_items = "center"

        caption_grid[0, 0] = Label("NO AUGMENTATIONS")
        caption_grid[0, 1] = Label("CURRENT AUGMENTATION")
        caption_grid[0, 2] = Label("CURRENT + PREVIOUS AUGMENTATIONS")

        for counter_ in range(self.num_rows):

            img_path = random.choice(self.img_paths)
            image = cv2.imread(img_path)
            image = cv2.resize(
                image,
                (self.shape[1], self.shape[0]),
                interpolation=cv2.INTER_CUBIC,
            )
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            current_augmented_image = augmentation(**params, p=1.0)(image=image)[
                "image"
            ]

            augmentations_list = self.augmentations + [augmentation(**params, p=1.0)]
            augmented = A.Compose(augmentations_list)
            augmented_image = augmented(image=image)["image"]
            shape = (augmented_image.shape[0], augmented_image.shape[1])
            channels = (
                1 if len(augmented_image.shape) == 2 else augmented_image.shape[-1]
            )

            image_no_aug = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            image_current = cv2.cvtColor(current_augmented_image, cv2.COLOR_RGB2BGR)
            image_all = cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR)

            _, image_bytes = cv2.imencode(".jpg", image_no_aug)
            _, image_current_bytes = cv2.imencode(".jpg", image_current)
            _, image_all_bytes = cv2.imencode(".jpg", image_all)

            grid[counter_, 0] = Image(
                value=image_bytes.tobytes(),
                format="jpg",
                width=200,
                height=200,
            )
            grid[counter_, 1] = Image(
                value=image_current_bytes.tobytes(),
                format="jpg",
                width=200,
                height=200,
            )
            grid[counter_, 2] = Image(
                value=image_all_bytes.tobytes(),
                format="jpg",
                width=200,
                height=200,
            )

        display(caption_grid, grid)
        self.add_augmentation(augmentation, shape, channels, **params)

    def add_augmentation(self, augmentation, shape, channels, **params):

        """
        augmentation - an augmentation to add
        shape - shape of the output image
        chennels - number of channels of the oputput image
        params - parameters of the augmentation
        """
        # the augmentation changes shape of the image -> its probability is 1
        condition = not (*self.shape, self.channels) == (*shape, channels)

        if condition:
            value = 1.0
        else:
            value = 0.5

        probability_slider = FloatSlider(
            value=value,
            min=0,
            max=1,
            step=0.01,
            description="Probability:",
            disabled=condition,
            continuous_update=False,
            orientation="horizontal",
            readout=True,
            readout_format=".2f",
        )
        button = Button(description="Add the augmentation")
        output = Output()

        display(probability_slider, button, output)

        def on_button_clicked(b):
            with output:
                it_exists = False
                if not condition:
                    p = probability_slider.value
                else:
                    p = 1.0

                params["p"] = p
                for existing_augmentation in self.augmentations:
                    existing_aug_repr = repr(existing_augmentation)
                    current_aug_repr = repr(augmentation(**params))
                    if existing_aug_repr == current_aug_repr:
                        it_exists = True

                if not it_exists:
                    print("AUGMENTATION ADDED")
                    self.shape = shape
                    self.channels = channels
                    self.augmentations.append(augmentation(**params))

                else:
                    print("THIS AUGMENTATION ALREADY EXISTS IN YOUR LIST")

        button.on_click(on_button_clicked)

    def get_augmentations(self):
        """
        Get a composition of the chosen augmentatinos
        """
        return A.Compose(self.augmentations)

    def delete_augmentation(self):
        """
        Choose augmentation to delete from your list
        """
        widget = Dropdown(
            options=self.augmentations,
            # description='AUG:',
            disabled=False,
        )

        description = HBox([Label("Choose the augmentation you want to delete")])
        button = Button(description="Delete")

        out = Output()

        display(description, widget, button, out)

        def on_button_clicked(b):
            if widget.value is not None:
                self.augmentations.remove(widget.value)
                print("AUGMENTATION DELETED")

                widget.options = self.augmentations

        button.on_click(on_button_clicked)
