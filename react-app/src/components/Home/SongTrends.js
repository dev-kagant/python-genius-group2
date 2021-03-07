import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllSongs } from '../../store/song.js';
import './styles/SongTrends.css';

function SongTrends () {
  const dispatch = useDispatch();
  const history = useHistory();
  const songs = useSelector((state) => Object.values(state.song.byId));

  useEffect(() => {
    dispatch(fetchAllSongs());
  }, [dispatch]);

  return (
    <div className='charts__list-wrapper'>
      {songs && songs.map((song, index = 1) =>
        <div className='song__outer-wrapper' key={song.id}>
          <div
            className='song__wrapper'
            onClick={() => history.push(`songs/${song.id}`)}
          >
            <div className='song__index'>{index + 1}</div>
            <div className='song__cover-wrapper'>
              {song.song_icon
                ? <img className='song__cover' src={song.song_icon} alt={song.title} />
                : <div className='song__default-cover' />}
            </div>
            <div className='song__text-info'>
              <div className='song__title'>{song.title}</div>
              <div className='song__artist'>{song.artist}</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default SongTrends;
