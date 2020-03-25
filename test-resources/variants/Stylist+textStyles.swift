//
//  Stylist+textStyles.swift
//
//  WARNING THIS FILE IS GENERATED *DO NOT* EDIT
//

// swiftlint:disable all

import UIKit
import StylableUIKit

extension Stylist {

    public func textStyle(_ style: StylistTextStyle, element: StylistElement? = nil, section: StylistSection? = nil) -> TextStyle {
        let atom = style.name

        // first section / element / atom
        if let sectionName = section?.name, let elementName = element?.name {

            if atom == "textStyle" && elementName == "*" && sectionName == "section" {
var variants: [BasicTextStyle] = []
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.3607843137254902, green: 0.5333333333333333, blue: 0.7058823529411765, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.selected)
    variants.append(item)
}() 
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.2705882352941176, green: 0.4, blue: 0.5294117647058824, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.disabled)
    variants.append(item)
}() 
// */*/textStyle - font is SFUIDisplay-Regular / 20 / UIColor(red: 0.4549019607843137, green: 0.6705882352941176, blue: 0.8862745098039215, alpha: 1.0) / left
return styleFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.4549019607843137, green: 0.6705882352941176, blue: 0.8862745098039215, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variants: variants)

            }
            if atom == "textStyle" && elementName == "element" && sectionName == "section" {
var variants: [BasicTextStyle] = []
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.07450980392156861, green: 0.3176470588235297, blue: 0.5647058823529412, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.selected)
    variants.append(item)
}() 
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.05490196078431368, green: 0.2392156862745098, blue: 0.4235294117647059, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.disabled)
    variants.append(item)
}() 
// */element/textStyle - font is SFUIDisplay-Regular / 20 / UIColor(red: 0.09411764705882351, green: 0.4, blue: 0.7058823529411765, alpha: 1.0) / left
return styleFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.09411764705882351, green: 0.4, blue: 0.7058823529411765, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variants: variants)

            }
        }

        //
        // then element / atom (aka * / element / atom)
        if let elementName = element?.name {

            if atom == "textStyle" && elementName == "*" {
var variants: [BasicTextStyle] = []
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.5568627450980392, green: 0.6627450980392158, blue: 0.7686274509803922, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.selected)
    variants.append(item)
}() 
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.4156862745098039, green: 0.4980392156862745, blue: 0.5764705882352941, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.disabled)
    variants.append(item)
}() 
// */*/textStyle - font is SFUIDisplay-Regular / 20 / UIColor(red: 0.6980392156862745, green: 0.8313725490196078, blue: 0.9607843137254902, alpha: 1.0) / left
return styleFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.6980392156862745, green: 0.8313725490196078, blue: 0.9607843137254902, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variants: variants)

            }
            if atom == "textStyle" && elementName == "element" {
var variants: [BasicTextStyle] = []
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.2117647058823529, green: 0.4901960784313726, blue: 0.7686274509803922, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.selected)
    variants.append(item)
}() 
_ = {
    let item = basicFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.1254901960784314, green: 0.2941176470588235, blue: 0.4588235294117647, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variantType: UIControl.State.disabled)
    variants.append(item)
}() 
// */element/textStyle - font is SFUIDisplay-Regular / 20 / UIColor(red: 0.2117647058823529, green: 0.4901960784313726, blue: 0.7686274509803922, alpha: 1.0) / left
return styleFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.2117647058823529, green: 0.4901960784313726, blue: 0.7686274509803922, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variants: variants)

            }
        }

        //
        // then section / * / atom
        if let sectionName = section?.name {

            if atom == "textStyle" && sectionName == "section" {

// *//textStyle - font is SFUIDisplay-Regular / 20 / UIColor(red: 0.4549019607843137, green: 0.6705882352941176, blue: 0.8862745098039215, alpha: 1.0) / left
return styleFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.4549019607843137, green: 0.6705882352941176, blue: 0.8862745098039215, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variants: [])

            }
        }

        //
        // finally just atom

        if atom == "textStyle" {

// *//textStyle - font is SFUIDisplay-Regular / 20 / UIColor(red: 0.6980392156862745, green: 0.8313725490196078, blue: 0.9607843137254902, alpha: 1.0) / left
return styleFrom(name: "SFUIDisplay-Regular", size: 20, textColor: UIColor(red: 0.6980392156862745, green: 0.8313725490196078, blue: 0.9607843137254902, alpha: 1.0), lineSpacing: 0, letterSpacing: 0, textAlignment: .left, variants: [])

        }
        print("[Stylist:textStyle] failed to find asset for \(atom) for element '\(element?.name ?? "nil")' in section '\(section?.name ?? "nil")'")

        // return a very visually obvious default...
        return TextStyle(font: fontOrDefault(name: "Papyrus", size: 12), textColor: .cyan)

    }

}

fileprivate func basicFrom(name: String, size: CGFloat, textColor: UIColor, lineSpacing: CGFloat, letterSpacing: CGFloat,
                                textAlignment: NSTextAlignment, textTransform: TextTransform = .none,
                                variantType: StylistVariant = UIControl.State.normal) -> BasicTextStyle {
    let font = fontOrDefault(name: name, size: size)
    let actualLineSpacing: CGFloat = {
        if lineSpacing > 0 {
            return lineSpacing - font.lineHeight
        }
        return lineSpacing
    }()

    return BasicTextStyle(font: font, textColor: textColor, lineSpacing: actualLineSpacing, letterSpacing: letterSpacing,
                          textAlignment: textAlignment, textTransform: textTransform, variantType: variantType)
}

fileprivate func styleFrom(name: String, size: CGFloat, textColor: UIColor, lineSpacing: CGFloat, letterSpacing: CGFloat,
                            textAlignment: NSTextAlignment, textTransform: TextTransform = .none,
                            variantType: StylistVariant = UIControl.State.normal, variants: [BasicTextStyle]) -> TextStyle {
    let font = fontOrDefault(name: name, size: size)
    let actualLineSpacing: CGFloat = {
        if lineSpacing > 0 {
            return lineSpacing - font.lineHeight
        }
        return lineSpacing
    }()

    return TextStyle(font: font, textColor: textColor, lineSpacing: actualLineSpacing, letterSpacing: letterSpacing,
                     textAlignment: textAlignment, textTransform: textTransform, variantType: variantType, variants: variants)
}



fileprivate func fontOrDefault(name: String, size: CGFloat) -> UIFont {
    guard let font = UIFont(name: name, size: size) else {
        print("🚨🚨 Font requested, but missing '\(name)'")
        return UIFont(name: "Papyrus", size: size)!
    }
    return font
}
