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
			transition: { duration: props.custom.duration},
			width: `${props.custom.initialWidth}%`,
		},
		mouseenter: {
			backgroundColor: props.custom.hoverColor,
			transition: { duration: props.custom.duration},
			width: `${props.custom.hoverWidth}%`,
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
				style={{ height: `${props.custom.height}px` }}
			></motion.div>
		</div>
	);
});

export default LineText;