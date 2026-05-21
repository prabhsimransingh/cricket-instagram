# Contributing to WicketGram

Thank you for your interest in contributing to WicketGram! 🏏 We welcome contributions from developers, designers, cricket enthusiasts, and anyone passionate about open source.

---

## 🚀 Ways to Contribute

### 1. **Report Bugs**
Found something broken? Help us improve!
- Create an [Issue](https://github.com/prabhsimransingh/cricket-instagram/issues) with:
  - Clear title describing the bug
  - Steps to reproduce
  - Expected vs. actual behavior
  - Screenshots if UI-related
  - Browser/device information

### 2. **Request Features**
Have an idea to make WicketGram better?
- Start a [Discussion](https://github.com/prabhsimransingh/cricket-instagram/discussions)
- Or create an Issue with label `enhancement`
- Describe:
  - What you want to build
  - Why it's useful
  - Possible implementation approach

### 3. **Fix Bugs**
- Look for issues labeled `bug` or `help-wanted`
- Comment on the issue to claim it
- Submit a PR with your fix

### 4. **Add Features**
- Check the [Roadmap](README.md#-roadmap)
- Look for issues labeled `good-first-issue` or `feature-request`
- Propose your implementation in a Discussion first
- Submit a PR once approved

### 5. **Improve Documentation**
- Fix typos or unclear instructions
- Add examples or tutorials
- Expand API setup guides
- Create video tutorials
- Improve code comments

### 6. **Add Integrations**
- TikTok post type (9:16 format with trending sounds)
- Facebook variant (1.91:1 aspect ratio)
- LinkedIn professional posts
- Twitter/X thread optimization
- YouTube Shorts format

---

## ⚡ Getting Started

### Local Development Setup

```bash
# 1. Fork the repository
# Click "Fork" on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/cricket-instagram.git
cd cricket-instagram

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Open the app locally
python serve.py

# Then visit: http://localhost:8732

# 5. Make your changes
# Edit: docs/index.html (main application file)

# 6. Test thoroughly
# - Test on desktop, tablet, mobile
# - Test all post types
# - Check console for errors
# - Verify responsive design

# 7. Commit your changes
git add docs/index.html
git commit -m "feat: add your feature description"

# 8. Push to your fork
git push origin feature/your-feature-name

# 9. Create a Pull Request
# Go to GitHub and click "New Pull Request"
```

### Code Style Guide

#### HTML & CSS
- Use semantic HTML5 elements
- Class names: `kebab-case` (e.g., `ai-preview-box`)
- Inline styles for dynamic properties, Tailwind for defaults
- Comments for complex sections

#### JavaScript (Alpine.js)
```javascript
// Use descriptive variable names
const marginValue = diff > 0 ? `${diff} runs` : '0 runs';

// Add comments for non-obvious logic
// Calculate wickets remaining for opposition (max 10 wickets)
const wktsRemaining = 10 - theirWicketsLost;

// Use consistent formatting
// Good:
if(victory === 'team_a'){
  // action
}

// Method naming: descriptive verbs
async generateAICardForType() { }
async shareToInstagramApp() { }
async copyImage() { }

// Add x- comments for Alpine.js bindings
// @click="submitMatch()" - Validates form and creates post
```

#### Form Data Models
```javascript
// Structure for new post types
postType: {
  opponent: '',           // Required fields with empty defaults
  result: 'won',          // Enums with sensible defaults
  date: '',               // ISO format for dates
  players: [],            // Arrays for collections
  
  // AI generation fields
  aiPrompt: '',           // Generated prompt
  aiImageUrl: '',         // Generated image URL
  aiCaptions: []          // Array of 3 caption options
}
```

#### Comments
- Comment complex algorithms
- Comment non-obvious design decisions
- Use `// TODO:` for future improvements
- Avoid over-commenting obvious code

---

## 📋 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] **Code Quality**
  - [ ] No console errors
  - [ ] Follows code style guide
  - [ ] Functions have clear names
  - [ ] Comments for complex logic

- [ ] **Testing**
  - [ ] Tested on desktop browser (Chrome, Firefox, Safari)
  - [ ] Tested on mobile/tablet
  - [ ] Tested all affected post types
  - [ ] No regression in existing features
  - [ ] API calls working (if API-related)

- [ ] **Documentation**
  - [ ] Clear commit message
  - [ ] Updated README if needed
  - [ ] Added comments in code
  - [ ] Updated docs/ files if applicable

- [ ] **Performance**
  - [ ] No memory leaks
  - [ ] Debounced event listeners (form inputs)
  - [ ] Canvas rendering optimized
  - [ ] Bundle size not significantly increased

- [ ] **Accessibility**
  - [ ] Form inputs have labels
  - [ ] Buttons have descriptive text
  - [ ] Color contrast sufficient
  - [ ] Mobile touch targets >= 48x48px

---

## 🎯 Good First Issues

Looking to start contributing? Try these:

### 🟢 Beginner-Friendly (1-2 hours)
- **Add dark mode toggle**
  - Add UI toggle in Settings
  - Use CSS variables for colors
  - Store preference in localStorage

- **Improve form validation**
  - Add real-time error messages
  - Validate API key format
  - Show helpful error toasts

- **Add keyboard shortcuts**
  - Cmd+Enter / Ctrl+Enter to submit form
  - Escape to clear form
  - Tab navigation improvements

- **Create example config**
  - `examples/sample-club-config.json`
  - Document all customization options
  - Add descriptions

### 🟡 Intermediate (2-4 hours)
- **Add TikTok post type**
  - Create post type form
  - Implement 9:16 canvas rendering
  - Add trending sounds metadata

- **Improve Settings UI**
  - Add form validation
  - Preview colors in real-time
  - Add preset color schemes

- **Write API setup guide**
  - Step-by-step for Instagram Graph API
  - Include screenshots
  - Troubleshooting section

- **Create video tutorial**
  - 5-10 min YouTube video
  - Screen recording of full workflow
  - Voice-over explanation

### 🔴 Advanced (4+ hours)
- **Add batch posting**
  - Implement scheduling UI
  - Queue multiple posts
  - Add time picker

- **Add Facebook variant**
  - Create 1.91:1 aspect ratio cards
  - Implement Facebook-specific prompts
  - Test with Facebook API

- **Mobile app skeleton**
  - React Native project setup
  - Basic screen layouts
  - API integration boilerplate

---

## 🔍 Code Review Process

### Our Review Standards
1. **Functionality**: Does it work as intended?
2. **Code Quality**: Is it clean, readable, maintainable?
3. **Testing**: Is it tested on multiple browsers/devices?
4. **Documentation**: Are changes documented?
5. **Performance**: Does it impact app speed/bundle size?

### Review Timeline
- **Bug fixes**: 1-3 days
- **Features**: 1 week
- **Documentation**: 2-3 days
- **Major changes**: Discussion required before PR

### What to Expect
- Constructive feedback on code
- Suggestions for improvements
- Requests for tests or documentation
- Approval once standards met

---

## 📝 Commit Message Format

Use clear, descriptive commit messages:

```
feat: add TikTok post type with trending sounds
fix: resolve canvas taint error for external images
docs: update API setup guide for Ayrshare
refactor: simplify margin calculation logic
test: add unit tests for victory context
style: improve code formatting and comments
perf: optimize canvas rendering for mobile
```

**Format**: `<type>: <subject>`

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code improvement
- `test`: Tests
- `style`: Formatting
- `perf`: Performance

---

## 🚀 Feature Development Workflow

### 1. **Discuss First**
- Start a [Discussion](https://github.com/prabhsimransingh/cricket-instagram/discussions)
- Or comment on a related [Issue](https://github.com/prabhsimransingh/cricket-instagram/issues)
- Get feedback before coding

### 2. **Plan Implementation**
- Outline changes needed
- Identify affected files
- Consider edge cases
- Plan testing approach

### 3. **Implement**
- Create feature branch from `main`
- Write code following style guide
- Test thoroughly
- Add comments for complex logic

### 4. **Test**
- Desktop browsers (Chrome, Firefox, Safari)
- Mobile browsers
- All affected post types
- Edge cases (empty fields, large files, etc.)

### 5. **Submit PR**
- Push to your fork
- Create PR with description
- Link related issues
- Wait for review

### 6. **Iterate**
- Address review feedback
- Update code as needed
- Re-test changes
- Respond to comments

### 7. **Merge**
- Maintainers merge once approved
- Thank you! You're now a contributor 🎉

---

## 💬 Communication

### GitHub
- **Issues**: Bug reports, feature requests
- **Discussions**: General questions, feature ideas
- **PRs**: Code reviews, implementation

### Standards
- Be respectful and inclusive
- Assume good intent
- Provide constructive feedback
- Help new contributors

---

## 📚 Useful Resources

### Understanding the Codebase
- [ARCHITECTURE.md](docs/ARCHITECTURE.md) - Code structure & patterns
- [API_SETUP.md](docs/API_SETUP.md) - How APIs are integrated
- Inline code comments - Look for `//` explanations
- README.md - Feature overview

### Web Technologies Used
- [Alpine.js Docs](https://alpinejs.dev/) - Reactive framework
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS
- [Canvas API Docs](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) - Drawing

### Cricket Concepts
- 20-over T20 format
- 50-over ODI format
- Wickets, runs, over calculations
- Match result margins

---

## ✅ Recognition

All contributors will be:
- Added to [Contributors](https://github.com/prabhsimransingh/cricket-instagram/graphs/contributors) list
- Featured in release notes
- Highlighted on social media (if desired)
- Included in "Contributor of the Month"

---

## ❓ Questions?

- 💬 Ask in [GitHub Discussions](https://github.com/prabhsimransingh/cricket-instagram/discussions)
- 📧 Email: (open an issue to contact)
- 🐛 Found a bug? [Open an issue](https://github.com/prabhsimransingh/cricket-instagram/issues)

---

## 🎓 Learning Resources

New to open source? Check out:
- [GitHub Guides](https://guides.github.com/)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [First Timers Only](https://www.firsttimersonly.com/)

---

**Thank you for being part of the WicketGram community! 🏏✨**

Your contributions help make cricket content creation easier for everyone.
