
import './App.css'
import { GoogleOAuthProvider } from '@react-oauth/google'
import Sign from './sign.jsx'
function App() {
 

  return (
   <GoogleOAuthProvider clientId="660229840633-m1romsqgst6mu1pkjth0io3hpq9a32jk.apps.googleusercontent.com">
 <div>
  <Sign/>
 </div>
   </GoogleOAuthProvider>
    
     
   
  )
}

export default App
