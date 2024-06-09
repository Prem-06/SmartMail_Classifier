import axios from 'axios'
import express from 'express'
const router=express.Router()


router.get('/get_emails',async(req,res)=>{
  const accessToken=req.headers.authorization
  const emails_count=Number(req.headers.emails_count)
  
 await fetchInboxMessages(accessToken,emails_count).then((val)=>{
    res.status(200).json({message:"done",data:val})
  })
    
 
})

function extractName(emailString) {
  const nameMatch = emailString.match(/^(.*?)(?=\s*<)/);
  return nameMatch ? nameMatch[0] : null;
}

const fetchInboxMessages = async (accessToken,email_count) => {
    try {
      const response = await axios.get(
        `https://gmail.googleapis.com/gmail/v1/users/me/messages?maxResults=${email_count}`,
        {
         
          headers: {
            Authorization: `Bearer ${accessToken}`,
            Accept: 'application/json',
          },
        },
      )
      let email_list=[]
          for(let i=0;i<email_count;i++){
         await fetchMessages_text(accessToken,response.data.messages[i].id).then((val)=>{
            email_list.push(val)
          })
          
          }
        return email_list
         
    } catch (error) {
      console.error('Error fetching Gmail data:', error)
      return []
    }
  }

  const fetchMessages_text = async (accessToken,id) => {
    try {
      const response = await axios.get(
        `https://gmail.googleapis.com/gmail/v1/users/me/messages/${id}`,
        {
          
          headers: {
            Authorization: `Bearer ${accessToken}`,
            Accept: 'application/json',
          },
        },
      )
      const val=response.data.payload.headers
      for(let i=0;i<val.length;i++){
        const data=response.data.payload.headers[i]
        if(data.name==="From"){
          const d={
            from:extractName(data.value),
            message:response.data.snippet
          }

          return d;
        }
        
      }
    return {
      from:"unknown",
      message:"no-message"
    }
    } catch (error) {
      console.error('Error fetching Gmail data message:', error)
      return {
        from:"unknown",
        message:"no-message"
      }
    }
  }

  export default router;