import React, { forwardRef } from "react";
import { motion } from "framer-motion";

export const ButtonFlex = forwardRef<
  HTMLDivElement,
  {
    styles: React.CSSProperties;
    children: React.ReactNode[];
    custom: {
        hoverColor?: string,
        hoverBackColor?: string,
        hoverBorderWidth?: string,
        hoverBorderStyle?: string,
        hoverBorderColor?: string,
        duration?: number,
    };
    className?: string;
    id?: string;
  }
>((props, ref) => {

    const variants={
        whileHover:{
            color: props.custom.hoverColor,
            backgroundColor: props.custom.hoverBackColor,
            border: `${props.custom.hoverBorderWidth}px ${props.custom.hoverBorderStyle} ${props.custom.hoverBorderColor}`,
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

export default ButtonFlex;