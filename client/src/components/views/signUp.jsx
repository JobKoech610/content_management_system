import { useState } from "react"

function SignUp() {
    const [formData, setFormData] = useState({
        firstName: "",
        lastName: "",
        email: "",
        password: ""
    })

    const handleOnChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        })
    }

    const validateForm=() =>{
        if (!formData.firstName || !formData.lastName) {
            alert("Please enter your full names")
            return false
            }
        else if (!formData.email) {
                alert("Please enter your last name")
                return false   
        }
        else if (!formData.password) {
            alert("Please enter your password")
            return false
            }
        else {
            return true;
            }
    }
    const handleSubmit = (e) => {
        e.preventDefault();
        if(validateForm()){
            console.log(formData)
            // send data to backend
    }}

    const post = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    }
    fetch('http://127.0.0.1:5000/user', post)
        .then(response => response.json())
        .then(data => setFormData(data))
        .catch((error) => {
            console.error('Error:', error);
        });

return (
    <div>

        <form onSubmit={handleSubmit}>
            <label>Firstname</label>
            <input type="text" placeholder="Firstname"  onChange={handleOnChange} name="firstName" value={formData.firstName}/>
            <label>Lastname</label>
            <input type="text" placeholder="Lastname"  onChange={handleOnChange} name="lastName" value={formData.lastName}/> 
            <label>email</label>
            <input type="text" placeholder="Email"  onChange={handleOnChange} name="email" value={formData.email}/>
            <label>Password</label>
            <input type="text" placeholder="Password"  onChange={handleOnChange} name="password" value={formData.password}/>
            <label>Confirm Password</label>
            <input type="text" placeholder="Confirm Password"  onChange={handleOnChange} name="Password" value={formData.password}/>
            <button type="submit" onClick={(e)=>alert(e.target.value)}>SignUp</button>
        </form>
    </div>
)
}

export default SignUp;