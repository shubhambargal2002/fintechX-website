import React, { useCallback } from "react";
import { motion, useAnimationControls } from "framer-motion";

const LineText = React.forwardRef<
	HTMLDivElement,
	{
        styles: React.CSSProperties;
		custom: {
            text?: string;
			hoverColor?: string;
			nonHoverColor?: string;
			height?: number;
			initialWidth?: number,
			hoverWidth?: number,
			bottomPadding?: number,
			duration?: number;
		};
        className?: string;
		id?: string;
	}
>((props, ref) => {
	const textVariants = {
		mouseleave: { color: props.custom.nonHoverColor },
		mouseenter: {
			color: props.custom.hoverColor ,
		},
	};
	const underlineVariants = {
		mouseleave: {
			backgroundColor: props.custom.nonHoverColor,
			width: `${props.custom.initialWidth}%`,
			transition: { duration: props.custom.duration},
		},
		mouseenter: {
			backgroundColor: props.custom.hoverColor,
			width: `${props.custom.hoverWidth}%`,
			transition: { duration: props.custom.duration},
		},
	};
	const controls = useAnimationControls();
	const onMouseEnter = useCallback((e: React.MouseEvent) => {
		controls.start("mouseenter");
	}, []);
	const onMouseLeave = useCallback((e: React.MouseEvent) => {
		controls.start("mouseleave");
	}, []);
	return (
		<div ref={ref} className={props.className} id={props.id} style={props.styles} onMouseEnter={onMouseEnter} onMouseLeave={onMouseLeave}>
			<motion.div
			    style={{paddingBottom: `${props.custom.bottomPadding}px`}}
				animate={controls}
				variants={textVariants}
				initial={"mouseleave"}
			>
				{props.custom.text}
			</motion.div>
			<motion.div
				animate={controls}
				variants={underlineVariants}
				initial={"mouseleave"}
				style={{ height: `${props.custom.height}px`}}
			></motion.div>
		</div>
	);
});

export default LineText;