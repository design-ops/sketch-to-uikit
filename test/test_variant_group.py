import unittest
from test.layer_styles_data import image_fill_fit, flat_color
from data.styles import LayerStyle
from data.asset import VariantGroup

class VariantGroupTest(unittest.TestCase):

    def test_variant_groups_images(self):
        layer_styles = [
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element/image")),
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element[selected]/image")),
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element[disabled]/image")),
        ]
        group = VariantGroup.create_array_from_base_styles(layer_styles)
        self.assertEqual(len(group), 1, "array of layer styles with 1 element create 1 variant group")

    def test_images_extracted_when_all_images(self):
        layer_styles = [
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element/image")),
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element[selected]/image")),
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element[disabled]/image")),
        ]
        group = VariantGroup.create_array_from_base_styles(layer_styles)
        found_layers = group[0].items_with_layer_style_image()
        self.assertCountEqual(layer_styles, found_layers, "image layer styles are extracted")

    def test_images_extracted_when_just_variants_are_images(self):
        layer_styles = [
            LayerStyle.create_from_sketch_dict(flat_color("*/element/image")),
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element[selected]/image")),
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element[disabled]/image")),
        ]
        group = VariantGroup.create_array_from_base_styles(layer_styles)
        found_layers = group[0].items_with_layer_style_image()
        self.assertEqual(len(found_layers), 2, "image layer styles are extracted from variants")

    def test_images_extracted_when_just_main_is_image(self):
        layer_styles = [
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element/image")),
            LayerStyle.create_from_sketch_dict(flat_color("*/element[selected]/image")),
            LayerStyle.create_from_sketch_dict(flat_color("*/element[disabled]/image")),
        ]
        group = VariantGroup.create_array_from_base_styles(layer_styles)
        found_layers = group[0].items_with_layer_style_image()
        self.assertEqual(len(found_layers), 1, "image layer styles are extracted from variants")

    def test_images_extracted_when_just_some_variants_are_images(self):
        layer_styles = [
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element/image")),
            LayerStyle.create_from_sketch_dict(image_fill_fit("*/element[selected]/image")),
            LayerStyle.create_from_sketch_dict(flat_color("*/element[disabled]/image")),
        ]
        group = VariantGroup.create_array_from_base_styles(layer_styles)
        found_layers = group[0].items_with_layer_style_image()
        self.assertEqual(len(found_layers), 2, "image layer styles are extracted from variants")