import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { editAnnotation, deleteAnnotation } from "../../store/annotation";
import "./styles/Annotation.css";
import "./styles/EditAnnotation.css";

const EditAnnotation = ({ setShowEditAnnotation }) => {
    const dispatch = useDispatch();
    const song = useSelector(state => state.song.currentSong);
    const currentAnnotation = useSelector(state => state.annotation.currentAnnotation);
    const loggedInUser = useSelector(state => state.user.loggedInUser);
    const [error, setErrors] = useState(null);
    const [loaded, setLoaded] = useState(false);
    const [input, setInput] = useState("");


    useEffect(() => {
        if (!currentAnnotation) return;
        setInput(currentAnnotation.annotation);
        setLoaded(true);
    }, [currentAnnotation])


    // Edit annotation
    const onSave = async (e) => {
        e.preventDefault();
        const editedAnnotation = input;
        const annoId = currentAnnotation.id;

        const res = await dispatch(editAnnotation(editedAnnotation, annoId))
        if (res.ok) {
            setShowEditAnnotation(false);
        } else {
            const data = await res.json();
            setErrors(data);
        }
    }


    // Delete annotation
    const onDelete = async () => {
        const annoId = currentAnnotation.id;
        await dispatch(deleteAnnotation(currentAnnotation.id))
        setShowEditAnnotation(false)
        document.location.reload();
    }

    if (!loaded) return null;

    return (
        <div className="annotation_container">
            {currentAnnotation && <div className="annotation_lyrics">{currentAnnotation.lyrics}</div>}
            {error && (<div>{error}</div>)}
            <form className="annotation_form" onSubmit={onSave}>
                <textarea
                    className="annotation_input"
                    placeholder="Add your annotations"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                />
                {loggedInUser && (
                    <>
                        <button type="submit">Save</button>
                        <button
                            type="button"
                            onClick={() => setShowEditAnnotation(false)}
                        >Cancel</button>
                        {currentAnnotation && loggedInUser.id == currentAnnotation.user_Id && <button type="button" onClick={onDelete}>Delete</button>}
                    </>
                )}
                {!loggedInUser && <button onClick={() => setShowEditAnnotation(false)}>Close</button>}

            </form>
        </div>
    )
}

export default EditAnnotation;
