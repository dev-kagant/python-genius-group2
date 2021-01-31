import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { postAnnotation } from "../../store/annotation";
import "./styles/Annotation.css";

const Annotation = ({ selectedlyrics, range, setShowAnnotation }) => {
    const dispatch = useDispatch();
    const song = useSelector(state => state.song.currentSong);
    const [errors, setErrors] = useState(null);
    const [input, setInput] = useState("");

    // Submit Event Handler
    const onSave = async (e) => {
        // e.preventDefault();
        const newAnnotation = {
            song_Id: song.id,
            annotation: input,
            start: range.startOffset,
            end: range.endOffset,
            lyrics: selectedlyrics
        }
        const res = await dispatch(postAnnotation(newAnnotation))
        if (res.ok) {
            setShowAnnotation(false)
        } else {
            const data = await res.json();
            setErrors(data);
        }
    }

    return (
        <div className="annotation_container">
            <div className="annotation_lyrics">{selectedlyrics}</div>
            {errors && <div>{errors}</div>}
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