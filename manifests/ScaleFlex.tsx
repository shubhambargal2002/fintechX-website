import React, { forwardRef } from "react";
import { motion } from "framer-motion";

export const ScaleFlex = forwardRef<
  HTMLDivElement,
  {
    styles: React.CSSProperties;
    children: React.ReactNode[];
    custom: {
        hoverScale?: number,
        duration?: number,
        hoverColor?: string,
        hoverBackColor?: string
    };
    className?: string;
    id?: string;
  }
>((props, ref) => {

    const variants={
        whileHover:{
            scale: props.custom.hoverScale,
            color: props.custom.hoverColor,
            backgroundColor: props.custom.hoverBackColor,
            transition:{
                duration: props.custom.duration,
            }
        }
    }
  
  return (
    <motion.div
      ref={ref}
      style={{ ...props.styles, display: "flex", position: "relative" }}
      id={props.id}
      className={props.className}
      variants={variants}
      whileHover="whileHover"
    >
      {props.children}
    </motion.div>
  );
});

export default ScaleFlex;