import unittest
from data.styles import LayerStyle
from test import layer_styles_data
from data.point import Point


class LayerStylesTest(unittest.TestCase):

    def test_create_flat_color_layer_styles(self):
        sketch_dict = layer_styles_data.flat_color()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/flatColor")
        self.assertEqual(generated.atom, "flatColor")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.gradient)
        self.assertIsNone(generated.outline)
        self.assertIsNone(generated.image)

        self.assertEqual(generated.color.red, 0.7669536564625851)
        self.assertEqual(generated.color.green, 0.1353305220841493)
        self.assertEqual(generated.color.blue, 0.1353305220841493)
        self.assertEqual(generated.color.alpha, 1.0)

    def test_create_linear_gradient_layer_style(self):
        sketch_dict = layer_styles_data.linear_gradient()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/linearGradient")
        self.assertEqual(generated.atom, "linearGradient")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.outline)
        self.assertIsNone(generated.image)
        self.assertIsNotNone(generated.gradient)

        self.assertEqual(generated.color.red, 0)
        self.assertEqual(generated.color.green, 0)
        self.assertEqual(generated.color.blue, 0)
        self.assertEqual(generated.color.alpha, 0)

        gradient = generated.gradient
        self.assertTrue(gradient['isAxial'])
        self.assertFalse(gradient['isRadial'])
        self.assertEqual(gradient['locations'], [0, 1])
        self.assertEqual(len(gradient['colors']), 2)

        self.assertEqual(gradient['colors'][0].red, 0.8916280506641954)
        self.assertEqual(gradient['colors'][0].green, 0.2812364847457446)
        self.assertEqual(gradient['colors'][0].blue, 0.2812364847457446)
        self.assertEqual(gradient['colors'][0].alpha, 1.0)
        self.assertEqual(gradient['colors'][1].red, 0.3298522534013605)
        self.assertEqual(gradient['colors'][1].green, 0.02545083970669037)
        self.assertEqual(gradient['colors'][1].blue, 0.02545083970669037)
        self.assertEqual(gradient['colors'][1].alpha, 1.0)

        self.assertEqual(gradient['from'], Point(0.5, 0.0))
        self.assertEqual(gradient['to'], Point(0.5, 1.0))

    def test_create_radial_gradient_layer_style(self):
        sketch_dict = layer_styles_data.radial_gradient()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/radialGradient")
        self.assertEqual(generated.atom, "radialGradient")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.outline)
        self.assertIsNone(generated.image)
        self.assertIsNotNone(generated.gradient)

        self.assertEqual(generated.color.red, 0)
        self.assertEqual(generated.color.green, 0)
        self.assertEqual(generated.color.blue, 0)
        self.assertEqual(generated.color.alpha, 0)

        gradient = generated.gradient
        self.assertFalse(gradient['isAxial'])
        self.assertTrue(gradient['isRadial'])
        self.assertEqual(gradient['locations'], [0, 1])
        self.assertEqual(len(gradient['colors']), 2)

        self.assertEqual(gradient['colors'][0].red, 0.8916280506641954)
        self.assertEqual(gradient['colors'][0].green, 0.2812364847457446)
        self.assertEqual(gradient['colors'][0].blue, 0.2812364847457446)
        self.assertEqual(gradient['colors'][0].alpha, 1.0)
        self.assertEqual(gradient['colors'][1].red, 0.3298522534013605)
        self.assertEqual(gradient['colors'][1].green, 0.02545083970669037)
        self.assertEqual(gradient['colors'][1].blue, 0.02545083970669037)
        self.assertEqual(gradient['colors'][1].alpha, 1.0)

        self.assertEqual(gradient['from'], Point(0.5, 0.53427734375))
        self.assertEqual(gradient['to'], Point(0.5, 1.53427734375))

    def test_create_noise_fill_layer_style(self):
        sketch_dict = layer_styles_data.noise_fill()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/noiseFill")
        self.assertEqual(generated.atom, "noiseFill")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.outline)
        self.assertIsNotNone(generated.image)
        self.assertIsNone(generated.gradient)

        self.assertEqual(generated.color.red, 0)
        self.assertEqual(generated.color.green, 0)
        self.assertEqual(generated.color.blue, 0)
        self.assertEqual(generated.color.alpha, 0)

    def test_create_image_fill_tile_layer_style(self):
        sketch_dict = layer_styles_data.image_fill_tile()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/patternFill_Tile")
        self.assertEqual(generated.atom, "patternFill_Tile")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.outline)
        self.assertIsNotNone(generated.image)
        self.assertIsNone(generated.gradient)

        self.assertEqual(generated.color.red, 0)
        self.assertEqual(generated.color.green, 0)
        self.assertEqual(generated.color.blue, 0)
        self.assertEqual(generated.color.alpha, 0)

        image = generated.image

        self.assertEqual(image["file_name"], "layer_*_*_patternFill_Tile")
        self.assertEqual(image["tile_scale"], 1)
        self.assertEqual(image["fill_type"], 0)
        self.assertEqual(image["resizingMode"], "tile")
        self.assertEqual(image["gravity"], "center")

    def test_create_image_fill_fill_layer_style(self):
        sketch_dict = layer_styles_data.image_fill_fill()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/patternFill_Fill")
        self.assertEqual(generated.atom, "patternFill_Fill")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.outline)
        self.assertIsNotNone(generated.image)
        self.assertIsNone(generated.gradient)

        self.assertEqual(generated.color.red, 0)
        self.assertEqual(generated.color.green, 0)
        self.assertEqual(generated.color.blue, 0)
        self.assertEqual(generated.color.alpha, 0)

        image = generated.image

        self.assertEqual(image["file_name"], "layer_*_*_patternFill_Fill")
        self.assertEqual(image["tile_scale"], 1)
        self.assertEqual(image["fill_type"], 1)
        self.assertEqual(image["resizingMode"], "stretch")
        self.assertEqual(image["gravity"], "resizeAspectFill")

    def test_create_image_fill_fit_layer_style(self):
        sketch_dict = layer_styles_data.image_fill_fit()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/patternFill_Fit")
        self.assertEqual(generated.atom, "patternFill_Fit")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.outline)
        self.assertIsNotNone(generated.image)
        self.assertIsNone(generated.gradient)

        self.assertEqual(generated.color.red, 0)
        self.assertEqual(generated.color.green, 0)
        self.assertEqual(generated.color.blue, 0)
        self.assertEqual(generated.color.alpha, 0)

        image = generated.image

        self.assertEqual(image["file_name"], "layer_*_*_patternFill_Fit")
        self.assertEqual(image["tile_scale"], 1)
        self.assertEqual(image["fill_type"], 3)
        self.assertEqual(image["resizingMode"], "stretch")
        self.assertEqual(image["gravity"], "resizeAspect")

    def test_create_image_fill_stretch_layer_style(self):
        sketch_dict = layer_styles_data.image_fill_stretch()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/patternFill_Stretch")
        self.assertEqual(generated.atom, "patternFill_Stretch")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNone(generated.outline)
        self.assertIsNotNone(generated.image)
        self.assertIsNone(generated.gradient)

        self.assertEqual(generated.color.red, 0)
        self.assertEqual(generated.color.green, 0)
        self.assertEqual(generated.color.blue, 0)
        self.assertEqual(generated.color.alpha, 0)

        image = generated.image

        self.assertEqual(image["file_name"], "layer_*_*_patternFill_Stretch")
        self.assertEqual(image["tile_scale"], 1)
        self.assertEqual(image["fill_type"], 2)
        self.assertEqual(image["resizingMode"], "stretch")
        self.assertEqual(image["gravity"], "resize")

    def test_create_solid_outline_inside(self):
        sketch_dict = layer_styles_data.solid_outline_inside()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/solidOutline_Inside")
        self.assertEqual(generated.atom, "solidOutline_Inside")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNotNone(generated.outline)
        self.assertIsNone(generated.image)
        self.assertIsNone(generated.gradient)

        outline = generated.outline

        self.assertEqual(outline["color"].red, 0)
        self.assertEqual(outline["color"].green, 0)
        self.assertEqual(outline["color"].blue, 0)
        self.assertEqual(outline["color"].alpha, 1.0)
        self.assertEqual(outline["line_width"], 1)
        self.assertEqual(outline["dash_pattern"], [])
        self.assertFalse(outline["is_dash"])

    def test_create_dashed_outline(self):
        sketch_dict = layer_styles_data.dashed_outline()
        generated = LayerStyle.create_from_sketch_dict(sketch_dict)

        self.assertEqual(generated.name, "*/*/dashed_outline")
        self.assertEqual(generated.atom, "dashed_outline")
        self.assertIsNone(generated.element)
        self.assertIsNone(generated.section)
        self.assertIsNotNone(generated.outline)
        self.assertIsNone(generated.image)
        self.assertIsNone(generated.gradient)

        outline = generated.outline

        self.assertEqual(outline["color"].red, 0)
        self.assertEqual(outline["color"].green, 0)
        self.assertEqual(outline["color"].blue, 0)
        self.assertEqual(outline["color"].alpha, 1.0)
        self.assertEqual(outline["line_width"], 1)
        self.assertEqual(outline["dash_pattern"], [5])
        self.assertTrue(outline["is_dash"])


