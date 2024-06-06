import { useState } from 'react'
//import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import NavBar from './components/views/NavBar'
import Cards from './components/viewModels/cards'
import LogIn from './components/views/logIn'
import SignUp from './components/views/signUp'
import Homepage from './components/views/Homepage';
//import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <NavBar/>
    {/* <SignUp/> */}
    <LogIn/>
    {/* <Cards/> */}
    {/* <Homepage/> */}
    </>
  )
}

export default App


{/* <Router>
  <Routes>
      <Route path="/login" element={<LogIn />} />
      <Route path="/home" element={<Home />} />
  </Routes>
</Router> */}