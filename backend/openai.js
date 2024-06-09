import express  from 'express' 
const router = express.Router();
import OpenAI from 'openai'

router.post('/classify', async (req, res) => {
  const list = req.body.list;
  const api_key = req.headers.authorization;
  let category_list = [];


  const openai = new OpenAI({
    apiKey: api_key,
  });

  async function classifyEmail(emailText) {
    const prompt = `Classify the following email into one of the categories: Important, Promotional, Social, Marketing, Spam.\n\nEmail: "${emailText}"\n\nCategory:`;

    try {
      const response = await openai.completions.create({
        model: 'gpt-3.5-turbo',
        prompt: prompt,
        max_tokens: 10,
      });
     
      const category = response.choices[0].text.trim();
      return category;
    } catch (error) {
      console.error('Error classifying email:', error);
      return 'General';
    }
  }

  try {
    const promises = list.map(item => classifyEmail(String(item.message)));
    category_list = await Promise.all(promises);

    res.status(200).json({ list: category_list });
  } catch (error) {
    console.error('Error processing classification:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

export default router
