import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { format } from 'date-fns';
import { addNewComment, getSongComments, deleteThisComment } from '../../store/comments';
import './styles/SongComments.css';

const Comments = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const currentSong = useSelector(state => state.song.currentSong);
  const currentLoggedInUser = useSelector(state => state.user.loggedInUser);

  const [userCommentBox, setUserCommentBox] = useState(true);
  const [songComments, setSongComments] = useState([]);
  const [comment, setComment] = useState('');
  const [deleteButton, setDeleteButton] = useState(false);
  const [errors, setErrors] = useState([]);

  useEffect(() => {
    (async () => {
      setSongComments(await dispatch(getSongComments(currentSong.id)));
    })();
  }, [dispatch, currentSong]);

  const commenting = () => {
    setUserCommentBox(false);
  };

  const doneCommenting = () => {
    setUserCommentBox(true);
  };

  const showDelete = () => {
    setDeleteButton(true);
  };

  const unShowDelete = () => {
    setDeleteButton(false);
  };

  const postComment = (e) => {
    e.preventDefault();
    setErrors([]);
    return dispatch(addNewComment({
      user_comment: comment,
      user_Id: currentLoggedInUser.id,
      song_Id: currentSong.id
    }))
      .then(() => setUserCommentBox(true))
      .then(() => history(`/songs/${currentSong.id}`))
      .catch((res) => {
        if (res.data && res.data.errors) setErrors(res.data.errors);
      });
  };

  const deleteUserComment = (commentId) => {
    setErrors([]);
    return dispatch(deleteThisComment({ commentId, songId: currentSong.id }))
      .then((res) => { setSongComments(res); })
      .then(() => { history(`/songs/${currentSong.id}`); })
      .catch((res) => {
        if (res.data && res.data.errors) setErrors(res.data.errors);
      });
  };

  return (
    <div className='comments_container'>
      {
        (userCommentBox)
          ? (
            <div className='comments-container_heading'>
              {
                  currentLoggedInUser && currentLoggedInUser.avatar
                    ? <img className='comments_header-default-avatar' src={currentLoggedInUser.avatar} alt='user avatar' />
                    : <div className='comments_header-default-avatar' />
                }
              <input placeholder='Add a comment' onClick={commenting} />
            </div>
            )
          : (
            <div className='comments-header_commenting'>
              <textarea
                type='text'
                autoFocus
                placeholder='Add a comment'
                onChange={(e) => setComment(e.target.value)}
              /> 
              <div className='comments-header_button-box'>
                <button type='submit' onClick={postComment} className='comments_submit-button'>Submit</button>
                <button type='button' onClick={doneCommenting} className='comments_cancel-button'>Cancel</button>
              </div>
            </div>
            )
      }
      <div className='comments-container_comments'>
        <ul>
          {songComments.map(comment => (
            <li className='solo-comment_container' key={comment.id}>
              <div className='solo-comment_header'>
                <div className='solo-comment_user'>{comment.username}</div>
                <div className='solo-comment_posted'>Posted {format(new Date(comment.created), "yyyy-MM-dd HH:mm")}</div>
              </div>
              <div className='solo-comment_comment'>
                <p>{comment.user_comment}</p>
              </div>
              <div className='solo-comment_buttons'>
                <div className='solo-comment_votes'>
                  <button className='comment-vote_icon-left'><i className='far fa-thumbs-up' /></button>
                  <div>+Votes</div>
                  <button className='comment-vote_icon-right fa-flip-horizontal'><i className='far fa-thumbs-down' /></button>
                </div>
                <div className='solo-comment-chevron'>
                  {
                    currentLoggedInUser && comment.user_Id === currentLoggedInUser.id
                      ? (
                        <div>
                          {
                            (deleteButton)
                              ? (
                                <div>
                                  <div>
                                    <button className='solo-comment_delete-button' type='button' onClick={unShowDelete}>
                                      <i className='fas fa-chevron-down' />
                                    </button>
                                  </div>
                                  <div className='solo-comments_transfer'>
                                    <button className='solo-comment_show-button' type='button' onClick={() => (deleteUserComment(comment.id))}>DELETE</button>
                                  </div>
                                </div>
                                )
                              : (
                                <div>
                                  <button className='solo-comment_delete-button' type='button' onClick={showDelete}>
                                    <i className='fas fa-chevron-down' />
                                  </button>
                                </div>
                                )
                          }
                        </div>
                        )
                      : (
                        <div />
                        )
                  }
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
      {/* <div className='comments_being-viewed'>
        <button>SHOW MORE (45)</button>
      </div> */}
    </div>
  );
};

export default Comments;
