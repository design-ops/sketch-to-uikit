//
//  Stylist+layerStyles.swift
//
//  WARNING THIS FILE IS GENERATED *DO NOT* EDIT
//

// swiftlint:disable all

import Foundation
import StylableUIKit

extension Stylist {

    public func layerStyle(_ style: StylistLayerStyle, element: StylistElement?, section: StylistSection?) -> LayerStyle {

        let atom = style.name
        // first section / element / atom
        if let sectionName = section?.name, let elementName = element?.name {

            if atom == "layerStyle" && elementName == "*" && sectionName == "section" {
var variants: [BasicLayerStyle] = []
_ = {
// section/*[selected]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.3607843137254902, green: 0.5333333333333333, blue: 0.7058823529411765, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.selected))
}() 
_ = {
// section/*[disabled]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.2705882352941176, green: 0.4, blue: 0.5294117647058824, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.disabled))
}() 
// section/*[normal]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.4549019607843137, green: 0.6705882352941176, blue: 0.8862745098039215, alpha: 1.0))

return LayerStyle(fill: fill, variants: variants)
            }
            if atom == "layerStyle" && elementName == "element" && sectionName == "section" {
var variants: [BasicLayerStyle] = []
_ = {
// section/element[selected]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.07450980392156861, green: 0.3176470588235297, blue: 0.5647058823529412, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.selected))
}() 
_ = {
// section/element[disabled]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.05490196078431368, green: 0.2392156862745098, blue: 0.4235294117647059, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.disabled))
}() 
// section/element[normal]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.0922628715634346, green: 0.4017830491065979, blue: 0.7071372270584106, alpha: 1.0))

return LayerStyle(fill: fill, variants: variants)
            }
        }

        //
        // then element / atom (aka * / element / atom)
        if let elementName = element?.name {

            if atom == "layerStyle" && elementName == "*" {
var variants: [BasicLayerStyle] = []
_ = {
// */*[selected]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.5568627450980392, green: 0.6627450980392158, blue: 0.7686274509803922, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.selected))
}() 
_ = {
// */*[disabled]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.4156862745098039, green: 0.4980392156862745, blue: 0.5764705882352941, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.disabled))
}() 
// */*[normal]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.6980392156862745, green: 0.8313725490196078, blue: 0.9607843137254902, alpha: 1.0))

return LayerStyle(fill: fill, variants: variants)
            }
            if atom == "layerStyle" && elementName == "element" {
var variants: [BasicLayerStyle] = []
_ = {
// */element[selected]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.1686274509803922, green: 0.3921568627450981, blue: 0.611764705882353, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.selected))
}() 
_ = {
// */element[disabled]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.1254901960784314, green: 0.2941176470588235, blue: 0.4588235294117647, alpha: 1.0))

variants.append(BasicLayerStyle(fill: fill, variantType: UIControl.State.disabled))
}() 
// */element[normal]/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.2117647058823529, green: 0.4901960784313726, blue: 0.7686274509803922, alpha: 1.0))

return LayerStyle(fill: fill, variants: variants)
            }
        }

        //
        // then section / * / atom
        if let sectionName = section?.name {

            if atom == "layerStyle" && sectionName == "section" {

// section/*/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.4549019607843137, green: 0.6705882352941176, blue: 0.8862745098039215, alpha: 1.0))

return LayerStyle(fill: fill)
            }
        }

        //
        // finally just atom
        if atom == "layerStyle" {

// */*/layerStyle
let fill = FlatLayerFill(color: UIColor(red: 0.6980392156862745, green: 0.8313725490196078, blue: 0.9607843137254902, alpha: 1.0))

return LayerStyle(fill: fill)
        }
        print("[Stylist:layerStyle] failed to find asset for \(atom) for element '\(element?.name ?? "nil")' in section '\(section?.name ?? "nil")'")

        // return a very visually obvious default...
        return LayerStyle(fill: FlatLayerFill(color: .cyan))

    }
}