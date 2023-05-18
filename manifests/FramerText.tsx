import React, { forwardRef } from "react";
import { motion } from "framer-motion";

export const FramerText = forwardRef<
  HTMLDivElement,
  {
    styles: React.CSSProperties;
    children: React.ReactNode[];
    custom: {
        text?: string;
        hoverColor?: string,
    };
    className?: string;
    id?: string;
  }
>((props, ref) => {

    const variants={
        whileHover:{
            color: props.custom.hoverColor,
        }
    }
  
  return (
    <motion.div
      ref={ref}
      style={{ ...props.styles }}
      id={props.id}
      className={props.className}
      variants={variants}
      whileHover="whileHover"
    >
      {props.custom.text}
    </motion.div>
  );
});

export default FramerText;