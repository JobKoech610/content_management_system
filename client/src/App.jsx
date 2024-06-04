import { useState } from 'react'
import NavBar from './components/views/NavBar'
import Cards from './components/viewModels/cards'
import LogIn from './components/views/logIn'
import SignUp from './components/views/signUp'
//import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <NavBar/>
    <SignUp/>
    {/* <LogIn/> */}
    {/* <Cards/> */}
    </>
  )
}

export default App
