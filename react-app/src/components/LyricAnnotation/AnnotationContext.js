import React, { useContext, useRef, useState, useEffect } from 'react';
import ReactDOM from 'react-dom';

export const AnnotationContext = React.createContext();

export const AnnotationContextProvider = ({ children }) => {
    const annotationRef = useRef();

    const [value, setValue] = useState();

    useEffect(() => {
        setValue(annotationRef.current);
    }, []);

    return (
        <>
            <AnnotationContext.Provider value={value}>
                {children}
            </AnnotationContext.Provider>
            <span ref={annotationRef}></span>
        </>
    )
}
