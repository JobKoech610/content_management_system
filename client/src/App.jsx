import { useState } from 'react'
import NavBar from './components/views/NavBar'
import Cards from './components/viewModels/cards'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <NavBar/>
    <Cards/>
    </>
  )
}

export default App
