import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "LineText",
    styles : {
        boxShadowOptions: true,
        flexContainerOptions: false,
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
        text: {type: 'text'},
		hoverColor: { type: "color" },
		nonHoverColor: { type: "color" },
		height: { type: "number" },
        initialWidth: { type: "number" },
        hoverWidth: { type: "number" },
		duration: { type: "number" },
	},

    initalCustomValues:{
        text: "Text",
        hoverColor: "",
        nonHoverColor: "",
        height: 0,
        initialWidth: 0,
        hoverWidth: 0,
        duration: 0
    }
});