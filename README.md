# 🏏 WicketGram - AI-Powered Cricket Instagram Content Creator

**Create stunning cricket social media posts in minutes — no design skills needed!**

![WicketGram Demo](https://img.shields.io/badge/Cricket-Instagram-E1306C?style=for-the-badge&logo=instagram)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/prabhsimransingh/cricket-instagram?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v12-blue?style=for-the-badge)

---

## ✨ What is WicketGram?

WicketGram is a free, open-source web application that helps cricket clubs and enthusiasts create professional Instagram posts in seconds. Using AI-powered image generation and intelligent caption creation, you can turn match results, fixtures, squad announcements, and milestones into eye-catching social media content.

**No design experience required. No credit card needed.**

### 🎯 Perfect For
- 🏟️ Cricket clubs managing social media
- 📱 Content creators posting match updates
- 🎓 Student teams sharing achievements
- 📸 Cricket enthusiasts creating fan content
- 🤖 Developers learning AI integration with web apps

---

## ⚡ Quick Start (5 Minutes)

### 1. Open the App
Visit the live demo: **[WicketGram Live](https://prabhsimransingh.github.io/cricket-instagram/)**

### 2. Set Your Club Details
- Go to **Settings** tab
- Enter your club name and brand colors
- Upload club/league logos (optional)
- Save settings

### 3. Generate Your First Post
1. Click **"Match Result"** tab
2. Click **"📋 Sample"** to load example data
3. Observe auto-calculated margin and AI preview
4. Click **"✨ Generate Post"** to create AI image
5. Click **"Copy Image"** → Paste into Instagram
6. Click **"📲 Instagram App"** → Opens app with image ready to paste

### 4. That's It! 
Post directly to Instagram in under 2 minutes.

---

## 🎨 Features

### 📝 6 Post Types
- **Match Result** - Match scores, winners, margin, top performers
- **Fixture** - Upcoming match announcements with date & venue
- **Squad** - Playing XI / team roster with player roles
- **MOTM** - Man of the Match highlights with player stats
- **Milestone** - Achievement celebrations (centuries, milestones)
- **Photo** - Custom posts with AI-generated captions

### 🤖 AI-Powered Generation
- **Smart Image Creation** - AI generates professional card designs
- **Intelligent Captions** - 3 caption options for each post
- **Victory Context** - Celebratory tone for wins, resilience for losses
- **Auto-Calculated Margins** - Automatically computes runs/wickets margin
- **Real-Time Preview** - See changes instantly

### 🎯 Creator-Friendly Features
- **Queue Management** - Save drafts, approve before posting
- **Canvas-Based Rendering** - Instagram-optimized 9:16 aspect ratio
- **Custom Branding** - Club logos, colors, league themes
- **Clipboard Copy** - Copy image & caption, paste directly to Instagram
- **Direct Posting** - Share directly to Instagram via Ayrshare
- **Local Storage** - All data saved in your browser (no server)

### ⚙️ Technical Highlights
- ✅ **Single HTML File** - No build process needed
- ✅ **Alpine.js Reactive** - Fast, responsive UI updates
- ✅ **Canvas API** - Professional card design & rendering
- ✅ **Free APIs** - Groq, Pollinations.ai (no credit card required)
- ✅ **Privacy First** - All API keys stored locally, never exposed
- ✅ **Mobile Responsive** - Works on desktop, tablet, mobile
- ✅ **No Backend** - Completely client-side application

---

## 🚀 API Setup (Choose Your Preference)

### Essential APIs (Recommended)

#### 1. **Ayrshare** - Direct Instagram Posting
Easiest way to post directly to Instagram from WicketGram.

```
✅ Free tier available
✅ No Facebook app setup needed
✅ Direct image + caption posting
⏱️ Setup time: 5 minutes
```

[👉 Ayrshare Setup Guide](docs/API_SETUP.md#ayrshare)

#### 2. **Groq** - AI Caption Generation
Uses Llama 3.3 model to generate 3 unique captions for each post.

```
✅ Free tier: 30 requests/minute
✅ No credit card required
✅ High-quality AI captions
⏱️ Setup time: 3 minutes
```

[👉 Groq Setup Guide](docs/API_SETUP.md#groq)

### Optional APIs

#### 3. **DALL-E 3** - Premium Images
OpenAI's advanced image generation for higher quality cards.

```
💰 Requires API key & credits
✨ Higher quality images
⏱️ Setup time: 5 minutes (requires OpenAI account)
```

#### 4. **Pollinations.ai** - Free Team Art
Free AI-generated team character art (no API key needed).

```
✅ Free, no key required
✅ Cricket-themed character generation
⏱️ Setup time: 0 minutes
```

#### 5. **Imgur** - Backup Image Hosting
Fallback hosting if Ayrshare unavailable.

```
✅ Free OAuth 2 setup
📦 Backup image hosting
⏱️ Setup time: 5 minutes
```

#### 6. **Instagram Graph API** - Alternative to Ayrshare
Direct Instagram posting without Ayrshare (more complex setup).

```
📌 Requires Facebook Business Account
🔗 Direct Instagram integration
⏱️ Setup time: 15-20 minutes
```

**[👉 Complete API Setup Guide](docs/API_SETUP.md)** - Step-by-step for each API

---

## 📊 Feature Showcase

### Create Match Result Posts
```
Input: Opponent, scores, wickets, overs, top performers
↓
Margin Auto-Calculation: "13 runs" or "by 5 wickets"
↓
AI Image Generation: Professional card design
↓
3 Caption Options: Victory celebration or resilience messaging
↓
Output: Copy image + caption → Paste into Instagram
```

### Queue Management
- **Draft** - Save posts for later
- **Approve** - Review before posting
- **Post** - Send to Instagram
- **History** - Track all posted content

### Customization
- Club name & colors (primary + accent)
- Club & league logos
- Player photos (optional)
- API key configuration
- Feature toggles (AI images, captions)

---

## 🔄 How It Works

```
┌─────────────────────────────────────────────┐
│ 1. FORM INPUT                               │
│    - Team names, scores, wickets, overs    │
│    - Top batter & bowler stats             │
│    - Victory selection                      │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 2. AUTO-CALCULATION                         │
│    - Margin: runs difference or wickets     │
│    - Full score format: 156/5               │
│    - Contextual messaging                   │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 3. AI GENERATION (via Groq + DALL-E)       │
│    - Image: Professional card design        │
│    - Captions: 3 unique options            │
│    - Tone: Celebratory or resilient        │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 4. PREVIEW & SELECT                         │
│    - Real-time card preview                │
│    - Select preferred caption               │
│    - Review before posting                  │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│ 5. COPY & POST                              │
│    - Copy Image to clipboard                │
│    - Copy Caption to clipboard              │
│    - Open Instagram app (mobile)            │
│    - Paste & post directly                  │
└─────────────────────────────────────────────┘
```

---

## 🛠️ Installation & Deployment

### Local Development
```bash
# Clone repository
git clone https://github.com/prabhsimransingh/cricket-instagram.git
cd cricket-instagram

# Serve locally
python serve.py

# Open in browser
# http://localhost:8732
```

### Deploy to Web
- **GitHub Pages** (recommended) - See [Deployment Guide](docs/DEPLOYMENT.md)
- **Vercel** - One-click deployment
- **Netlify** - Drag & drop deployment
- **Docker** - Containerized deployment

[👉 Complete Deployment Guide](docs/DEPLOYMENT.md)

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [API_SETUP.md](docs/API_SETUP.md) | Detailed guide for each API configuration |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute to the project |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Code structure & how to extend |
| [DEPLOYMENT.md](docs/DEPLOYMENT.md) | Hosting options & deployment steps |
| [FEATURES.md](docs/FEATURES.md) | Complete feature overview & roadmap |
| [SCREENSHOTS.md](docs/SCREENSHOTS.md) | Visual walkthrough with GIFs |

---

## 🗺️ Roadmap

### v12 (Current)
✅ Intelligent Match form (auto-calculated margins, victory selection)
✅ Motivational context in AI prompts (wins vs losses)
✅ All 6 post types with AI generation
✅ Clipboard copy for images & captions
✅ Instagram app integration

### v13 (Next)
- [ ] TikTok post type (shorter format, trending sounds)
- [ ] Facebook variant posts (1.91:1 aspect ratio)
- [ ] Batch posting & scheduling
- [ ] Post analytics & performance tracking
- [ ] Dark mode toggle
- [ ] Multiple club profiles

### v14 (Future)
- [ ] Android app launch (React Native)
- [ ] iOS app launch
- [ ] Video post support
- [ ] Community gallery (view other clubs' posts)
- [ ] Integration with cricket databases (player stats)
- [ ] Sponsorship features

---

## 🤝 Contributing

We welcome contributions from developers, designers, cricket enthusiasts, and anyone interested in building amazing content creation tools!

### How to Contribute
1. **Report Bugs** - Found an issue? Let us know!
2. **Request Features** - Have an idea? Suggest it!
3. **Fix Code** - Submit PRs for bugs or improvements
4. **Improve Docs** - Help others get started
5. **Add Integrations** - Support new platforms (TikTok, Facebook, etc.)

### Getting Started
See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Setup instructions
- Feature ideas with difficulty levels
- Code style guidelines
- PR review process

### Good First Issues
- Add TikTok post type (3-4 hours)
- Improve Settings UI (2-3 hours)
- Write API setup guide for Instagram Graph API
- Add dark mode toggle (1-2 hours)
- Create example: custom post type template

[👉 View all open issues](https://github.com/prabhsimransingh/cricket-instagram/issues)

---

## 💡 Technology Stack

### Frontend
- **HTML5** - Semantic structure
- **Tailwind CSS v3** - Styling via CDN
- **Alpine.js v3** - Reactive UI & state management
- **Canvas API** - Professional card rendering

### AI & APIs
- **Groq API** - Caption generation (Llama 3.3)
- **DALL-E 3** - Image generation (optional)
- **Pollinations.ai** - Free team art
- **Ayrshare API** - Instagram posting
- **Instagram Graph API** - Alternative posting

### Storage & Hosting
- **Browser localStorage** - Client-side data persistence
- **GitHub Pages** - Free static hosting
- **Vercel/Netlify** - Optional cloud deployment

### No Backend Required ✨
- Single-file application
- No server infrastructure
- No database
- All computation client-side
- Perfect for static hosting

---

## 📝 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

**TL;DR**: You can use, modify, and distribute this freely, including for commercial purposes. Just include the original license.

---

## 👨‍💻 Credits & Attribution

**Created by**: [Prabh Singh](https://github.com/prabhsimransingh)

**Built with**: 
- Alpine.js - Reactive UI framework
- Tailwind CSS - Utility-first CSS
- Groq API - AI caption generation
- Ayrshare - Instagram posting API
- Pollinations.ai - AI art generation

**Special thanks to**: Cricket enthusiasts, beta testers, and early contributors who helped shape WicketGram.

---

## 📞 Support & Community

### Have Questions?
- 📖 Check the [API Setup Guide](docs/API_SETUP.md)
- 🏗️ Read the [Architecture Guide](docs/ARCHITECTURE.md)
- 💬 Open an [Issue](https://github.com/prabhsimransingh/cricket-instagram/issues)
- 🤝 Join the [Discussions](https://github.com/prabhsimransingh/cricket-instagram/discussions)

### Share Your Creations
Found WicketGram helpful? Show us what you've created!
- Tag us on Instagram
- Share your posts with #WicketGram
- Feature in our community gallery

---

## 🌟 Show Your Support

If you find WicketGram useful, please:
- ⭐ Star this repository
- 🍴 Fork and contribute
- 📢 Share with cricket clubs & communities
- 💬 Leave feedback & suggestions

---

## 📜 Status

| Component | Status | Version |
|-----------|--------|---------|
| Web App | ✅ Production | v12 |
| Android App | 🚀 In Development | - |
| iOS App | 📋 Planned | - |
| API Integration | ✅ Complete | Multiple APIs |
| Documentation | ✅ Comprehensive | Full |
| Community | 🌱 Growing | - |

---

**Made with ❤️ for cricket lovers and developers**

[Open the App →](https://prabhsimransingh.github.io/cricket-instagram/) | [GitHub →](https://github.com/prabhsimransingh/cricket-instagram) | [Report Bug →](https://github.com/prabhsimransingh/cricket-instagram/issues)
