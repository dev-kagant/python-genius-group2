import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { fetchSongInfo } from '../../store/search.js';
import './styles/SearchBar.css';

function SearchBar () {
  const [search, setSearch] = useState();
  const dispatch = useDispatch();
  const history = useHistory();

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(fetchSongInfo(search));
    history.push('/search');
  };

  return (
    <form className='nav-search__form' onSubmit={handleSubmit}>
      <input
        className='nav-search__input'
        placeholder='Search'
        type='text'
        name='term'
        onChange={(e) => setSearch(e.target.value)}
        value={search}
      />
      <button className='nav-search__submit' type='submit'>
        <i className='fas fa-search fa-lg' />
      </button>
    </form>
  );
}

export default SearchBar;
