import { useState } from "react"
import { useNavigate } from 'react-router-dom'

function LogIn(){

    const [email, setEmail]= useState("");
    const [password, setPassword]= useState("");
    const [error, setError]= useState(null);
    //const navigate= useNavigate()

    const handleLogin =async(e)=>{
        e.preventDefault();
        try{const response= await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({email, password}),
                    });
    const data= await response.json()
        if(data.token){
            localStorage.setItem('token', data.token)
            //navigate('/home')
            console.log("Welcome")
        }else{
            setError(data.message || "LoginFailed")
           }
            }catch(error){
                setError('An error occurred, please do try again')
        }
    }
    return(
        <div>
            <form onSubmit={handleLogin}>
            <label>Email</label>    
            <input type="text" placeholder="email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <br />
            <label>Password</label>
            <input type="text" placeholder="password" value={password} onChange={(e) =>setPassword(e.target.value)} />
            <br />
            <button type="submit">Login</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    )
}

export default LogIn;