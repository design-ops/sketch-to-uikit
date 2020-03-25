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

        // first section / element / atom// (not present)
        //
        // then element / atom (aka * / element / atom)// (not present)
        //
        // then section / * / atom// (not present)
        //
        // finally just atom

        if atom == "centerBottom" {

// *//centerBottom - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / center
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .center, textTransform: .lowercased, variants: [])

        }

        if atom == "centerMiddle" {

// *//centerMiddle - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / center
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .center, textTransform: .uppercased, variants: [])

        }

        if atom == "centerTop" {

// *//centerTop - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / center
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .center, variants: [])

        }

        if atom == "leftBottom" {

// *//leftBottom - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / left
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .left, textTransform: .lowercased, variants: [])

        }

        if atom == "leftMiddle" {

// *//leftMiddle - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / left
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .left, textTransform: .uppercased, variants: [])

        }

        if atom == "leftTop" {

// *//leftTop - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / left
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .left, variants: [])

        }

        if atom == "rightBottom" {

// *//rightBottom - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / right
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .right, textTransform: .lowercased, variants: [])

        }

        if atom == "rightMiddle" {

// *//rightMiddle - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / right
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .right, textTransform: .uppercased, variants: [])

        }

        if atom == "rightTop" {

// *//rightTop - font is SanFranciscoDisplay-Regular / 15 / UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) / right
return styleFrom(name: "SanFranciscoDisplay-Regular", size: 15, textColor: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), lineSpacing: 22, letterSpacing: 1, textAlignment: .right, variants: [])

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
