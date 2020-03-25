//
//  Stylist+animatedAsset.swift
//
//  WARNING THIS FILE IS GENERATED *DO NOT* EDIT
//

import UIKit
import StylableUIKit

extension Stylist {

    public func animatedAsset(_ identifier: StylistAsset, element: StylistElement? = nil, section: StylistSection? = nil) -> StylistAnimatedAsset? {
        let name = identifier.name

        #if STYLABLE_SUPPORTS_LOTTIE
        if let animatedView = name.asLottieAnimationView() {
            animatedView.playLooped()
            return animatedView
        }
        #endif

        if let asset = self.asset(identifier, element: element, section: section) {
            return UIImageView(image: asset.image)
        }

        // failed to get either animation or asset
        return nil
    }
}
