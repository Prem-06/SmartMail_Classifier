import React from 'react'
import './email_component.css'
const Email_component = (props) => {
  const {data,category}=props
  return (
    <div className='email_component'>
        <div className='sender'>
        <p>{data.from}</p>
        <p>{category}</p>
        </div>
        <div className='message'><p>{data.message}</p></div>
      
    </div>
  )
}

export default Email_component