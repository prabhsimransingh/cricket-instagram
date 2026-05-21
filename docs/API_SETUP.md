# API Setup Guide

Complete step-by-step instructions for configuring each API with WicketGram.

---

## 🚀 Quick Setup (5 Minutes)

### Minimum Required
1. **Groq** (AI Captions) - Free, no credit card
2. **Ayrshare** (Instagram Posting) - Free tier available

### Optional but Recommended
3. **Pollinations.ai** (Free Team Art) - No setup needed
4. **DALL-E 3** (Premium Images) - Optional, requires OpenAI account

---

## 1️⃣ Groq - AI Caption Generation

**What it does**: Generates 3 unique, engaging captions for each post using Llama 3.3 AI model.

**Free Tier**: 30 requests/minute (more than enough for casual use)

### Step 1: Create Groq Account
1. Visit [console.groq.com](https://console.groq.com)
2. Click **"Sign Up"**
3. Create account with email or Google/GitHub
4. Verify email
5. Accept terms

### Step 2: Generate API Key
1. Go to [API Keys](https://console.groq.com/keys)
2. Click **"Create API Key"**
3. Name it: `WicketGram` (optional)
4. Copy the key (starts with `gsk_`)
5. **Keep it safe** - don't share publicly

### Step 3: Add to WicketGram
1. Open WicketGram app
2. Click **Settings** tab
3. Paste key in **"Groq API Key"** field
4. Click **Save**

### Step 4: Test It
1. Go to **Match Result** tab
2. Click **"📋 Sample"**
3. Click **"✨ Generate Post"**
4. Wait 10-15 seconds
5. Should see AI-generated captions below image

### Troubleshooting
| Problem | Solution |
|---------|----------|
| "Invalid API key" | Check you copied full key (starts with `gsk_`) |
| No captions generating | Check internet connection |
| Rate limit error | Wait a minute, then try again |
| Blank captions | API key may be expired - generate new one |

---

## 2️⃣ Ayrshare - Instagram Posting

**What it does**: Posts your cricket cards directly to Instagram with one click.

**Free Tier**: 50 posts/month (perfect for regular clubs)

**Paid Plans**: $15-50/month for unlimited posts

### Step 1: Create Ayrshare Account
1. Visit [ayrshare.com](https://www.ayrshare.com)
2. Click **"Get Started Free"**
3. Sign up with email
4. Verify email
5. Create account

### Step 2: Connect Instagram
1. Login to Ayrshare dashboard
2. Click **"Add Social Profile"**
3. Select **Instagram**
4. Choose **Business Account** (personal accounts work too)
5. Authorize Ayrshare to post
6. Follow Instagram prompts to authorize
7. Return to Ayrshare - should show "Connected ✓"

### Step 3: Get API Key
1. Click your **Profile** (top right)
2. Go to **"API Keys"**
3. You'll see **API Key** (long alphanumeric string)
4. Copy it

### Step 4: Add to WicketGram
1. Open WicketGram app
2. Click **Settings** tab
3. Paste key in **"Ayrshare API Key"** field
4. Click **Save**

### Step 5: Test It
1. Go to any post type
2. Load sample data
3. Generate AI image
4. Click **"📲 Instagram App"** button
5. Image copied to clipboard
6. Open Instagram app
7. Paste and post

### Alternative: Direct Ayrshare Button
1. After generating image
2. Click **"📱 Share Image"** button
3. This posts directly via Ayrshare API
4. Should see confirmation toast

### Troubleshooting
| Problem | Solution |
|---------|----------|
| "Invalid API key" | Generate new key on Ayrshare dashboard |
| Instagram won't authorize | Check that account is eligible |
| Can't post to Instagram | Business account may have restrictions - check Ayrshare settings |
| Rate limit reached | Upgrade plan or wait for monthly reset |

### Free Tier Limits
- 50 posts/month
- Image + text only
- No video, carousel, or stories
- Perfect for weekly match updates

---

## 3️⃣ Pollinations.ai - Free Team Art

**What it does**: AI-generates cricket team character art for home/away teams.

**Cost**: FREE (no API key needed)

### Setup
1. **No setup required!**
2. Pollinations.ai is called automatically in WicketGram
3. Images are generated on-demand

### How It Works
- WicketGram automatically generates team character art
- Images cached in browser
- No API calls charged to you

### Customization
In WicketGram Settings:
- Check/uncheck **"AI Team Characters"** to enable/disable

---

## 4️⃣ DALL-E 3 - Premium Image Generation

**What it does**: Advanced image generation for highest quality card designs.

**Cost**: **Paid** - $0.04-0.10 per image (requires OpenAI account with credits)

### When to Use
- Want highest quality cricket card designs
- Can afford API costs
- Need custom detailed images
- Professional social media presence

### Step 1: Create OpenAI Account
1. Visit [platform.openai.com](https://platform.openai.com)
2. Click **"Sign Up"**
3. Create account with email
4. Add payment method (credit/debit card)
5. Add initial credits ($5-20)

### Step 2: Create API Key
1. Go to [API Keys](https://platform.openai.com/api/keys)
2. Click **"Create new secret key"**
3. Name it: `WicketGram`
4. Copy key (starts with `sk-proj-`)
5. **Keep secure** - don't commit to git

### Step 3: Add to WicketGram
1. Open WicketGram Settings
2. Check **"Enable DALL-E Image Generation"**
3. Paste key in **"OpenAI API Key"** field
4. Save

### Step 4: Use It
1. Create any post (Match, Fixture, etc.)
2. Click **"✨ Generate Post"**
3. WicketGram will use DALL-E for image
4. Higher quality output
5. ~$0.08-0.10 per image

### Cost Estimation
| Posts/Month | Estimated Cost |
|------------|----------------|
| 5 posts | $0.40-0.50 |
| 10 posts | $0.80-1.00 |
| 20 posts | $1.60-2.00 |
| 50 posts | $4.00-5.00 |

### Troubleshooting
| Problem | Solution |
|---------|----------|
| "Insufficient credits" | Add payment method and credits to OpenAI account |
| "Invalid API key" | Check key wasn't truncated when copying |
| No DALL-E toggle showing | Refresh page after saving |
| Slow image generation | DALL-E takes 30-60 seconds per image |

---

## 5️⃣ Instagram Graph API - Alternative Posting

**What it does**: Direct Instagram posting without Ayrshare (more complex setup).

**Cost**: FREE (Facebook owns Instagram, no API charges)

**When to Use**: Advanced users, technical teams, custom integrations

### Prerequisites
- Facebook Business Account
- Instagram Business Account connected to Facebook
- Basic tech knowledge

### Step 1-5: Setup (15-20 minutes)
1. Create Facebook Business Account at [business.facebook.com](https://business.facebook.com)
2. Create Meta App at [developers.facebook.com](https://developers.facebook.com)
3. Add Instagram Graph API product
4. Get Access Token
5. Get Instagram Account ID

### Step 2: Add to WicketGram
1. Open Settings
2. Paste Instagram Access Token
3. Paste Instagram Account ID
4. Save

### Detailed Guide
See full tutorial: [Instagram Graph API Setup](https://developers.facebook.com/docs/instagram-graph-api)

---

## 6️⃣ Imgur - Backup Image Hosting

**What it does**: Hosts card images as backup if Ayrshare unavailable.

**Cost**: FREE (unless you want advanced features)

**When to Use**: Redundancy, backup hosting, image sharing

### Step 1: Create Imgur Account
1. Visit [imgur.com](https://imgur.com)
2. Click **"Sign In"** → **"Register"**
3. Create account with email
4. Verify email

### Step 2: Register Application
1. Go to [Imgur API](https://api.imgur.com)
2. Click **"Register Application"**
3. App Name: `WicketGram`
4. Select **OAuth 2** authorization type
5. Agree to terms
6. Submit

### Step 3: Get Credentials
1. Copy **Client ID**
2. Copy **Client Secret**
3. Note **Authorization URL**

### Step 4: Add to WicketGram
1. Open Settings
2. Paste **Imgur Client ID**
3. Save
4. Click **"Authorize Imgur"**
5. Approve access
6. Done!

---

## 🔑 API Key Security

### ⚠️ Important
- **Never commit API keys to GitHub**
- **Never share publicly**
- **Never post in Discord/Slack**
- Keys are stored in browser localStorage only
- WicketGram never sends keys to servers

### How Keys Are Stored
```javascript
// In browser localStorage (client-side only)
{
  "groqKey": "gsk_...",
  "ayrshareKey": "AYS_...",
  "igToken": "EAAB...",
  "dalleApiKey": "sk-proj-..."
}
```

### Safety Tips
1. ✅ Keys stored locally in your browser only
2. ✅ Never exposed in network requests
3. ✅ Each API call made directly from your browser
4. ✅ Clear browser storage if using shared computer
5. ✅ Regenerate keys if accidentally exposed

---

## 🧪 Testing Your Setup

### Test 1: Groq API
```
1. Go to Settings
2. Enter Groq API key
3. Save
4. Match Result tab → Click Sample
5. Click "Generate Post"
6. Wait 15 seconds
7. Should see 3 captions appear ✅
```

### Test 2: Ayrshare API
```
1. Go to Settings
2. Enter Ayrshare API key
3. Save
4. Match Result tab → Click Sample
5. Click "Generate Post"
6. Click "📱 Share Image"
7. Should see success toast ✅
8. Or: Click "📲 Instagram App" → Image in clipboard ✅
```

### Test 3: Both APIs
```
1. Set Groq + Ayrshare keys
2. Create new post (any type)
3. Click "Generate Post"
4. Wait for AI image + 3 captions
5. Select a caption
6. Click "📲 Instagram App"
7. Open Instagram app
8. Paste and verify image appears ✅
```

---

## 💰 Cost Summary

| API | Free Tier | Paid | Best For |
|-----|-----------|------|----------|
| **Groq** | 30 req/min | - | AI Captions (Essential) |
| **Ayrshare** | 50 posts/mo | $15-50/mo | Instagram Posting |
| **DALL-E 3** | No | $0.04-0.10/img | Premium Images |
| **Pollinations** | Unlimited | - | Free Team Art |
| **Imgur** | Unlimited | - | Backup Hosting |
| **Instagram Graph API** | Unlimited | - | Direct Posting |

### Recommended Setup (Free)
- Groq (captions)
- Ayrshare free tier (50 posts/month)
- Pollinations (free team art)
- **Total Cost: $0**

### Recommended Setup (Premium)
- Groq (captions)
- Ayrshare paid ($15/month)
- DALL-E 3 ($40-50/month estimated)
- **Total Cost: $55-65/month**

---

## 🆘 Troubleshooting

### General Issues
| Error | Solution |
|-------|----------|
| "No images generating" | Check all API keys are entered |
| "Toast says API error" | Verify key format matches API provider |
| "Keys keep disappearing" | Browser localStorage may be disabled |
| "API calls timing out" | Check internet connection, retry |

### Per API
- **Groq**: [Groq Docs](https://console.groq.com/docs)
- **Ayrshare**: [Ayrshare Docs](https://docs.ayrshare.com)
- **DALL-E**: [OpenAI Docs](https://platform.openai.com/docs)
- **Instagram Graph API**: [Meta Docs](https://developers.facebook.com/docs/instagram-graph-api)

---

## ✅ Verification Checklist

After setup, verify:
- [ ] Groq API key working (captions generate)
- [ ] Ayrshare API key working (can post to Instagram)
- [ ] Image generation working (AI creates card design)
- [ ] No console errors (F12 → Console tab)
- [ ] API keys saved in Settings
- [ ] Tested full workflow (form → image → captions → copy → Instagram)

---

## 📞 Need Help?

- Check [Troubleshooting](#troubleshooting) section
- Open an [Issue](https://github.com/prabhsimransingh/cricket-instagram/issues)
- Start a [Discussion](https://github.com/prabhsimransingh/cricket-instagram/discussions)
- Read individual API documentation links above

---

**You're all set! Create your first cricket post! 🏏**
