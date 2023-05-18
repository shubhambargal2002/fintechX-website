import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "ScaleFlex",
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
        hoverScale: { type: "number" },
        duration: { type: "number" },
        hoverColor: { type: "color" },
        hoverBackColor: { type: "color" }
	},

	initalCustomValues: {
        hoverScale: 0,
        duration: 0,
        hoverColor: "",
        hoverBackColor: ""
	},
});