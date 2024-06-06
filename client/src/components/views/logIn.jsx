import { useState } from "react"
import { useNavigate } from 'react-router-dom'

function LogIn(){

    const [email, setEmail]= useState("");
    const [password, setPassword]= useState("");
    const [error, setError]= useState(null);
    const navigate= useNavigate()

    const handleLogin =async()=>{
        try{const response= await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({email, password}),
                    });
    const data= await response.json()
        if(data.success){
            localStorage.setItem('token', data.token)
            navigate('/home')
        }else{
            setError(data.error)
           }
            }catch(error){
                setError('An error occurred, please do try again')
        }
    }
    return(
        <div>
            <form>
            <label>email</label>    
            <input type="text" placeholder="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <br />
            <label>Password</label>
            <input type="text" placeholder="password" value={password} onChange={(e) =>setPassword(e.target.value)} />
            </form>
            <br />
            <button type="button" onChange={handleLogin}>Login</button>
        </div>
    )
}

export default LogIn;