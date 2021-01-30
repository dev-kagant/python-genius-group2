import React from "react";

import "./Annotation.css";

const Annotation = ({ lyrics, range, setShowAnnotation }) => {
    

    const onSave = () => {
        setShowAnnotation(false);
    }

    return (
        <div className="annotation_container">
            <div className="annotation_lyrics">{lyrics}</div>
            <form onSubmit={onSave}>
                <textarea 
                    className="annotation_input"
                    placeholder="Add your annotations"
                    // value={}
                />
                <button type="submit">Save</button>
                <button 
                    type="button"
                    onClick={() => setShowAnnotation(false)}
                >Cancel</button>
            </form>
        </div>
    )
}

export default Annotation;