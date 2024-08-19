import React from 'react'
import './email_component.css'
const Email_component = (props) => {
  const {data,category}=props
  function category_color(category) {
    if (category === "spam") {
        return "#FF4500"; 
    }
    else if (category === "important") {
        return "#FFD700";  
    }
    else if (category === "social") {
        return "#1E90FF";  
    }
    else if (category === "promotional") {
        return "#FF69B4"; 
    }
    else {
        return "#000000";  
    }
}

  return (
    <div className='email_component'>
        <div className='sender'>
        <p>{data.from}</p>
        <p style={{color:category_color(category)}}>{category}</p>
        </div>
        <div className='message'><p>{data.message}</p></div>
      
    </div>
  )
}

export default Email_component