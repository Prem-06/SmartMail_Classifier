import './App.css'
import { GoogleOAuthProvider } from '@react-oauth/google'
import { ToastContainer } from 'react-toastify';
import Sign from './component/sign.jsx'
import Email_page from './component/email_page.jsx'
import 'react-toastify/dist/ReactToastify.css';
import {BrowserRouter,Routes,Route} from "react-router-dom"
import { Audio } from 'react-loader-spinner'
import Context from './context.jsx';
import { useState } from 'react';
function App() {
 const [loader,setloader]=useState(false)
const backend_url="https://email-assignment.onrender.com"
const model_url="https://email-assignment-1.onrender.com"
  return (
    <Context.Provider value={{setloader,backend_url,model_url}}>
      {loader?(<Audio
  height="80"
  width="80"
  radius="9"
  color="black"
  ariaLabel="loading"
  wrapperStyle
  wrapperClass
/>):( <BrowserRouter>
   
   <GoogleOAuthProvider clientId='105699803734-s127tjsrli19c9qq71fomh3o669dg29b.apps.googleusercontent.com'>
     
<Routes>
     <Route path='/' exact element={<Sign/>}></Route>
     <Route path='/sigin' element={<Sign/>}></Route>
     <Route path='/email_page' element={<Email_page/>}></Route>
   </Routes>


 </GoogleOAuthProvider>
 <ToastContainer theme="dark"/>
   </BrowserRouter>)}
   
    </Context.Provider>

  )
}

export default App
