import React from 'react'
import './content.css'
import { useNavigate } from 'react-router-dom'
import { toast } from 'react-toastify'
const Content = (prop) => {
   const {profile}=prop
   const notifyA=(val)=> toast.success(val)
   const navigate=useNavigate()
   function logout(){
    localStorage.removeItem('profile')
    localStorage.removeItem('access_token')
    localStorage.removeItem('openai_key')
    notifyA('Logout Sucessfully')
    navigate('/')
   
   }
  return (
    <div className="profile-info">
    <div className="profile-div">
        <div className="profile-pic"><img src={profile.picture} alt=""/></div>
        <div className="detail">
            <p>{profile.name}</p>
            <p>{profile.email}</p>
        </div>
    
    </div>
      <div className="logout-div">
        <button onClick={logout}>Logout</button>
       
       
      </div>
    </div>
    
     
  )
}

export default Content