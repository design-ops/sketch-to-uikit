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
        // first section / element / atom// (not present)
        //
        // then element / atom (aka * / element / atom)// (not present)
        //
        // then section / * / atom// (not present)
        //
        // finally just atom
        if atom == "angularGradient" {

// */*/angularGradient
let fill = FlatLayerFill(color: UIColor(red: 0, green: 0, blue: 0, alpha: 0))

return LayerStyle(fill: fill)
        }
        if atom == "dashedOutline" {

// */*/dashedOutline
let fill = FlatLayerFill(color: UIColor(red: 0.774994338768116, green: 0.774994338768116, blue: 0.774994338768116, alpha: 1.0))
// Linear outline
let outline = DashedLayerOutline(color: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), width: 1, lineDashPattern: [5])

return LayerStyle(fill: fill, outline: outline)
        }
        if atom == "flatColor" {

// */*/flatColor
let fill = FlatLayerFill(color: UIColor(red: 0.7669536564625851, green: 0.1353305220841493, blue: 0.1353305220841493, alpha: 1.0))

return LayerStyle(fill: fill)
        }
        if atom == "linearGradient" {

// */*/linearGradient
let locations: [Double] = [0,1,]
// Axial (Linear) Gradient
let direction = GradientLayerFill.Direction(start: CGPoint(x: 0.5, y: 0.0), end: CGPoint(x: 0.5, y: 1.0))
let style = GradientLayerFill.Style.axial(direction: direction, locations: locations)
let colors = [UIColor(red: 0.8916280506641954, green: 0.2812364847457446, blue: 0.2812364847457446, alpha: 1.0),UIColor(red: 0.3298522534013605, green: 0.02545083970669037, blue: 0.02545083970669037, alpha: 1.0),]
let fill = GradientLayerFill(colors: colors, style: style)


return LayerStyle(fill: fill)
        }
        if atom == "noiseFill" {

// */*/noiseFill
let fill = ImageLayerFill(image: UIImage(named: "layer_*_*_noiseFill")!, resizingMode: .tile, gravity: .center) /* tile_scale=1 fill_type=0  */


return LayerStyle(fill: fill)
        }
        if atom == "patternFill_Fill" {

// */*/patternFill_Fill
let fill = ImageLayerFill(image: UIImage(named: "layer_*_*_patternFill_Fill")!, resizingMode: .stretch, gravity: .resizeAspectFill) /* tile_scale=1 fill_type=1  */


return LayerStyle(fill: fill)
        }
        if atom == "patternFill_Fit" {

// */*/patternFill_Fit
let fill = ImageLayerFill(image: UIImage(named: "layer_*_*_patternFill_Fit")!, resizingMode: .stretch, gravity: .resizeAspect) /* tile_scale=1 fill_type=3  */


return LayerStyle(fill: fill)
        }
        if atom == "patternFill_Stretch" {

// */*/patternFill_Stretch
let fill = ImageLayerFill(image: UIImage(named: "layer_*_*_patternFill_Stretch")!, resizingMode: .stretch, gravity: .resize) /* tile_scale=1 fill_type=2  */


return LayerStyle(fill: fill)
        }
        if atom == "patternFill_Tile" {

// */*/patternFill_Tile
let fill = ImageLayerFill(image: UIImage(named: "layer_*_*_patternFill_Tile")!, resizingMode: .tile, gravity: .center) /* tile_scale=1 fill_type=0  */


return LayerStyle(fill: fill)
        }
        if atom == "radialGradient" {

// */*/radialGradient
let locations: [Double] = [0,1,]
// Radial Gradient
let center = CGPoint(x: 0.5, y: 0.53427734375)
let style = GradientLayerFill.Style.radial(center: center, locations: locations)
let colors = [UIColor(red: 0.8916280506641954, green: 0.2812364847457446, blue: 0.2812364847457446, alpha: 1.0),UIColor(red: 0.3298522534013605, green: 0.02545083970669037, blue: 0.02545083970669037, alpha: 1.0),]
let fill = GradientLayerFill(colors: colors, style: style)


return LayerStyle(fill: fill)
        }
        if atom == "solidOutline_Inside" {

// */*/solidOutline_Inside
let fill = FlatLayerFill(color: UIColor(red: 0.774994338768116, green: 0.774994338768116, blue: 0.774994338768116, alpha: 1.0))
// Linear outline
let outline = LinearLayerOutline(color: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), width: 1)

return LayerStyle(fill: fill, outline: outline)
        }
        if atom == "solidOutline_Outside" {

// */*/solidOutline_Outside
let fill = FlatLayerFill(color: UIColor(red: 0.774994338768116, green: 0.774994338768116, blue: 0.774994338768116, alpha: 1.0))
// Linear outline
let outline = LinearLayerOutline(color: UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0), width: 1)

return LayerStyle(fill: fill, outline: outline)
        }
        print("[Stylist:layerStyle] failed to find asset for \(atom) for element '\(element?.name ?? "nil")' in section '\(section?.name ?? "nil")'")

        // return a very visually obvious default...
        return LayerStyle(fill: FlatLayerFill(color: .cyan))

    }
}