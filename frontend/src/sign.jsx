import React from 'react'
import { GoogleLogin } from '@react-oauth/google'
const Sign = () => {
    const handleSuccess = (credentialResponse) => {
        console.log("sign in succes");
      };
    
      const handleError = () => {
        console.log('Login Failed');
      };
    
  return (
    <div>
        <GoogleLogin  onSuccess={handleSuccess}
      onError={handleError}/>
    </div>
  )
}

export default Sign