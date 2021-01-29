import React, { useState } from 'react';
import { useSelector, useDispatch } from "react-redux";

import './Annotations.css';

const handleHighlight = (event) => {
    console.log(`Selected text: ${window.getSelection().toString()}`);

    // encode selected text
    const selection = encodeURIComponent(window.getSelection().toString()).replace(/[!'()*]/g, escape);

    // find out how far user has scrolled
    var scrollTop = (window.pageYOffset !== undefined) ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;

    // selected position
    // const posX = event.clientX - 100;
    // const posY = event.clientY + 20 + scrollTop;

}

const Annotations = () => {
    if (handleHighlight()) {
        return (
            <div className='text-container'>
                <textarea name='annotation'></textarea>
            </div>
        )
    }
}

export default Annotations;