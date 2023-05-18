import { createComponentManifest } from "@atrilabs/utils";

export default createComponentManifest({
	name: "ButtonFlex",
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
        hoverColor: { type: "color" },
        hoverBackColor: { type: "color" },
        hoverBorderWidth: { type: "number" },
        hoverBorderStyle: { type: "text" },
        hoverBorderColor: { type: "color" },
        duration: { type: "number" },
	},

	initalCustomValues: {
        hoverColor: "",
        hoverBackColor: "",
        hoverBorderWidth: "",
        hoverBorderStyle: "",
        hoverBorderColor: "",
        duration: 0,
	},
});