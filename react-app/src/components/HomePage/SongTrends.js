import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import getSong from '../../store/song.js';

function SongTrends(){
    const songs = useSelector(state => state.song);

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getSong());
    }, [dispatch]);

    return(
        <h1>Hello World</h1>
    )

}

export default SongTrends;
