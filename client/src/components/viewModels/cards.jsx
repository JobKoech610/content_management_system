import { useEffect, useState } from "react"
import "../styles/cards.css"


function Cards(){
  const [data, setData] = useState([])
  console.log(data)

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    const url = 'http://127.0.0.1:5000/platforms'
    try {
      const response = await fetch(url)
      const data = await response.json()
      console.log(data)
      setData(data)
    } catch (error) {
      console.log(error)
    }
  }


    return(
        <div className="cardHolder">
        {data.map((item, index) => (
            <div key={index} className="card">
                <img src={item.Image}/>
                <p>{item.Description}</p>
                <p>Price: {item.Amount}</p>
            </div>))}
        </div>
    )
 }

 export default Cards