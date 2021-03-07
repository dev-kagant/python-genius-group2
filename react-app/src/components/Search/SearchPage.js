import React from 'react';
import { useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import './styles/search.css';

function SearchPage () {
  const history = useHistory();

  const songs = useSelector(state => state.search.song);
  const artists = useSelector(state => state.search.artist);
  const lyrics = useSelector(state => state.search.lyrics);

  return (
    <div className='search-page__container'>
      <div className='search-page__heading'>ALL RESULTS</div>
      <div className='search-page__top'>
        <div className='search-page__songs-session-wrapper'>
          <div className='search-page__songs-heading'>SONGS</div>
          <div className='search-page__songs-wrapper'>
            {songs && songs.map((song) => (
              <div
                className='search-page__individual search-page__song-wrapper'
                key={song.id}
                onClick={() => history.push(`songs/${song.id}`)}
              >
                {
                song.song_icon
                  ? <img className='search-page__song-cover' src={song.song_icon} alt={song.title} />
                  : <div className='search-page__default-song-cover' />

              }
                <div className='search-page__song-text-info'>
                  <div className='search-page__song-title'>{song.title}</div>
                  <div className='search-page__song-artist'>{song.artist}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
        <div className='search-page__artists-session-wrapper'>
          <div className='search-page__artists-heading'>ARTISTS</div>
          <div className='search-page__artists-wrapper'>
            {artists && artists.map((artist) => (
              <div
                className='search-page__individual search-page__artist-wrapper'
                key={artist.artist}
                onClick={() => history.push(`songs/${artist.id}`)}
              >
                {
                artist.song_icon
                  ? <img className='search-page__artist-cover' src={artist.song_icon} alt={artist.id} />
                  : <div className='search-page__artist-default-cover' />
              }
                <div className='search-page__artist-name'>{artist.artist}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
      <div className='search-page__bottom'>
        <div className='search-page__lyrics-session-wrapper'>
          <div className='search-page__lyrics-heading'>LYRIC MATCHES</div>
          <div className='search-page__lyrics-wrapper'>
            {lyrics && lyrics.map((lyric) => (
              <div
                className='search-page__individual search-page__lyric-wrapper'
                key={lyric.lyrics}
                onClick={() => history.push(`songs/${lyric.id}`)}
              >
                {
                  lyric.song_icon
                    ? <img className='search-page__lyric-cover' src={lyric.song_icon} alt='song cover' />
                    : <div className='search-page__default-lyric-cover' />
                }
                <div className='search-page__lyric-album-info'>
                  <div className='search-page__lyric-title'>{lyric.title}</div>
                  <div className='search-page__lyric-artist'>{lyric.artist}</div>
                  <div className='search-page__lyric-album-name'>{lyric.album}</div>
                </div>
                <div className='search-page__lyric'>
                  <div className='search-page__lyric-inner-container'>
                    {lyric.lyrics}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default SearchPage;
