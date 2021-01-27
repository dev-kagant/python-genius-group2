import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllSongs } from '../../store/song.js';

function SongTrends(){
    const songs = useSelector(state => state.songs);

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(fetchAllSongs());
    }, [dispatch]);

    return(
        <div>
            <ul>{songs && songs.map((song) =>
            <>
                <li>Hello World</li>
                <li className="title">{song.title}</li>
            </>
            )}</ul>
        </div>
    )

}

export default SongTrends;
