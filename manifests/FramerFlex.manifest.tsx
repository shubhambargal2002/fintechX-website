import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "FramerFlex",
	acceptsChild: "flex",
    styles:{
        boxShadowOptions: true,
        flexContainerOptions: true,
        flexChildOptions: true,
        positionOptions: true,
        typographyOptions: true,
        spacingOptions: true,
        sizeOptions: true,
        borderOptions: true,
        outlineOptions: true,
        backgroundOptions: true,
        miscellaneousOptions: true,
    },

	custom: {
        duration: { type: "number" },
        delay: { type: "number" }
	},

	initalCustomValues: {
        duration: 0,
        delay: 0
	},
});