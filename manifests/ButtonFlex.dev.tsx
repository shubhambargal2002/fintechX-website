import ButtonFlex from "./ButtonFlex";
import React from "react";

const DevButtonFlex: typeof ButtonFlex =
	React.forwardRef((props, ref) => {
		const overrideStyles =
			props.children.length === 0
				? {
						height: "100px",
						border: "1px dashed red",
                        minWidth: "100px"
				  }
				: props.styles;
		return (
			<ButtonFlex
				ref={ref}
				{...props}
				styles={overrideStyles}
			/>
		);
	});

export default DevButtonFlex;