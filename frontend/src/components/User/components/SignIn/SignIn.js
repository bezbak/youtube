import axios from 'axios';
import React, { useState } from 'react';


const SignIn = () => {
    const [userStatus, setUserStatus] = useState(null);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const sign_in = ()=>{
        const data = new FormData()
        data.append('username',username)
        data.append('password',password)
        axios.post('http://127.0.0.1:8000/api/users/login/', data) 
        .then((response)=>{
            console.log(response);
        }).catch((error) => {
            console.log(error);
        });
        
    }
    return (
        <div className='register'>
                <label>
                    <input placeholder='Username' onChange={(item)=>{
                        setUsername(item.target.value)
                    }}/>
                </label>
                <label>
                    <input placeholder='Password'
                        onChange={(item)=>{
                        setPassword(item.target.value)
                    }}
                    />
                </label>
                <button onClick={()=>{
                    sign_in()
                }}>register</button>
        </div>
    );
};

export default SignIn;