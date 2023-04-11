import React, {useState, useEffect} from 'react';
import './home.css'
import moment from 'moment';
import 'moment/locale/ru';
// import img1 from '../../static/images/video.webp'
import axios from 'axios';
const Home = () => {
    const [videos, setVideos] = useState([]);
    useEffect(()=>{
        axios('http://127.0.0.1:8000/api/videos/')
        .then((data)=>{
            setVideos(data.data)
            console.log(data.data);
        })
    },[])
    return (
        <div className={'home'}>
            <a href='/user/register'>Register</a>
            <a href='/user/login'>Login</a>
            <a href='/user'>Account</a>
            <div className={'home__inner'}>
                {videos.map((item)=>(
                    <VideoBlock item={item} key={item.id}/>
                ))}
            </div>            
        </div>
    );
};

const VideoBlock = ({item})=>{
    const {channel, title, poster, video_views, created} = item
    const [timeDiff, setTimeDiff] = useState([]);
    useEffect(() => {
        const interval = setInterval(() => {
          const now = moment();
          const then = moment(created);
          const diff = moment.duration(now.diff(then));
    
          moment.locale('ru');
          setTimeDiff(diff.humanize());
        }, 1000);
    
        return () => clearInterval(interval);
      }, []);
    return (
        <div className='video__block'>
            <div className='video'>
                <img src={poster} alt='video' className='video__file'></img>
            </div>
            <div className='video__info'>
                <div className='ava'>
                    <img className='ava__img' alt='ava' src={channel.profile_image}/>
                </div>
                <div className='videoinfo__inner'>
                    <a href='dafa' className='video__title'>{title}</a>
                    <a href='dafa' className='account'>{channel.username}</a>
                    <p className='video_views_date'>{video_views.length} просмотров {timeDiff} назад</p>
                </div>
            </div>
        </div>
    )
}

export default Home;
