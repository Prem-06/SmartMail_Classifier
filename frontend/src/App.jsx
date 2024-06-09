import './App.css'
import { GoogleOAuthProvider } from '@react-oauth/google'
import { ToastContainer } from 'react-toastify';
import Sign from './component/sign.jsx'
import Email_page from './component/email_page.jsx'
import 'react-toastify/dist/ReactToastify.css';
import {BrowserRouter,Routes,Route} from "react-router-dom"
function App() {
 

  return (
    <BrowserRouter>
    <GoogleOAuthProvider clientId='105699803734-s127tjsrli19c9qq71fomh3o669dg29b.apps.googleusercontent.com'>
    <Routes>
      <Route path='/' exact element={<Sign/>}></Route>
      <Route path='/sigin' element={<Sign/>}></Route>
      <Route path='/email_page' element={<Email_page/>}></Route>
    </Routes>
  </GoogleOAuthProvider>
  <ToastContainer theme="dark"/>
    </BrowserRouter>
  

  )
}

export default App
