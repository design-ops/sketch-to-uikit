import re
from enum import IntEnum
from typing import Optional
from dataclasses import dataclass
from data.colour import Colour
from data.point import Point
from utils import empty_str


class ItemGrouping(IntEnum):
    SECTION_ELEMENT_ATOM = 1
    SECTION_ATOM = 2
    ELEMENT_ATOM = 3
    ATOM = 4
    INVALID = 5


@dataclass
class BaseStyle:

    name: str
    atom: Optional[str]
    element: Optional[str]
    section: Optional[str]
    variant: Optional[str]
    grouping: ItemGrouping

    @classmethod
    def create_from_name(cls, name: str, *args, **kwargs):
        name_for_splitting = name.split('/')
        section = None
        element = None
        atom = None
        variant = None
        if len(name_for_splitting) == 3:
            section = value_or_none(name_for_splitting[0])
            element = value_or_none(name_for_splitting[1])
            atom = value_or_none(name_for_splitting[2])

        grouping = ItemGrouping.ATOM
        if section is not None and element is not None:
            grouping = ItemGrouping.SECTION_ELEMENT_ATOM

        elif section is not None and element is None:
            grouping = ItemGrouping.SECTION_ATOM

        elif section is None and element is not None:
            grouping = ItemGrouping.ELEMENT_ATOM

        if element is not None:
            if element[-1:] == "]":
                # it has a state
                variant = re.search('\[(.*)\]', element).group(1)
                element = element.split("[")[0]

        if atom is None:
            print("🚨 couldn't find atom for '"+name+"'")
            grouping = ItemGrouping.INVALID

        base_style = cls(section=section,
                         element=element,
                         atom=atom,
                         variant=variant,
                         grouping=grouping,
                         name=name,
                         *args, **kwargs)
        return base_style

    @property
    def variant_name(self) -> str:
        return value_or_default(self.variant, "<no-variant>")

    @property
    def variant_object(self):
        if self.variant is None:
            return "UIControl.State.normal"
        switcher = {
            "normal": "UIControl.State.normal",
            "highlighted": "UIControl.State.highlighted",
            "disabled": "UIControl.State.disabled",
            "selected": "UIControl.State.selected",
            "focused": "UIControl.State.focused",
        }
        control_state = switcher.get(self.variant, None)
        if control_state is not None:
            return control_state
        # return a special variant
        return "AppVariant."+self.variant

    def get(self, key: str) -> Optional[str]:
        switcher = {
            "section": self.section,
            "element": self.element,
            "atom": self.atom,
            "variant": self.variant
        }
        return switcher.get(key, None)


@dataclass
class TextStyle(BaseStyle):
    fontName: str
    fontSize: float
    fontColor: Colour
    characterSpacing: float
    lineSpacing: float
    paragraphSpacing: float
    alignment: str
    textTransform: Optional[str]

    @staticmethod
    def create_from_sketch_dict(n: dict, default_font: str):
        text_style = n['value']['textStyle']['encodedAttributes']

        try:
            font_details = text_style['MSAttributedStringFontAttribute']['attributes']

            # Font name and color
            font_name = font_details.get('name', default_font)
            font_size = font_details['size']
            font_color = Colour.from_dict(text_style['MSAttributedStringColorAttribute'])

            # Paragraph details & other font details (kerning, spacing, )
            paragraph_details = text_style['paragraphStyle']
            alignment_names = ["left", "right", "center", "justified", "natural"]
            transform_names = [None, "uppercased", "lowercased"]
            character_spacing = text_style.get('kerning', 0)  # NSKern is not always there :-/
            line_spacing = paragraph_details.get('minimumLineHeight', 0)
            paragraph_spacing = paragraph_details.get('paragraphSpacing', 0)
            alignment = alignment_names[paragraph_details['alignment']]
            text_transform = transform_names[text_style.get('MSAttributedStringTextTransformAttribute', 0)]

            instance = TextStyle.create_from_name(n['name'], fontName=font_name, fontSize=font_size, fontColor=font_color,
                                                  characterSpacing=character_spacing, lineSpacing=line_spacing,
                                                  paragraphSpacing=paragraph_spacing, alignment=alignment, textTransform=text_transform)

            if instance.fontName is default_font:
                print("🚨 ERROR: missing font for style '" + instance.name + "'")

            # print(text_style)
        except KeyError as error:
            print("🚨 Missing required key {} on node {} so returning a default font".format(error, n['name']))
            print(text_style)
            instance = TextStyle.create_from_name(n['name'], fontName=default_font, fontSize=12, fontColor="#000000",
                                                  characterSpacing=0, lineSpacing=0,
                                                  paragraphSpacing=0, alignment=0)

        return instance


@dataclass
class LayerStyle(BaseStyle):
    color: Colour
    gradient: Optional[dict]
    outline: Optional[dict]
    image: Optional[dict]

    @staticmethod
    def create_from_sketch_dict(n: dict):
        fills = n['value'].get('fills', [])
        outlines = n['value'].get('borders', [])
        name = n['name']
        color_object = Colour.default()
        instance = LayerStyle.create_from_name(n['name'], color=color_object, gradient=None, image=None, outline=None)

        # TODO check fills[0].fillType
        #  - 0 is flat color
        #  - 1 is gradient
        #  - 4 is image fill (aka pattern fill)
        #  - 5 is noise fill
        # for gradient check fills[n].gradient.gradientType - 0 is linear, 1 is radial, 2 is angular

        # remove disable fills
        fills = [fill for fill in fills if fill["isEnabled"] == 1]

        # TODO loop through fills and find first where fills[n][isEnabled] == 1

        if fills:

            if len(fills) > 1:
                print("🚨WARNING🚨 '" + name + "' has more than 1 fill specified, only processing the first!!")

            fill = fills[0]

            # for gradient check fills[n].gradient.gradientType - 0 is linear, 1 is radial, 2 is angular
            if fill['fillType'] == 0:
                color = fill['color']
                color_object = Colour.from_dict(color)

            elif fill['fillType'] == 1:
                gradient = fill['gradient']
                # @TODO this should be 2 objects, but need to handle handlebars & polymorphism
                instance.gradient = {
                    'isAxial': False,
                    'isRadial': False,
                    'locations': [stop['position'] for stop in gradient['stops']],
                    'colors': [Colour.from_dict(stop['color']) for stop in gradient['stops']],
                    'from': Point.from_string(gradient['from']),
                    'to': Point.from_string(gradient['to'])
                }

                if gradient['gradientType'] == 0:
                    instance.gradient['isAxial'] = True

                elif gradient['gradientType'] == 1:
                    instance.gradient['isRadial'] = True

                else:
                    print("🚨WARNING🚨 '" + name + "' has unsupported gradient type (" + str(
                        gradient['gradientType']) + ")")
                    instance.gradient = None

            elif fill['fillType'] == 4:
                instance.image = {
                    "ref": fill['image']['_ref'],
                    "file_name": instance.safe_name,
                    "tile_scale": fill['patternTileScale'],
                    "fill_type": fill['patternFillType']
                }
                switcher = {
                    0: ("tile", "center"),
                    1: ("stretch", "resizeAspectFill"),
                    2: ("stretch", "resize"),
                    3: ("stretch", "resizeAspect")
                }
                default_gravity = "top"
                values = switcher.get(fill['patternFillType'], ("tile", default_gravity))
                instance.image["resizingMode"] = values[0]
                instance.image["gravity"] = values[1]
                if values[1] == default_gravity:
                    print("🚨WARNING🚨 '" + name + "' has image fill with unknown patternFillType (" + str(
                        fill['patternFillType']) + ")")

        else:
            print("🚨WARNING🚨 '" + name + "' has no fills specified, so returning default values!!")

        # remove disable outlines
        outlines = [outline for outline in outlines if outline["isEnabled"] == 1]

        if outlines:
            borderOptions = n['value'].get('borderOptions', None)
            dash_pattern = borderOptions['dashPattern'] if borderOptions else []

            color_outline_object = Colour.default()

            if len(outlines) > 1:
                print("🚨WARNING🚨 '" + name + "' has more than 1 border specified, only processing the first!!")
            outline = outlines[0]
            if outline['fillType'] == 0:
                color_outline = outline['color']
                color_outline_object = Colour.from_dict(color_outline)
            else:
                print("🚨WARNING🚨 outline'" + name + "' has the fill type '" + outline['fillType'] + "', this one isn't implemented!!")

            line_width = outline["thickness"]

            instance.outline = {
                "color": color_outline_object,
                "line_width": line_width,
                "dash_pattern": dash_pattern,
                "is_dash": len(dash_pattern) > 0
            }

        instance.color = color_object
        return instance

    @property
    def safe_name(self):
        return "layer_" + empty_str('*_', self.section, "", "_") \
               + empty_str('*_', self.element, "", "_") \
               + self.atom


def value_or_none(s: str) -> Optional[str]:
    return None if s is '*' else str(s).replace(".","_")


def value_or_default(value: Optional[str], default: str) -> str:
    return default if value is None else value


def unique_entries_dict(asset_list: [BaseStyle], key: str) -> [dict]:
    unique = set()
    unique_assets = [x.get(key) for x in asset_list
                     if (x.get(key) is not None) and not (x.get(key) in unique or unique.add(x.get(key)))]
    unique_assets.sort()
    return unique_assets
