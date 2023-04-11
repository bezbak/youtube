import axios from 'axios';
import React, { useState } from 'react';
import './createvideo.css'
const CreateVideo = () => {
    const [title, setTitle] = useState('');
    const [desc, setDesc] = useState('');
    const [poster, setPoster] = useState(null);
    const [file, setFile] = useState(null);
    const create_video = ()=>{
        axios('/api/video/create/')
        
    }
    
    return (
        <div>
            <form action="">
                <label htmlFor="" className="text_label">
                    <input type="text" />
                </label>
                <label htmlFor="" className="text_label">
                    <input type="text" />
                </label>
                <label htmlFor="" className="text_label">
                    <input type="file" />
                </label>
                <label htmlFor="" className="text_label">
                    <input type="file" />
                </label>
            </form>
        </div>
    );
};

export default CreateVideo;