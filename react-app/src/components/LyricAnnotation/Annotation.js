import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { postAnnotation } from "../../store/annotation";
import "./Annotation.css";

const Annotation = ({ lyrics, range, setShowAnnotation }) => {
    const dispatch = useDispatch();
    const song = useSelector(state => state.song.currentSong);
    const [error, setErrors] = useState(null);
    const [input, setInput] = useState("");


    // Submit Event Handler
    const onSave = async (e) => {
        e.preventDefault();

        const song_Id = song.id;
        const annotation = input;
        const start = range.startOffset;
        const end = range.endOffset;

        const res = await dispatch(postAnnotation(song_Id, annotation, start, end))
        
        if (res.ok) {
            setShowAnnotation(false);
        } else {
            const data = await res.json();
            setErrors(data);
        }
    }

    return (
        <div className="annotation_container">
            <div className="annotation_lyrics">{lyrics}</div>
            {error && (<div>{error}</div>)}
            <form onSubmit={onSave}>
                <textarea 
                    className="annotation_input"
                    placeholder="Add your annotations"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
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