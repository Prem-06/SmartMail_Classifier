
import './App.css'
import { GoogleOAuthProvider } from '@react-oauth/google'
import Sign from './sign.jsx'
function App() {
 

  return (
   <GoogleOAuthProvider clientId="105699803734-s127tjsrli19c9qq71fomh3o669dg29b.apps.googleusercontent.com">
 <div>
  <Sign/>
 </div>
   </GoogleOAuthProvider>
    
     
   
  )
}

export default App
