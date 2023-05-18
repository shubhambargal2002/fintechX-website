import ScaleFlex from "./ScaleFlex";
import React from "react";

const DevScaleFlex: typeof ScaleFlex =
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
			<ScaleFlex
				ref={ref}
				{...props}
				styles={overrideStyles}
			/>
		);
	});

export default DevScaleFlex;