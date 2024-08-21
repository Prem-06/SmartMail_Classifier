import './App.css'
import { GoogleOAuthProvider } from '@react-oauth/google'
import { ToastContainer } from 'react-toastify';
import Sign from './component/sign.jsx'
import Email_page from './component/email_page.jsx'
import 'react-toastify/dist/ReactToastify.css';
import {BrowserRouter,Routes,Route} from "react-router-dom"
import Context from './context.jsx';
function App() {
const backend_url=import.meta.env.VITE_BACKEND_URL
const model_url=import.meta.env.VITE_MODEL_URL
const client_id=import.meta.env.VITE_CLIENT_ID

  return (
    <Context.Provider value={{backend_url,model_url}}>
       <BrowserRouter>
   <GoogleOAuthProvider clientId={client_id}>
     
<Routes>
     <Route path='/' exact element={<Sign/>}></Route>
     <Route path='/sigin' element={<Sign/>}></Route>
     <Route path='/email_page' element={<Email_page/>}></Route>
   </Routes>


 </GoogleOAuthProvider>
 <ToastContainer style={{width:"270px"}}/>
   </BrowserRouter>
   
    </Context.Provider>

  )
}

export default App
