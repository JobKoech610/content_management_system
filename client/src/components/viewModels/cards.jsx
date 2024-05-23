import { useEffect, useState } from "react"


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
      //const data = await response.json()
      console.log(data)
      setData(data)
    } catch (error) {
      console.log(error)
    }
  }


    return(
        <>
        {data.map((item, index) => (
            <div key={index} className="card">
                <h2>{item.Image}</h2>
                <p>{item.Description}</p>
                <p>Price: {item.Amount}</p>
            </div>))}
        </>
    )
 }

 export default Cards