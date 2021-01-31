import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router-dom"
import { addNewComment, getSongComments } from "../../store/comments";
import "./styles/SongComments.css";

const Comments = () => {
    const dispatch = useDispatch();
    const history = useHistory();
    const currentSong = useSelector(state => state.song.currentSong);
    const currentLoggedInUser = useSelector(state => state.user.loggedInUser);

    const [userCommentBox, setUserCommentBox] = useState(true);
    const [songComments, setSongComments] = useState([]);
    const [comment, setComment] = useState("");
    const [errors, setErrors] = useState([]);

    useEffect(async () => {
        setSongComments(await dispatch(getSongComments(currentSong.id)))
    }, [dispatch])

    const commenting = () => {
        setUserCommentBox(false)
    }
    const doneCommenting = () => {
        setUserCommentBox(true)
    }

    const postComment = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(addNewComment({
            user_comment: comment,
            user_Id: currentLoggedInUser.id,
            song_Id: currentSong.id,
        }))
            .then(() => setUserCommentBox(true))
            .then(() => history(`/songs/${currentSong.id}`))
            .catch((res) => {
                if (res.data && res.data.errors) setErrors(res.data.errors);
            })
    }

    return (
        <div className="comments_container">
            {(userCommentBox) ? (<div className="comments-container_heading">
                { currentLoggedInUser.avatar ?
                    <img src={currentLoggedInUser.avatar} /> :
                    <div className="comments_header-default-avatar" />
                }
                <input
                    placeholder="Add a comment"
                    onClick={commenting}
                />
            </div>) : (
                    <div className="comments-header_commenting">
                        <textarea
                            type="text"
                            placeholder="Add a comment"
                            onChange={(e) => setComment(e.target.value)}
                        />
                        <div className="comments-header_button-box">
                            <button type="submit" onClick={postComment} className="comments_submit-button">Submit</button>
                            <button type="button" onClick={doneCommenting} className="comments_cancel-button">Cancel</button>
                        </div>
                    </div>)}
            <div className="comments-container_comments">
                <ul>
                    {songComments.map(comment => (
                        <li className="solo-comment_container">
                            <div className="solo-comment_header">
                                <div className="solo-comment_user">{currentLoggedInUser.username}</div>
                                <div className="solo-comment_posted">Posted {comment.created}</div>
                            </div>
                            <div className="solo-comment_comment">
                                <p>{comment.user_comment}</p>
                            </div>
                            <div className="solo-comment_votes">
                                <button className="comment-vote_icon-left"><i class="far fa-thumbs-up"></i></button>
                                <div>+Votes</div>
                                <button className="comment-vote_icon-right fa-flip-horizontal"><i class="far fa-thumbs-down"></i></button>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
            <div className="comments_being-viewed">
                <button>SHOW MORE (45)</button>
            </div>
        </div >
    )
}

export default Comments;
