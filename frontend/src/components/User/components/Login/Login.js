import axios from 'axios';
import React, { useState } from 'react';


const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState(''); 
    const register = ()=>{
        const data = new FormData()
        data.append('username',username)
        data.append('password',password)
        data.append('password2',confirmPassword)
        axios.post('http://127.0.0.1:8000/api/users/register/', data) 
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
                <label>
                    <input placeholder='Confirm password'
                        onChange={(item)=>{
                            setConfirmPassword(item.target.value)
                    }}
                    />
                </label>
                <button onClick={()=>{
                    register()
                }}>register</button>
        </div>
    );
};

export default Login;